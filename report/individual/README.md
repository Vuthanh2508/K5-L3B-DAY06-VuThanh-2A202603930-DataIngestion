# Báo cáo cá nhân — Day 6: Data Ingestion Engineering

**Học viên:** Vũ Thành  
**MSSV:** 2A202603930  
**Tài liệu báo cáo chi tiết:** [`2A202603930_VuThanh.md`](2A202603930_VuThanh.md)

---

## Dữ liệu và pipeline
- **Chủ đề, nguồn/quyền, số trang và quy tắc tính trang:**
  - *Chủ đề:* Báo cáo tài chính quý 2 năm 2023 của Netflix, Inc. (SEC Form 10-Q cho quý kết thúc ngày 30/06/2023, CIK 0001065280).
  - *Nguồn & Bản quyền:* Hồ sơ công bố thông tin công khai theo quy định của Ủy ban Giao dịch và Chứng khoán Hoa Kỳ (US SEC EDGAR).
  - *Số trang & Quy tắc tính:* Đúng 31 trang vật lý chứa nội dung phân tích tài chính hữu ích (`NETFLIX_2023Q2_10Q-3-33.pdf`, tương ứng số trang in 3 đến 33 trên hồ sơ 10-Q gốc, bỏ qua trang bìa và mục lục theo quy tắc `RULES.md`).
  - *Dung lượng văn bản:* 102,536 ký tự sau chuẩn hóa; 29,387 tokens theo BAAI/bge-m3.
- **Chuẩn hóa, lỗi và giới hạn:**
  - *Pipeline trích xuất:* Trích xuất layout bằng Docling (bật RapidOCR và Table Transformer) xuất ra Markdown giữ nguyên cấu trúc tiêu đề cấp 1-3 và bảng biểu.
  - *Chuẩn hóa làm sạch:* Áp dụng chuẩn Unicode NFKC, chuẩn hóa khoảng trắng phi chuẩn (`\xa0`, `\u200b`, `\ufeff`), căn chỉnh và gọt sạch ô bảng (`cell.strip()`), co gọn dòng trống thừa `\n{3,}` thành `\n\n`.
  - *Giới hạn bảng biểu & Thử thách trần 500 tokens:* Toàn bộ tài liệu có 57 bảng Markdown. 52 bảng có độ dài ≤ 469 tokens được các chiến lược cấu trúc (B, D, E) bảo toàn trọn vẹn 100% trong 1 chunk duy nhất. Tuy nhiên, có 5 bảng báo cáo tài chính hợp nhất lớn (Cash Flows: 1,197 tokens; Balance Sheets: 760 tokens; Stockholders' Equity: 728 tokens; Senior Notes: 628 tokens; Operations: 622 tokens) có độ dài token tự nhiên vượt quá trần ngân sách 500 tokens của bài lab, do đó bắt buộc phải phân tách thành 2–3 chunks liên tiếp. Ngược lại, chiến lược Fixed-size (Strategy A) cắt mù theo bước nhảy token làm xé đôi tới 55/57 bảng (96.5%).
- **Embedding model/provider/version/số chiều, vector store/version, metric, lệnh chạy và chi phí:**
  - *Embedding Model:* `BAAI/bge-m3` (FlagEmbedding, Dense 1024 chiều, chạy local trên GPU NVIDIA GeForce RTX 3050 Ti Laptop, FP16 half precision, batch size 16, VRAM ~1.16 GB).
  - *Vector Store:* Qdrant v1.19.2 (chạy container Docker `day06-qdrant`, cổng 6333 REST / 6334 gRPC, volume lưu trữ bền vững `./data/qdrant_storage`).
  - *Khoảng cách vector (Metric):* Cosine Similarity (`Distance.COSINE`).
  - *Lệnh chạy tái hiện:*
    ```bash
    # 1. Khởi động Qdrant vector database
    docker compose up -d

    # 2. Chạy toàn bộ pipeline (chunking, embedding, Qdrant upsert, retrieval benchmark)
    python -m starter.src.run
    ```
  - *Chi phí API:* **0 USD** (100% chạy offline trên phần cứng local).
- **Metadata bắt buộc, trường lọc bổ sung, nguồn giá trị và lý do chọn:**
  - *Metadata bắt buộc:* `chunk_id`, `document_id`, `source`, `page` (trang 1-31), `doc_page` (trang in 10-Q 3-33).
  - *Trường lọc bổ sung:* `section` (các giá trị: *Financial Statements*, *Notes to Consolidated Financial Statements*, *Management’s Discussion and Analysis*, *Market Risk*, *Other Information*).
  - *Lý do chọn:* Hồ sơ 10-Q có cấu trúc báo cáo chuẩn mực và phân cấp ranh giới rõ ràng. Lọc theo `section` giúp loại bỏ hoàn toàn nhiễu chéo miền (cross-domain noise) giữa các thuyết minh kế toán chi tiết và phần thảo luận triển vọng tương lai của ban quản trị.

---

## Cấu hình và benchmark
- **Các chiến lược chunking (Thử nghiệm kiểm soát cùng ngân sách 500 tokens):**
  - **Strategy A (Fixed-size Token Window):** Cửa sổ cố định 500 tokens, overlap 50 tokens cắt theo tokenizer BGE-M3 (78 chunks).
  - **Strategy B (Recursive Token Chunking):** Cắt phân cấp theo dấu ngắt đoạn và câu `[\n\n, \n, . , ' ']`, trần 500 tokens, overlap 50 tokens (88 chunks).
  - **Strategy C (Section-based Token Chunking):** Định biên theo tiêu đề phần/mục (Note, Item, Part) của Form 10-Q, trần 500 tokens, overlap 50 tokens (78 chunks).
  - **Strategy D (Paragraph-based Token Chunking):** Nhóm theo đoạn văn bản tự nhiên (`\n\n`) và khối bảng biểu Markdown, trần 500 tokens, overlap 50 tokens, không lọc metadata (88 chunks).
  - **Strategy E (Paragraph-based Token + Metadata Filter):** Cùng bộ chunk và vector với Strategy D (88 chunks), nhưng kích hoạt bộ lọc Payload Filter `section` trên Qdrant.
  - *Khác biệt duy nhất giữa D và E:* E kích hoạt metadata payload filtering trong khi D tìm kiếm toàn bộ corpus.
- **Bộ benchmark ≥20 câu:**
  - *Phân chia:* 15 câu Dev / 5 câu Test (tổng cộng 20 câu).
  - *Phân loại câu hỏi:* 7 câu trực tiếp, 3 câu diễn đạt lại, 5 câu điều kiện ngoại lệ/phủ định, 5 câu có điều kiện lọc metadata (3 dev, 2 test).
  - *Kiểm chứng evidence:* 20/20 câu có evidence trích xuất nguyên văn từ PDF gốc, được xác thực tự động bởi `benchmark/validate_gold.py` (tỷ lệ khớp 100%).
- **Tiêu chí chọn chiến lược đã chốt trước khi xem test:**
  1. Evidence Hit@3 cao nhất trên tập Dev.
  2. Hit@1 cao nhất trên tập Dev.
  3. Coherence trung bình cao nhất (không cắt xẻ bảng/câu).
  4. Filter tuân thủ 100% trên các câu truy vấn có điều kiện lọc.

---

## Kết quả

### Bảng 1: Hiệu năng Truy xuất (Retrieval Accuracy & Performance)
| Strategy | Split | Hit@1 (n/N) | Evidence Hit@3 (n/N) | Chunk count | Thời gian | Chi phí |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Strategy A** *(Fixed-size)* | Dev | 10/15 (66.7%) | 13/15 (86.7%) | 78 chunks | 1.25s | $0 |
| | Test | 0/5 (0.0%) | 2/5 (40.0%) | | | |
| | **Tổng** | **10/20 (50.0%)** | **15/20 (75.0%)** | | | |
| **Strategy B** *(Recursive)* | Dev | 12/15 (80.0%) | 13/15 (86.7%) | 88 chunks | 1.59s | $0 |
| | Test | 0/5 (0.0%) | 2/5 (40.0%) | | | |
| | **Tổng** | **12/20 (60.0%)** | **15/20 (75.0%)** | | | |
| **Strategy C** *(Section-based)* | Dev | 10/15 (66.7%) | 13/15 (86.7%) | 78 chunks | 1.14s | $0 |
| | Test | 0/5 (0.0%) | 2/5 (40.0%) | | | |
| | **Tổng** | **10/20 (50.0%)** | **15/20 (75.0%)** | | | |
| **Strategy D** *(Paragraph)* | Dev | 12/15 (80.0%) | 13/15 (86.7%) | 88 chunks | 1.19s | $0 |
| | Test | 0/5 (0.0%) | 2/5 (40.0%) | | | |
| | **Tổng** | **12/20 (60.0%)** | **15/20 (75.0%)** | | | |
| **Strategy E** *(Para + Filter)* | Dev | 12/15 (80.0%) | 13/15 (86.7%) | 88 chunks | 1.00s | $0 |
| | Test | 1/5 (20.0%) | 2/5 (40.0%) | | | |
| | **Tổng** | **13/20 (65.0%)** | **15/20 (75.0%)** | | | |

### Bảng 2: Đánh giá Thủ công (Manual Audit: Coherence, Metadata, Grounding)
| Strategy | Coherence trung bình /2 (n=10) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N) | Grounding 0/1/2 (số câu) và trung bình /2 |
| :--- | :---: | :---: | :---: | :---: |
| **Strategy A** | 0.3 / 2.0 (0: 7, 1: 3, 2: 0) | 15/15 (100%) | 1/5 (20%) | 0: 0 câu, 1: 3 câu, 2: 2 câu (ĐTB: 1.4 / 2.0) |
| **Strategy B** | 1.8 / 2.0 (0: 0, 1: 2, 2: 8) | 15/15 (100%) | 1/5 (20%) | 0: 0 câu, 1: 3 câu, 2: 2 câu (ĐTB: 1.4 / 2.0) |
| **Strategy C** | 1.2 / 2.0 (0: 3, 1: 2, 2: 5) | 15/15 (100%) | 1/5 (20%) | 0: 0 câu, 1: 3 câu, 2: 2 câu (ĐTB: 1.4 / 2.0) |
| **Strategy D** | 1.8 / 2.0 (0: 0, 1: 2, 2: 8) | 15/15 (100%) | 1/5 (20%) | 0: 0 câu, 1: 3 câu, 2: 2 câu (ĐTB: 1.4 / 2.0) |
| **Strategy E** | **1.8 / 2.0 (0: 0, 1: 2, 2: 8)** | **15/15 (100%)** | **5/5 (100%)** | **0: 0 câu, 1: 3 câu, 2: 2 câu (ĐTB: 1.4 / 2.0)** |

- **Đường dẫn dữ liệu và trace:**
  - File traces kết quả top-3 từng câu: [`results/traces.json`](../../results/traces.json)
  - Tóm tắt benchmark máy: [`results/benchmark_summary.json`](../../results/benchmark_summary.json)
  - Nhật ký đánh giá thủ công: [`results/MANUAL_AUDIT.md`](../../results/MANUAL_AUDIT.md) và [`results/manual_audit.json`](../../results/manual_audit.json)
  - Báo cáo cá nhân chi tiết: [`report/individual/2A202603930_VuThanh.md`](2A202603930_VuThanh.md)
  - Phương pháp chọn mẫu Coherence: Chọn 10 vị trí trang cố định trải đều toàn bộ 31 trang (`page`: 1, 4, 6, 8, 9, 10, 13, 15, 26, 31).

---

## Phân tích và kết luận
- **So sánh A–B và B–C; 2 ví dụ sai cụ thể:**
  - *A vs B:* Strategy B vượt trội Strategy A hoàn toàn về Coherence (1.8 vs 0.3) và Hit@1 (60% vs 50%). Fixed window (A) cắt đứt câu giữa chừng (cắt cụt từ, cụt số như `,081,277`, `ree cash flow`), xé đôi bảng tài chính và mất sạch header cột khiến 7/10 vị trí bị chấm 0 điểm theo Rubric. Trong khi đó, Recursive (B) bảo toàn ranh giới phân cấp đoạn văn và câu, đạt 1.8/2.0 (chỉ mất điểm ở 2 bảng lớn vượt trần 500 tokens).
  - *B vs C vs D/E:* Strategy C nhóm theo Section lớn nên khi section vượt 500 tokens, nó phải fallback cắt token mù làm đứt ngang câu/bảng khiến Coherence giảm còn 1.2 (có 3 vị trí bị 0 điểm). Strategy D và E bảo tồn trọn vẹn ranh giới đoạn văn bản và khối bảng biểu, đạt Coherence 1.8/2.0 (8 vị trí đạt 2 tuyệt đối, 2 vị trí đạt 1 do 2 bảng tài chính lớn >500 tokens).
  - *2 ví dụ sai điển hình (Failure Analysis):*
    1. **`q16` (Trang 16 / Doc page 18):** Hỏi về việc HĐQT có thể đình chỉ/chấm dứt chương trình mua lại cổ phiếu mà không cần thông báo trước. Chunk chứa bằng chứng trực tiếp (`stre_p15_003`) bị đẩy khỏi Top-3 xếp sau các đoạn mua lại cổ phiếu ở Trang 25 (MD&A) và miễn trừ trách nhiệm ở Trang 17 do Trang 17 chứa cụm từ tương đồng *"without notice"*.
    2. **`q19` (Trang 29):** Hỏi Netflix có sử dụng công cụ phái sinh/hợp đồng ngoại tệ để phòng ngừa rủi ro không. Bằng chứng gốc là câu khẳng định phủ định: *"We do not use foreign exchange contracts..."*. Dense Bi-Encoder BGE-M3 gặp hiện tượng điểm mù phủ định (Negation Blindness), gán điểm cao hơn cho các đoạn phân tích rủi ro biến động tỷ giá khẳng định ở Trang 17 và Trang 6, đẩy Trang 29 xuống Rank 5.
- **Chiến lược chọn, đánh đổi, điều kiện áp dụng:**
  - *Chiến lược tối ưu:* **Strategy E (Paragraph-based Token Chunking + Metadata Filter)**.
  - *Đánh đổi:* Cần thêm bước phân loại và gán metadata chính xác ở tầng tiền xử lý. Nếu truy vấn của người dùng không có thông tin section, hiệu năng sẽ tương đương Strategy D.
  - *Điều kiện áp dụng:* Các tài liệu kỹ thuật, báo cáo tài chính, văn bản luật pháp có cấu trúc phân mục rõ ràng.
- **Hạn chế của dữ liệu, nhãn, test nhỏ, đo thời gian/chi phí:**
  - Tập Test gồm 5 câu là kích thước tương đối nhỏ ($N=5$), mỗi câu tương ứng 20% tổng điểm nên có độ nhạy cảm cao với các câu hỏi phức tạp.
  - Thời gian đo trên phần cứng laptop GPU có thể dao động nhẹ tùy thuộc vào trạng thái điều tiết xung nhịp và nhiệt độ.
- **Nếu làm lại hoặc mở rộng, cải tiến gì?**
  1. Bổ sung **Hybrid Search (BM25 + Dense BGE-M3)**: Giúp bắt chính xác các từ khóa phủ định (`do not use`) và số liệu tài chính tuyệt đối.
  2. Bổ sung **Cross-Encoder Reranker (`bge-reranker-large`)**: Xếp hạng lại Top-10 ứng viên bằng cách chú ý chéo toàn diện giữa câu hỏi và tài liệu, giải quyết triệt để vấn đề phủ định của `q19`.
  3. Mở rộng `top_k = 5`: Cả `q16` (Rank 4) và `q19` (Rank 5) đều nằm trong Top-5, giúp Evidence Coverage của tập Test đạt ngay 80%.
