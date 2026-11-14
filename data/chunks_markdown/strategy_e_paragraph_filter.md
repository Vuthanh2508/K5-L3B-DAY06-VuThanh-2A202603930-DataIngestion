# [Strategy E: Paragraph-Based Token Chunking + Metadata Filter] Văn Bản Báo Cáo Netflix Form 10-Q Tách Theo Chunks
> **Tài liệu nguồn:** `NETFLIX_2023Q2_10Q-3-33.pdf` (31 trang nội dung chuẩn hóa)
> **Thuật toán & Tham số Token:** `{'max_tokens': 500, 'overlap': 50, 'filter': True, 'filter_field': 'section'}`
> **Mô tả:** Nhóm theo đoạn văn bản tự nhiên tối đa 500 tokens, overlap 50 tokens, kết hợp bộ lọc metadata section trên Qdrant.
> **Thống kê:** Tổng cộng **88 chunks** | Tokens: Min 13 - Max 500 - TB 337.4 | Ký tự: Min 64 - Max 2350 - TB 1170.4

---


# 📄 [Trang PDF 01 / Form 10-Q Trang 03] — Mục: *Financial Statements*

### 🔹 [Chunk 001/088] `stre_p01_000` | Trang PDF: 01 (Doc Page: 03) | 32 tokens (112 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 32` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Consolidated Statements of Operations (unaudited)

## (in thousands, except per share data)
```

---

### 🔹 [Chunk 002/088] `stre_p01_001` | Trang PDF: 01 (Doc Page: 03) | 500 tokens (1062 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 500` | `strategy = "strategy_e"`

```markdown
| | Three Months Ended - June 30, 2023 | Three Months Ended - June 30, 2022 | Six Months Ended - June 30, 2023 | Six Months Ended - June 30, 2022 | | --- | --- | --- | --- | --- | | Revenues | $ 8,187,301 | $ 7,970,141 | $ 16,348,804 | $ 15,837,908 | | Cost of revenues | 4,673,470 | 4,690,755 | 9,477,095 | 8,975,460 | | Marketing | 627,168 | 574,960 | 1,182,530 | 1,130,938 | | Technology and development | 657,983 | 716,846 | 1,345,258 | 1,374,376 | | General and administrative | 401,497 | 409,297 | 802,421 | 807,225 | | Operating income | 1,827,183 | 1,578,283 | 3,541,500 | 3,549,909 | | Other income (expense): | | | | | | Interest expense | (174,812) | (175,455) | (349,051) | (363,034) | | Interest and other income (expense) | 26,961 | 220,226 | (44,243) | 415,871 | | Income before income taxes | 1,679,332 | 1,623,054 | 3,148,206 | 3,602,746 | | Provision for income taxes | (191,722) | (182,103) | (355,476) | (564,348) | | Net income | $ 1,487,610 | $ 1,440,951 | $ 2,792,730 | $ 3,038,398 | | Earnings per share: | | | | | | Basic | $ 3.35 | $ 3.
```

---

### 🔹 [Chunk 003/088] `stre_p01_002` | Trang PDF: 01 (Doc Page: 03) | 172 tokens (326 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 172` | `strategy = "strategy_e"`

```markdown
951 | $ 2,792,730 | $ 3,038,398 | | Earnings per share: | | | | | | Basic | $ 3.35 | $ 3.24 | $ 6.28 | $ 6.84 | | Diluted | $ 3.29 | $ 3.20 | $ 6.18 | $ 6.73 | | Weighted-average shares of common stock outstanding: | | | | | | Basic | 443,881 | 444,557 | 444,559 | 444,352 | | Diluted | 451,572 | 450,169 | 451,990 | 451,578 |
```

---

### 🔹 [Chunk 004/088] `stre_p01_003` | Trang PDF: 01 (Doc Page: 03) | 13 tokens (64 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 13` | `strategy = "strategy_e"`

```markdown
See accompanying notes to the consolidated financial statements.
```

---


# 📄 [Trang PDF 02 / Form 10-Q Trang 04] — Mục: *Financial Statements*

### 🔹 [Chunk 005/088] `stre_p02_000` | Trang PDF: 02 (Doc Page: 04) | 242 tokens (632 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 242` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Consolidated Statements of Comprehensive Income (unaudited) (in thousands)

|  | Three Months Ended - June 30, 2023 | Three Months Ended - June 30, 2022 | Six Months Ended - June 30, 2023 | Six Months Ended - June 30, 2022 |
| --- | --- | --- | --- | --- |
| Net income | $ 1,487,610 | $ 1,440,951 | $ 2,792,730 | $ 3,038,398 |
| Other comprehensive income (loss): |  |  |  |  |
| Foreign currency translation adjustments | 52,429 | (70,306) | 78,040 | (103,981) |
| Comprehensive income | $ 1,540,039 | $ 1,370,645 | $ 2,870,770 | $ 2,934,417 |

See accompanying notes to the consolidated financial statements.
```

---


# 📄 [Trang PDF 03 / Form 10-Q Trang 05] — Mục: *Financial Statements*

### 🔹 [Chunk 006/088] `stre_p03_000` | Trang PDF: 03 (Doc Page: 05) | 28 tokens (89 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 28` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Consolidated Statements of Cash Flows

## (unaudited) (in thousands)
```

---

### 🔹 [Chunk 007/088] `stre_p03_001` | Trang PDF: 03 (Doc Page: 05) | 500 tokens (1220 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 500` | `strategy = "strategy_e"`

```markdown
| | Three Months Ended - June 30, 2023 | Three Months Ended - June 30, 2022 | Six Months Ended - June 30, 2023 | Six Months Ended - June 30, 2022 | | --- | --- | --- | --- | --- | | Cash flows from operating activities: | | | | | | Net income | $ 1,487,610 | $ 1,440,951 | $ 2,792,730 | $ 3,038,398 | | Adjustments to reconcile net income to net cash provided by operating activities: | | | | | | Additions to content assets | (3,683,007) | (4,687,011) | (6,141,673) | (8,271,175) | | Change in content liabilities | 46,119 | 191,228 | (308,672) | (155,921) | | Amortization of content assets | 3,410,021 | 3,261,348 | 6,870,005 | 6,427,713 | | Depreciation and amortization of property, equipment and intangibles | 89,385 | 83,505 | 179,720 | 158,107 | | Stock-based compensation expense | 78,030 | 150,392 | 177,129 | 269,601 | | Foreign currency remeasurement loss (gain) on debt | 28,952 | (304,513) | 109,603 | (466,334) | | Other non-cash items | 121,483 | 205,374 | 241,491 | 307,342 | | Deferred income taxes | (103,172) | (115,820) | (201,954) | (184,726) | | Changes in operating assets and liabilities: | | | | | | Other current assets | (183,049) | 123,399 | (271,571) | 164,556 | | Accounts payable | 38,332
```

---

### 🔹 [Chunk 008/088] `stre_p03_002` | Trang PDF: 03 (Doc Page: 05) | 499 tokens (1151 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 499` | `strategy = "strategy_e"`

```markdown
: | | | | | | Other current assets | (183,049) | 123,399 | (271,571) | 164,556 | | Accounts payable | 38,332 | (122,048) | (51,336) | (337,492) | | Accrued expenses and other liabilities | 177,831 | (238,719) | 363,130 | 112,044 | | Deferred revenue | 49,647 | (10,376) | 47,257 | 6,367 | | Other non-current assets and liabilities | (117,950) | 125,040 | (186,887) | (42,891) | | Net cash provided by operating activities | 1,440,232 | 102,750 | 3,618,972 | 1,025,589 | | Cash flows from investing activities: | | | | | | Purchases of property and equipment | (100,972) | (90,018) | (162,991) | (211,176) | | Acquisitions | - | (68,876) | - | (193,397) | | Purchases of short-term investments | (303,228) | - | (504,862) | - | | Proceeds from maturities of short-term investments | 501,937 | - | 501,937 | - | | Net cash provided by (used in) investing activities | 97,737 | (158,894) | (165,916) | (404,573) | | Cash flows from financing activities: | | | | | | Repayments of debt | - | - | - | (700,000) | | Proceeds from issuance of common stock | 34,717 | 11,250 | 60,745 | 24,928 | | Repurchases of common stock | (645,146) | - | (1,045,247) | -
```

---

### 🔹 [Chunk 009/088] `stre_p03_003` | Trang PDF: 03 (Doc Page: 05) | 298 tokens (746 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 298` | `strategy = "strategy_e"`

```markdown
4,717 | 11,250 | 60,745 | 24,928 | | Repurchases of common stock | (645,146) | - | (1,045,247) | - | | Other financing activities | (38,920) | - | (38,920) | - | | Net cash provided by (used in) financing activities | (649,349) | 11,250 | (1,023,422) | (675,072) | | Effect of exchange rate changes on cash, cash equivalents and restricted cash | 39,626 | (145,198) | 66,049 | (156,646) | | Net increase (decrease) in cash, cash equivalents and restricted cash | 928,246 | (190,092) | 2,495,683 | (210,702) | | Cash, cash equivalents and restricted cash at beginning of period | 6,738,019 | 6,034,501 | 5,170,582 | 6,055,111 | | Cash, cash equivalents and restricted cash at end of period | $ 7,666,265 | $ 5,844,409 | $ 7,666,265 | $ 5,844,409 |
```

---

### 🔹 [Chunk 010/088] `stre_p03_004` | Trang PDF: 03 (Doc Page: 05) | 13 tokens (64 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 13` | `strategy = "strategy_e"`

```markdown
See accompanying notes to the consolidated financial statements.
```

---


# 📄 [Trang PDF 04 / Form 10-Q Trang 06] — Mục: *Financial Statements*

### 🔹 [Chunk 011/088] `stre_p04_000` | Trang PDF: 04 (Doc Page: 06) | 26 tokens (96 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 26` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Consolidated Balance Sheets (in thousands, except share and par value data)
```

---

### 🔹 [Chunk 012/088] `stre_p04_001` | Trang PDF: 04 (Doc Page: 06) | 499 tokens (1122 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 499` | `strategy = "strategy_e"`

```markdown
| | As of - June 30, 2023 | As of - December 31, 2022 | | --- | --- | --- | | Assets | (unaudited) | | | Current assets: | | | | Cash and cash equivalents | $ 7,662,788 | $ 5,147,176 | | Short-term investments | 914,201 | 911,276 | | Other current assets | 2,929,347 | 3,208,021 | | Total current assets | 11,506,336 | 9,266,473 | | Content assets, net | 32,520,774 | 32,736,713 | | Property and equipment, net | 1,471,968 | 1,398,257 | | Other non-current assets | 5,318,395 | 5,193,325 | | Total assets | $ 50,817,473 | $ 48,594,768 | | Liabilities and Stockholders' Equity | | | | Current liabilities: | | | | Current content liabilities | $ 4,440,412 | $ 4,480,150 | | Accounts payable | 615,374 | 671,513 | | Accrued expenses and other liabilities | 1,908,714 | 1,514,650 | | Deferred revenue | 1,311,918 | 1,264,661 | | Short-term debt | 399,387 | - | | Total current liabilities | 8,675,805 | 7,930,974 | | Non-current content liabilities | 2,849,387 | 3,081,277 | | Long-term debt | 14,070,151 | 14,353,076 | | Other non-current liabilities | 2,389,915 | 2,452,040 | | Total liabilities | 27,985,258 | 27,817,367 |
```

---

### 🔹 [Chunk 013/088] `stre_p04_002` | Trang PDF: 04 (Doc Page: 06) | 310 tokens (806 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 310` | `strategy = "strategy_e"`

```markdown
| | Other non-current liabilities | 2,389,915 | 2,452,040 | | Total liabilities | 27,985,258 | 27,817,367 | | Commitments and contingencies (Note 7) | | | | Stockholders' equity: | | | | Common stock, $0.001 par value; 4,990,000,000 shares authorized at June 30, 2023 and December 31, 2022; 443,146,751 and 445,346,776 issued and outstanding at June 30, 2023 and December 31, 2022, respectively | 4,874,208 | 4,637,601 | | Treasury stock at cost (4,635,858 and 1,564,478 shares at June 30, 2023 and December 31, 2022, respectively) | (1,876,753) | (824,190) | | Accumulated other comprehensive loss | (139,266) | (217,306) | | Retained earnings | 19,974,026 | 17,181,296 | | Total stockholders' equity | 22,832,215 | 20,777,401 | | Total liabilities and stockholders' equity | $ 50,817,473 | $ 48,594,768 |
```

---

### 🔹 [Chunk 014/088] `stre_p04_003` | Trang PDF: 04 (Doc Page: 06) | 13 tokens (64 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 13` | `strategy = "strategy_e"`

```markdown
See accompanying notes to the consolidated financial statements.
```

---


# 📄 [Trang PDF 05 / Form 10-Q Trang 07] — Mục: *Financial Statements*

### 🔹 [Chunk 015/088] `stre_p05_000` | Trang PDF: 05 (Doc Page: 07) | 30 tokens (95 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 30` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Consolidated Statements of Stockholders' Equity (unaudited) (in thousands)
```

---

### 🔹 [Chunk 016/088] `stre_p05_001` | Trang PDF: 05 (Doc Page: 07) | 500 tokens (1135 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 500` | `strategy = "strategy_e"`

```markdown
| | Three Months Ended - June 30, 2023 | Three Months Ended - June 30, 2022 | Six Months Ended - June 30, 2023 | Six Months Ended - June 30, 2022 | | --- | --- | --- | --- | --- | | Total stockholders' equity, beginning balances | $ 21,828,196 | $ 17,544,039 | $ 20,777,401 | $ 15,849,248 | | Common stock and additional paid-in capital: | | | | | | Beginning balances | $ 4,762,395 | $ 4,155,580 | $ 4,637,601 | $ 4,024,561 | | Issuance of common stock upon exercise of options | 33,783 | 10,898 | 59,478 | 22,708 | | Stock-based compensation expense | 78,030 | 150,392 | 177,129 | 269,601 | | Ending balances | $ 4,874,208 | $ 4,316,870 | $ 4,874,208 | $ 4,316,870 | | Treasury stock: | | | | | | Beginning balances | $ (1,228,920) | $ (824,190) | $ (824,190) | $ (824,190) | | Repurchases of common stock to be held as treasury stock | (647,833) | - | (1,052,563) | - | | Ending balances | $ (1,876,753) | $ (824,190) | $ (1,876,753) | $ (824,190) | | Accumulated other comprehensive loss: | | | | | | Beginning balances | $ (191,695) | $ (74,170) | $ (217,306) | $ (40,495) | | Other comprehensive income (loss) | 52,429 | (70,306)
```

---

### 🔹 [Chunk 017/088] `stre_p05_002` | Trang PDF: 05 (Doc Page: 07) | 278 tokens (571 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 278` | `strategy = "strategy_e"`

```markdown
(191,695) | $ (74,170) | $ (217,306) | $ (40,495) | | Other comprehensive income (loss) | 52,429 | (70,306) | 78,040 | (103,981) | | Ending balances | $ (139,266) | $ (144,476) | $ (139,266) | $ (144,476) | | Retained earnings: | | | | | | Beginning balances | $ 18,486,416 | $ 14,286,819 | $ 17,181,296 | $ 12,689,372 | | Net income | 1,487,610 | 1,440,951 | 2,792,730 | 3,038,398 | | Ending balances | $ 19,974,026 | $ 15,727,770 | $ 19,974,026 | $ 15,727,770 | | Total stockholders' equity, ending balances | $ 22,832,215 | $ 19,075,974 | $ 22,832,215 | $ 19,075,974 |
```

---

### 🔹 [Chunk 018/088] `stre_p05_003` | Trang PDF: 05 (Doc Page: 07) | 13 tokens (64 ký tự)
> **Metadata:** `section = "Financial Statements"` | `tokens = 13` | `strategy = "strategy_e"`

```markdown
See accompanying notes to the consolidated financial statements.
```

---


# 📄 [Trang PDF 06 / Form 10-Q Trang 08] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 019/088] `stre_p06_000` | Trang PDF: 06 (Doc Page: 08) | 453 tokens (2126 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 453` | `strategy = "strategy_e"`

```markdown
## NETFLIX, INC.

## Notes to Consolidated Financial Statements (unaudited)

## 1. Basis of Presentation and Summary of Significant Accounting Policies

The accompanying interim consolidated financial statements of Netflix, Inc. and its wholly owned subsidiaries (the 'Company') have been prepared in conformity with accounting principles generally accepted in the United States ('U.S.') and are consistent in all material respects with those applied in the Company's Annual Report on Form 10-K for the year ended December 31, 2022 filed with the Securities and Exchange Commission (the 'SEC') on January 26, 2023. The preparation of consolidated financial statements in conformity with U.S. generally accepted accounting principles ('GAAP') requires management to make estimates and judgments that affect the amounts reported in the consolidated financial statements and accompanying notes. Significant items subject to such estimates and assumptions include the amortization of content assets and the recognition and measurement of income tax assets and liabilities. The Company bases its estimates on historical experience and on various other assumptions that the Company believes to be reasonable under the circumstances. On a regular basis, the Company evaluates the assumptions, judgments and estimates. Actual results may differ from these estimates.

The interim financial information is unaudited, but reflects all normal recurring adjustments that are, in the opinion of management, necessary to fairly present the information set forth herein. The interim consolidated financial statements should be read in conjunction with the audited consolidated financial statements and related notes included in the Company's Annual Report on Form 10-K for the year ended December 31, 2022. Interim results are not necessarily indicative of the results for a full year.

There have been no material changes in the Company's significant accounting policies as compared to the significant accounting policies described in the Company's Annual Report on Form 10-K for the year ended December 31, 2022.

## 2. Revenue Recognition
```

---

### 🔹 [Chunk 020/088] `stre_p06_001` | Trang PDF: 06 (Doc Page: 08) | 334 tokens (1578 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 334` | `strategy = "strategy_e"`

```markdown
The Company's primary source of revenues is from monthly membership fees. Members are billed in advance of the start of their monthly membership and revenues are recognized ratably over each monthly membership period. Revenues are presented net of the taxes that are collected from members and remitted to governmental authorities. The Company is the principal in all its relationships where partners, including consumer electronics ('CE') manufacturers, multichannel video programming distributors ('MVPDs'), mobile operators and internet service providers ('ISPs'), provide access to the service as the Company retains control over service delivery to its members. Typically, payments made to the partners, such as for marketing, are expensed. However, if there is no distinct service provided in exchange for the payments made to the partners or if the price that the member pays is established by the partners and there is no standalone price for the Netflix service (for instance, in a bundle), these payments are recognized as a reduction of revenues.

The Company also earns revenue from advertisements presented on its streaming service, consumer products and various other sources. Revenues earned from sources other than monthly membership fees were not material for the three and six months ended June 30, 2023 and June 30, 2022.

The following tables summarize revenues, paid net membership additions (losses), and ending paid memberships by region for the three and six months ended June 30, 2023 and June 30, 2022, respectively:

## United States and Canada (UCAN)
```

---

### 🔹 [Chunk 021/088] `stre_p06_002` | Trang PDF: 06 (Doc Page: 08) | 210 tokens (502 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 210` | `strategy = "strategy_e"`

```markdown
|  | As of/ Three Months Ended - June 30, 2023 - (in thousands) | As of/ Three Months Ended - June 30, 2022 - (in thousands) | As of/ Six Months Ended - June 30, 2023 - (in thousands) | As of/ Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Revenues | $ 3,599,448 | $ 3,537,863 | $ 7,208,093 | $ 6,888,287 |
| Paid net membership additions (losses) | 1,173 | (1,296) | 1,275 | (1,932) |
| Paid memberships at end of period (1) | 75,571 | 73,283 | 75,571 | 73,283 |
```

---


# 📄 [Trang PDF 07 / Form 10-Q Trang 09] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 022/088] `stre_p07_000` | Trang PDF: 07 (Doc Page: 09) | 444 tokens (1088 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 444` | `strategy = "strategy_e"`

```markdown
## Europe, Middle East, and Africa (EMEA)

|  | As of/ Three Months Ended - June 30, 2023 - (in thousands) | As of/ Three Months Ended - June 30, 2022 - (in thousands) | As of/ Six Months Ended - June 30, 2023 - (in thousands) | As of/ Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Revenues | $ 2,562,170 | $ 2,457,235 | $ 5,079,811 | $ 5,019,066 |
| Paid net membership additions (losses) | 2,434 | (767) | 3,078 | (1,070) |
| Paid memberships at end of period (1) | 79,807 | 72,966 | 79,807 | 72,966 |

## Latin America (LATAM)

|  | As of/ Three Months Ended - June 30, 2023 - (in thousands) | As of/ Three Months Ended - June 30, 2022 - (in thousands) | As of/ Six Months Ended - June 30, 2023 - (in thousands) | As of/ Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Revenues | $ 1,077,435 | $ 1,030,234 | $ 2,147,627 | $ 2,029,182 |
| Paid net membership additions (losses) | 1,217 | 14 | 767 | (337) |
| Paid memberships at end of period (1) | 42,466 | 39,624 | 42,466 | 39,624 |

## Asia-Pacific (APAC)
```

---

### 🔹 [Chunk 023/088] `stre_p07_001` | Trang PDF: 07 (Doc Page: 09) | 411 tokens (1467 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 411` | `strategy = "strategy_e"`

```markdown
|  | As of/ Three Months Ended - June 30, 2023 - (in thousands) | As of/ Three Months Ended - June 30, 2022 - (in thousands) | As of/ Six Months Ended - June 30, 2023 - (in thousands) | As of/ Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Revenues | $ 919,273 | $ 907,719 | $ 1,852,796 | $ 1,824,473 |
| Paid net membership additions (losses) | 1,068 | 1,080 | 2,523 | 2,167 |
| Paid memberships at end of period (1) | 40,546 | 34,799 | 40,546 | 34,799 |

(1) A paid membership (also referred to as a paid subscription) is defined as a membership that has the right to receive Netflix service following sign-up and a method of payment being provided, and that is not part of a free trial or certain other promotions that may be offered by the Company to new or rejoining members. Certain members have the option to add extra member sub accounts. These extra member sub accounts are not included in paid memberships. A membership is canceled and ceases to be reflected in the above metrics as of the effective cancellation date. V oluntary cancellations generally become effective at the end of the prepaid membership period. Involuntary cancellations, as a result of a failed method of payment, become effective immediately. Memberships are assigned to territories based on the geographic location used at time of sign-up as determined by the Company's internal systems, which utilize industry standard geo-location technology.
```

---

### 🔹 [Chunk 024/088] `stre_p07_002` | Trang PDF: 07 (Doc Page: 09) | 291 tokens (1281 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 291` | `strategy = "strategy_e"`

```markdown
Total U.S. revenues, inclusive of DVD revenues not reported in the tables above, were $3.3 billion and $6.6 billion, respectively, for the three and six months ended June 30, 2023 and $3.3 billion and $6.4 billion, respectively, for the three and six months ended June 30, 2022. DVD revenues were $29 million and $60 million, respectively, for the three and six months ended June 30, 2023 and $37 million and $77 million, respectively, for the three and six months ended June 30, 2022.

Deferred revenue consists of membership fees billed that have not been recognized, as well as gift cards and other prepaid memberships that have not been fully redeemed. As of June 30, 2023, total deferred revenue was $1,312 million, the vast majority of which was related to membership fees billed that are expected to be recognized as revenue within the next month. The remaining deferred revenue balance, which is related to gift cards and other prepaid memberships, will be recognized as revenue over the period of service after redemption, which is expected to occur over the next 12 months. The $47 million increase in deferred revenue as compared to the balance of $1,265 million as of December 31, 2022 is a result of the increase in membership fees billed due to increased memberships.
```

---


# 📄 [Trang PDF 08 / Form 10-Q Trang 10] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 025/088] `stre_p08_000` | Trang PDF: 08 (Doc Page: 10) | 115 tokens (517 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 115` | `strategy = "strategy_e"`

```markdown
## 3. Earnings Per Share

Basic earnings per share is computed using the weighted-average number of outstanding shares of common stock during the period. Diluted earnings per share is computed using the weighted-average number of outstanding shares of common stock and, when dilutive, potential outstanding shares of common stock during the period. Potential shares of common stock consist of incremental shares issuable upon the assumed exercise of stock options. The computation of earnings per share is as follows:
```

---

### 🔹 [Chunk 026/088] `stre_p08_001` | Trang PDF: 08 (Doc Page: 10) | 469 tokens (1117 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 469` | `strategy = "strategy_e"`

```markdown
|  | Three Months Ended - June 30, 2023 - (in thousands, except per share data) | Three Months Ended - June 30, 2022 - (in thousands, except per share data) | Six Months Ended - June 30, 2023 - (in thousands, except per share data) | Six Months Ended - June 30, 2022 - (in thousands, except per share data) |
| --- | --- | --- | --- | --- |
| Basic earnings per share: |  |  |  |  |
| Net income | $ 1,487,610 | $ 1,440,951 | $ 2,792,730 | $ 3,038,398 |
| Shares used in computation: |  |  |  |  |
| Weighted-average shares of common stock outstanding | 443,881 | 444,557 | 444,559 | 444,352 |
| Basic earnings per share | $ 3.35 | $ 3.24 | $ 6.28 | $ 6.84 |
| Diluted earnings per share: |  |  |  |  |
| Net income | $ 1,487,610 | $ 1,440,951 | $ 2,792,730 | $ 3,038,398 |
| Shares used in computation: |  |  |  |  |
| Weighted-average shares of common stock outstanding | 443,881 | 444,557 | 444,559 | 444,352 |
| Employee stock options | 7,691 | 5,612 | 7,431 | 7,226 |
| Weighted-average number of shares | 451,572 | 450,169 | 451,990 | 451,578 |
| Diluted earnings per share | $ 3.29 | $ 3.20 | $ 6.18 | $ 6.73 |
```

---

### 🔹 [Chunk 027/088] `stre_p08_002` | Trang PDF: 08 (Doc Page: 10) | 187 tokens (610 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 187` | `strategy = "strategy_e"`

```markdown
Employee stock options with exercise prices greater than the average market price of the common stock were excluded from the diluted calculation as their inclusion would have been anti-dilutive. The following table summarizes the potential shares of common stock excluded from the diluted calculation:

|  | Three Months Ended - June 30, 2023 - (in thousands) | Three Months Ended - June 30, 2022 - (in thousands) | Six Months Ended - June 30, 2023 - (in thousands) | Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Employee stock options | 4,348 | 8,175 | 5,097 | 5,462 |
```

---


# 📄 [Trang PDF 09 / Form 10-Q Trang 11] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 028/088] `stre_p09_000` | Trang PDF: 09 (Doc Page: 11) | 438 tokens (1348 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 438` | `strategy = "strategy_e"`

```markdown
## 4. Cash, Cash Equivalents, Restricted Cash, and Short-term Investments

The Company's investment policy is consistent with the definition of available-for-sale securities. The Company does not buy and hold securities principally for the purpose of selling them in the near future. The Company's policy is focused on the preservation of capital, liquidity and return. From time to time, the Company may sell certain securities but the objectives are generally not to generate profits on short-term differences in price. The following tables summarize the Company's cash, cash equivalents, restricted cash and short-term investments as of June 30, 2023 and December 31, 2022:

|  | As of June 30, 2023 - Cash and cash equivalents - (in thousands) | As of June 30, 2023 - Short-term investments - (in thousands) | As of June 30, 2023 - Other Current Assets - (in thousands) | As of June 30, 2023 - Non-current Assets - (in thousands) | As of June 30, 2023 - Total - (in thousands) |
| --- | --- | --- | --- | --- | --- |
| Cash | $ 4,662,668 | $ - | $ 1,763 | $ 1,660 | $ 4,666,091 |
| Level 1 securities: |  |  |  |  |  |
| Money market funds | 2,628,351 | - | - | 54 | 2,628,405 |
| Level 2 securities: |  |  |  |  |  |
| Time Deposits (1) | 371,769 | 914,201 | - | - | 1,285,970 |
|  | $ 7,662,788 | $ 914,201 | $ 1,763 | $ 1,714 | $ 8,580,466 |
```

---

### 🔹 [Chunk 029/088] `stre_p09_001` | Trang PDF: 09 (Doc Page: 11) | 464 tokens (1563 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 464` | `strategy = "strategy_e"`

```markdown
|  | As of December 31, 2022 - Cash and cash equivalents - (in thousands) | As of December 31, 2022 - Short-term investments - (in thousands) | As of December 31, 2022 - Other Current Assets - (in thousands) | As of December 31, 2022 - Non-current Assets - (in thousands) | As of December 31, 2022 - Total - (in thousands) |
| --- | --- | --- | --- | --- | --- |
| Cash | $ 4,071,584 | $ - | $ 3,410 | $ 19,874 | $ 4,094,868 |
| Level 1 securities: |  |  |  |  |  |
| Money market funds | 569,826 | - | - | 122 | 569,948 |
| Level 2 securities: |  |  |  |  |  |
| Time Deposits (1) | 505,766 | 911,276 | - | - | 1,417,042 |
|  | $ 5,147,176 | $ 911,276 | $ 3,410 | $ 19,996 | $ 6,081,858 |

(1) The majority of the Company's time deposits are domestic deposits, which mature within one year.

Other current assets include restricted cash for deposits related to self insurance and letter of credit agreements. Non-current assets include restricted cash related to letter of credit agreements. The fair value of cash equivalents and short-term investments included in the Level 2 category is based on observable inputs, such as quoted prices for similar assets at the measurement date; quoted prices in markets that are not active; or other inputs that are observable, either directly or indirectly.

See Note 6 Debt to the consolidated financial statements for further information regarding the fair value of the Company's senior notes.

There were no material gross realized gains or losses in the three and six months ended June 30, 2023 and 2022, respectively.
```

---


# 📄 [Trang PDF 10 / Form 10-Q Trang 12] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 030/088] `stre_p10_000` | Trang PDF: 10 (Doc Page: 12) | 473 tokens (1410 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 473` | `strategy = "strategy_e"`

```markdown
## 5. Balance Sheet Components

## Content Assets, Net

Content assets consisted of the following:

|  | As of - June 30, 2023 - (in thousands) | As of - December 31, 2022 - (in thousands) |
| --- | --- | --- |
| Licensed content, net | $ 12,622,409 | $ 12,732,549 |
| Produced content, net |  |  |
| Released, less amortization | 9,286,399 | 9,110,518 |
| In production | 9,796,704 | 10,255,940 |
| In development and pre-production | 815,262 | 637,706 |
|  | 19,898,365 | 20,004,164 |
| Content assets, net | $ 32,520,774 | $ 32,736,713 |

As of June 30, 2023, approximately $5,495 million, $2,844 million, and $1,971 million of the $12,622 million unamortized cost of the licensed content is expected to be amortized in each of the next three years. As of June 30, 2023, approximately $3,544 million, $2,420 million, and $1,710 million of the $9,286 million unamortized cost of the produced content that has been released is expected to be amortized in each of the next three years.

As of June 30, 2023, the amount of accrued participations and residuals was not material.

The following table represents the amortization of content assets:

|  | Three Months Ended - June 30, 2023 - (in thousands) | Three Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- |
| Licensed content | $ 1,779,321 | $ 1,899,782 |
| Produced content | 1,630,700 | 1,361,566 |
| Total | $ 3,410,021 | $ 3,261,348 |
```

---

### 🔹 [Chunk 031/088] `stre_p10_001` | Trang PDF: 10 (Doc Page: 12) | 114 tokens (260 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 114` | `strategy = "strategy_e"`

```markdown
|  | Six Months Ended - June 30, 2023 - (in thousands) | Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- |
| Licensed content | $ 3,502,999 | $ 3,784,220 |
| Produced content | 3,367,006 | 2,643,493 |
| Total | $ 6,870,005 | $ 6,427,713 |
```

---


# 📄 [Trang PDF 11 / Form 10-Q Trang 13] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 032/088] `stre_p11_000` | Trang PDF: 11 (Doc Page: 13) | 481 tokens (1455 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 481` | `strategy = "strategy_e"`

```markdown
## Property and Equipment, Net

Property and equipment and accumulated depreciation consisted of the following:

|  | As of - June 30, 2023 - (in thousands) | As of - December 31, 2022 - (in thousands) | Estimated Useful Lives |
| --- | --- | --- | --- |
| Land | $ 86,662 | $ 85,005 |  |
| Buildings | 60,720 | 52,106 | 30 years |
| Leasehold improvements | 1,068,757 | 1,040,570 | Over life of lease |
| Furniture and fixtures | 155,401 | 153,682 | 3 years |
| Information technology | 461,590 | 442,681 | 3 years |
| Corporate aircraft | 133,998 | 115,578 | 8-10 years |
| Machinery and equipment | 27,384 | 26,821 | 3-5 years |
| Capital work-in-progress | 348,194 | 235,555 |  |
| Property and equipment, gross | 2,342,706 | 2,151,998 |  |
| Less: Accumulated depreciation | (870,738) | (753,741) |  |
| Property and equipment, net | $ 1,471,968 | $ 1,398,257 |  |

## Leases

The Company has entered into operating leases primarily for real estate. Operating leases are included in "Other non-current assets" on the Company's Consolidated Balance Sheets, and represent the Company's right to use the underlying asset for the lease term. The Company's obligations to make lease payments are included in "Accrued expenses and other liabilities" and "Other non-current liabilities" on the Company's Consolidated Balance Sheets.

Information related to the Company's operating right-of-use assets and related operating lease liabilities were as follows:
```

---

### 🔹 [Chunk 033/088] `stre_p11_001` | Trang PDF: 11 (Doc Page: 13) | 423 tokens (1117 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 423` | `strategy = "strategy_e"`

```markdown
|  | Three Months Ended - June 30, 2023 - (in thousands) | Three Months Ended - (in thousands) | Three Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- |
| Cash paid for operating lease liabilities | $ | 114,760 $ | 99,758 |
| Right-of-use assets obtained in exchange for new operating lease obligations |  | 91,572 | 39,304 |

|  | Six Months Ended - June 30, 2023 - (in thousands) | Six Months Ended - (in thousands) | Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- |
| Cash paid for operating lease liabilities | $ | 228,167 $ | 202,899 |
| Right-of-use assets obtained in exchange for new operating lease obligations |  | 112,466 | 180,602 |

|  | As of - June 30, 2023 - (in thousands) | As of - (in thousands) | As of - December 31, 2022 - (in thousands) |
| --- | --- | --- | --- |
| Operating lease right-of-use assets, net | $ | 2,187,732 $ | 2,227,122 |
| Current operating lease liabilities |  | 376,847 | 355,985 |
| Non-current operating lease liabilities |  | 2,147,306 | 2,222,503 |
| Total operating lease liabilities | $ | 2,524,153 $ | 2,578,488 |
```

---


# 📄 [Trang PDF 12 / Form 10-Q Trang 14] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 034/088] `stre_p12_000` | Trang PDF: 12 (Doc Page: 14) | 428 tokens (1543 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 428` | `strategy = "strategy_e"`

```markdown
## Other Current Assets

Other current assets consisted of the following:

|  | As of - June 30, 2023 - (in thousands) | As of - December 31, 2022 - (in thousands) |
| --- | --- | --- |
| Trade receivables | $ 1,218,326 | $ 988,898 |
| Prepaid expenses | 481,546 | 392,735 |
| Other | 1,229,475 | 1,826,388 |
| Total other current assets | $ 2,929,347 | $ 3,208,021 |

The decrease in Other was primarily driven by receipt of amounts due under a modified content licensing arrangement.

## 6. Debt

As of June 30, 2023, the Company had aggregate outstanding notes of $14,470 million, net of $72 million of issuance costs, with varying maturities (the "Notes"). Of the outstanding balance, $399 million, net of issuance costs, is classified as short-term debt on the Consolidated Balance Sheets. As of December 31, 2022, the Company had aggregate outstanding notes of $14,353 million, net of $79 million of issuance costs. Each of the Notes were issued at par and are senior unsecured obligations of the Company. Interest is payable semi-annually at fixed rates. A portion of the outstanding Notes is denominated in foreign currency (comprised of €5,170 million) and is remeasured into U.S. dollars at each balance sheet date (with remeasurement loss totaling $29 million and $110 million, respectively, for the three and six months ended June 30, 2023).

The following table provides a summary of the Company's outstanding debt and the fair values based on quoted market prices in less active markets as of June 30, 2023 and December 31, 2022:
```

---

### 🔹 [Chunk 035/088] `stre_p12_001` | Trang PDF: 12 (Doc Page: 14) | 500 tokens (1256 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 500` | `strategy = "strategy_e"`

```markdown
| | Principal Amount at Par - June 30, 2023 - (in millions) | Principal Amount at Par - December 31, 2022 - (in millions) | Principal Amount at Par - Issuance Date | Maturity | Level 2 Fair Value as of - June 30, 2023 - (in millions) | Level 2 Fair Value as of - December 31, 2022 - (in millions) | | --- | --- | --- | --- | --- | --- | --- | | 5.750% Senior Notes | $ 400 | $ 400 | February 2014 | March 2024 | $ 401 | $ 404 | | 5.875% Senior Notes | 800 | 800 | February 2015 | February 2025 | 804 | 811 | | 3.000% Senior Notes (1) | 513 | 503 | April 2020 | June 2025 | 503 | 495 | | 3.625% Senior Notes | 500 | 500 | April 2020 | June 2025 | 483 | 479 | | 4.375% Senior Notes | 1,000 | 1,000 | October 2016 | November 2026 | 979 | 980 | | 3.625% Senior Notes (1) | 1,419 | 1,391 | May 2017 | May 2027 | 1,387 | 1,338 | | 4.875% Senior Notes | 1,600 | 1,600 | October 2017 | April 2028 | 1,584 | 1,557 | | 5.875% Senior Notes | 1,900 | 1,900 | April 2018 | November 2028 | 1,972 | 1,930 | | 4.625% Senior Notes (1) | 1,200 | 1,177 | October 2018 | May 2029 | 1,216 | 1,151 | | 6.375% Senior Notes | 800 | 800 | October 2018 | May 2029 | 848 | 830 | | 3.875% Senior Notes (1) | 1,310 | 1,284 | April 2019 | November 2029 | 1,279 | 1,201 | | 5.375% Senior
```

---

### 🔹 [Chunk 036/088] `stre_p12_002` | Trang PDF: 12 (Doc Page: 14) | 179 tokens (397 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 179` | `strategy = "strategy_e"`

```markdown
| 848 | 830 | | 3.875% Senior Notes (1) | 1,310 | 1,284 | April 2019 | November 2029 | 1,279 | 1,201 | | 5.375% Senior Notes | 900 | 900 | April 2019 | November 2029 | 904 | 885 | | 3.625% Senior Notes (1) | 1,200 | 1,177 | October 2019 | June 2030 | 1,145 | 1,078 | | 4.875% Senior Notes | 1,000 | 1,000 | October 2019 | June 2030 | 986 | 944 | | | $ 14,542 | $ 14,432 | | | $ 14,491 | $ 14,083 |
```

---

### 🔹 [Chunk 037/088] `stre_p12_003` | Trang PDF: 12 (Doc Page: 14) | 79 tokens (277 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 79` | `strategy = "strategy_e"`

```markdown
(1) The following Senior Notes have a principal amount denominated in euro: 3.000% Senior Notes for €470 million, 3.625% Senior Notes for €1,300 million, 4.625% Senior Notes for €1,100 million, 3.875% Senior Notes for €1,200 million, and 3.625% Senior Notes for €1,100 million.
```

---


# 📄 [Trang PDF 13 / Form 10-Q Trang 15] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 038/088] `stre_p13_000` | Trang PDF: 13 (Doc Page: 15) | 395 tokens (1671 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 395` | `strategy = "strategy_e"`

```markdown
Each of the Notes are repayable in whole or in part upon the occurrence of a change of control, at the option of the holders, at a purchase price in cash equal to 101% of the principal plus accrued interest. The Company may redeem the Notes prior to maturity in whole or in part at an amount equal to the principal amount thereof plus accrued and unpaid interest and an applicable premium. The Notes include, among other terms and conditions, limitations on the Company's ability to create, incur or allow certain liens; enter into sale and lease-back transactions; create, assume, incur or guarantee additional indebtedness of certain of the Company's subsidiaries; and consolidate or merge with, or convey, transfer or lease all or substantially all of the Company's and its subsidiaries assets, to another person. As of June 30, 2023 and December 31, 2022, the Company was in compliance with all related covenants.

## Revolving Credit Facility

On March 6, 2023, the Company amended its $1 billion unsecured revolving credit facility ("Revolving Credit Agreement") to replace the London interbank offered rate to a variable secured overnight financing rate (the 'Term SOFR Rate') as the rate to which interest payments are indexed, among other things. The Revolving Credit Agreement matures on June 17, 2026. Revolving loans may be borrowed, repaid and reborrowed until June 17, 2026, at which time all amounts borrowed must be repaid. The Company may use the proceeds of future borrowings under the Revolving Credit Agreement for working capital and general corporate purposes. As of June 30, 2023, no amounts have been borrowed under the Revolving Credit Agreement.
```

---

### 🔹 [Chunk 039/088] `stre_p13_001` | Trang PDF: 13 (Doc Page: 15) | 489 tokens (2009 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 489` | `strategy = "strategy_e"`

```markdown
The borrowings under the Revolving Credit Agreement bear interest, at the Company's option, of either (i) a floating rate equal to a base rate (the 'Alternate Base Rate') or (ii) a rate equal to the Term SOFR Rate (or the applicable benchmark replacement), plus a margin of 0.75%. The Alternate Base Rate is defined as the greatest of (A) the rate of interest published by the Wall Street Journal, from time to time, as the prime rate, (B) the federal funds rate, plus 0.500% and (C) the Term SOFR Rate for a one-month tenor, plus 1.00%. The Term SOFR Rate is the forward-looking secured overnight financing rate administered by the Federal Reserve Bank of New York or a successor administrator, for the relevant interest period, but in no event shall the Term SOFR Rate be less than 0.00% per annum.

The Company is also obligated to pay a commitment fee on the undrawn amounts of the Revolving Credit Agreement at an annual rate of 0.10%. The Revolving Credit Agreement requires the Company to comply with certain covenants, including covenants that limit or restrict the ability of the Company's subsidiaries to incur debt and limit or restrict the ability of the Company and its subsidiaries to grant liens and enter into sale and leaseback transactions; and, in the case of the Company or a guarantor, merge, consolidate, liquidate, dissolve or sell, transfer, lease or otherwise dispose of all or substantially all of the assets of the Company and its subsidiaries, taken as a whole. As of June 30, 2023 and December 31, 2022, the Company was in compliance with all related covenants.

## 7. Commitments and Contingencies

## Content

As of June 30, 2023, the Company had $20.9 billion of obligations comprised of $4.4 billion included in "Current content liabilities" and $2.8 billion of "Non-current content liabilities" on the Consolidated Balance Sheets and $13.7 billion of obligations that are not reflected on the Consolidated Balance Sheets as they did not yet meet the criteria for recognition.
```

---

### 🔹 [Chunk 040/088] `stre_p13_002` | Trang PDF: 13 (Doc Page: 15) | 267 tokens (863 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 267` | `strategy = "strategy_e"`

```markdown
As of December 31, 2022, the Company had $21.8 billion of obligations comprised of $4.5 billion included in "Current content liabilities" and $3.1 billion of "Non-current content liabilities" on the Consolidated Balance Sheets and $14.2 billion of obligations that are not reflected on the Consolidated Balance Sheets as they did not yet meet the criteria for recognition.

The expected timing of payments for these content obligations is as follows:

|  | As of - June 30, 2023 - (in thousands) | As of - December 31, 2022 - (in thousands) |
| --- | --- | --- |
| Less than one year | $ 9,818,370 | $ 10,038,483 |
| Due after one year and through three years | 9,131,131 | 9,425,551 |
| Due after three years and through five years | 1,662,733 | 2,124,307 |
| Due after five years | 288,054 | 243,606 |
| Total content obligations | $ 20,900,288 | $ 21,831,947 |
```

---


# 📄 [Trang PDF 14 / Form 10-Q Trang 16] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 041/088] `stre_p14_000` | Trang PDF: 14 (Doc Page: 16) | 445 tokens (2042 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 445` | `strategy = "strategy_e"`

```markdown
Content obligations include amounts related to the acquisition, licensing and production of content. Obligations that are in non-U.S. dollar currencies are translated to the U.S. dollar at period end rates. An obligation for the production of content includes non-cancelable commitments under creative talent and employment agreements as well as other production related commitments. An obligation for the acquisition and licensing of content is incurred at the time the Company enters into an agreement to obtain future titles. Once a title becomes available, a content liability is recorded on the Consolidated Balance Sheets. Certain agreements include the obligation to license rights for unknown future titles, the ultimate quantity and/or fees for which are not yet determinable as of the reporting date. Traditional film output deals, or certain TV series license agreements where the number of seasons to be aired is unknown, are examples of such license agreements. The Company does not include any estimated obligation for these future titles beyond the known minimum amount. However, the unknown obligations are expected to be significant.

## Legal Proceedings

From time to time, in the normal course of its operations, the Company is subject to litigation matters and claims, including claims relating to employee relations, business practices and patent infringement. Litigation can be expensive and disruptive to normal business operations. Moreover, the results of complex legal proceedings are difficult to predict and the Company's view of these matters may change in the future as the litigation and events related thereto unfold. The Company expenses legal fees as incurred. The Company records a provision for contingent losses when it is both probable that a liability has been incurred and the amount of the loss can be reasonably estimated. An unfavorable outcome to any legal matter, if material, could have an adverse effect on the Company's operations or its financial position, liquidity or results of operations.
```

---

### 🔹 [Chunk 042/088] `stre_p14_001` | Trang PDF: 14 (Doc Page: 16) | 476 tokens (2251 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 476` | `strategy = "strategy_e"`

```markdown
The Company is involved in litigation matters not listed herein but does not consider the matters to be material either individually or in the aggregate at this time. The Company's view of the matters not listed may change in the future as the litigation and events related thereto unfold.

## Indemnification

In the ordinary course of business, the Company has entered into contractual arrangements under which it has agreed to provide indemnification of varying scope and terms to business partners and other parties with respect to certain matters, including, but not limited to, losses arising out of the Company's breach of such agreements and out of intellectual property infringement claims made by third parties. In these circumstances, payment may be conditional on the other party making a claim pursuant to the procedures specified in the particular contract.

The Company's obligations under these agreements may be limited in terms of time or amount, and in some instances, the Company may have recourse against third parties for certain payments. In addition, the Company has entered into indemnification agreements with its directors and certain of its officers that will require it, among other things, to indemnify them against certain liabilities that may arise by reason of their status or service as directors or officers. The terms of such obligations vary.

It is not possible to make a reasonable estimate of the maximum potential amount of future payments under these or similar agreements due to the conditional nature of the Company's obligations and the unique facts and circumstances involved in each particular agreement. No amount has been accrued in the accompanying consolidated financial statements with respect to these indemnification obligations.

## 8. Stockholders' Equity

## Stock Option Plan

In June 2020, the Company's stockholders approved the 2020 Stock Plan, which was adopted by the Company's Board of Directors in March 2020 subject to stockholder approval. The 2020 Stock Plan provides for the grant of incentive stock options to employees and for the grant of non-statutory stock options, stock appreciation rights, restricted stock and restricted stock units to employees, directors and consultants.
```

---


# 📄 [Trang PDF 15 / Form 10-Q Trang 17] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 043/088] `stre_p15_000` | Trang PDF: 15 (Doc Page: 17) | 478 tokens (1445 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 478` | `strategy = "strategy_e"`

```markdown
A summary of the activities related to the Company's stock option plans is as follows:

|  | Shares Available for Grant | Options Outstanding - Number of Shares | Options Outstanding - Weighted- Average Exercise Price (per share) | Weighted-Average Remaining Contractual Term (in years) | Aggregate Intrinsic Value (in thousands) |
| --- | --- | --- | --- | --- | --- |
| Balances as of December 31, 2022 | 16,454,103 | 19,896,861 | $ 242.22 |  |  |
| Granted | (1,025,300) | 1,025,300 | 333.49 |  |  |
| Exercised | - | (871,355) | 68.23 |  |  |
| Expired | - | (574) | 13.14 |  |  |
| Balances as of June 30, 2023 | 15,428,803 | 20,050,232 | $ 254.46 | 5.52 | $ 3,982,709 |
| Vested and expected to vest as of June 30, 2023 |  | 20,050,232 | $ 254.46 | 5.52 | $ 3,982,709 |
| Exercisable as of June 30, 2023 |  | 19,918,808 | $ 253.84 | 5.49 | $ 3,970,659 |

The aggregate intrinsic value in the table above represents the total pretax intrinsic value (the difference between the Company's closing stock price on the last trading day of the second quarter of 2023 and the exercise price, multiplied by the number of in-the-money options) that would have been received by the option holders had all option holders exercised their options on the last trading day of the second quarter of 2023. This amount changes based on the fair market value of the Company's common stock.

A summary of the amounts related to option exercises, is as follows:
```

---

### 🔹 [Chunk 044/088] `stre_p15_001` | Trang PDF: 15 (Doc Page: 17) | 267 tokens (940 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 267` | `strategy = "strategy_e"`

```markdown
|  | Three Months Ended - June 30, 2023 - (in thousands) | Three Months Ended - June 30, 2022 - (in thousands) | Six Months Ended - June 30, 2023 - (in thousands) | Six Months Ended - June 30, 2022 - (in thousands) |
| --- | --- | --- | --- | --- |
| Total intrinsic value of options exercised | $ 137,791 | $ 83,030 | $ 254,101 | $ 197,792 |
| Cash received from options exercised | 34,717 | 11,250 | 60,745 | 24,928 |

## Stock-based Compensation

Stock options are generally vested in full upon grant date and exercisable for the full ten year contractual term regardless of employment status. Stock options granted to certain named executive officers vest on the one-year anniversary of the grant date, subject to the employee's continuous employment or service with the Company through the vesting date. The following table summarizes the assumptions used to value option grants using the lattice-binomial model and the valuation data:
```

---

### 🔹 [Chunk 045/088] `stre_p15_002` | Trang PDF: 15 (Doc Page: 17) | 306 tokens (732 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 306` | `strategy = "strategy_e"`

```markdown
|  | Three Months Ended - June 30, 2023 | Three Months Ended - June 30, 2022 | Six Months Ended - June 30, 2023 | Six Months Ended - June 30, 2022 |
| --- | --- | --- | --- | --- |
| Dividend yield | - % | - % | - % | - % |
| Expected volatility | 43 % | 49 % | 43% - 46% | 38% - 49% |
| Risk-free interest rate | 3.57 % | 2.57 % | 3.57% - 3.63% | 1.71% - 2.57% |
| Suboptimal exercise factor | 4.27 | 4.71 | 4.22 - 4.27 | 4.71 |
| Weighted-average fair value (per share) | $ 200 | $ 138 | $ 192 | $ 167 |
| Total stock-based compensation expense (in thousands) | $ 78,030 | $ 150,392 | $ 177,129 | $ 269,601 |
| Total income tax impact on provision (in thousands) | $ 17,148 | $ 33,335 | $ 38,859 | $ 59,748 |

## Stock Repurchases
```

---

### 🔹 [Chunk 046/088] `stre_p15_003` | Trang PDF: 15 (Doc Page: 17) | 337 tokens (1440 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 337` | `strategy = "strategy_e"`

```markdown
In March 2021, the Company's Board of Directors authorized the repurchase of up to $5 billion of its common stock, with no expiration date. Stock repurchases may be effected through open market repurchases in compliance with Rule 10b-18 under the Exchange Act, including through the use of trading plans intended to qualify under Rule 10b5-1 under the Exchange Act, privately-negotiated transactions, accelerated stock repurchase plans, block purchases, or other similar purchase techniques and in such amounts as management deems appropriate. The Company is not obligated to repurchase any specific number of shares, and the timing and actual number of shares repurchased will depend on a variety of factors, including the Company's stock price, general economic, business and market conditions, and alternative investment opportunities. The Company may discontinue any repurchases of its common stock at any time without prior notice. During the three and six months ended June 30, 2023, the Company repurchased 1,849,324 and 3,071,380 shares, respectively, for an aggregate amount of $645 million and $1,045 million, respectively. As of June 30, 2023, $3.4 billion remain available for repurchases. Shares repurchased by the Company are accounted for when the transaction is settled. As of June 30, 2023, there were no unsettled share repurchases. Direct costs incurred to acquire the shares are included in the total cost of the shares.
```

---


# 📄 [Trang PDF 16 / Form 10-Q Trang 18] — Mục: *Notes to Consolidated Financial Statements*

### 🔹 [Chunk 047/088] `stre_p16_000` | Trang PDF: 16 (Doc Page: 18) | 498 tokens (2018 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 498` | `strategy = "strategy_e"`

```markdown
## 9. Income Taxes

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Provision for income taxes | $ 191,722 | $ 182,103 | $ 355,476 | $ 564,348 |
| Effective tax rate | 11 % | 11 % | 11 % | 16 % |

The effective tax rates for the three and six months ended June 30, 2023 differed from the Federal statutory rate primarily due to the impact of international provisions of the Tax Cuts and Jobs Act, research and development credits, and the recognition of excess tax benefits of stock-based compensation. The effective tax rates for the three and six months ended June 30, 2022 differed from the Federal statutory rate primarily due to the impact of foreign taxes, international provisions of the Tax Cuts and Jobs Act, research and development credits, and the recognition of excess tax benefits of stock-based compensation.

The effective tax rate for the three months ended June 30, 2023 was consistent compared to the same period in 2022. The decrease in the effective tax rate for the six months ended June 30, 2023, as compared to the same period in 2022 was primarily due to a decrease in foreign taxes. For the three and six months ended June 30, 2023, the Company recognized a discrete tax benefit related to the excess tax benefits from stock-based compensation of $28 million and $52 million, compared to the three and six months ended June 30, 2022 of $18 million and $43 million.

Gross unrecognized tax benefits were $240 million and $227 million as of June 30, 2023 and December 31, 2022, respectively. The gross unrecognized tax benefits, if recognized by the Company, will result in a reduction of approximately $164 million to the provision for income taxes thereby favorably impacting the Company's effective tax rate.
```

---

### 🔹 [Chunk 048/088] `stre_p16_001` | Trang PDF: 16 (Doc Page: 18) | 492 tokens (2097 ký tự)
> **Metadata:** `section = "Notes to Consolidated Financial Statements"` | `tokens = 492` | `strategy = "strategy_e"`

```markdown
The Company files U.S. Federal, state and foreign tax returns. The Company is currently under examination by the IRS for the years 2016 through 2018 and is subject to examination for 2019 through 2022. The foreign and state tax returns for the years 2015 through 2022 are subject to examination by various states and foreign jurisdictions. While the Company is in various stages of inquiries and examinations by federal, state and foreign taxing authorities, we believe that our tax positions will more likely than not be sustained. Nonetheless, it is possible that future obligations related to these matters could arise.

Given the potential outcome of the current examinations as well as the impact of the current examinations on the potential expiration of the statute of limitations, it is reasonably possible that the balance of unrecognized tax benefits could significantly change within the next twelve months. However, an estimate of the range of reasonably possible adjustments cannot be made at this time.

## 10. Segment and Geographic Information

The Company operates as one operating segment. The Company's chief operating decision maker ("CODM") is its co-chief executive officers, who review financial information presented on a consolidated basis for the purposes of making operating decisions, assessing financial performance and allocating resources.

Total U.S. revenues were $3.3 billion and $6.6 billion, respectively, for the three and six months ended June 30, 2023, and $3.3 billion and $6.4 billion, respectively, for the three and six months ended June 30, 2022. See Note 2 Revenue Recognition for additional information about streaming revenue by region.

The Company's long-lived tangible assets, as well as the Company's operating lease right-of-use assets recognized on the Consolidated Balance Sheets as of June 30, 2023 and December 31, 2022, were located as follows:

|  | As of - June 30, 2023 - (in thousands) | As of - December 31, 2022 - (in thousands) |
| --- | --- | --- |
| United States | $ 2,795,979 | $ 2,745,071 |
| International | 863,721 | 880,308 |
```

---


# 📄 [Trang PDF 17 / Form 10-Q Trang 19] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 049/088] `stre_p17_000` | Trang PDF: 17 (Doc Page: 19) | 486 tokens (2308 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 486` | `strategy = "strategy_e"`

```markdown
## Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations

## Forward-Looking Statements

This Quarterly Report on Form 10-Q contains forward-looking statements within the meaning of the federal securities laws. These forward-looking statements include, but are not limited to, statements regarding: our core strategy; our ability to improve our content offerings and service; our future financial performance, including expectations regarding revenues, deferred revenue, operating income and margin, net income, expenses, and profitability; liquidity, including the sufficiency of our capital resources, net cash provided by (used in) operating activities, access to financing sources, and free cash flows; capital allocation strategies, including any stock repurchases or repurchase programs; seasonality; stock price volatility; impact of foreign exchange rate fluctuations, including on net income, revenues and average revenues per paying member; impact of interest rate fluctuations; adequacy of existing facilities; future regulatory changes and their impact on our business; intellectual property; price changes and testing; accounting treatment for changes related to content assets; acquisitions; membership growth, including impact of content and pricing changes on membership growth; partnerships; member viewing patterns; dividends; future contractual obligations, including unknown content obligations and timing of payments; our global content and marketing investments, including investments in original programming; impact of work stoppages; content amortization; resolution of tax examinations; tax expense; unrecognized tax benefits; deferred tax assets; and our ability to effectively manage change and growth. These forward-looking statements are subject to risks and uncertainties that could cause actual results and events to differ materially from those included in forward-looking statements. Factors that might cause or contribute to such differences include, but are not limited to, those discussed in our Annual Report on Form 10-K for the year ended December 31, 2022 filed with the Securities and Exchange Commission ('SEC') on January 26, 2023, in particular the risk factors discussed under the heading 'Risk Factors' in Part I, Item 1A.
```

---

### 🔹 [Chunk 050/088] `stre_p17_001` | Trang PDF: 17 (Doc Page: 19) | 415 tokens (2015 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 415` | `strategy = "strategy_e"`

```markdown
We assume no obligation to revise or publicly release any revision to any forward-looking statements contained in this Quarterly Report on Form 10-Q, unless required by law.

Investors and others should note that we announce material financial information to our investors using our investor relations website ( ir .netflix.net ), SEC filings, press releases, public conference calls and webcasts. We use these channels, as well as social media and blogs to communicate with our members and the public about our company, our services and other issues. It is possible that the information we post on social media and blogs could be deemed to be material information. Therefore, we encourage investors, the media, and others interested in our company to review the information we post on the social media channels and blogs listed on our investor relations website.

## Overview

We are one of the world's leading entertainment services with over 238 million paid memberships in over 190 countries enjoying TV series, films and games across a wide variety of genres and languages. Members can play, pause and resume watching as much as they want, anytime, anywhere, and can change their plans at any time.

Our core strategy is to grow our business globally within the parameters of our operating margin target. We strive to continuously improve our members' experience by offering compelling content that delights them and attracts new members. We seek to drive conversation around our content to further enhance member joy, and we are continuously enhancing our user interface to help our members more easily choose content that they will find enjoyable.

Our membership growth exhibits a seasonal pattern that reflects variations when consumers buy internet-connected screens and when they tend to increase their viewing. Historically, the fourth quarter represents our greatest streaming membership growth. In addition, our membership growth can be impacted by our content release schedule and changes to pricing.
```

---


# 📄 [Trang PDF 18 / Form 10-Q Trang 20] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 051/088] `stre_p18_000` | Trang PDF: 18 (Doc Page: 20) | 496 tokens (1385 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 496` | `strategy = "strategy_e"`

```markdown
## Results of Operations

The following represents our consolidated performance highlights:

|  | As of/ Three Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Three Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Financial Results: |  |  |  |  |
| Streaming revenues | $ 8,158,326 | $ 7,933,051 | $ 225,275 | 3 % |
| DVD revenues (1) | 28,975 | 37,090 | (8,115) | (22)% |
| Total revenues | $ 8,187,301 | $ 7,970,141 | $ 217,160 | 3 % |
| Operating income | $ 1,827,183 | $ 1,578,283 | $ 248,900 | 16 % |
| Operating margin | 22 % | 20 % | 2 % |  |
| Global Streaming Memberships: |  |  |  |  |
| Paid net membership additions (losses) | 5,892 | (969) | 6,861 | 708 % |
| Paid memberships at end of period | 238,390 | 220,672 | 17,718 | 8 % |
| Average paying memberships | 235,444 | 221,157 | 14,287 | 6 % |
| Average monthly revenue per paying membership | $ 11.55 | $ 11.96 | $ (0.41) | (3)% |

(1) In April 2023, we announced our plans to discontinue our DVD-by-mail service, which we do not expect to have a material effect on our operations or financial results.
```

---

### 🔹 [Chunk 052/088] `stre_p18_001` | Trang PDF: 18 (Doc Page: 20) | 464 tokens (2270 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 464` | `strategy = "strategy_e"`

```markdown
Consolidated revenues for the three months ended June 30, 2023 increased 3% as compared to the three months ended June 30, 2022. The increase in our consolidated revenues was due to the 6% growth in average paying memberships, partially offset by a 3% decrease in average monthly revenue per paying membership. The decrease in average monthly revenue per paying membership was primarily due to the strengthening of the U.S. dollar relative to certain foreign currencies, higher membership growth in regions with lower average monthly revenue per paying membership and timing of paid net membership additions. These decreases were partially offset by price increases in certain regions.

The increase in operating margin is primarily due to the 3% growth in revenue coupled with lower cost of revenues, technology and development expenses, and general and administrative expenses for the three months ended June 30, 2023 as compared to the corresponding prior year period. The decrease in expenses was impacted by approximately $150 million of expenses related to cost restructuring initiatives incurred during the three months ended June 30, 2022 with no similar transactions for the three months ended June 30, 2023.

## Streaming Revenues

We primarily derive revenues from monthly membership fees for services related to streaming content to our members. We offer a variety of streaming membership plans, the price of which varies by country and the features of the plan. As of June 30, 2023, pricing on our paid plans ranged from the U.S. dollar equivalent of $1 to $27 per month, and pricing on our extra member sub accounts ranged from the U.S. dollar equivalent of $2 to $8 per month. We expect that from time to time the prices of our membership plans in each country may change and we may test other plan and price variations.

We also earn revenue from advertisements presented on our streaming service, consumer products and various other sources. Revenues earned from sources other than monthly membership fees were not material for the three and six months ended June 30, 2023 and June 30, 2022.

The following tables summarize streaming revenue and other streaming membership information by region for the three and six months ended June 30, 2023 and 2022.
```

---


# 📄 [Trang PDF 19 / Form 10-Q Trang 21] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 053/088] `stre_p19_000` | Trang PDF: 19 (Doc Page: 21) | 330 tokens (969 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 330` | `strategy = "strategy_e"`

```markdown
## United States and Canada (UCAN)

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | As of/ Three Months Ended - June 30, 2023 - (in | As of/ Three Months Ended - June 30, 2022 - thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 3,599,448 | $ 3,537,863 | $ 61,585 | 2 % |
| Paid net membership additions (losses) | 1,173 | (1,296) | 2,469 | 191 % |
| Paid memberships at end of period | 75,571 | 73,283 | 2,288 | 3 % |
| Average paying memberships | 74,985 | 73,931 | 1,054 | 1 % |
| Average monthly revenue per paying membership | $ 16.00 | $ 15.95 | $ 0.05 | - % |
| Constant currency change (1) |  |  |  | 1 % |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---

### 🔹 [Chunk 054/088] `stre_p19_001` | Trang PDF: 19 (Doc Page: 21) | 336 tokens (963 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 336` | `strategy = "strategy_e"`

```markdown
|  | As of/ Six Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Six Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 7,208,093 $ | 6,888,287 | $ 319,806 | 5 % |
| Paid net membership additions (losses) | 1,275 | (1,932) | 3,207 | 166 % |
| Paid memberships at end of period | 75,571 | 73,283 | 2,288 | 3 % |
| Average paying memberships | 74,666 | 74,414 | 252 | - % |
| Average monthly revenue per paying membership | $ 16.09 | $ 15.43 | $ 0.66 | 4 % |
| Constant currency change (1) |  |  |  | 5 % |

## Europe, Middle East, and Africa (EMEA)

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022
```

---

### 🔹 [Chunk 055/088] `stre_p19_002` | Trang PDF: 19 (Doc Page: 21) | 321 tokens (920 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 321` | `strategy = "strategy_e"`

```markdown
|  | As of/ Three Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Three Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 2,562,170 $ | 2,457,235 | $ 104,935 | 4 % |
| Paid net membership additions (losses) | 2,434 | (767) | 3,201 | 417 % |
| Paid memberships at end of period | 79,807 | 72,966 | 6,841 | 9 % |
| Average paying memberships | 78,590 | 73,350 | 5,240 | 7 % |
| Average monthly revenue per paying membership | $ 10.87 | $ 11.17 | $ (0.30) | (3)% |
| Constant currency change (1) |  |  |  | (1)% |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---


# 📄 [Trang PDF 20 / Form 10-Q Trang 22] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 056/088] `stre_p20_000` | Trang PDF: 20 (Doc Page: 22) | 337 tokens (950 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 337` | `strategy = "strategy_e"`

```markdown
|  | As of/ Six Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Six Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 5,079,811 | $ 5,019,066 | $ 60,745 | 1 % |
| Paid net membership additions (losses) | 3,078 | (1,070) | 4,148 | 388 % |
| Paid memberships at end of period | 79,807 | 72,966 | 6,841 | 9 % |
| Average paying memberships | 77,821 | 73,618 | 4,203 | 6 % |
| Average monthly revenue per paying membership | $ 10.88 | $ 11.36 | $ (0.48) | (4)% |
| Constant currency change (1) |  |  |  | - % |

## Latin America (LATAM)

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022
```

---

### 🔹 [Chunk 057/088] `stre_p20_001` | Trang PDF: 20 (Doc Page: 22) | 320 tokens (915 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 320` | `strategy = "strategy_e"`

```markdown
|  | As of/ Three Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Three Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 1,077,435 $ | 1,030,234 | $ 47,201 | 5 % |
| Paid net membership additions (losses) | 1,217 | 14 | 1,203 | 8,593 % |
| Paid memberships at end of period | 42,466 | 39,624 | 2,842 | 7 % |
| Average paying memberships | 41,858 | 39,617 | 2,241 | 6 % |
| Average monthly revenue per paying membership | $ 8.58 | $ 8.67 | $ (0.09) | (1)% |
| Constant currency change (1) |  |  |  | 8 % |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---

### 🔹 [Chunk 058/088] `stre_p20_002` | Trang PDF: 20 (Doc Page: 22) | 333 tokens (940 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 333` | `strategy = "strategy_e"`

```markdown
|  | As of/ Six Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Six Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 2,147,627 $ | 2,029,182 | $ 118,445 | 6 % |
| Paid net membership additions (losses) | 767 | (337) | 1,104 | 328 % |
| Paid memberships at end of period | 42,466 | 39,624 | 2,842 | 7 % |
| Average paying memberships | 41,666 | 39,702 | 1,964 | 5 % |
| Average monthly revenue per paying membership | $ 8.59 | $ 8.52 | $ 0.07 | 1 % |
| Constant currency change (1) |  |  |  | 8 % |

## Asia-Pacific (APAC)

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022
```

---


# 📄 [Trang PDF 21 / Form 10-Q Trang 23] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 059/088] `stre_p21_000` | Trang PDF: 21 (Doc Page: 23) | 320 tokens (914 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 320` | `strategy = "strategy_e"`

```markdown
|  | As of/ Three Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Three Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 919,273 $ | 907,719 | $ 11,554 | 1 % |
| Paid net membership additions (losses) | 1,068 | 1,080 | (12) | (1)% |
| Paid memberships at end of period | 40,546 | 34,799 | 5,747 | 17 % |
| Average paying memberships | 40,012 | 34,259 | 5,753 | 17 % |
| Average monthly revenue per paying membership | $ 7.66 | $ 8.83 | $ (1.17) | (13)% |
| Constant currency change (1) |  |  |  | (7)% |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---

### 🔹 [Chunk 060/088] `stre_p21_001` | Trang PDF: 21 (Doc Page: 23) | 443 tokens (1542 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 443` | `strategy = "strategy_e"`

```markdown
|  | As of/ Six Months Ended - June 30, 2023 - (in thousands, except revenue per membership and percentages) | As of/ Six Months Ended - June 30, 2022 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except revenue per membership and percentages) |
| --- | --- | --- | --- | --- |
| Revenues | $ 1,852,796 $ | 1,824,473 | $ 28,323 | 2 % |
| Paid net membership additions (losses) | 2,523 | 2,167 | 356 | 16 % |
| Paid memberships at end of period | 40,546 | 34,799 | 5,747 | 17 % |
| Average paying memberships | 39,382 | 33,718 | 5,664 | 17 % |
| Average monthly revenue per paying membership | $ 7.84 | $ 9.02 | $ (1.18) | (13)% |
| Constant currency change (1) |  |  |  | (6)% |

(1) We believe constant currency information is useful in analyzing the underlying trends in average monthly revenue per paying membership. In order to exclude the effect of foreign currency rate fluctuations on average monthly revenue per paying membership, we estimate current period revenue assuming foreign exchange rates had remained constant with foreign exchange rates from each of the corresponding months of the prior-year period. For the three and six months ended June 30, 2023, our revenues would have been approximately $231 million and $577 million higher had foreign currency exchange rates remained constant with those for the three and six months ended June 30, 2022.

## Cost of Revenues
```

---

### 🔹 [Chunk 061/088] `stre_p21_002` | Trang PDF: 21 (Doc Page: 23) | 444 tokens (1810 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 444` | `strategy = "strategy_e"`

```markdown
Amortization of content assets makes up the majority of cost of revenues. Expenses associated with the acquisition, licensing and production of content (such as payroll and related personnel expenses, costs associated with obtaining rights to music included in our content, overall deals with talent, miscellaneous production related costs and participations and residuals), streaming delivery costs and other operations costs make up the remainder of cost of revenues. We have built our own global content delivery network ('Open Connect') to help us efficiently stream a high volume of content to our members over the internet. Delivery expenses, therefore, include equipment costs related to Open Connect, payroll and related personnel expenses and all third-party costs, such as cloud computing costs, associated with delivering content over the internet. Other operations costs include customer service and payment processing fees, including those we pay to our integrated payment partners, as well as other costs incurred in making our content available to members.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Cost of revenues | $ 4,673,470 | $ 4,690,755 | $ (17,285) | - % |
| As a percentage of revenues | 57 % | 59 % |  |  |

Cost of revenues for the three months ended June 30, 2023 as compared to the three months ended June 30, 2022 remained relatively flat.

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---


# 📄 [Trang PDF 22 / Form 10-Q Trang 24] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 062/088] `stre_p22_000` | Trang PDF: 22 (Doc Page: 24) | 486 tokens (1656 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 486` | `strategy = "strategy_e"`

```markdown
|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Cost of revenues | $ 9,477,095 | $ 8,975,460 | $ 501,635 | 6 % |
| As a percentage of revenues | 58 % | 57 % |  |  |

The increase in cost of revenues was primarily due to a $442 million increase in content amortization relating to our existing and new content, including more exclusive and original programming.

## Marketing

Marketing expenses consist primarily of advertising expenses and certain payments made to our marketing and advertising sales partners, including consumer electronics ('CE') manufacturers, multichannel video programming distributors ('MVPDs'), mobile operators, and internet service providers ('ISPs'). Advertising expenses include promotional activities such as digital and television advertising. Marketing expenses also include payroll and related expenses for personnel that support marketing activities.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Marketing | $ 627,168 | $ 574,960 | $ 52,208 | 9 % |
| As a percentage of revenues | 8 % | 7 % |  |  |
```

---

### 🔹 [Chunk 063/088] `stre_p22_001` | Trang PDF: 22 (Doc Page: 24) | 372 tokens (1513 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 372` | `strategy = "strategy_e"`

```markdown
The increase in marketing expenses was primarily due to an $88 million increase in advertising expenses, partially offset by a $20 million decrease in personnel-related costs and a $11 million decrease in payments to our marketing partners.

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022

|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Marketing | $ 1,182,530 | $ 1,130,938 | $ 51,592 | 5 % |
| As a percentage of revenues | 7 % | 7 % |  |  |

The increase in marketing expenses was primarily due to a $107 million increase in advertising expenses, partially offset by a $34 million decrease in personnel-related costs and a $20 million decrease in payments to our marketing partners.

## Technology and Development

Technology and development expenses consist primarily of payroll and related expenses for technology personnel responsible for making improvements to our service offerings, including testing, maintaining and modifying our user interface, our recommendations, merchandising and infrastructure. Technology and development expenses also include costs associated with general use computer hardware and software.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022
```

---

### 🔹 [Chunk 064/088] `stre_p22_002` | Trang PDF: 22 (Doc Page: 24) | 226 tokens (748 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 226` | `strategy = "strategy_e"`

```markdown
|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Technology and development | $ 657,983 | $ 716,846 | $ (58,863) | (8)% |
| As a percentage of revenues | 8 % | 9 % |  |  |

The decrease in technology and development expenses was primarily due to a $62 million decrease in personnel-related costs, partially offset by an increase in expenses related to continued improvements in our streaming service.

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---


# 📄 [Trang PDF 23 / Form 10-Q Trang 25] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 065/088] `stre_p23_000` | Trang PDF: 23 (Doc Page: 25) | 487 tokens (1715 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 487` | `strategy = "strategy_e"`

```markdown
|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Technology and development | $ 1,345,258 | $ 1,374,376 | $ (29,118) | (2)% |
| As a percentage of revenues | 8 % | 9 % |  |  |

The decrease in technology and development expenses was primarily due to a $36 million decrease in personnel-related costs, partially offset by an increase in expenses related to continued improvements in our streaming service.

## General and Administrative

General and administrative expenses consist primarily of payroll and related expenses for corporate personnel. General and administrative expenses also include professional fees and other general corporate expenses.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| General and administrative | $ 401,497 | $ 409,297 | $ (7,800) | (2)% |
| As a percentage of revenues | 5 % | 5 % |  |  |

The decrease in general and administrative expenses was primarily due to a $15 million decrease in personnel-related costs and a decrease in administrative expenses, partially offset by an increase in third-party expenses, including costs for contractors and consultants.
```

---

### 🔹 [Chunk 066/088] `stre_p23_001` | Trang PDF: 23 (Doc Page: 25) | 214 tokens (670 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 214` | `strategy = "strategy_e"`

```markdown
Six months ended June 30, 2023 as compared to the six months ended June 30, 2022

|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| General and administrative | $ 802,421 | $ 807,225 | $ (4,804) | (1)% |
| As a percentage of revenues | 5 % | 5 % |  |  |

General and administrative expenses for the six months ended June 30, 2023 as compared to the six months ended June 30, 2022 remained relatively flat.
```

---


# 📄 [Trang PDF 24 / Form 10-Q Trang 26] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 067/088] `stre_p24_000` | Trang PDF: 24 (Doc Page: 26) | 426 tokens (1322 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 426` | `strategy = "strategy_e"`

```markdown
## Interest Expense

Interest expense consists primarily of the interest associated with our outstanding debt obligations, including the amortization of debt issuance costs. See Note 6 Debt in the accompanying notes to our consolidated financial statements for further detail on our debt obligations.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Interest expense | $ 174,812 | $ 175,455 | $ (643) | - % |
| As a percentage of revenues | 2 % | 2 % |  |  |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022

|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Interest expense | $ 349,051 | $ 363,034 | $ (13,983) | (4)% |
| As a percentage of revenues | 2 % | 2 % |  |  |
```

---

### 🔹 [Chunk 068/088] `stre_p24_001` | Trang PDF: 24 (Doc Page: 26) | 372 tokens (1354 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 372` | `strategy = "strategy_e"`

```markdown
Interest expense primarily consists of interest on our Notes of $175 million and $349 million for the three and six months ended June 30, 2023. Interest expense for the three months ended June 30, 2023 as compared to the three months ended June 30, 2022 remained relatively flat. The decrease in interest expense for the six months ended June 30, 2023 as compared to the six months ended June 30, 2022 was due to the lower average aggregate principal of interest bearing notes outstanding.

## Interest and Other Income (Expense)

Interest and other income (expense) consists primarily of foreign exchange gains and losses on foreign currency denominated balances and interest earned on cash, cash equivalents and short-term investments.

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Interest and other income (expense) | $ 26,961 | $ 220,226 | $ (193,265) | (88)% |
| As a percentage of revenues | - % | 3 % |  |  |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022
```

---

### 🔹 [Chunk 069/088] `stre_p24_002` | Trang PDF: 24 (Doc Page: 26) | 173 tokens (450 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 173` | `strategy = "strategy_e"`

```markdown
|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Interest and other income (expense) | $ (44,243) | $ 415,871 | $ (460,114) | (111)% |
| As a percentage of revenues | - % | 3 % |  |  |
```

---

### 🔹 [Chunk 070/088] `stre_p24_003` | Trang PDF: 24 (Doc Page: 26) | 355 tokens (1471 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 355` | `strategy = "strategy_e"`

```markdown
Interest and other income (expense) decreased in the three and six months ended June 30, 2023 primarily due to foreign exchange losses of $23 million and $130 million, respectively, compared to gains of $239 million and $431 million, respectively, for the corresponding periods in 2022. In the three months ended June 30, 2023, the foreign exchange losses were primarily driven by the non-cash losses of $29 million from the remeasurement of our €5,170 million Senior Notes, partially offset by the remeasurement of cash and content liability positions in currencies other than the functional currencies. In the six months ended June 30, 2023, the foreign exchange losses were primarily driven by the non-cash losses of $110 million from the remeasurement of our €5,170 million Senior Notes, coupled with the remeasurement of cash and content liability positions in currencies other than the functional currencies. In the three and six months ended June 30, 2022, the foreign exchange gains were primarily driven by the non-cash gains of $305 million and $466 million, respectively, from the remeasurement of our €5,170 million Senior Notes, partially offset by the remeasurement of cash and content liability positions in currencies other than the functional currencies. The change in foreign currency gains and losses was partially offset by higher interest income earned in the three and six months ended June 30, 2023 as compared to the corresponding periods in 2022.
```

---


# 📄 [Trang PDF 25 / Form 10-Q Trang 27] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 071/088] `stre_p25_000` | Trang PDF: 25 (Doc Page: 27) | 498 tokens (1687 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 498` | `strategy = "strategy_e"`

```markdown
## Provision for Income Taxes

Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Provision for income taxes | $ 191,722 | $ 182,103 | $ 9,619 | 5 % |
| Effective tax rate | 11 % | 11 % |  |  |

Six months ended June 30, 2023 as compared to the six months ended June 30, 2022

|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Provision for income taxes | $ 355,476 | $ 564,348 | $ (208,872) | (37)% |
| Effective tax rate | 11 % | 16 % |  |  |

The effective tax rates for the three and six months ended June 30, 2023 differed from the Federal statutory rate primarily due to the impact of international provisions of the Tax Cuts and Jobs Act, research and development credits, and the recognition of excess tax benefits of stock-based compensation.

The effective tax rate for the three months ended June 30, 2023 was consistent compared to the same period in 2022. The decrease in the effective tax rate for the six months ended June 30, 2023, as compared to the same period in 2022 was primarily due to a decrease in foreign taxes.

## Liquidity and Capital Resources
```

---

### 🔹 [Chunk 072/088] `stre_p25_001` | Trang PDF: 25 (Doc Page: 27) | 487 tokens (1906 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 487` | `strategy = "strategy_e"`

```markdown
|  | As of - June 30, 2023 - (in thousands, except percentages) | As of - December 31, 2022 - (in thousands, except percentages) | Change - June 30, 2023 vs. December 31, 2022 - (in thousands, except percentages) | Change - June 30, 2023 vs. December 31, 2022 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Cash, cash equivalents, restricted cash and short-term investments | $ 8,580,466 | $ 6,081,858 | $ 2,498,608 | 41 % |
| Short-term and long-term debt | 14,469,538 | 14,353,076 | 116,462 | 1 % |

Cash, cash equivalents, restricted cash and short-term investments increased $2,499 million in the six months ended June 30, 2023 primarily due to cash provided by operations, partially offset by the repurchase of stock.

Debt, net of debt issuance costs, increased $116 million primarily due to the remeasurement of our euro-denominated notes. The amount of principal and interest on our outstanding notes due in the next twelve months is $1,086 million. As of June 30, 2023, no amounts had been borrowed under the $1 billion Revolving Credit Agreement. See Note 6 Debt in the accompanying notes to our consolidated financial statements.

We anticipate that our future capital needs from the debt market will be more limited compared to prior years. Our ability to obtain this or any additional financing that we may choose or need, including for potential strategic acquisitions and investments, will depend on, among other things, our development efforts, business plans, operating performance, and the condition of the capital markets at the time we seek financing. We may not be able to obtain such financing on terms acceptable to us or at all. If we raise additional funds through the issuance of equity or debt securities, those securities may have rights, preferences or privileges senior to the rights of our common stock, and our stockholders may experience dilution.
```

---

### 🔹 [Chunk 073/088] `stre_p25_002` | Trang PDF: 25 (Doc Page: 27) | 255 tokens (1111 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 255` | `strategy = "strategy_e"`

```markdown
In March 2021, our Board of Directors authorized the repurchase of up to $5 billion of our common stock, with no expiration date. Stock repurchases may be effected through open market repurchases in compliance with Rule 10b-18 under the Exchange Act, including through the use of trading plans intended to qualify under Rule 10b5-1 under the Exchange Act, privately-negotiated transactions, accelerated stock repurchase plans, block purchases, or other similar purchase techniques and in such amounts as management deems appropriate. We are not obligated to repurchase any specific number of shares, and the timing and actual number of shares repurchased will depend on a variety of factors, including our stock price, general economic, business and market conditions, and alternative investment opportunities. We may discontinue any repurchases of our common stock at any time without prior notice. During the six months ended June 30, 2023, the Company repurchased 3,071,380 shares of common stock for an aggregate amount of $1,045 million. As of June 30, 2023, $3.4 billion remains available for repurchases.
```

---


# 📄 [Trang PDF 26 / Form 10-Q Trang 28] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 074/088] `stre_p26_000` | Trang PDF: 26 (Doc Page: 28) | 499 tokens (1979 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 499` | `strategy = "strategy_e"`

```markdown
Our primary uses of cash include the acquisition, licensing and production of content, marketing programs, streaming delivery and personnel-related costs, as well as for strategic acquisitions and investments. Cash payment terms for non-original content have historically been in line with the amortization period. Investments in original content, and in particular content that we produce and own, require more cash upfront relative to licensed content. For example, production costs are paid as the content is created, well in advance of when the content is available on the service and amortized. We expect to continue to significantly invest in global content, particularly in original content, which will impact our liquidity. We currently anticipate that cash flows from operations, available funds and access to financing sources, including our revolving credit facility, will continue to be sufficient to meet our cash needs for the next twelve months and beyond.

Our material cash requirements from known contractual and other obligations primarily relate to our content, debt and lease obligations. As of June 30, 2023, the expected timing of those payments are as follows:

| Contractual obligations (in thousands): | Payments due by Period - Total | Payments due by Period - Next 12 Months | Payments due by Period - Beyond 12 Months |
| --- | --- | --- | --- |
| Content obligations (1) | $ 20,900,288 | $ 9,818,370 | $ 11,081,918 |
| Debt (2) | 18,002,660 | 1,086,201 | 16,916,459 |
| Operating lease obligations (3) | 3,223,471 | 490,130 | 2,733,341 |
| Total | $ 42,126,419 | $ 11,394,701 | $ 30,731,718 |

- (1) As of June 30, 2023, content obligations were comprised of $4.4 billion included in 'Current content liabilities' and $2.8 billion of 'Non-current content liabilities' on the Consolidated Balance Sheets and $13.7 billion of obligations that are not reflected on the Consolidated Balance Sheets as they did not then meet the criteria for recognition.
```

---

### 🔹 [Chunk 075/088] `stre_p26_001` | Trang PDF: 26 (Doc Page: 28) | 498 tokens (2350 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 498` | `strategy = "strategy_e"`

```markdown
The material cash requirements above do not include any estimated obligation for the unknown future titles, payment for which could range from less than one year to more than five years. However, these unknown obligations are expected to be significant and we believe could include approximately $1 billion to $4 billion over the next three years, with the payments for the vast majority of such amounts expected to occur after the next twelve months. The foregoing range is based on considerable management judgments and the actual amounts may differ. Once we know the title that we will receive and the license fees, we include the amount in the contractual obligations table above.

- (2) Debt obligations include our Notes consisting of principal and interest payments. See Note 6 Debt to the consolidated financial statements for further details.
- (3) Operating lease obligations are comprised of operating lease liabilities included in "Accrued expenses and other liabilities" and "Other non-current liabilities" on the Consolidated Balance Sheets, inclusive of imputed interest. Operating lease obligations also include additional obligations that are not reflected on the Consolidated Balance Sheets as they did not meet the criteria for recognition. See Note 5 Balance Sheet Components in the accompanying notes to our consolidated financial statements for further details regarding leases.

As of June 30, 2023, we had gross unrecognized tax benefits of $240 million. At this time, an estimate of the range of reasonably possible adjustments to the balance of unrecognized tax benefits cannot be made.

## Free Cash Flow

We define free cash flow as cash provided by (used in) operating activities less purchases of property and equipment and change in other assets. We believe free cash flow is an important liquidity metric because it measures, during a given period, the amount of cash generated that is available to repay debt obligations, make strategic acquisitions and investments and for certain other activities like stock repurchases. Free cash flow is considered a non-GAAP financial measure and should not be considered in isolation of, or as a substitute for, net income, operating income, net cash provided by operating activities, or any other measure of financial performance or liquidity presented in accordance with GAAP.
```

---

### 🔹 [Chunk 076/088] `stre_p26_002` | Trang PDF: 26 (Doc Page: 28) | 129 tokens (574 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 129` | `strategy = "strategy_e"`

```markdown
In assessing liquidity in relation to our results of operations, we compare free cash flow to net income, noting that the major recurring differences are excess content payments over amortization, non-cash stock-based compensation expense, non-cash remeasurement gain/loss on our euro-denominated debt, and other working capital differences. Working capital differences include deferred revenue, excess property and equipment purchases over depreciation, taxes and semi-annual interest payments on our outstanding debt. Our receivables from members generally settle quickly.
```

---


# 📄 [Trang PDF 27 / Form 10-Q Trang 29] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 077/088] `stre_p27_000` | Trang PDF: 27 (Doc Page: 29) | 362 tokens (986 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 362` | `strategy = "strategy_e"`

```markdown
Three months ended June 30, 2023 as compared to the three months ended June 30, 2022

|  | Three Months Ended - June 30, 2023 - (in thousands, except percentages) | Three Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) | Change - Q2'23 vs. Q2'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | $ 1,440,232 | $ 102,750 | $ 1,337,482 | 1,302 % |
| Net cash provided by (used in) investing activities | 97,737 | (158,894) | 256,631 | 162 % |
| Net cash provided by (used in) financing activities | (649,349) | 11,250 | (660,599) | (5,872)% |
| Non-GAAP reconciliation of free cash flow: |  |  |  |  |
| Net cash provided by operating activities | 1,440,232 | 102,750 | 1,337,482 | 1,302 % |
| Purchases of property and equipment | (100,972) | (90,018) | 10,954 | 12 % |
| Free cash flow | $ 1,339,260 | $ 12,732 | $ 1,326,528 | 10,419 % |
```

---

### 🔹 [Chunk 078/088] `stre_p27_001` | Trang PDF: 27 (Doc Page: 29) | 462 tokens (1954 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 462` | `strategy = "strategy_e"`

```markdown
Net cash provided by operating activities increased $1,337 million to $1,440 million for the three months ended June 30, 2023. The increase in net cash provided by operating activities was primarily driven by a decrease in payments for content assets, coupled with a $217 million or 3% increase in revenues. The payments for content assets decreased $859 million, from $4,496 million to $3,637 million, or 19%. On May 1, 2023, the collective bargaining agreement between the Writers Guild of America ('WGA') and the Alliance of Motion Picture and Television Producers ('AMPTP') expired, and on May 2, 2023, the WGA commenced an industry-wide strike. On July 12, 2023, the collective bargaining agreement between the Screen Actors Guild - American Federation of Television and Radio Artists ('SAG-AFTRA') and the AMPTP expired, and on July 14, 2023, the SAG-AFTRA commenced an industry-wide strike. We have paused and expect to pause additional productions in response to the concurrent WGA and SAG-AFTRA strikes. As a result, the timing of certain production payments will be delayed until productions can resume and may increase the variability in payments for content assets in future periods.

Net cash provided by (used in) investing activities increased $257 million for the three months ended June 30, 2023, primarily due to proceeds from maturities of short-term investments and there being no acquisitions in the three months ended June 30, 2023, as compared to acquisitions for an aggregate amount of $69 million in the three months ended June 30, 2022, partially offset by purchases of short-term investments.

Net cash provided by (used in) financing activities decreased $661 million for the three months ended June 30, 2023, primarily due to the repurchases of common stock for an aggregate amount of $645 million in the three months ended June 30, 2023, as compared to no repurchases of common stock in the three months ended June 30, 2022.
```

---

### 🔹 [Chunk 079/088] `stre_p27_002` | Trang PDF: 27 (Doc Page: 29) | 200 tokens (832 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 200` | `strategy = "strategy_e"`

```markdown
Free cash flow was $148 million lower than net income for the three months ended June 30, 2023, primarily due to $227 million of cash payments for content assets exceeding amortization expense and $28 million in other non-favorable working capital differences, partially offset by $78 million of non-cash stock-based compensation expense and $29 million of non-cash remeasurement loss on our euro-denominated debt.

Free cash flow was $1,428 million lower than net income for the three months ended June 30, 2022, primarily due to $1,234 million of cash payments for content assets exceeding amortization expense, $305 million of non-cash remeasurement gain on our euro-denominated debt and $39 million in other nonfavorable working capital differences, partially offset by $150 million of non-cash stock-based compensation expense.
```

---


# 📄 [Trang PDF 28 / Form 10-Q Trang 30] — Mục: *Management’s Discussion and Analysis*

### 🔹 [Chunk 080/088] `stre_p28_000` | Trang PDF: 28 (Doc Page: 30) | 453 tokens (1372 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 453` | `strategy = "strategy_e"`

```markdown
Six months ended June 30, 2023 as compared to the six months ended June 30, 2022

|  | Six Months Ended - June 30, 2023 - (in thousands, except percentages) | Six Months Ended - June 30, 2022 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) | Change - YTD'23 vs. YTD'22 - (in thousands, except percentages) |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | $ 3,618,972 | $ 1,025,589 | $ 2,593,383 | 253 % |
| Net cash used in investing activities | (165,916) | (404,573) | (238,657) | (59)% |
| Net cash used in financing activities | (1,023,422) | (675,072) | 348,350 | 52 % |
| Non-GAAP reconciliation of free cash flow: |  |  |  |  |
| Net cash provided by operating activities | 3,618,972 | 1,025,589 | 2,593,383 | 253 % |
| Purchases of property and equipment | (162,991) | (211,176) | (48,185) | (23)% |
| Free cash flow | $ 3,455,981 | $ 814,413 | $ 2,641,568 | 324 % |

Net cash provided by operating activities increased $2,593 million to $3,619 million for the six months ended June 30, 2023. The increase in net cash provided by operating activities was primarily driven by a decrease in payments for content assets, coupled with a $511 million or 3% increase in revenues. The payments for content assets decreased $1,977 million, from $8,427 million to $6,450 million, or 23%.
```

---

### 🔹 [Chunk 081/088] `stre_p28_001` | Trang PDF: 28 (Doc Page: 30) | 474 tokens (2012 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 474` | `strategy = "strategy_e"`

```markdown
Net cash used in investing activities decreased $239 million for the six months ended June 30, 2023, primarily due to proceeds from the maturities of short-term investments and there being no acquisitions in the six months ended June 30, 2023, as compared to acquisitions for an aggregate amount of $193 million in the six months ended June 30, 2022, partially offset by purchases of short-term investments.

Net cash used in financing activities increased $348 million for the six months ended June 30, 2023, primarily due to repurchases of common stock for an aggregate amount of $1,045 million in the six months ended June 30, 2023, as compared to no repurchases of common stock in the six months ended June 30, 2022, partially offset by there being no repayment of debt in the six months ended June 30, 2023 as compared to the repayment upon maturity of the $700 million aggregate principal amount of our 5.500% Senior Notes in February 2022.

Free cash flow was $663 million higher than net income for the six months ended June 30, 2023 primarily due to $420 million of amortization expense exceeding cash payments for content assets, $177 million of non-cash stock-based compensation expense and $110 million of non-cash remeasurement loss on our euro-denominated debt, partially offset by $44 million in other non-favorable working capital differences.

Free cash flow was $2,224 million lower than net income for the six months ended June 30, 2022 primarily due to $1,999 million of cash payments for content assets exceeding amortization expense, $466 million of non-cash remeasurement gain on our euro-denominated debt and $29 million in other nonfavorable working capital differences, partially offset by $270 million of non-cash stock-based compensation expense.

## Indemnification

The information set forth under Note 7 Commitments and Contingencies to the consolidated financial statements under the caption 'Indemnification' is incorporated herein by reference.

## Critical Accounting Estimates
```

---

### 🔹 [Chunk 082/088] `stre_p28_002` | Trang PDF: 28 (Doc Page: 30) | 198 tokens (938 ký tự)
> **Metadata:** `section = "Management’s Discussion and Analysis"` | `tokens = 198` | `strategy = "strategy_e"`

```markdown
The preparation of financial statements and related disclosures in conformity with U.S. generally accepted accounting principles and the Company's discussion and analysis of its financial condition and operating results require the Company's management to make judgments, assumptions and estimates that affect the amounts reported. Note 1, 'Basis of Presentation and Summary of Significant Accounting Policies' of the Notes to consolidated Financial Statements in Part I, Item 1 of this Form 10-Q and in the Notes to Consolidated Financial Statements in Part II, Item 8 of our Annual Report on Form 10-K for the year ended December 31, 2022, describe the significant accounting policies and methods used in the preparation of the Company's consolidated financial statements. There have been no material changes to the Company's critical accounting estimates included in our Annual Report on Form 10-K for the year ended December 31, 2022.
```

---


# 📄 [Trang PDF 29 / Form 10-Q Trang 31] — Mục: *Market Risk*

### 🔹 [Chunk 083/088] `stre_p29_000` | Trang PDF: 29 (Doc Page: 31) | 431 tokens (1935 ký tự)
> **Metadata:** `section = "Market Risk"` | `tokens = 431` | `strategy = "strategy_e"`

```markdown
## Item 3. Quantitative and Qualitative Disclosures About Market Risk

For financial market risks related to changes in interest rates, reference is made to Item 7A 'Quantitative and Qualitative Disclosures About Market Risk' contained in Part II of our Annual Report on Form 10-K for the year ended December 31, 2022. Our exposure to market risk has not changed significantly since December 31, 2022.

## Interest Rate Risk

At June 30, 2023, our cash equivalents and short-term investments were generally invested in money market funds and time deposits. Interest paid on such funds fluctuates with the prevailing interest rate.

As of June 30, 2023, we had $14.5 billion of debt, consisting of fixed rate unsecured debt in fourteen tranches due between 2024 and 2030. Refer to Note 6 Debt to the consolidated financial statements for details about all issuances. The fair value of our debt will fluctuate with movements of interest rates, increasing in periods of declining rates of interest and declining in periods of increasing rates of interest. The fair value of our debt will also fluctuate based on changes in foreign currency rates, as discussed below.

## Foreign Currency Risk

Currencies denominated in other than the U.S. dollar account for 57% of revenue for the six months ended June 30, 2023. We therefore have foreign currency risk related to these currencies, which are primarily the euro, the British pound, the Brazilian real, the Canadian dollar, the Mexican Peso, the Japanese yen, and the Australian dollar.

Accordingly, changes in exchange rates, and in particular a weakening of foreign currencies relative to the U.S. dollar may negatively affect our revenue and operating income as expressed in U.S. dollars. In the six months ended June 30, 2023, our revenues would have been approximately $577 million higher had foreign currency exchange rates remained consistent with those in the same period of 2022.
```

---

### 🔹 [Chunk 084/088] `stre_p29_001` | Trang PDF: 29 (Doc Page: 31) | 279 tokens (1271 ký tự)
> **Metadata:** `section = "Market Risk"` | `tokens = 279` | `strategy = "strategy_e"`

```markdown
We have also experienced and will continue to experience fluctuations in our net income as a result of gains (losses) on the settlement and the remeasurement of monetary assets and liabilities denominated in currencies that are not the functional currency. In the six months ended June 30, 2023, we recognized a $130 million foreign exchange loss primarily due to the non-cash remeasurement of our Senior Notes denominated in euros, coupled with the remeasurement of cash and content liabilities denominated in currencies other than the functional currencies.

In addition, the effect of exchange rate changes on cash, cash equivalents and restricted cash as disclosed on the Consolidated Statements of Cash Flow for the six months ended June 30, 2023 was an increase of $66 million.

We do not use foreign exchange contracts or derivatives to hedge any foreign currency exposures. The volatility of exchange rates depends on many factors that we cannot forecast with reliable accuracy. Our continued international expansion increases our exposure to exchange rate fluctuations and, as a result, such fluctuations could have a significant impact on our future results of operations.

## Item 4. Controls and Procedures

## Evaluation of Disclosure Controls and Procedures
```

---

### 🔹 [Chunk 085/088] `stre_p29_002` | Trang PDF: 29 (Doc Page: 31) | 445 tokens (2117 ký tự)
> **Metadata:** `section = "Market Risk"` | `tokens = 445` | `strategy = "strategy_e"`

```markdown
Our management, with the participation of our co-Chief Executive Officers and Chief Financial Officer, evaluated the effectiveness of our disclosure controls and procedures (as defined in Rules 13a-15(e) and 15d-15(e) under the Exchange Act) as of the end of the period covered by this Quarterly Report on Form 10-Q. Based on that evaluation, our co-Chief Executive Officers and Chief Financial Officer concluded that our disclosure controls and procedures as of the end of the period covered by this Quarterly Report on Form 10-Q were effective in providing reasonable assurance that information required to be disclosed by us in reports that we file or submit under the Exchange Act, is recorded, processed, summarized and reported within the time periods specified in the Securities and Exchange Commission's rules and forms, and that such information is accumulated and communicated to our management, including our coChief Executive Officers and Chief Financial Officer, as appropriate, to allow timely decisions regarding required disclosures.

Our management, including our co-Chief Executive Officers and Chief Financial Officer, does not expect that our disclosure controls and procedures or our internal controls will prevent all error and all fraud. A control system, no matter how well conceived and operated, can provide only reasonable, not absolute, assurance that the objectives of the control system are met. Further, the design of a control system must reflect the fact that there are resource constraints, and the benefits of controls must be considered relative to their costs. Because of the inherent limitations in all control systems, no evaluation of controls can provide absolute assurance that all control issues and instances of fraud, if any, within the Company have been detected.

## Changes in Internal Control Over Financial Reporting

There were no changes in our internal control over financial reporting that occurred during the quarter ended June 30, 2023, that have materially affected, or are reasonably likely to materially affect, our internal control over financial reporting.
```

---


# 📄 [Trang PDF 30 / Form 10-Q Trang 32] — Mục: *Other Information*

### 🔹 [Chunk 086/088] `stre_p30_000` | Trang PDF: 30 (Doc Page: 32) | 60 tokens (258 ký tự)
> **Metadata:** `section = "Other Information"` | `tokens = 60` | `strategy = "strategy_e"`

```markdown
## Item 1. Legal Proceedings

The information set forth under Note 7 Commitments and Contingencies in the notes to the consolidated financial statements under the caption 'Legal Proceedings' is incorporated herein by reference.

## PART II. OTHER INFORMATION
```

---


# 📄 [Trang PDF 31 / Form 10-Q Trang 33] — Mục: *Other Information*

### 🔹 [Chunk 087/088] `stre_p31_000` | Trang PDF: 31 (Doc Page: 33) | 498 tokens (1736 ký tự)
> **Metadata:** `section = "Other Information"` | `tokens = 498` | `strategy = "strategy_e"`

```markdown
## Item 1A. Risk Factors

There have been no material changes from the risk factors previously disclosed under the heading "Risk Factors" in the Company's Annual Report on Form 10-K for the year ended December 31, 2022.

## Item 2. Unregistered Sales of Equity Securities and Use of Proceeds

## Company Purchases of Equity Securities

Stock repurchases during the three months ended June 30, 2023 were as follows:

| Period | Total Number of Shares Purchased (1) | Average Price Paid per Share (2) | Total Number of Shares Purchased as Part of Publicly Announced Programs (1) | Approximate Dollar Value of Shares that May Yet Be Purchased Under the Program (1) (in thousands) |
| --- | --- | --- | --- | --- |
| April 1 - 30, 2023 | - | $ - | - | $ 4,000,000 |
| May 1 - 31, 2023 | 1,417,075 | $ 336.81 | 1,417,075 | $ 3,522,717 |
| June 1 - 30, 2023 | 432,249 | $ 388.35 | 432,249 | $ 3,354,855 |
| Total | 1,849,324 |  | 1,849,324 |  |

(1) In March 2021, the Company's Board of Directors authorized the repurchase of up to $5 billion of its common stock, with no expiration date. For further information regarding stock repurchase activity, see Note 8 Stockholders' Equity to the consolidated financial statements in this Quarterly Report.

(2) Average price paid per share includes costs associated with the repurchases.

## Item 5. Other Information

## Rule 10b5-1 Trading Plans

The adoption or termination of contracts, instructions or written plans for the purchase or sale of our securities by our Section 16 officers and directors for the three months ended June 30, 2023, each of which is intended to satisfy the affirmative defense conditions of Rule 10b5-1(c) under the Exchange Act ('Rule 10b5-1 Plan'), were as follows:
```

---

### 🔹 [Chunk 088/088] `stre_p31_001` | Trang PDF: 31 (Doc Page: 33) | 394 tokens (1337 ký tự)
> **Metadata:** `section = "Other Information"` | `tokens = 394` | `strategy = "strategy_e"`

```markdown
| Name | Title | Action | Date Adopted | Expiration Date | Aggregate # of Securities to be Purchased/Sold |
| --- | --- | --- | --- | --- | --- |
| Ann Mather (1) | Director | Adoption | 5/4/2023 | 2/28/2025 | 6,385 |
| Ted Sarandos (2) | Co-CEO and Director | Adoption | 5/5/2023 | 8/2/2024 | 55,386 |

(1) Ann Mather, a member of the Board of Directors, entered into a Rule 10b5-1 Plan on May 4, 2023. Ms. Mather's plan provides for the potential exercise of vested stock options and the associated sale of up to 6,385 shares of the Company's common stock. The plan expires on February 28, 2025, or upon the earlier completion of all authorized transactions under the plan.

(2) Ted Sarandos, co-CEO and a member of the Board of Directors, entered into a Rule 10b5-1 Plan on May 5, 2023. Mr. Sarandos' plan provides for the potential exercise of vested stock options and the associated sale of up to 55,386 shares of the Company's common stock. The plan expires on August 2, 2024, or upon the earlier completion of all authorized transactions under the plan.

None of our directors or officers adopted or terminated a "non-Rule 10b5-1 trading arrangement" as defined in Item 408 of Regulation S-K.

## Item 6. Exhibits

## (a) Exhibits:

See Exhibit Index immediately following the signature page of this Quarterly Report on Form 10-Q.
```

---
