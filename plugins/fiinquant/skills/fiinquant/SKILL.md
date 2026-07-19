---
name: fiinquant
description: >-
  Sinh code Python FiinQuantX chính xác cho thị trường chứng khoán Việt Nam.
  Kích hoạt khi người dùng hỏi/cần code về: cài đặt, đăng nhập (install, login,
  setup); danh sách mã, rổ chỉ số, ngành (ticker, index, VN30, VNINDEX, sector,
  ICB, vốn hóa, room ngoại, freefloat); giá realtime, lịch sử, sổ lệnh, tick
  (realtime, historical, OHLCV, orderbook); BCTC, P/E, P/B, ROE, định giá
  (financial statement, valuation, ratios); độ rộng thị trường, seasonality
  (market breadth); rebalance, RRG, tối ưu danh mục (portfolio optimization);
  đặt/sửa/hủy lệnh, vị thế, tài khoản (place order, position, account); chỉ báo
  kỹ thuật SMA, EMA, RSI, MACD, Bollinger, ATR, OBV, fibonacci, Smart Money
  (technical indicators, SMC); mô hình nến, vai đầu vai, cốc tay cầm
  (candlestick chart patterns); lọc cổ phiếu (stock screening, screener).
  FiinQuantX là thư viện dữ liệu tài chính Python (HOSE/HNX/UPCOM). Luôn đọc file
  references/ theo bản đồ định tuyến bên dưới TRƯỚC khi viết code.
---

# 🧭 FiinQuant Skill Dispatcher

> **Mục đích**: Đây là skill điều phối trung tâm cho thư viện **FiinQuantX**. Khi nhận
> được câu hỏi từ người dùng, hệ thống PHẢI đọc file này trước để xác định nhóm hàm nào
> cần dùng, sau đó **mở đúng file `references/<tên>.md`** để đọc chi tiết signature,
> tham số và ví dụ trước khi viết code.
>
> **Cơ chế progressive disclosure:** File `SKILL.md` này luôn được nạp; mỗi file trong
> `references/` chỉ được đọc khi câu hỏi cần đến nhóm hàm tương ứng.
>
> **Phiên bản thư viện:** Bộ reference viết theo `FiinQuantX` bản **mới nhất (latest)**
> trên index chính thức — xem `README.md` để biết cách cài đặt/cập nhật.

---

## 1. Bản đồ điều phối (Routing Map)

### Nhóm 0 — Cài đặt & Giới thiệu
**Khi nào trigger:** Người dùng hỏi về cài đặt, setup, import, login, lỗi cài đặt, giới thiệu FiinQuant.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `cài đặt`, `install`, `pip`, `setup`, `import`, `FiinQuant là gì`, `hướng dẫn sử dụng`, `đăng nhập`, `login`, `lỗi import`, `NameError` | **Cài đặt & Giới thiệu** | `references/0-installation-introduction.md` |

> [!TIP]
> Nếu người dùng hỏi "Làm sao để dùng FiinQuant?" (câu hỏi chung chung), hãy
> cung cấp tổng quan ngắn gọn từ file này, sau đó HỎI LẠI người dùng muốn làm gì cụ thể.

---

### Nhóm 1 — Danh mục & Thông tin cơ bản
**Khi nào trigger:** Người dùng cần danh sách mã chứng khoán, thông tin công ty, vốn hóa, room ngoại, freefloat, giá trần sàn.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `danh sách mã`, `VN30`, `HNX30`, `rổ chỉ số`, `VNINDEX`, `VN100`, `thành phần` | **1.1. Danh sách mã theo index** | `references/1.1-ticker-list-by-index.md` |
| `ngành`, `ngân hàng`, `bất động sản`, `thép`, `công nghệ`, `sector`, `ICB` | **1.2. Danh sách mã theo ngành** | `references/1.2-ticker-list-by-sector.md` |
| `tỷ trọng`, `trọng số`, `weight`, `market cap weight` | **1.3. Danh sách mã theo tỷ trọng** | `references/1.3-ticker-list-by-weight.md` |
| `vốn hóa`, `market cap`, `giá trị vốn hóa` | **1.4. Lấy dữ liệu vốn hóa** | `references/1.4-market-cap.md` |
| `room nước ngoài`, `room ngoại`, `NĐTNN`, `foreign room`, `tỷ lệ room` | **1.5. Lấy dữ liệu room NĐTNN** | `references/1.5-foreign-room.md` |
| `freefloat`, `free float`, `cổ phiếu tự do lưu hành` | **1.6. Lấy dữ liệu Freefloat** | `references/1.6-freefloat.md` |
| `giá trần`, `giá sàn`, `ceiling`, `floor`, `tham chiếu` | **1.7. Lấy dữ liệu giá trần, giá sàn** | `references/1.7-ceiling-floor-price.md` |
| `giao dịch theo nhà đầu tư`, `tổ chức`, `cá nhân`, `tự doanh`, `khối ngoại mua ròng` | **1.8. Giao dịch theo nhà đầu tư** | `references/1.8-trading-by-investor.md` |
| `thông tin cơ bản`, `tên công ty`, `sàn giao dịch`, `ngành nghề`, `company profile`, `hồ sơ công ty` | **1.9. Thông tin cơ bản của mã** | `references/1.9-ticker-basic-info.md` |

> [!IMPORTANT]
> **Bẫy nhập nhằng phổ biến:**
> - "Các công ty về công nghệ" → Có nhiều phân ngành ICB. PHẢI hỏi lại người dùng muốn phân ngành nào.
> - "Thông tin VNM" → Quá mơ hồ. Cần hỏi: thông tin cơ bản? giá? tài chính? kỹ thuật?
> - Mã viết sai format (VN-30 thay vì VN30) → Tự động sửa và giải thích.

---

### Nhóm 2 — Dữ liệu giao dịch
**Khi nào trigger:** Người dùng cần giá realtime, giá lịch sử, sổ lệnh, dữ liệu tick, merge dữ liệu.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `giá realtime`, `giá hiện tại`, `cập nhật giá`, `livestream`, `real-time`, `streaming`, `websocket` | **2.1. Hàm dữ liệu Realtime** | `references/2.1-realtime-data.md` |
| `dữ liệu lịch sử`, `giá quá khứ`, `historical`, `OHLCV`, `từ ngày đến ngày`, `timeframe`, `nến` | **2.2. Hàm dữ liệu Lịch sử** | `references/2.2-historical-data.md` |
| `kết hợp lịch sử và realtime`, `merge data`, `ghép dữ liệu`, `nối realtime` | **2.3. Nối dữ liệu Realtime và lịch sử** | `references/2.3-merge-realtime-historical.md` |
| `sổ lệnh`, `orderbook`, `bid ask`, `bước giá`, `khối lượng chờ` | **2.4. Hàm dữ liệu sổ lệnh** | `references/2.4-orderbook-data.md` |
| `theo dõi hủy lệnh`, `lệnh bị hủy`, `cancel tracking` | **2.5. Hàm theo dõi huỷ lệnh** | `references/2.5-cancel-order-tracking.md` |
| `quản lý kết nối`, `connection lifecycle`, `reconnect`, `quota websocket`, `tối ưu tốc độ`, `cache`, `sidecar`, `nhiều mã realtime` | **2.6. Quản lý kết nối và tối ưu hiệu năng** | `references/2.6-connection-lifecycle-performance.md` |
| `tick data`, `tick by tick`, `từng tick`, `lịch sử khớp lệnh` | **2.2. Hàm dữ liệu Lịch sử** (timeframe tick) | `references/2.2-historical-data.md` |

> [!IMPORTANT]
> **Bẫy nhập nhằng phổ biến:**
> - "Lấy dữ liệu lịch sử VNM" — thiếu timeframe và khoảng thời gian → PHẢI hỏi lại:
>   - Timeframe nào? (1min, 5min, 15min, 1h, 4h, 1D)
>   - Từ ngày nào đến ngày nào?
> - "Giá VNM" — không rõ realtime hay lịch sử → Hỏi lại hoặc mặc định trả giá realtime.
> - Ngày sai format (1-1-2024 thay vì 2024-01-01) → Tự động convert và thông báo.

---

### Nhóm 3 — Phân tích cơ bản & Định giá
**Khi nào trigger:** Người dùng hỏi về BCTC, chỉ số tài chính, P/E, P/B, định giá.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `báo cáo tài chính`, `BCTC`, `financial statement`, `bảng cân đối`, `kết quả kinh doanh`, `lưu chuyển tiền tệ` | **3.1. Báo cáo tài chính** | `references/3.1-financial-statements.md` |
| `chỉ số tài chính`, `ROE`, `ROA`, `EPS`, `debt/equity`, `financial ratios`, `tỷ suất lợi nhuận` | **3.2. Chỉ số báo cáo tài chính** | `references/3.2-financial-ratios.md` |
| `P/E`, `P/B`, `định giá theo mã`, `valuation`, `PE ratio`, `PB ratio` (1 hoặc nhiều **mã cổ phiếu**) | **3.3. Định giá P/E, P/B theo mã** → `get_stock_valuation` | `references/3.3-stock-valuation-pe-pb.md` |
| `P/E`, `P/B`, `định giá theo chỉ số`, `định giá VN30/VNINDEX` (1 hoặc nhiều **nhóm chỉ số**) | **3.4. Định giá P/E, P/B theo nhóm chỉ số** → `get_index_valuation` | `references/3.4-index-valuation-pe-pb.md` |

> [!IMPORTANT]
> **Phân biệt 3.3 vs 3.4 (tránh nhầm — đây là 2 hàm KHÁC nhau):**
> - **3.3** = `get_stock_valuation` → định giá P/E, P/B của **một/nhiều MÃ cổ phiếu** (VNM, HPG…).
> - **3.4** = `get_index_valuation` → định giá P/E, P/B của **một/nhiều NHÓM CHỈ SỐ** (VN30, VNINDEX…).
> - Đầu vào quyết định: nếu user đưa mã CP → 3.3; nếu user đưa tên rổ/chỉ số → 3.4.
>
> **Bẫy nhập nhằng phổ biến:**
> - "Báo cáo tài chính VNM" — thiếu loại báo cáo (CĐKT/KQKD/LCTT) và kỳ → HỎI LẠI loại + kỳ, hoặc gợi ý mặc định kỳ gần nhất.
> - "P/E của HPG" — HPG ngành thép, P/E có thể âm hoặc rất cao → PHẢI giải thích ngữ cảnh.

---

### Nhóm 4 — Thống kê thị trường
**Khi nào trigger:** Người dùng hỏi về tổng quan thị trường, số mã tăng/giảm, seasonality.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `độ rộng thị trường`, `market breadth`, `số mã tăng giảm`, `advance decline`, `mã trần sàn` | **4.1. Độ rộng thị trường** | `references/4.1-market-breadth.md` |
| `seasonality`, `mùa vụ giá`, `biến động theo tháng/quý`, `hiệu ứng lịch` | **4.3. SeasonalityPrice** | `references/4.3-seasonality-price.md` |

---

### Nhóm 5 — Chiến lược & Công cụ
**Khi nào trigger:** Người dùng hỏi về rebalance, tái cơ cấu, biểu đồ RRG, portfolio optimization.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `rebalance`, `tái cơ cấu`, `cân bằng lại`, `phân bổ lại`, `điều chỉnh tỷ trọng` | **5.1. Rebalance** | `references/5.1-rebalance.md` |
| `RRG`, `relative rotation`, `sức mạnh giá`, `biểu đồ xoay vòng`, `quadrant` | **5.2. Biểu đồ sức mạnh giá (RRG)** | `references/5.2-rrg-relative-rotation.md` |

> [!WARNING]
> **Nhóm kỹ năng dễ bị bỏ sót (F1=0.0 trong trigger test):**
> - `portfolio_optimization` / `rebalance` — Các câu như "tối ưu danh mục", "Markowitz",
>   "efficient frontier", "phân bổ vốn" PHẢI được route vào nhóm 5.
> - Hệ thống thường nhầm lẫn giữa `rebalance` (tái cơ cấu) với `stock_screening` (lọc cổ phiếu).

---

### Nhóm 6 — Đặt lệnh giao dịch
**Khi nào trigger:** Người dùng muốn đặt/sửa/hủy lệnh, xem tài khoản, vị thế, danh sách lệnh.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `đăng nhập đặt lệnh`, `login broker`, `kết nối DNSE`, `FiinQuantConnector` | **6.1. Đăng nhập** | `references/6.1-login.md` |
| `thông tin tài khoản`, `số dư`, `account info` | **6.2. Thông tin tài khoản** | `references/6.2-account-info.md` |
| `gói vay`, `nguồn tiền`, `loan`, `margin` | **6.3. Thông tin gói vay** | `references/6.3-loan-package.md` |
| `khởi tạo orderbook`, `get_orderbook`, `get_derivative_orderbook` | **6.4. Khởi tạo OrderBook** | `references/6.4-init-orderbook.md` |
| `thông tin tiền`, `số dư tiền`, `cash info` | **6.5. Thông tin tiền** | `references/6.5-cash-info.md` |
| `sức mua`, `sức bán`, `buying power`, `selling power` | **6.6. Sức mua-bán** | `references/6.6-buying-selling-power.md` |
| `đặt lệnh mua`, `đặt lệnh bán`, `place order`, `mua cổ phiếu`, `bán cổ phiếu`, `lệnh LO`, `lệnh MP`, `sửa lệnh`, `hủy lệnh`, `cancel order` | **6.7. Lệnh** | `references/6.7-place-order.md` |
| `danh sách lệnh`, `lệnh đang chờ`, `pending orders`, `order list` | **6.8. Danh sách lệnh** | `references/6.8-order-list.md` |
| `vị thế`, `position`, `cổ phiếu đang giữ`, `danh mục nắm giữ`, `holdings` | **6.9. Lấy vị thế** | `references/6.9-get-position.md` |
| `đóng deal`, `close position`, `phái sinh` | **6.10. Đóng deal (phái sinh)** | `references/6.10-close-deal-derivative.md` |

> [!CAUTION]
> **⚠️ NHÓM AN TOÀN QUAN TRỌNG — CẦN XÁC NHẬN KÉP:**
> - Mọi thao tác đặt/sửa/hủy lệnh PHẢI yêu cầu xác nhận từ người dùng trước khi thực thi.
> - Nếu thiếu thông tin (mã, số lượng, giá, loại lệnh) → PHẢI hỏi đầy đủ, KHÔNG giả định.
> - "Mua VNM" (thiếu số lượng, giá) → HỎI LẠI: bao nhiêu cổ? giá bao nhiêu? loại lệnh gì?
> - Số lượng lớn bất thường (> 100,000 cổ) → CẢNH BÁO và hỏi xác nhận lần 2.

---

### Nhóm 7 — Chỉ báo kỹ thuật (Technical Analysis)
**Khi nào trigger:** Người dùng hỏi về MA, RSI, MACD, Bollinger, OBV, Smart Money, v.v.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `SMA`, `EMA`, `MA`, `đường trung bình`, `trend`, `xu hướng`, `DEMA`, `TEMA`, `WMA` | **7.1. Trend Indicators** | `references/7.1-trend-indicators.md` |
| `RSI`, `MACD`, `Stochastic`, `momentum`, `động lượng`, `CCI`, `Williams %R`, `ROC` | **7.2. Momentum Indicators** | `references/7.2-momentum-indicators.md` |
| `Bollinger Bands`, `ATR`, `Keltner Channel`, `biến động giá`, `volatility`, `BB` | **7.3. Volatility Indicators** | `references/7.3-volatility-indicators.md` |
| `OBV`, `Volume Profile`, `khối lượng`, `volume`, `VWAP`, `chỉ báo khối lượng` | **7.4. Volume Indicators** | `references/7.4-volume-indicators.md` |
| `Order Block`, `Fair Value Gap`, `FVG`, `Smart Money`, `Change of Character`, `BOS`, `Break of Structure` | **7.5. Smart Money Concepts** | `references/7.5-smart-money-concepts.md` |
| `risk`, `rủi ro`, `Sharpe Ratio`, `Sortino`, `Max Drawdown`, `VaR`, `Value at Risk` | **7.6. Risk Indicators** | `references/7.6-risk-indicators.md` |
| `dòng tiền`, `money flow`, `MFI`, `CMF`, `Chaikin`, `BU-SD`, `mua bán ròng` | **7.7. Money Flow Indicators** | `references/7.7-money-flow-indicators.md` |
| `hỗ trợ kháng cự`, `support resistance`, `pivot`, `trendline`, `đường xu hướng`, `kênh giá`, `fibonacci`, `fibo`, `thoái lui` | **7.8. Price Level Indicators** | `references/7.8-price-level-indicators.md` |

> [!WARNING]
> **Nhóm kỹ năng dễ bị bỏ sót (F1=0.0 trong trigger test):**
> - `volatility_indicators` — "Bollinger Bands", "ATR", "dải biến động" → Route vào 7.3
> - `trendline_analysis` / `fibonacci_retracement` — "vẽ trendline", "kênh giá",
>   "fibonacci thoái lui", "mức fibo", "kéo fibo" → Route vào 7.8
> - Hệ thống thường nhầm các câu về fibonacci/trendline thành trend_indicators (7.1).
>   **Quy tắc phân biệt:**
>   - 7.1 = Chỉ báo tính toán (SMA, EMA, DEMA...) → trả về chuỗi số
>   - 7.8 = Chỉ báo mức giá (hỗ trợ/kháng cự, trendline, fibonacci) → trả về vùng giá cụ thể

---

### Nhóm 8 — Mô hình biểu đồ (Chart Patterns)
**Khi nào trigger:** Người dùng hỏi về nhận dạng mô hình nến, mô hình giá.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `mô hình nến`, `chart pattern`, `candlestick`, `vai đầu vai`, `head and shoulders`, `cốc tay cầm`, `cup and handle`, `double top`, `double bottom`, `mẫu hình`, `bullish engulfing`, `bearish`, `đảo chiều`, `tiếp diễn` | **8.1. Mô hình biểu đồ** | `references/8.1-chart-patterns.md` |

> [!WARNING]
> **Nhóm kỹ năng dễ bị bỏ sót (F1=0.0 trong trigger test):**
> - `chart_patterns` — "mô hình Cốc tay cầm", "Vai đầu vai", "candlestick pattern"
>   → PHẢI route vào nhóm 8, KHÔNG nhầm với 7.1 (trend) hay 7.2 (momentum).
> - **Quy tắc phân biệt:** Nếu người dùng nói về HÌNH DẠNG biểu đồ → Nhóm 8.
>   Nếu nói về CHỈ SỐ tính toán → Nhóm 7.

---

### Nhóm 9 — Bộ lọc cổ phiếu (Stock Screening)
**Khi nào trigger:** Người dùng muốn lọc/tìm cổ phiếu theo điều kiện.

| Từ khóa / Intent | Nhóm hàm | File reference |
|---|---|---|
| `lọc cổ phiếu`, `tìm cổ phiếu`, `screen`, `bộ lọc`, `CP có PE <`, `ROE >`, `điều kiện lọc`, `stock screener` | **9. Bộ lọc cổ phiếu** | `references/9-stock-screening.md` |

> [!TIP]
> Viết tắt phổ biến: "CP" = "cổ phiếu". Hệ thống cần nhận diện các viết tắt thường gặp của tiếng Việt.

---

## 1b. Reference dữ liệu (schema & danh mục giá trị)

Các file dưới đây KHÔNG mô tả hàm mà là bảng tra cứu, đọc khi cần map giá trị/đầu ra:

| Khi nào đọc | File reference |
|---|---|
| Danh mục index/ngành/field hợp lệ để truyền vào hàm | `references/code_lists.md` |
| Ý nghĩa các trường đầu ra của hàm chỉ số tài chính | `references/financial_indicator_output.md` |
| Schema field của báo cáo tài chính | `references/financial_statement_field_schema.md` |
| Mẫu đầu ra báo cáo tài chính | `references/financial_statement_output.md` |
| Danh mục field dùng cho bộ lọc cổ phiếu | `references/stock_screening_filter.md` |

---

## 2. Quy tắc xử lý đa kỹ năng (Cross-Skill Orchestration)

Khi câu hỏi của người dùng YÊU CẦU NHIỀU NHÓM HÀM cùng lúc, hệ thống PHẢI tuân thủ quy trình sau:

### 2.1. Phân tách yêu cầu
Tách câu hỏi phức tạp thành từng bước đơn lẻ, mỗi bước map với 1 nhóm hàm.

**Ví dụ:**
> "Phân tích toàn diện VNM: BCTC, chỉ số tài chính, giá lịch sử 6 tháng, chỉ báo kỹ thuật, và khuyến nghị"

→ Phân tách thành:
1. **Bước 1**: Đọc `references/3.1-financial-statements.md` → Lấy BCTC VNM
2. **Bước 2**: Đọc `references/3.2-financial-ratios.md` → Tính ROE, ROA, EPS...
3. **Bước 3**: Đọc `references/2.2-historical-data.md` → Lấy giá 6 tháng
4. **Bước 4**: Đọc `references/7.1-trend-indicators.md` + `7.2` + `7.3` → Tính SMA, RSI, Bollinger...
5. **Bước 5**: Tổng hợp → Đưa ra khuyến nghị dựa trên kết quả 4 bước trên

### 2.2. Thứ tự ưu tiên nhóm hàm
Khi có xung đột hoặc phụ thuộc:
- **Dữ liệu trước, phân tích sau**: Luôn lấy dữ liệu (Nhóm 1-2) trước khi phân tích (Nhóm 3-4, 7-8)
- **Login trước, lệnh sau**: Mọi thao tác Nhóm 6 đều yêu cầu đăng nhập qua `6.1` trước
- **Lọc trước, phân tích sau**: Nếu "lọc cổ phiếu rồi phân tích" → Nhóm 9 trước, rồi đến nhóm phân tích

### 2.3. Mẫu kịch bản phức tạp thường gặp

| Kịch bản | Chuỗi nhóm hàm |
|---|---|
| "Lọc top 10 theo ROE rồi backtest MA crossover" | `9 → 2.2 → 7.1` |
| "Theo dõi realtime, khi RSI < 30 thì mua" | `2.1 → 7.2 → 6.7` |
| "So sánh tài chính VNM vs VIC qua 4 quý" | `3.1 (×2) → 3.2 (×2)` |
| "Rebalance VN30 theo quý, backtest từ 2020" | `1.1 → 5.1 → 2.2` |
| "Tìm mô hình đảo chiều trên toàn VN30" | `1.1 → 8.1` |

---

## 3. Quy tắc xử lý Edge Cases

### 3.1. Input mơ hồ / thiếu thông tin
```
LUÔN HỎI LẠI trước khi hành động. Các trường hợp PHẢI hỏi:
- Thiếu mã cổ phiếu → "Bạn muốn xem mã nào?"
- Thiếu khoảng thời gian → "Từ ngày nào đến ngày nào?"
- Thiếu timeframe → "Timeframe nào? (1min/5min/15min/1h/4h/1D)"
- Thiếu loại báo cáo → "Loại BCTC nào? (CĐKT/KQKD/LCTT)"
- Thiếu kỳ báo cáo → "Quý/năm nào?"
- Thiếu thông tin lệnh → "Số lượng? Giá? Loại lệnh?"
```

### 3.2. Input sai format
```
TỰ ĐỘNG SỬA và THÔNG BÁO cho người dùng:
- "VN-30" → "VN30" (tự sửa, giải thích format đúng)
- "1-1-2024" → "2024-01-01" (tự convert, nêu format chuẩn)
- "CP" → "cổ phiếu" (nhận diện viết tắt tiếng Việt)
- "vnm" → "VNM" (tự uppercase mã chứng khoán)
```

### 3.3. Mã cổ phiếu không tồn tại
```
KHÔNG bịa dữ liệu. Phải:
1. Thông báo mã không tồn tại
2. Gợi ý các mã tương tự (nếu có)
3. Hướng dẫn cách kiểm tra danh sách mã hợp lệ (nhóm 1.1 hoặc 1.2)
```

### 3.4. Yêu cầu bất khả thi
```
Từ chối lịch sự + giải thích + đưa ra giải pháp thay thế:
- "Dự đoán giá chính xác 100%" → Giải thích không thể, gợi ý phân tích kịch bản/xác suất
- "Mua 1,000,000 cổ phiếu VNM" → Cảnh báo rủi ro, kiểm tra sức mua
```

---

## 4. Sơ đồ ra quyết định (Decision Flowchart)

```
Nhận câu hỏi từ người dùng
        │
        ▼
┌───────────────────────┐
│ Câu hỏi có đủ thông   │──── Không ──→ HỎI LẠI thông tin thiếu
│ tin để xử lý không?    │
└───────────┬───────────┘
            │ Có
            ▼
┌───────────────────────┐
│ Câu hỏi thuộc 1 nhóm  │──── Có ──→ Đọc references/<file>.md → Viết code → Trả lời
│ hàm duy nhất?          │
└───────────┬───────────┘
            │ Không (multi-skill)
            ▼
┌───────────────────────┐
│ Phân tách thành các    │
│ bước đơn lẻ            │
│ Áp dụng thứ tự ưu tiên│
│ (Mục 2.2)              │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Có thao tác đặt lệnh? │──── Có ──→ XÁC NHẬN KÉP với người dùng
│                        │
└───────────┬───────────┘
            │ Không
            ▼
     Thực thi tuần tự
     Tổng hợp kết quả
     Trả lời người dùng
```

---

## 5. Bảng tham chiếu nhanh — Từ khóa → Nhóm

| Từ khóa (Tiếng Việt) | Từ khóa (English) | Nhóm |
|---|---|---|
| cài đặt, đăng nhập, import | install, login, setup | **0** |
| danh sách mã, rổ chỉ số, ngành | listing, index, sector | **1** |
| giá realtime, lịch sử, sổ lệnh, tick | realtime, historical, orderbook, tick | **2** |
| BCTC, P/E, ROE, định giá | financial, valuation, ratios | **3** |
| độ rộng, seasonality, thống kê TT | breadth, seasonality, market stats | **4** |
| rebalance, RRG, portfolio | rebalance, RRG, optimization | **5** |
| đặt lệnh, hủy lệnh, vị thế, tài khoản | order, cancel, position, account | **6** |
| SMA, RSI, Bollinger, OBV, SMC, fibonacci | MA, RSI, BB, volume, SMC, fibonacci | **7** |
| mô hình nến, chart pattern, vai đầu vai | candlestick, pattern, head shoulders | **8** |
| lọc cổ phiếu, bộ lọc, screening | screen, filter, screener | **9** |

---

## 6. Lưu ý từ kết quả Testing

> [!WARNING]
> Kết quả trigger accuracy test cho thấy các nhóm sau có **tỷ lệ bị trigger sai cao nhất**.
> Hệ thống cần đặc biệt cẩn thận khi phân loại (xem thêm bộ test ở `evals/`):
>
> 1. **`trendline_analysis` / `fibonacci_retracement`** (Nhóm 7.8) — Dễ nhầm với 7.1 (Trend Indicators)
> 2. **`volatility_indicators`** (Nhóm 7.3) — Dễ nhầm với 7.2 (Momentum) hoặc 7.1 (Trend)
> 3. **`chart_patterns`** (Nhóm 8) — Dễ nhầm với bất kỳ nhóm TA nào trong Nhóm 7
> 4. **`portfolio_optimization` / `rebalance`** (Nhóm 5) — Dễ nhầm với Stock Screening (Nhóm 9)
> 5. **`cash_flow_statement` vs `income_statement` vs `balance_sheet`** — Tất cả thuộc Nhóm 3.1 nhưng cần phân biệt rõ loại báo cáo

> [!IMPORTANT]
> Kết quả evaluation-based test cho thấy các lỗ hổng chất lượng output:
>
> 1. **Thiếu giải thích context cho edge values** — P/E âm, ROE cực cao → Hệ thống PHẢI giải thích tại sao
> 2. **Không xử lý dữ liệu không đủ** — Mã mới niêm yết, thiếu lịch sử → PHẢI gợi ý thay thế
> 3. **Thiếu xác nhận an toàn cho lệnh giao dịch** — PHẢI luôn hỏi xác nhận trước khi đặt lệnh
> 4. **Không xử lý câu hỏi đa bước** — Cross-skill queries cần được phân tách rõ ràng
> 5. **Không nhận diện abbreviation tiếng Việt** — "CP", "BCTC", "KQKD", "CĐKT", "LCTT"

---

## 7. Bảng viết tắt tiếng Việt thường gặp

| Viết tắt | Nghĩa đầy đủ | Nhóm liên quan |
|---|---|---|
| CP | Cổ phiếu | Tất cả |
| BCTC | Báo cáo tài chính | 3 |
| CĐKT | Bảng cân đối kế toán | 3 |
| KQKD | Kết quả kinh doanh | 3 |
| LCTT | Lưu chuyển tiền tệ | 3 |
| NĐTNN | Nhà đầu tư nước ngoài | 1, 4 |
| CTCK | Công ty chứng khoán | 1 |
| HOSE | Sở giao dịch TP.HCM | 1 |
| HNX | Sở giao dịch Hà Nội | 1 |
| TA | Technical Analysis (Phân tích kỹ thuật) | 7 |
| FA | Fundamental Analysis (Phân tích cơ bản) | 3 |
| TT | Thị trường | 4 |
| DN | Doanh nghiệp | 1 |
| GD | Giao dịch | 2, 6 |
