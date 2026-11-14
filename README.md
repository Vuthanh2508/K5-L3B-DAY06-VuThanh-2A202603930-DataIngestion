# Day 06 · Data Ingestion Engineering

**Học viên:** Vũ Thành  
**MSSV:** 2A202603930 — **Lớp:** L3B  
**Chủ đề & Corpus:** Báo cáo tài chính quý 2/2023 của Netflix, Inc. (SEC Form 10-Q — `NETFLIX_2023Q2_10Q-3-33.pdf`, 31 trang nội dung hữu ích).  
**Báo cáo cá nhân chi tiết:** [report/individual/2A202603930_VuThanh.md](report/individual/2A202603930_VuThanh.md)

---

## 🚀 Hướng Dẫn Tái Hiện (Quickstart & Reproduction)

### 1. Cài đặt môi trường Python
Khuyến nghị sử dụng Python 3.10+:
```bash
pip install -r requirements.txt
```

### 2. Khởi động Qdrant Vector Database qua Docker
Hệ thống sử dụng Qdrant v1.19.2 được cấu hình sẵn trong `docker-compose.yml`:
```bash
docker compose up -d
```
* Container: `day06-qdrant` chạy cổng `6333` (REST API) và `6334` (gRPC).
* Dữ liệu được lưu trữ bền vững tại `./data/qdrant_storage`.
* *(Ghi chú: Nếu môi trường không có Docker, hệ thống sẽ tự động fallback về embedded local disk mode tại `./data/qdrant_db`).*

### 3. Chạy Toàn Bộ Pipeline Đánh Giá
Chạy 1 lệnh duy nhất để thực thi toàn bộ pipeline (Parse $\to$ Normalize $\to$ Chunking 5 cấu hình $\to$ Embeddings GPU $\to$ Upsert Qdrant $\to$ Benchmark 20 queries $\to$ Export kết quả):
```bash
python -m starter.src.run
```

---

## 📊 Kết Quả Tóm Tắt 5 Chiến Lược Chunking & Ingestion

Tất cả các chiến lược đều sử dụng tokenizer `BAAI/bge-m3` với ngân sách thống nhất `max_tokens = 500, overlap = 50` để đảm bảo thử nghiệm kiểm soát công bằng:

| Chiến Lược | Mô Tả Kỹ Thuật | Số Chunks | Dev Hit@1 (n=15) | Dev Hit@3 (n=15) | Test Hit@1 (n=5) | Test Hit@3 (n=5) | Tuân thủ Filter | Thời Gian |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Strategy A** | Fixed-size Token Window (500 tokens) | 78 | 10/15 (66.7%) | 13/15 (86.7%) | 0/5 (0.0%) | 2/5 (40.0%) | 1/5 | 1.25s |
| **Strategy B** | Recursive Token Chunking ([\n\n, \n, . , ' ']) | 88 | **12/15 (80.0%)** | **13/15 (86.7%)** | 0/5 (0.0%) | 2/5 (40.0%) | 1/5 | 1.59s |
| **Strategy C** | Section-based Token Chunking (Note/Item) | 78 | 10/15 (66.7%) | 13/15 (86.7%) | 0/5 (0.0%) | 2/5 (40.0%) | 1/5 | 1.14s |
| **Strategy D** | Paragraph-based Token Chunking (No Filter) | 88 | **12/15 (80.0%)** | **13/15 (86.7%)** | 0/5 (0.0%) | 2/5 (40.0%) | 1/5 | 1.19s |
| **Strategy E** | Paragraph-based Token + Metadata Filter | 88 | **12/15 (80.0%)** | **13/15 (86.7%)** | **1/5 (20.0%)** | **2/5 (40.0%)** | **5/5 (100%)** | **1.00s ⚡** |

---

## 📁 Cấu Trúc Thư Mục Nộp Bài

```text
├── STUDENT.md                                      # Thông tin học viên và mã commit chốt bài
├── requirements.txt                                # Danh sách thư viện phụ thuộc
├── docker-compose.yml                              # Cấu hình Qdrant Vector Store Container
├── NETFLIX_2023Q2_10Q-3-33.pdf                     # Tài liệu nguồn SEC Form 10-Q (31 trang)
├── starter/src/                                    # Toàn bộ mã nguồn pipeline
│   ├── ingestion.py                                # Đọc PDF (Docling OCR) & Chuẩn hóa NFKC
│   ├── chunking.py                                 # 5 thuật toán chunking theo BGE-M3 Tokenizer
│   ├── embeddings.py                               # BGE-M3 Embedder (GPU FP16, 1024-d)
│   ├── store.py                                    # Qdrant Vector Store client & Payload Filter
│   ├── evaluation.py                               # Đánh giá Hit@1, Hit@3, Filter compliance
│   └── run.py                                      # Orchestration script chạy end-to-end
├── data/ & artifacts/                              # Dữ liệu trung gian đồng bộ 100%
│   ├── manifest.json                               # Khai báo nguồn, quyền, thống kê 31 trang
│   ├── parsed_corpus.md / parsed_document.md       # Văn bản đã OCR và chuẩn hóa sạch
│   ├── pages_markdown/                             # 31 file markdown cho 31 trang PDF
│   ├── chunks/                                     # File JSON 5 chiến lược chunk (A -> E)
│   ├── chunks_markdown/                            # Bản hiển thị trực quan các chunk theo trang
│   ├── CHUNKING_REPORT.md                          # Báo cáo thống kê phân bổ độ dài chunk
│   └── experiment_log.csv                          # Nhật ký thí nghiệm 5 cấu hình
├── benchmark/                                      # Bộ benchmark đánh giá
│   ├── gold_qa.json                                # 20 câu hỏi (15 dev / 5 test, 5 metadata filter)
│   ├── BENCHMARK_GOLD.md                           # Thuyết minh chi tiết 20 câu hỏi & bằng chứng
│   └── validate_gold.py                            # Script tự động kiểm chứng 20/20 câu với PDF
├── results/                                        # Kết quả truy xuất & Đánh giá
│   ├── traces.json                                 # Vết truy xuất chi tiết từng query
│   ├── benchmark_summary.json                      # Tổng hợp chỉ số Hit@1, Hit@3
│   ├── MANUAL_AUDIT.md                             # Bảng chấm thủ công Coherence, Metadata, Grounding
│   └── manual_audit.json                           # Dữ liệu chấm thủ công dạng JSON
└── report/individual/
    └── 2A202603930_VuThanh.md                      # Báo cáo cá nhân hoàn chỉnh theo Rubric
```
