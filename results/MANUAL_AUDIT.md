# Báo Cáo Audit Thủ Công (Manual Audit Report) — Day 06 Data Ingestion

Theo quy định tại [GUIDE.md](../../GUIDE.md) (Mục 4) và [BENCHMARK.md](../../BENCHMARK.md), báo cáo này ghi nhận kết quả đánh giá thủ công độc lập trên 3 khía cạnh: **Chunk Coherence**, **Metadata Usefulness**, và **Grounding Quality**.

---

## 1. Chunk Coherence (Tính mạch lạc của Chunk)
* **Phương pháp:** Chọn cùng 10 vị trí nội dung cố định trải dài trên 31 trang của báo cáo Netflix Form 10-Q (trước khi xem điểm).
* **Thang điểm chuẩn theo Rubric:**
  - `0`: Bị cắt giữa ý, mất chủ thể, cắt đứt giữa từ/số, hoặc đứt đoạn bảng biểu làm mất ngữ cảnh (không có header cột/dòng làm người đọc không hiểu được).
  - `1`: Hiểu được một phần nhưng thiếu ngữ cảnh mở đầu hoặc điều kiện ràng buộc (hoặc bảng bị chia đôi do giới hạn trần 500 tokens nhưng phần trước vẫn đọc được).
  - `2`: Tự hiểu được độc lập, cấu trúc câu/đoạn trọn vẹn ý nghĩa, khối bảng biểu nguyên vẹn.

| Vị trí | Mô tả nội dung nguồn | Strategy A (Fixed-size) | Strategy B (Recursive) | Strategy C (Section) | Strategy D (Paragraph) | Strategy E (Para + Filter) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Trang 1: Báo cáo kết quả HĐKD (*Statements of Operations*) | 0 (đứt đoạn bảng, mất header cột, mở đầu cụt `\| (355,476) \|`) | 1 (bảng 622 toks vượt trần 500 nên chia 2 chunk, chunk sau thiếu header) | 0 (section dài fallback cắt token mù, đứt bảng biểu mất header) | 1 (bảng 622 toks vượt trần 500 chia 2 chunk, chunk sau thiếu header) | 1 (bảng 622 toks vượt trần 500 chia 2 chunk, chunk sau thiếu header) |
| 2 | Trang 4: Bảng cân đối kế toán (*Balance Sheets*) | 0 (cắt đứt giữa con số `,081,277`, mất toàn bộ cấu trúc bảng) | 1 (bảng 760 toks vượt trần 500 nên ngắt ở Total liabilities, nửa sau thiếu header) | 0 (cắt token mù giữa con số `,081,277`, mất toàn bộ cấu trúc bảng) | 1 (bảng 760 toks vượt trần 500 ngắt tại liabilities, nửa sau thiếu header) | 1 (bảng 760 toks vượt trần 500 ngắt tại liabilities, nửa sau thiếu header) |
| 3 | Trang 6: Thuyết minh 1: Ghi nhận doanh thu hội viên | 0 (cắt đứt ngang giữa con số và dòng bảng biểu) | 2 (đoạn thuyết minh và bảng 210 toks giữ nguyên vẹn) | 2 (giữ trọn vẹn thuyết minh doanh thu) | 2 (khối đoạn văn và bảng nhỏ giữ nguyên vẹn) | 2 (khối đoạn văn và bảng nhỏ giữ nguyên vẹn) |
| 4 | Trang 8: Thuyết minh 2: Loại trừ quyền chọn khỏi Diluted EPS | 0 (cắt mất tiêu đề cột bảng EPS, chunk sau cụt ngủn) | 2 (đoạn thuyết minh và bảng 469 toks trọn vẹn trong 500 toks) | 2 (giữ trọn vẹn thuyết minh EPS) | 2 (giữ trọn vẹn đoạn văn và bảng) | 2 (giữ trọn vẹn đoạn văn và bảng) |
| 5 | Trang 9: Thuyết minh 4: Định nghĩa Tiền gửi bị hạn chế (*Restricted Cash*) | 1 (cắt mất câu dẫn đầu, bảng hiểu được một phần) | 2 (đoạn định nghĩa và bảng 287 toks giữ trọn vẹn ý nghĩa) | 2 (nguyên thuyết minh Note 4) | 2 (đoạn văn bản tự nhiên giữ nguyên) | 2 (đoạn văn bản tự nhiên giữ nguyên) |
| 6 | Trang 10: Thuyết minh 5: Bảng tài sản nội dung tự sản xuất vs cấp phép | 0 (cắt đứt giữa con số `566 \| \| Total`, đứt đoạn bảng biểu) | 2 (các bảng nhỏ 113 và 191 toks đều nằm trọn trong chunk) | 1 (section dài bị ngắt làm mất tiêu đề Note) | 2 (giữ trọn vẹn khối bảng biểu và chú thích) | 2 (giữ trọn vẹn khối bảng biểu và chú thích) |
| 7 | Trang 13: Thuyết minh 6: Điều khoản Senior Notes khi đổi quyền kiểm soát | 0 (cắt cụt giữa chữ `m SOFR Rate`, mất hoàn toàn chủ ngữ câu) | 2 (cắt phân cấp câu hoàn chỉnh, giữ trọn điều khoản) | 2 (giữ nguyên vẹn điều khoản hợp đồng nợ) | 2 (đoạn văn bản trọn vẹn ý nghĩa) | 2 (đoạn văn bản trọn vẹn ý nghĩa) |
| 8 | Trang 15: Thuyết minh 6: Chương trình mua lại cổ phiếu 5 tỷ & 3.4 tỷ còn lại | 1 (cắt câu cuối về điều kiện chấm dứt chương trình) | 2 (đoạn văn bản tự nhiên về Stock Repurchases trọn vẹn) | 2 (nguyên vẹn thuyết minh mua lại cổ phiếu) | 2 (đoạn văn bản độc lập hoàn chỉnh) | 2 (đoạn văn bản độc lập hoàn chỉnh) |
| 9 | Trang 26: MD&A: Định nghĩa Dòng tiền tự do (*Free Cash Flow*) | 0 (cắt giữa từ `ree cash flow` và cụt câu `, the amount`) | 2 (đoạn định nghĩa Free Cash Flow hoàn chỉnh, trọn vẹn) | 0 (fallback cắt token làm đứt giữa câu định nghĩa) | 2 (đoạn văn bản tự nhiên trọn vẹn ý nghĩa) | 2 (đoạn văn bản tự nhiên trọn vẹn ý nghĩa) |
| 10 | Trang 31: Phần II: Item 1A Yếu tố rủi ro (*Risk Factors*) | 1 (cắt giữa câu dẫn bảng Rule 10b5-1) | 2 (khối Item 1A trọn vẹn, bảng Rule 10b5-1 130 toks nguyên vẹn) | 1 (thiếu đoạn mở đầu của bảng Rule 10b5-1) | 2 (đoạn văn và bảng 130 toks trọn vẹn ý nghĩa) | 2 (đoạn văn và bảng 130 toks trọn vẹn ý nghĩa) |
| **Phân bổ** | **Số lượng (0 / 1 / 2)** | **0: 7 câu, 1: 3 câu, 2: 0 câu** | **0: 0 câu, 1: 2 câu, 2: 8 câu** | **0: 3 câu, 1: 2 câu, 2: 5 câu** | **0: 0 câu, 1: 2 câu, 2: 8 câu** | **0: 0 câu, 1: 2 câu, 2: 8 câu** |
| **ĐTB** | **Điểm trung bình Coherence / 2.0** | **0.3 / 2.0** | **1.8 / 2.0** | **1.2 / 2.0** | **1.8 / 2.0** | **1.8 / 2.0** |

---

## 2. Metadata Usefulness (Độ đầy đủ và hữu ích của Siêu dữ liệu)
* **Phương pháp:** Kiểm tra 5 câu hỏi Test $\times$ Top-3 kết quả = 15 chunks được truy xuất cho mỗi chiến lược.
* **Các trường kiểm tra:** `source`, `page`, `doc_page`, `section`, `chunk_id`.
* **Kết quả:**
  - **Strategy A, B, C, D, E:** **15/15 (100%)** bản ghi có metadata đầy đủ, chính xác, map đúng trang vật lý và số trang in trên Form 10-Q.
  - **Tuân thủ bộ lọc (Filter Compliance):**
    - Strategy A, B, C, D: **1/5 (20%)** (chỉ 1 câu vô tình rơi vào đúng section mà không có ràng buộc).
    - Strategy E: **5/5 (100%)** tuân thủ tuyệt đối điều kiện lọc trên Qdrant.

---

## 3. Grounding Quality (Chất lượng Bằng chứng đối với Tập Test)
* **Phương pháp:** Đánh giá Top-3 chunks của 5 câu hỏi Test (`q16` – `q20`).
* **Thang điểm:**
  - `0`: Không có bằng chứng liên quan.
  - `1`: Có bằng chứng liên quan nhưng còn thiếu ngữ cảnh hoặc chưa đủ điều kiện chi tiết để kết luận chắc chắn.
  - `2`: Chứa đầy đủ bằng chứng trực tiếp để trả lời chính xác và truy vết nguồn.

| Query ID | Nội dung câu hỏi Test | Strategy A | Strategy B | Strategy C | Strategy D | Strategy E | Nhận xét chi tiết |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `q16` | Quyền chấm dứt mua lại cổ phiếu không cần báo trước | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các thảo luận mua lại cổ phiếu $5 tỷ (Trang 25) và miễn trừ (Trang 17), thiếu câu trực tiếp ở Trang 16 (Doc page 18 / chunk `stre_p15_003`). |
| `q17` | Số tiền còn lại $3.4 tỷ mua lại cổ phiếu đến 30/6/2023 | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các bảng số liệu tài chính quý 2/2023 (Trang 7, 2, 22), thiếu câu trực tiếp $3.4 tỷ ở Trang 16 (Doc page 18 / chunk `stre_p15_003`). |
| `q18` | Tiền gửi bị hạn chế (Restricted cash) phân bổ cho thỏa thuận nào | 2 | 2 | 2 | 2 | 2 | Chunk Trang 9 xuất hiện trong Top-3 (Rank 2 ở E, Rank 3 ở B) chứa đầy đủ chữ *letters of credit and legal agreements*. |
| `q19` | Có dùng hợp đồng phái sinh phòng ngừa rủi ro ngoại hối không | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các đoạn rủi ro tỷ giá ở Trang 17 và Trang 6, thiếu câu phát biểu phủ định ngắn ở Trang 29 (Rank 5). |
| `q20` | Thay đổi yếu tố rủi ro (Risk Factors) ở Phần II so với 10-K | 2 | 2 | 2 | 2 | 2 | Chunk Trang 31 xuất hiện ở Rank 1 (Strategy E) và Rank 2 (Strategy A-D), cung cấp đầy đủ bằng chứng *no material changes*. |
| **Phân bổ** | **Số lượng (0 / 1 / 2)** | **0: 0 câu, 1: 3 câu, 2: 2 câu** | **0: 0 câu, 1: 3 câu, 2: 2 câu** | **0: 0 câu, 1: 3 câu, 2: 2 câu** | **0: 0 câu, 1: 3 câu, 2: 2 câu** | **0: 0 câu, 1: 3 câu, 2: 2 câu** | **Cả 5 chiến lược đều có 2 câu đạt mức 2, 3 câu đạt mức 1, không có câu nào mức 0.** |
| **ĐTB** | **Điểm trung bình Grounding / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **Tập Test nhỏ (n=5) nên các chiến lược bộc lộ độ nhạy tương đồng trên 3 câu khó.** |
