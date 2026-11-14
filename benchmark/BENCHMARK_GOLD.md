# Bộ câu hỏi Gold Benchmark — Netflix Q2 2023 Form 10-Q

- **Tài liệu nguồn (Corpus):** `NETFLIX_2023Q2_10Q-3-33.pdf` (Báo cáo Quý Q2 2023 nộp SEC của Netflix, Inc., gồm 31 trang vật lý tương ứng trang 3 đến trang 33 của Form 10-Q).
- **Tổng số câu hỏi:** 20 câu.
- **Phân chia split:** 15 Dev / 5 Test (đã chốt trước khi chạy thử nghiệm).
- **Số câu có metadata filter:** 5 câu (3 Dev, 2 Test — thỏa mãn yêu cầu tối thiểu 3 câu filter, ít nhất 1 câu test).
- **Đa dạng các dạng câu hỏi:**
  - Trực tiếp (`truc_tiep`): 7 câu
  - Diễn đạt lại ngữ nghĩa (`dien_dat_lai`): 3 câu
  - Điều kiện / Ngoại lệ (`dieu_kien_ngoai_le`): 5 câu
  - Phân loại / Lọc theo Metadata (`metadata_filter`): 5 câu

---

## 1. Danh sách câu hỏi tập Dev (15 câu)

| ID | Dạng câu | PDF Page (Doc Page) | Câu hỏi | Expected Answer | Filter |
|---|---|---|---|---|---|
| **q01** | Trực tiếp | 1 (Doc 3) | Tổng doanh thu (Revenues) của Netflix trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 là bao nhiêu? | 8.187.301 nghìn USD (khoảng 8,19 tỷ USD) | `None` |
| **q02** | Trực tiếp | 4 (Doc 6) | Tính đến ngày 30 tháng 6 năm 2023, khoản mục tiền và các khoản tương đương tiền (Cash and cash equivalents) trên Bảng cân đối kế toán là bao nhiêu? | 7.662.788 nghìn USD (khoảng 7,66 tỷ USD) | `None` |
| **q03** | Diễn đạt lại | 6 (Doc 8) | Mô hình ghi nhận doanh thu từ phí thành viên hàng tháng của Netflix được thực hiện theo nguyên tắc nào? | Doanh thu được ghi nhận phân bổ đều (ratably) theo từng chu kỳ thành viên hàng tháng, sau khi khách hàng được lập hóa đơn trả trước trước khi kỳ hạn bắt đầu. | `None` |
| **q04** | Metadata Filter | 6 (Doc 8) | Theo Thuyết minh báo cáo tài chính (Notes to Consolidated Financial Statements), các khoản thanh toán cho đối tác (partners) sẽ được ghi nhận giảm trừ doanh thu (reduction of revenues) trong trường hợp nào? | Khi không có dịch vụ riêng biệt nào được cung cấp đổi lại khoản thanh toán, hoặc khi giá thành viên trả do đối tác ấn định và không có giá độc lập cho dịch vụ Netflix (ví dụ gói bundle). | `{"section": "Notes to Consolidated Financial Statements"}` |
| **q05** | Trực tiếp | 7 (Doc 9) | Doanh thu của khu vực Châu Âu, Trung Đông và Châu Phi (EMEA) trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 là bao nhiêu? | 2.562.170 nghìn USD (khoảng 2,56 tỷ USD) | `None` |
| **q06** | Điều kiện / Ngoại lệ | 8 (Doc 10) | Những quyền chọn cổ phiếu nào của nhân viên bị loại trừ khỏi phép tính lãi suy giảm trên mỗi cổ phiếu (diluted EPS) và vì sao? | Các quyền chọn cổ phiếu có giá thực hiện cao hơn giá thị trường trung bình của cổ phiếu phổ thông bị loại khỏi phép tính diluted EPS vì nếu đưa vào, chúng sẽ có tác động chống pha loãng (anti-dilutive), tức làm tăng EPS thay vì làm giảm EPS. | `None` |
| **q07** | Diễn đạt lại | 9 (Doc 11) | Chính sách đầu tư đối với các chứng khoán khả dụng để bán (available-for-sale securities) của Netflix tập trung vào mục tiêu gì và có nhằm kiếm lời chênh lệch giá ngắn hạn không? | Chính sách tập trung vào bảo toàn vốn, duy trì thanh khoản và sinh lời; công ty không nắm giữ chứng khoán vì mục đích tạo lợi nhuận từ biến động chênh lệch giá ngắn hạn. | `None` |
| **q08** | Trực tiếp | 10 (Doc 12) | Giá trị ròng của tài sản nội dung tự sản xuất (Produced content, net) so với nội dung được cấp phép (Licensed content, net) tính đến ngày 30 tháng 6 năm 2023 là bao nhiêu? | Produced content, net là 19.898.365 nghìn USD (khoảng 19,9 tỷ USD) và Licensed content, net là 12.622.409 nghìn USD (khoảng 12,6 tỷ USD). | `None` |
| **q09** | Metadata Filter | 13 (Doc 15) | Theo Thuyết minh Nợ (Note 6 Debt), thỏa thuận tín dụng tuần hoàn (Revolving Credit Agreement) được sửa đổi vào tháng 3 năm 2023 có quy mô hạn mức bao nhiêu và chuyển sang lãi suất tham chiếu nào? | Hạn mức tín dụng tuần hoàn không bảo đảm là 1 tỷ USD, được sửa đổi ngày 6 tháng 3 năm 2023 để thay thế lãi suất LIBOR bằng lãi suất Term SOFR thả nổi. | `{"section": "Notes to Consolidated Financial Statements"}` |
| **q10** | Điều kiện / Ngoại lệ | 13 (Doc 15) | Khi xảy ra sự kiện thay đổi quyền kiểm soát (change of control), chủ sở hữu trái phiếu Senior Notes có quyền yêu cầu Netflix mua lại với mức giá nào? | Bằng 101% giá trị mệnh giá gốc bằng tiền mặt cộng với lãi tích dồn phát sinh. | `None` |
| **q11** | Điều kiện / Ngoại lệ | 14 (Doc 16) | Theo thuyết minh về content obligations, nghĩa vụ mua lại và cấp phép nội dung phát sinh ở thời điểm nào, và khoản content liability được ghi nhận trên Bảng cân đối kế toán khi nào? | Nghĩa vụ mua lại và cấp phép nội dung phát sinh khi Netflix ký thỏa thuận nhận các tựa phim trong tương lai. Tuy nhiên, khoản content liability chỉ được ghi nhận trên Consolidated Balance Sheets khi tựa phim đó trở nên available. | `None` |
| **q12** | Trực tiếp | 18 (Doc 20) | Trong thông báo tháng 4 năm 2023 về dịch vụ DVD-by-mail, Netflix đã lên kế hoạch gì và dự kiến tác động thế nào đến kết quả hoạt động hoặc tài chính? | Netflix công bố kế hoạch dừng dịch vụ gửi DVD qua thư (DVD-by-mail) và dự kiến điều này không gây ảnh hưởng trọng yếu đến hoạt động hoặc kết quả tài chính. | `None` |
| **q13** | Trực tiếp | 18 (Doc 20) | Số lượng thành viên đăng ký xem trực tuyến trả phí tăng thêm ròng (Paid net membership additions) toàn cầu của Netflix trong quý 2 năm 2023 là bao nhiêu so với quý 2 năm 2022? | Tăng thêm 5.892 nghìn thành viên (khoảng 5,89 triệu) trong quý 2 năm 2023, so với mức giảm ròng 969 nghìn thành viên ở quý 2 năm 2022. | `None` |
| **q14** | Metadata Filter | 26 (Doc 28) | Theo phần Thảo luận của Ban giám đốc (Management’s Discussion and Analysis - MD&A), công ty định nghĩa Dòng tiền tự do (Free cash flow) như thế nào? | Dòng tiền tự do được định nghĩa bằng tiền thuần từ hoạt động kinh doanh trừ đi tiền mua sắm tài sản cố định và biến động các tài sản khác. | `{"section": "Management’s Discussion and Analysis"}` |
| **q15** | Diễn đạt lại | 27 (Doc 29) | Dòng tiền tự do (Free Cash Flow) của Netflix trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 đạt bao nhiêu và cải thiện như thế nào so với cùng kỳ năm 2022? | FCF đạt 1.339.260 nghìn USD trong Q2 2023, so với 12.732 nghìn USD trong Q2 2022, tăng 1.326.528 nghìn USD, tương đương 10.419% theo bảng báo cáo. | `None` |

---

## 2. Danh sách câu hỏi tập Test (5 câu)

| ID | Dạng câu | PDF Page (Doc Page) | Câu hỏi | Expected Answer | Filter |
|---|---|---|---|---|---|
| **q16** | Điều kiện / Ngoại lệ | 16 (Doc 18) | Netflix có quyền chấm dứt việc mua lại cổ phiếu phổ thông vào bất kỳ lúc nào mà không cần thông báo trước hay không? | Có, công ty có quyền chấm dứt bất kỳ đợt mua lại cổ phiếu phổ thông nào tại bất kỳ thời điểm nào mà không cần thông báo trước. | `None` |
| **q17** | Trực tiếp | 16 (Doc 18) | Tính đến ngày 30 tháng 6 năm 2023, số tiền còn lại được phép dùng cho chương trình mua lại cổ phiếu của Netflix là bao nhiêu? | 3,4 tỷ USD. | `None` |
| **q18** | Metadata Filter | 9 (Doc 11) | Theo Thuyết minh báo cáo tài chính (Notes to Consolidated Financial Statements), các khoản tiền gửi bị giới hạn sử dụng (restricted cash) trong tài sản ngắn hạn và tài sản dài hạn được phân bổ cho các thỏa thuận nào? | Tài sản ngắn hạn gồm tiền bị hạn chế cho tự bảo hiểm và thỏa thuận thư tín dụng; tài sản dài hạn gồm tiền bị hạn chế cho thỏa thuận thư tín dụng. | `{"section": "Notes to Consolidated Financial Statements"}` |
| **q19** | Điều kiện / Ngoại lệ | 29 (Doc 31) | Netflix có sử dụng các hợp đồng ngoại hối hoặc công cụ phái sinh để phòng ngừa rủi ro phơi nhiễm ngoại tệ hay không? | Không, công ty không sử dụng hợp đồng ngoại hối hay các công cụ phái sinh để phòng ngừa rủi ro tỷ giá. | `None` |
| **q20** | Metadata Filter | 31 (Doc 33) | Theo Phần II - Thông tin khác (Part II. Other Information), có thay đổi trọng yếu nào đối với các yếu tố rủi ro (Risk Factors) so với báo cáo thường niên Form 10-K năm 2022 không? | Không có thay đổi trọng yếu nào so với các yếu tố rủi ro đã công bố trước đó trong Báo cáo thường niên Form 10-K năm 2022. | `{"section": "Other Information"}` |

---

## 3. Cấu trúc lưu trữ dữ liệu JSON
Bộ benchmark được lưu tại: [`benchmark/gold_qa.json`](file:///c:/HUST/VIN/lab6/K5-L3-Day06-DataIngestionEngineering/benchmark/gold_qa.json) với schema chuẩn:
```json
{
  "id": "q01",
  "split": "dev",
  "type": "truc_tiep",
  "question": "...",
  "expected_answer": "...",
  "gold_source_id": "netflix-2023q2-10q",
  "gold_page": 1,
  "doc_page": 3,
  "evidence_quote": "...",
  "filter": null
}
```
Tất cả các đoạn `evidence_quote` đều đã được kiểm tra khớp 100% từng ký tự thực tế trong trang PDF nguồn (`NETFLIX_2023Q2_10Q-3-33.pdf`). Toàn bộ số trang (`gold_page`, `doc_page`) và trích dẫn được neo chặt chẽ theo tài liệu PDF gốc, hoàn toàn độc lập với các artifacts sinh ra từ parser (nhằm loại trừ hoàn toàn nguy cơ data leakage từ quá trình parsing/OCR).
