# Thư Mục Các Bản Markdown Tách Theo Chunk (5 Cấu Hình Token BGE-M3)
Tài liệu văn bản **Netflix Form 10-Q (Q2 2023)** sau khi chuẩn hóa khoảng trắng, được tách theo Tokenizer của BGE-M3.

| Tệp Markdown | Chiến Lược | Thuật toán & Tham số | Số Chunks | Độ dài Tokens (TB) | Độ dài Ký tự (TB) |
|---|---|---|:---:|:---:|:---:|
| [`strategy_a_fixed.md`](./strategy_a_fixed.md) | **Strategy A: Fixed-Size Token Window** | `{'token_size': 500, 'overlap': 50}` | **78** | 406.9 tokens | 1412.8 ký tự |
| [`strategy_b_recursive.md`](./strategy_b_recursive.md) | **Strategy B: Recursive Token Chunking** | `{'max_tokens': 500, 'overlap': 50, 'separators': ['\\n\\n', '\\n', '. ', ' ']}` | **88** | 333.9 tokens | 1164.0 ký tự |
| [`strategy_c_section.md`](./strategy_c_section.md) | **Strategy C: Section-Based Token Chunking** | `{'max_tokens': 500, 'overlap': 50, 'header_boundary_aware': True}` | **78** | 406.9 tokens | 1412.9 ký tự |
| [`strategy_d_paragraph.md`](./strategy_d_paragraph.md) | **Strategy D: Paragraph-Based Token Chunking (No Filter)** | `{'max_tokens': 500, 'overlap': 50, 'filter': False}` | **88** | 337.4 tokens | 1170.4 ký tự |
| [`strategy_e_paragraph_filter.md`](./strategy_e_paragraph_filter.md) | **Strategy E: Paragraph-Based Token Chunking + Metadata Filter** | `{'max_tokens': 500, 'overlap': 50, 'filter': True, 'filter_field': 'section'}` | **88** | 337.4 tokens | 1170.4 ký tự |