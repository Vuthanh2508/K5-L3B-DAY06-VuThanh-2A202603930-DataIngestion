"""Orchestration script for Day 06 Data Ingestion Engineering.

Evaluates 5 Token-Based Chunking & Retrieval Strategies (BGE-M3 Tokenizer, 500 tokens, overlap 50):
- Strategy A: Fixed-size token windows (500 tokens, overlap 50)
- Strategy B: Recursive token chunking (separators [\\n\\n, \\n, . , ' '], max 500 tokens, overlap 50)
- Strategy C: Section-based token chunking (aligned with SEC Form 10-Q Notes/Items, max 500 tokens, overlap 50)
- Strategy D: Paragraph-based token chunking (natural paragraphs and tables, max 500 tokens, overlap 50, no filter)
- Strategy E: Paragraph-based token chunking + Metadata Filter (max 500 tokens, overlap 50, filter by 'section')
"""
import csv
import json
import os
import time
from pathlib import Path

from .chunking import (
    by_paragraph,
    fixed_size,
    recursive_chunking,
    run_all_chunking,
    section_chunking,
)
from .embeddings import BGEM3Embedder
from .evaluation import evaluate_query, summarize
from .ingestion import load_pdf
from .store import QdrantVectorStore


def run_pipeline() -> None:
    print("=" * 75)
    print("🚀 BẮT ĐẦU PIPELINE THỰC HÀNH DAY 06 - 5 CHIẾN LƯỢC DATA INGESTION")
    print("=" * 75)

    # 1. Kiểm tra tài liệu & nạp dữ liệu (Docling + pdfplumber)
    pdf_path = Path("NETFLIX_2023Q2_10Q-3-33.pdf")
    if not pdf_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file tài liệu tại {pdf_path}")

    pages = load_pdf(pdf_path, document_id="netflix-2023q2-10q", source="NETFLIX_2023Q2_10Q-3-33.pdf")
    total_pages = len(pages)
    total_chars = sum(len(p.text) for p in pages)
    print(f"📄 Tài liệu: {total_pages} trang nội dung hữu ích, {total_chars:,} ký tự.")

    # 2. Xây dựng 5 cấu hình chunking
    chunks_dict = run_all_chunking(pages, export_artifacts=True)
    chunks_a = chunks_dict["A"]
    chunks_b = chunks_dict["B"]
    chunks_c = chunks_dict["C"]
    chunks_d = chunks_dict["D"]
    chunks_e = chunks_dict["E"]

    # 3. Nạp Embedder BGE-M3
    embedder = BGEM3Embedder(model_name="BAAI/bge-m3")

    # 4. Tạo embeddings cho các chunks
    print("\n--> [Embeddings] Tiến hành mã hóa vector trên GPU...")
    # Strategy A
    t0_emb_a = time.time()
    vectors_a = embedder.embed_documents([c.text for c in chunks_a], batch_size=16)
    time_emb_a = round(time.time() - t0_emb_a, 2)
    print(f"✅ Strategy A: {len(vectors_a)} vectors trong {time_emb_a}s")

    # Strategy B
    t0_emb_b = time.time()
    vectors_b = embedder.embed_documents([c.text for c in chunks_b], batch_size=16)
    time_emb_b = round(time.time() - t0_emb_b, 2)
    print(f"✅ Strategy B: {len(vectors_b)} vectors trong {time_emb_b}s")

    # Strategy C
    t0_emb_c = time.time()
    vectors_c = embedder.embed_documents([c.text for c in chunks_c], batch_size=16)
    time_emb_c = round(time.time() - t0_emb_c, 2)
    print(f"✅ Strategy C: {len(vectors_c)} vectors trong {time_emb_c}s")

    # Strategy D & E (Nội dung text giống nhau, tái sử dụng vector để tiết kiệm tài nguyên)
    t0_emb_d = time.time()
    vectors_d = embedder.embed_documents([c.text for c in chunks_d], batch_size=16)
    vectors_e = vectors_d  # Tái sử dụng
    time_emb_d = round(time.time() - t0_emb_d, 2)
    print(f"✅ Strategy D & E: {len(vectors_d)} vectors trong {time_emb_d}s")

    # 5. Lưu trữ vào các Collection độc lập trên Qdrant (Docker Container / Local)
    print("\n--> [VectorStore] Kết nối và lưu vào Qdrant (Docker / Local)...")
    store = QdrantVectorStore(dimensions=embedder.dimensions)

    store.create_collection("strategy_a")
    store.upsert("strategy_a", chunks_a, vectors_a)

    store.create_collection("strategy_b")
    store.upsert("strategy_b", chunks_b, vectors_b)

    store.create_collection("strategy_c")
    store.upsert("strategy_c", chunks_c, vectors_c)

    store.create_collection("strategy_d")
    store.upsert("strategy_d", chunks_d, vectors_d)

    store.create_collection("strategy_e")
    store.upsert("strategy_e", chunks_e, vectors_e)

    # 6. Đọc bộ câu hỏi benchmark gold
    bench_file = Path("benchmark/gold_qa.json")
    if not bench_file.exists():
        raise FileNotFoundError(f"Không tìm thấy file benchmark tại {bench_file}")
    with open(bench_file, "r", encoding="utf-8") as f:
        questions = json.load(f)
    print(f"\n🎯 Đã nạp {len(questions)} câu hỏi benchmark ({sum(1 for q in questions if q['split']=='dev')} dev, {sum(1 for q in questions if q['split']=='test')} test)")

    # 7. Chạy benchmark cho cả 5 chiến lược
    strategies = ["A", "B", "C", "D", "E"]
    all_traces = {}
    summaries = {}
    time_metrics = {}

    for strat in strategies:
        print(f"\n" + "-" * 55)
        print(f"🔍 Chạy Benchmark cho Strategy {strat}...")
        traces = []
        t0_search = time.time()

        for q in questions:
            q_vec = embedder.embed_query(q["question"])
            filter_to_use = q.get("filter") if strat == "E" else None
            hits = store.search(
                strategy=f"strategy_{strat.lower()}",
                query_vector=q_vec,
                top_k=3,
                filters=filter_to_use
            )
            trace_record = evaluate_query(q, hits)
            traces.append(trace_record)

        elapsed = round(time.time() - t0_search, 2)
        summary = summarize(traces)
        all_traces[strat] = traces
        summaries[strat] = summary
        time_metrics[strat] = elapsed

        print(f"📊 Kết quả Strategy {strat}:")
        print(f"   - Dev  (15 câu): Hit@1 = {summary['dev']['hit1_str']} ({summary['dev']['hit1_pct']}%), Hit@3 = {summary['dev']['hit3_str']} ({summary['dev']['hit3_pct']}%)")
        print(f"   - Test (5 câu) : Hit@1 = {summary['test']['hit1_str']} ({summary['test']['hit1_pct']}%), Hit@3 = {summary['test']['hit3_str']} ({summary['test']['hit3_pct']}%)")
        print(f"   - Tổng (20 câu): Hit@1 = {summary['overall']['hit1_str']} ({summary['overall']['hit1_pct']}%), Hit@3 = {summary['overall']['hit3_str']} ({summary['overall']['hit3_pct']}%)")
        print(f"   - Tuân thủ Filter: {summary['filter_compliance']}")
        print(f"   - Thời gian truy xuất: {elapsed}s")

    store.close()

    # 8. Lưu kết quả traces & summary
    os.makedirs("results", exist_ok=True)
    os.makedirs("starter/results", exist_ok=True)

    with open("results/traces.json", "w", encoding="utf-8") as f:
        json.dump(all_traces, f, ensure_ascii=False, indent=2)
    with open("starter/results/traces.json", "w", encoding="utf-8") as f:
        json.dump(all_traces, f, ensure_ascii=False, indent=2)

    chunk_counts = {
        "A": len(chunks_a),
        "B": len(chunks_b),
        "C": len(chunks_c),
        "D": len(chunks_d),
        "E": len(chunks_e),
    }

    benchmark_summary = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model": embedder.model_name,
        "vector_store": "Qdrant Docker Server (http://localhost:6333)" if getattr(store, "is_server", False) else "Qdrant Embedded Local Disk",
        "strategies": {
            strat: {
                "chunk_count": chunk_counts[strat],
                "summary": summaries[strat],
                "search_time_sec": time_metrics[strat]
            }
            for strat in strategies
        }
    }
    with open("results/benchmark_summary.json", "w", encoding="utf-8") as f:
        json.dump(benchmark_summary, f, ensure_ascii=False, indent=2)
    with open("starter/results/benchmark_summary.json", "w", encoding="utf-8") as f:
        json.dump(benchmark_summary, f, ensure_ascii=False, indent=2)

    # 9. Ghi vào artifacts/experiment_log.csv & data/experiment_log.csv
    log_rows = [
        {
            "strategy": "A",
            "chunking": "Fixed-size Token Window",
            "chunk_size": "500 tokens",
            "overlap": "50 tokens",
            "metadata": "source, page, doc_page, section",
            "filter": "None",
            "vectorizer": "BAAI/bge-m3 (1024d)",
            "hypothesis": "Cắt cố định theo token window 500 tokens; đơn giản nhưng có thể cắt ngang bảng biểu.",
            "dev_hit1": summaries["A"]["dev"]["hit1_str"],
            "dev_hit3": summaries["A"]["dev"]["hit3_str"],
            "test_hit1": summaries["A"]["test"]["hit1_str"],
            "test_hit3": summaries["A"]["test"]["hit3_str"],
            "notes": f"{chunk_counts['A']} chunks, search time {time_metrics['A']}s"
        },
        {
            "strategy": "B",
            "chunking": "Recursive Token Chunking",
            "chunk_size": "max 500 tokens",
            "overlap": "50 tokens",
            "metadata": "source, page, doc_page, section",
            "filter": "None",
            "vectorizer": "BAAI/bge-m3 (1024d)",
            "hypothesis": "Cắt đệ quy theo phân cấp [\\n\\n, \\n, . , ' '] tôn trọng cấu trúc câu và đoạn trong ngân sách 500 tokens.",
            "dev_hit1": summaries["B"]["dev"]["hit1_str"],
            "dev_hit3": summaries["B"]["dev"]["hit3_str"],
            "test_hit1": summaries["B"]["test"]["hit1_str"],
            "test_hit3": summaries["B"]["test"]["hit3_str"],
            "notes": f"{chunk_counts['B']} chunks, search time {time_metrics['B']}s"
        },
        {
            "strategy": "C",
            "chunking": "Section-based Token Chunking",
            "chunk_size": "max 500 tokens",
            "overlap": "50 tokens",
            "metadata": "source, page, doc_page, section",
            "filter": "None",
            "vectorizer": "BAAI/bge-m3 (1024d)",
            "hypothesis": "Gom toàn bộ nội dung của từng Thuyết minh/Tiêu mục Form 10-Q giúp giữ đầy đủ ngữ cảnh báo cáo tài chính.",
            "dev_hit1": summaries["C"]["dev"]["hit1_str"],
            "dev_hit3": summaries["C"]["dev"]["hit3_str"],
            "test_hit1": summaries["C"]["test"]["hit1_str"],
            "test_hit3": summaries["C"]["test"]["hit3_str"],
            "notes": f"{chunk_counts['C']} chunks, search time {time_metrics['C']}s"
        },
        {
            "strategy": "D",
            "chunking": "Paragraph-based Token Chunking",
            "chunk_size": "max 500 tokens",
            "overlap": "50 tokens",
            "metadata": "source, page, doc_page, section",
            "filter": "None",
            "vectorizer": "BAAI/bge-m3 (1024d)",
            "hypothesis": "Cấu trúc đoạn văn tự nhiên (\\n\\n) và khối bảng biểu giúp cân bằng giữa độ dài chunk và tính toàn vẹn ý.",
            "dev_hit1": summaries["D"]["dev"]["hit1_str"],
            "dev_hit3": summaries["D"]["dev"]["hit3_str"],
            "test_hit1": summaries["D"]["test"]["hit1_str"],
            "test_hit3": summaries["D"]["test"]["hit3_str"],
            "notes": f"{chunk_counts['D']} chunks, search time {time_metrics['D']}s"
        },
        {
            "strategy": "E",
            "chunking": "Paragraph-based Token + Metadata Filter",
            "chunk_size": "max 500 tokens",
            "overlap": "50 tokens",
            "metadata": "source, page, doc_page, section",
            "filter": "section metadata filter",
            "vectorizer": "BAAI/bge-m3 (1024d)",
            "hypothesis": "Sử dụng chunk giống D kết hợp bộ lọc trường metadata section trên Qdrant giúp loại bỏ hoàn toàn nhiễu từ các phần khác.",
            "dev_hit1": summaries["E"]["dev"]["hit1_str"],
            "dev_hit3": summaries["E"]["dev"]["hit3_str"],
            "test_hit1": summaries["E"]["test"]["hit1_str"],
            "test_hit3": summaries["E"]["test"]["hit3_str"],
            "notes": f"{chunk_counts['E']} chunks, search time {time_metrics['E']}s, filter {summaries['E']['filter_compliance']}"
        }
    ]

    fieldnames = [
        "strategy", "chunking", "chunk_size", "overlap", "metadata", "filter",
        "vectorizer", "hypothesis", "dev_hit1", "dev_hit3", "test_hit1", "test_hit3", "notes"
    ]
    for path in ["artifacts/experiment_log.csv", "data/experiment_log.csv"]:
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(log_rows)

    print("\n" + "=" * 75)
    print("🎉 HOÀN THÀNH TOÀN BỘ BENCHMARK CHO 5 CHIẾN LƯỢC (A, B, C, D, E)!")
    print("=" * 75)
    print("📁 Đã lưu:")
    print("   - Traces chi tiết: results/traces.json")
    print("   - Tổng hợp kết quả: results/benchmark_summary.json")
    print("   - Nhật ký thí nghiệm: artifacts/experiment_log.csv & data/experiment_log.csv")


def main() -> None:
    run_pipeline()


if __name__ == "__main__":
    main()
