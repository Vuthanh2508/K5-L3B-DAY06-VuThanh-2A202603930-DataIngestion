"""Generate and export the gold benchmark dataset for Netflix Q2 2023 Form 10-Q.

Decoupled generator: Only run this script when explicitly generating or rebuilding
benchmark/gold_qa.json and artifacts/gold_qa.json.
Validation is handled separately by validate_gold.py.
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

QUESTIONS = [
    # --- DEV SET (15 questions: q01 - q15) ---
    {
        "id": "q01",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Tổng doanh thu (Revenues) của Netflix trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 là bao nhiêu?",
        "expected_answer": "8.187.301 nghìn USD (khoảng 8,19 tỷ USD)",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 1,
        "doc_page": 3,
        "evidence_quote": "(in thousands, except per share data)\nThree Months Ended\nSix Months Ended\nJune 30,\n2023\nJune 30,\n2022\nJune 30,\n2023\nJune 30,\n2022\nRevenues\n$\n8,187,301",
        "filter": None
    },
    {
        "id": "q02",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Tính đến ngày 30 tháng 6 năm 2023, khoản mục tiền và các khoản tương đương tiền (Cash and cash equivalents) trên Bảng cân đối kế toán là bao nhiêu?",
        "expected_answer": "7.662.788 nghìn USD (khoảng 7,66 tỷ USD)",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 4,
        "doc_page": 6,
        "evidence_quote": "(in thousands, except share and par value data)\n...\nAs of\nJune 30,\n2023\nDecember 31,\n2022\n(unaudited)\nAssets\nCurrent assets:\nCash and cash equivalents\n$\n7,662,788",
        "filter": None
    },
    {
        "id": "q03",
        "split": "dev",
        "type": "dien_dat_lai",
        "question": "Mô hình ghi nhận doanh thu từ phí thành viên hàng tháng của Netflix được thực hiện theo nguyên tắc nào?",
        "expected_answer": "Doanh thu được ghi nhận phân bổ đều (ratably) theo từng chu kỳ thành viên hàng tháng, sau khi khách hàng được lập hóa đơn trả trước trước khi kỳ hạn bắt đầu.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 6,
        "doc_page": 8,
        "evidence_quote": "Members are billed in advance of the start of their monthly membership and revenues are recognized ratably over each monthly membership period.",
        "filter": None
    },
    {
        "id": "q04",
        "split": "dev",
        "type": "metadata_filter",
        "question": "Theo Thuyết minh báo cáo tài chính (Notes to Consolidated Financial Statements), các khoản thanh toán cho đối tác (partners) sẽ được ghi nhận giảm trừ doanh thu (reduction of revenues) trong trường hợp nào?",
        "expected_answer": "Khi không có dịch vụ riêng biệt nào được cung cấp đổi lại khoản thanh toán, hoặc khi giá thành viên trả do đối tác ấn định và không có giá độc lập cho dịch vụ Netflix (ví dụ gói bundle).",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 6,
        "doc_page": 8,
        "evidence_quote": "However, if there is no distinct service provided in exchange for the payments made to the partners or if the price that the member pays is established by the partners and there is no standalone price for the Netflix service (for instance, in a bundle), these payments are recognized as a reduction of revenues.",
        "filter": {"section": "Notes to Consolidated Financial Statements"}
    },
    {
        "id": "q05",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Doanh thu của khu vực Châu Âu, Trung Đông và Châu Phi (EMEA) trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 là bao nhiêu?",
        "expected_answer": "2.562.170 nghìn USD (khoảng 2,56 tỷ USD)",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 7,
        "doc_page": 9,
        "evidence_quote": "Europe, Middle East, and Africa (EMEA)\nAs of/ Three Months Ended\nAs of/ Six Months Ended\n \nJune 30,\n2023\nJune 30,\n2022\nJune 30,\n2023\nJune 30,\n2022\n \n(in thousands)\nRevenues\n$\n2,562,170",
        "filter": None
    },
    {
        "id": "q06",
        "split": "dev",
        "type": "dieu_kien_ngoai_le",
        "question": "Những quyền chọn cổ phiếu nào của nhân viên bị loại trừ khỏi phép tính lãi suy giảm trên mỗi cổ phiếu (diluted EPS) và vì sao?",
        "expected_answer": "Các quyền chọn cổ phiếu có giá thực hiện cao hơn giá thị trường trung bình của cổ phiếu phổ thông bị loại khỏi phép tính diluted EPS vì nếu đưa vào, chúng sẽ có tác động chống pha loãng (anti-dilutive), tức làm tăng EPS thay vì làm giảm EPS.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 8,
        "doc_page": 10,
        "evidence_quote": "Employee stock options with exercise prices greater than the average market price of the common stock were excluded from the diluted calculation as their inclusion would have been anti-dilutive.",
        "filter": None
    },
    {
        "id": "q07",
        "split": "dev",
        "type": "dien_dat_lai",
        "question": "Chính sách đầu tư đối với các chứng khoán khả dụng để bán (available-for-sale securities) của Netflix tập trung vào mục tiêu gì và có nhằm kiếm lời chênh lệch giá ngắn hạn không?",
        "expected_answer": "Chính sách tập trung vào bảo toàn vốn, duy trì thanh khoản và sinh lời; công ty không nắm giữ chứng khoán vì mục đích tạo lợi nhuận từ biến động chênh lệch giá ngắn hạn.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 9,
        "doc_page": 11,
        "evidence_quote": "The Company does not buy and hold securities principally for the purpose of selling them in the near future. The Company’s policy is focused on the preservation of capital, liquidity and return. From time to time, the Company may sell certain securities but the objectives are generally not to generate profits on short-term differences in price.",
        "filter": None
    },
    {
        "id": "q08",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Giá trị ròng của tài sản nội dung tự sản xuất (Produced content, net) so với nội dung được cấp phép (Licensed content, net) tính đến ngày 30 tháng 6 năm 2023 là bao nhiêu?",
        "expected_answer": "Produced content, net là 19.898.365 nghìn USD (khoảng 19,9 tỷ USD) và Licensed content, net là 12.622.409 nghìn USD (khoảng 12,6 tỷ USD).",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 10,
        "doc_page": 12,
        "evidence_quote": "As of\nJune 30,\n2023\nDecember 31,\n2022\n(in thousands)\nLicensed content, net\n$\n12,622,409\n$\n12,732,549\nProduced content, net\nReleased, less amortization\n9,286,399\n9,110,518\nIn production\n9,796,704\n10,255,940\nIn development and pre-production\n815,262\n637,706\n19,898,365",
        "filter": None
    },
    {
        "id": "q09",
        "split": "dev",
        "type": "metadata_filter",
        "question": "Theo Thuyết minh Nợ (Note 6 Debt), thỏa thuận tín dụng tuần hoàn (Revolving Credit Agreement) được sửa đổi vào tháng 3 năm 2023 có quy mô hạn mức bao nhiêu và chuyển sang lãi suất tham chiếu nào?",
        "expected_answer": "Hạn mức tín dụng tuần hoàn không bảo đảm là 1 tỷ USD, được sửa đổi ngày 6 tháng 3 năm 2023 để thay thế lãi suất LIBOR bằng lãi suất Term SOFR thả nổi.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 13,
        "doc_page": 15,
        "evidence_quote": 'On March 6, 2023, the Company amended its $1\xa0billion unsecured revolving credit facility ("Revolving Credit Agreement") to replace the London interbank offered rate to a variable secured overnight financing rate (the “Term SOFR Rate”)',
        "filter": {"section": "Notes to Consolidated Financial Statements"}
    },
    {
        "id": "q10",
        "split": "dev",
        "type": "dieu_kien_ngoai_le",
        "question": "Khi xảy ra sự kiện thay đổi quyền kiểm soát (change of control), chủ sở hữu trái phiếu Senior Notes có quyền yêu cầu Netflix mua lại với mức giá nào?",
        "expected_answer": "Bằng 101% giá trị mệnh giá gốc bằng tiền mặt cộng với lãi tích dồn phát sinh.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 13,
        "doc_page": 15,
        "evidence_quote": "Each of the Notes are repayable in whole or in part upon the occurrence of a change of control, at the option of the holders, at a purchase price in cash equal to 101% of the principal plus accrued interest.",
        "filter": None
    },
    {
        "id": "q11",
        "split": "dev",
        "type": "dieu_kien_ngoai_le",
        "question": "Theo thuyết minh về content obligations, nghĩa vụ mua lại và cấp phép nội dung phát sinh ở thời điểm nào, và khoản content liability được ghi nhận trên Bảng cân đối kế toán khi nào?",
        "expected_answer": "Nghĩa vụ mua lại và cấp phép nội dung phát sinh khi Netflix ký thỏa thuận nhận các tựa phim trong tương lai. Tuy nhiên, khoản content liability chỉ được ghi nhận trên Consolidated Balance Sheets khi tựa phim đó trở nên available.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 14,
        "doc_page": 16,
        "evidence_quote": "An obligation for the acquisition and licensing of content is incurred at the time the Company enters into an agreement to obtain future titles. Once a title becomes available, a content liability is recorded on the Consolidated Balance Sheets.",
        "filter": None
    },
    {
        "id": "q12",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Trong thông báo tháng 4 năm 2023 về dịch vụ DVD-by-mail, Netflix đã lên kế hoạch gì và dự kiến tác động thế nào đến kết quả hoạt động hoặc tài chính?",
        "expected_answer": "Netflix công bố kế hoạch dừng dịch vụ gửi DVD qua thư (DVD-by-mail) và dự kiến điều này không gây ảnh hưởng trọng yếu đến hoạt động hoặc kết quả tài chính.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 18,
        "doc_page": 20,
        "evidence_quote": "In April 2023, we announced our plans to discontinue our DVD-by-mail service, which we do not expect to have a material effect on our operations or financial results.",
        "filter": None
    },
    {
        "id": "q13",
        "split": "dev",
        "type": "truc_tiep",
        "question": "Số lượng thành viên đăng ký xem trực tuyến trả phí tăng thêm ròng (Paid net membership additions) toàn cầu của Netflix trong quý 2 năm 2023 là bao nhiêu so với quý 2 năm 2022?",
        "expected_answer": "Tăng thêm 5.892 nghìn thành viên (khoảng 5,89 triệu) trong quý 2 năm 2023, so với mức giảm ròng 969 nghìn thành viên ở quý 2 năm 2022.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 18,
        "doc_page": 20,
        "evidence_quote": "As of/ Three Months Ended\nChange\nJune 30,\n2023\nJune 30,\n2022\nQ2'23 vs. Q2'22\n(in thousands, except revenue per membership and percentages)\n...\nGlobal Streaming Memberships:\nPaid net membership additions (losses)\n5,892\n(969)\n6,861\n708 %",
        "filter": None
    },
    {
        "id": "q14",
        "split": "dev",
        "type": "metadata_filter",
        "question": "Theo phần Thảo luận của Ban giám đốc (Management’s Discussion and Analysis - MD&A), công ty định nghĩa Dòng tiền tự do (Free cash flow) như thế nào?",
        "expected_answer": "Dòng tiền tự do được định nghĩa bằng tiền thuần từ hoạt động kinh doanh trừ đi tiền mua sắm tài sản cố định và biến động các tài sản khác.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 26,
        "doc_page": 28,
        "evidence_quote": "We define free cash flow as cash provided by (used in) operating activities less purchases of property and equipment and change in other assets.",
        "filter": {"section": "Management’s Discussion and Analysis"}
    },
    {
        "id": "q15",
        "split": "dev",
        "type": "dien_dat_lai",
        "question": "Dòng tiền tự do (Free Cash Flow) của Netflix trong 3 tháng kết thúc ngày 30 tháng 6 năm 2023 đạt bao nhiêu và cải thiện như thế nào so với cùng kỳ năm 2022?",
        "expected_answer": "FCF đạt 1.339.260 nghìn USD trong Q2 2023, so với 12.732 nghìn USD trong Q2 2022, tăng 1.326.528 nghìn USD, tương đương 10.419% theo bảng báo cáo.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 27,
        "doc_page": 29,
        "evidence_quote": "Three Months Ended\nChange\nJune 30,\n2023\nJune 30,\n2022\nQ2'23 vs. Q2'22\n(in thousands, except percentages)\n...\nFree cash flow\n$\n1,339,260\n$\n12,732  $\n1,326,528\n10,419 %",
        "filter": None
    },

    # --- TEST SET (5 questions: q16 - q20) ---
    {
        "id": "q16",
        "split": "test",
        "type": "dieu_kien_ngoai_le",
        "question": "Netflix có quyền chấm dứt việc mua lại cổ phiếu phổ thông vào bất kỳ lúc nào mà không cần thông báo trước hay không?",
        "expected_answer": "Có, công ty có quyền chấm dứt bất kỳ đợt mua lại cổ phiếu phổ thông nào tại bất kỳ thời điểm nào mà không cần thông báo trước.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 16,
        "doc_page": 18,
        "evidence_quote": "The Company may discontinue any repurchases of its common stock at any time without prior notice.",
        "filter": None
    },
    {
        "id": "q17",
        "split": "test",
        "type": "truc_tiep",
        "question": "Tính đến ngày 30 tháng 6 năm 2023, số tiền còn lại được phép dùng cho chương trình mua lại cổ phiếu của Netflix là bao nhiêu?",
        "expected_answer": "3,4 tỷ USD.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 16,
        "doc_page": 18,
        "evidence_quote": "As of June\xa030, 2023, $3.4\xa0billion remain available for repurchases.",
        "filter": None
    },
    {
        "id": "q18",
        "split": "test",
        "type": "metadata_filter",
        "question": "Theo Thuyết minh báo cáo tài chính (Notes to Consolidated Financial Statements), các khoản tiền gửi bị giới hạn sử dụng (restricted cash) trong tài sản ngắn hạn và tài sản dài hạn được phân bổ cho các thỏa thuận nào?",
        "expected_answer": "Tài sản ngắn hạn gồm tiền bị hạn chế cho tự bảo hiểm và thỏa thuận thư tín dụng; tài sản dài hạn gồm tiền bị hạn chế cho thỏa thuận thư tín dụng.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 9,
        "doc_page": 11,
        "evidence_quote": "Other current assets include restricted cash for deposits related to self insurance and letter of credit agreements. Non-current assets include restricted cash related to letter of credit agreements.",
        "filter": {"section": "Notes to Consolidated Financial Statements"}
    },
    {
        "id": "q19",
        "split": "test",
        "type": "dieu_kien_ngoai_le",
        "question": "Netflix có sử dụng các hợp đồng ngoại hối hoặc công cụ phái sinh để phòng ngừa rủi ro phơi nhiễm ngoại tệ hay không?",
        "expected_answer": "Không, công ty không sử dụng hợp đồng ngoại hối hay các công cụ phái sinh để phòng ngừa rủi ro tỷ giá.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 29,
        "doc_page": 31,
        "evidence_quote": "We do not use foreign exchange contracts or derivatives to hedge any foreign currency exposures.",
        "filter": None
    },
    {
        "id": "q20",
        "split": "test",
        "type": "metadata_filter",
        "question": "Theo Phần II - Thông tin khác (Part II. Other Information), có thay đổi trọng yếu nào đối với các yếu tố rủi ro (Risk Factors) so với báo cáo thường niên Form 10-K năm 2022 không?",
        "expected_answer": "Không có thay đổi trọng yếu nào so với các yếu tố rủi ro đã công bố trước đó trong Báo cáo thường niên Form 10-K năm 2022.",
        "gold_source_id": "netflix-2023q2-10q",
        "gold_page": 31,
        "doc_page": 33,
        "evidence_quote": 'There have been no material changes from the risk factors previously disclosed under the heading "Risk Factors" in the Company\'s Annual Report on Form 10-K for the year ended December 31, 2022.',
        "filter": {"section": "Other Information"}
    }
]


def generate():
    """Write benchmark JSON to benchmark/gold_qa.json and artifacts/gold_qa.json."""
    out_paths = [
        BASE_DIR / "benchmark" / "gold_qa.json",
        BASE_DIR / "artifacts" / "gold_qa.json"
    ]
    for p in out_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(QUESTIONS, f, ensure_ascii=False, indent=2)
        print(f"Generated {len(QUESTIONS)} questions -> {p}")


if __name__ == "__main__":
    generate()
