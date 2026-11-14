# Báo Cáo Audit Thủ Công (Manual Audit Report) — Day 06 Data Ingestion

Theo quy định tại [GUIDE.md](../../GUIDE.md) (Mục 4), báo cáo này ghi nhận kết quả đánh giá thủ công độc lập trên 3 khía cạnh: **Chunk Coherence**, **Metadata Usefulness**, và **Grounding Quality**.

---

## 1. Chunk Coherence (Tính mạch lạc của Chunk)
* **Phương pháp:** Chọn cùng 10 vị trí nội dung cố định trải dài trên 31 trang của báo cáo Netflix Form 10-Q (trước khi xem điểm).
* **Thang điểm:**
  - `0`: Bị cắt giữa ý, mất chủ thể hoặc đứt đoạn bảng biểu làm người đọc không hiểu được.
  - `1`: Hiểu được một phần nhưng thiếu ngữ cảnh mở đầu hoặc điều kiện ràng buộc.
  - `2`: Tự hiểu được độc lập, cấu trúc câu/đoạn trọn vẹn ý nghĩa.

| Vị trí | Mô tả nội dung nguồn | Strategy A (Fixed) | Strategy B (Recursive) | Strategy C (Section) | Strategy D (Paragraph) | Strategy E (Para + Filter) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Trang 1: Tiêu đề Form 10-Q & Báo cáo kết quả HĐKD | 1 (cắt ngang bảng) | 2 (giữ trọn khối) | 2 (khối nguyên vẹn) | 2 (khối nguyên vẹn) | 2 (khối nguyên vẹn) |
| 2 | Trang 4: Bảng cân đối kế toán (Tài sản ngắn hạn & dài hạn) | 1 (cắt giữa bảng) | 2 (giữ nguyên bảng) | 1 (cắt theo token) | 2 (giữ nguyên bảng) | 2 (giữ nguyên bảng) |
| 3 | Trang 6: Thuyết minh 1: Ghi nhận doanh thu hội viên | 2 (vừa vặn window) | 2 (đoạn tự nhiên) | 2 (nguyên thuyết minh) | 2 (đoạn tự nhiên) | 2 (đoạn tự nhiên) |
| 4 | Trang 8: Thuyết minh 2: Loại trừ quyền chọn khỏi Diluted EPS | 1 (mất câu dẫn) | 2 (đoạn tự nhiên) | 2 (nguyên thuyết minh) | 2 (đoạn tự nhiên) | 2 (đoạn tự nhiên) |
| 5 | Trang 9: Thuyết minh 4: Định nghĩa Tiền gửi bị hạn chế (Restricted Cash) | 1 (cắt đôi câu) | 2 (đoạn tự nhiên) | 2 (nguyên thuyết minh) | 2 (đoạn tự nhiên) | 2 (đoạn tự nhiên) |
| 6 | Trang 10: Thuyết minh 5: Bảng tài sản nội dung tự sản xuất vs cấp phép | 1 (cắt đôi bảng) | 2 (giữ trọn bảng) | 1 (cắt theo token) | 2 (giữ trọn bảng) | 2 (giữ trọn bảng) |
| 7 | Trang 13: Thuyết minh 6: Điều khoản Senior Notes khi đổi quyền kiểm soát | 1 (cắt giữa câu) | 2 (đoạn tự nhiên) | 2 (nguyên thuyết minh) | 2 (đoạn tự nhiên) | 2 (đoạn tự nhiên) |
| 8 | Trang 15: Thuyết minh 6: Chương trình mua lại cổ phiếu 5 tỷ & 3.4 tỷ còn lại | 1 (cắt đoạn cuối) | 2 (đoạn tự nhiên) | 2 (nguyên thuyết minh) | 2 (đoạn tự nhiên) | 2 (đoạn tự nhiên) |
| 9 | Trang 26: MD&A: Định nghĩa Dòng tiền tự do (Free Cash Flow) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) |
| 10 | Trang 31: Phần II: Item 1A Yếu tố rủi ro (Risk Factors) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) | 2 (trọn vẹn) |
| **ĐTB** | **Điểm trung bình Coherence / 2.0** | **1.3 / 2.0** | **2.0 / 2.0** | **1.8 / 2.0** | **2.0 / 2.0** | **2.0 / 2.0** |

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
| `q16` | Quyền chấm dứt mua lại cổ phiếu không cần báo trước | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các thảo luận mua lại cổ phiếu $5 tỷ (Trang 25) và miễn trừ (Trang 17), thiếu câu trực tiếp ở Trang 15 (Rank 4). |
| `q17` | Số tiền còn lại $3.4 tỷ mua lại cổ phiếu đến 30/6/2023 | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các bảng số liệu tài chính quý 2/2023 (Trang 7, 2, 22), thiếu câu trực tiếp $3.4 tỷ ở Trang 15. |
| `q18` | Tiền gửi bị hạn chế (Restricted cash) phân bổ cho thỏa thuận nào | 2 | 2 | 2 | 2 | 2 | Chunk Trang 9 xuất hiện trong Top-3 (Rank 2 ở E, Rank 3 ở B) chứa đầy đủ chữ *letters of credit and legal agreements*. |
| `q19` | Có dùng hợp đồng phái sinh phòng ngừa rủi ro ngoại hối không | 1 | 1 | 1 | 1 | 1 | Top-3 chứa các đoạn rủi ro tỷ giá ở Trang 17 và Trang 6, thiếu câu phát biểu phủ định ngắn ở Trang 29 (Rank 5). |
| `q20` | Thay đổi yếu tố rủi ro (Risk Factors) ở Phần II so với 10-K | 2 | 2 | 2 | 2 | 2 | Chunk Trang 31 xuất hiện ở Rank 1 (Strategy E) và Rank 2 (Strategy A-D), cung cấp đầy đủ bằng chứng *no material changes*. |
| **ĐTB** | **Điểm trung bình Grounding / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **1.4 / 2.0** | **2 câu đạt mức 2, 3 câu đạt mức 1, không có câu nào mức 0.** |
