---
name: fiinquant-ui-errors
description: Hướng dẫn xử lý các lỗi crash giao diện kinh điển (màn hình tối thui/trắng bóc) khi tích hợp FiinQuant API với React và lightweight-charts. Đọc skill này để tránh lỗi unmount component tree.
---

# Lỗi Frontend kinh điển khi tích hợp FiinQuant & Lightweight Charts

Khi xây dựng các dashboard hoặc trading terminal sử dụng **React** kết hợp thư viện biểu đồ như **lightweight-charts** cùng dữ liệu từ **FiinQuant SDK**, các bộ xử lý và lập trình viên thường mắc các lỗi chí mạng dẫn đến crash toàn bộ ứng dụng (Blank Screen of Death - màn hình trắng/tối) ngay sau khi login thành công. 

Dưới đây là cẩm nang phân tích lỗi và giải pháp bắt buộc.

## 1. Màn hình tối thui (Blank Screen) do thiếu ErrorBoundary
**Nguyên nhân gốc rễ (Root Cause):**
Trong React phiên bản 16 trở lên, bất kỳ lỗi nào (Unhandled Exception) xảy ra bên trong *rendering phase* hoặc *lifecycle hooks* (`useEffect`) mà không được bắt cấu trúc sẽ khiến React **tự động unmount toàn bộ giao diện (component tree)**. Đối với app tài chính khối lượng lớn, sự cố API hoặc lỗi thư viện biểu đồ là cực kỳ phổ biến. Thiếu Error Boundary, app sẽ biến thành một màn hình đen/trắng trống trơn.

**Giải pháp (Quy tắc triển khai):**
- **Bắt buộc:** Phải luôn bọc component biểu đồ (`<TradingChart />`) bằng một thẻ `<ErrorBoundary>`.
- Ngăn chặn lỗi lan truyền: Nếu biểu đồ crash, app phải giữ nguyên UI xung quanh (header, login, form đặt lệnh) và chỉ hiển thị thông báo lỗi cục bộ ngay tại vùng chứa biểu đồ đó.

## 2. Fatal Date Parsing Error & Breaking Changes (Lightweight-Charts v5)
**Nguyên nhân gây crash chủ yếu:**
- **Định dạng dữ liệu FiinQuant:** Thuộc tính `timestamp` của `Fetch_Trading_Data` được trả ra dưới dạng string `%Y-%m-%d %H:%M` (VD: `"2024-11-28 00:00"`). 
- **Lỗi Parse:** Constructor `new Date("2024-11-28 00:00")` không phải format đạt chuẩn ISO 8601 (thiếu chữ `T`). Hàm này tuy chạy được trên môi trường V8 (Chrome) nhưng có thể ngầm trả về `NaN` hoặc ném lỗi trên các browser nhân Safari/web-kit.
- **Lightweight-Charts khắt khe:** Trong v5, các hàm `.setData()` hoặc `.update()` sẽ lập tức văng `Fatal RuntimeError` nếu:
  1. `time` bằng `NaN`.
  2. Mảng Data bị trùng UNIX timestamp.
  3. Dữ liệu không được sắp xếp chronological (thời gian tăng dần một cách tuyệt đối).

**Giải pháp (Quy tắc triển khai):**
- **Sử dụng API mới của v5:** Lưu ý KHÔNG CÒN HÀM `chart.addCandlestickSeries()`! Bạn phải import trực tiếp component series từ thư viện: `import { createChart, CandlestickSeries } from 'lightweight-charts'` sau đó khởi tạo bằng `chart.addSeries(CandlestickSeries, {...options})`.
- **Chuẩn hóa chuỗi thời gian:** Thay khoảng trắng bằng kí tự `T` (VD: `d.time.replace(' ', 'T')`) và chỉ định timezone Việt Nam `+07:00` trước khi cho vào `Date.parse()`.
- **Validation Strict:** Phải lọc mảng dữ liệu trước khi nạp vào chart: `.filter(d => !isNaN(d.time))` để tránh ném rác vào hàm `setData`. Dữ liệu trùng timestamp sẽ gây crash.

## 3. Race Conditions: Xử lý State khi WebSockets chưa sẵn sàng
**Nguyên nhân:**
- Callback `.on_tick` (Realtime Stream) nhận dữ liệu WebSocket và cập nhật `candlestickSeries.update()`. Lỗi sẽ làm sập React nếu `candlestickSeries` chưa được khởi tạo đầy đủ hoặc `currentCandle` bị `undefined`.

**Giải pháp (Quy tắc triển khai):**
- Sử dụng *Optional Chaining* (`?.`) đối với các object thư viện.
- Khởi tạo *safe check*: Chỉ apply `update()` vào biểu đồ khi object biểu đồ tồn tại và tick price khác `null`.

## 4. Màn hình rỗng (Empty Chart) nhưng Không văng báo lỗi ErrorBoundary
**Nguyên nhân:**
- Backend bắt được Exception (như truyền sai Argument `timeframe="1D"` thay vì phải lowercase `"1d"` vào API của FiinQuant) và trả về `HTTP 500`.
- Frontend bắt qua hook `useEffect` bằng `.catch()` rồi print nội bộ thay vì throw ra ngoài để kích hoạt `ErrorBoundary`, khiến mảng dữ liệu cung cấp cho chart bị rành/rỗng tuyệt đối. Đồng thời làm tắt nghẽn luôn luồng lắng nghe WebSocket vì không có last Candle.

**Giải pháp (Quy tắc triển khai):**
- **Sửa API Tham Số Hợp Lệ:** Đối với các `timeframe`, luôn dùng `.lower()` trước khi nạp tham số `by="1d"` vào hệ thống phân tích. (Trừ các mã cổ phiếu ở API `tickers=[]` thì phải `.upper()`)
- Phải cập nhật State thông báo lỗi cục bộ (`[loadError, setLoadError]`) trên React thay vì nuốt log âm thầm (swallow error).

## 5. Hiện Lỗi Ngày Tháng: Nến của ngày 09/04 bị dời về 08/04 17:00
**Nguyên nhân:**
- Cấu hình gốc của `lightweight-charts` diễn dịch toàn bộ UNIX timestamp dưới con mắt của một máy chủ London (chuẩn GMT/UTC +0).
- Khi FiinQuant trả về `"2026-04-09 00:00"` (tức 0h ngày 9 tháng 4 ở múi giờ VN GMT+7). Lệnh `new Date()` chuyển đổi nó sang mã Unix đúng chuẩn. Tuy nhiên lúc quăng vào chart, thư viện lấy mã Unix đó trừ ngược lại 7 múi giờ để ép về múi giờ UTC, tạo ra `17:00 ngày 2026-04-08` (Ngày biểu kiến bị lùi về hôm qua). 

**Giải pháp (Quy tắc triển khai bắt buộc):**
- Trong vòng lặp fetch dữ liệu, phải áp dụng **Timezone Offset Hack** để fake (làm giả) mã UNIX cho biểu đồ: `chartTime = unixTime + (7 * 3600)`. Khi chart Render, nó sẽ hiển thị chính xác khớp với thời gian Local (Việt Nam).
- Logic này cũng phải cập nhật đồng bộ ở hàm Websocket Realtime `on_tick()`.

## 6. Lỗi WebSocket "Tịt Ngòi" (Tưởng Không Lỗi Mà Lỗi Không Tưởng)
**Nguyên nhân 1: Xung đột Đa luồng (Multi-threading) và Asyncio**
- Hàm `Trading_Data_Stream.start()` của FiinQuant tạo ra một **Background Thread** độc lập. Do đó hàm Callback `on_tick()` của bạn bị gọi trong Thread phụ này thay vì Main Thread.
- Khi bạn dùng hàm `asyncio.get_running_loop()` bên trong `on_tick` để push data, Python sẽ ném thẳng `RuntimeError: no running event loop` và crash ngầm luồng WebSocket mà không hiện ErrorBoundary trên React (swallow error).

**Nguyên nhân 2: Truy xuất thuộc tính RealTimeData bị rỗng**
- Đối tượng `RealTimeData` trả về trong Callback tuy chứa Data, nhưng nó ẩn đi (encapsulate) các Getter. Dùng `getattr(data, 'Close')` sẽ trả về lỗi hoặc giá trị rỗng/mặc định (`0`), qua đó WebSocket liên tục bắn giá `$0` ra màn hình, khóa chết nến.

**Giải pháp (Quy tắc triển khai bắt buộc):**
- **Trị lỗi Threading:** Bạn BẮT BUỘC phải lấy sẵn Asyncio Loop ở Main context (`loop = asyncio.get_running_loop()`) ngay bên ngoài Callback. Gửi data vào Queue phải dùng `asyncio.run_coroutine_threadsafe(queue.put(...), loop)` truyền tham số Loop gốc này vào.
- **Trị lỗi Object:** TUYỆT ĐỐI KHÔNG xài `getattr()`. Bạn phải gọi ép về Dataframe: `df = data.to_dataFrame()`, sau đó lấy dòng đầu tiên `row = df.iloc[0].to_dict()`. Khi đó `row['Close']` hoặc `row['MatchVolume']` mới xài được an toàn.

## 7. Lỗi Đẻ Nến Liên Tục (Tách Nến Realtime ở Timeframe 1D)
**Nguyên nhân:**
- Khi frontend load lịch sử nến với Timeframe 1 ngày (`1d`), các cây nến lịch sử có Timestamp chốt tại mốc `00:00:00`.
- Tuy nhiên luồng dữ liệu WebSocket (`Trading_Data_Stream`) lại đẩy Tick về với thời gian thực tính bằng giây (ví dụ: `11:21:49`). Khi gọi `series.update({time: tickUnix})`, vì Timestamp này lớn hơn và không khớp định kỳ, `lightweight-charts` lập tức **đẻ ra vô số cây nến mới** (mỏng như sợi chỉ nối đuôi nhau) thay vì ghi đè lên nến hiện hành.

**Giải pháp (Quy tắc triển khai bắt buộc):**
- BẮT BUỘC thực hiện Time-Boundary matching (đồng bộ mốc thời gian bắt đầu nến).
- Trên React, trước khi `update()` giá trị của Tick, phải ép ngày của Tick đó lùi về mốc `00:00:00` (nếu dùng Timeframe 1D) bằng hàm `setHours(0, 0, 0, 0)`:
```javascript
const tickDate = new Date(tick.timestamp);
tickDate.setHours(0, 0, 0, 0); // Ép về 0h sáng cùng ngày
const tickUnix = Math.floor(tickDate.getTime() / 1000) + (7 * 3600);
series.update({ time: tickUnix, ... });
```
- Việc này giúp Tick sở hữu chung ID Timestamp với cây nến Lịch sử cuối cùng, khiến thư viện *ghi đè* vào đúng cây nến đó để tạo hiệu ứng nhấp nháy giá.

## Tổng kết Checklist Code Dành Cho hệ thống triển khai:
1. [ ] Có fallback ErrorBoundary khi mount Chart chưa?
2. [ ] Đã sử dụng đúng Cú pháp v5 cho Chart chưa? (`chart.addSeries(CandlestickSeries)` thay vì `chart.addCandlestickSeries()`)
3. [ ] Các biến String như Timeframe (1d 1m) dùng cho backend API có gọi bằng chữ cái viết thường (lowercase) không?
4. [ ] Đã replace space bằng `T` cho `timestamp` và vá bù Local UTC+7 (`+ (7*3600)`) chưa?
5. [ ] Khởi tạo WS stream có tuân thủ lấy `loop` từ Main Thread và ép Dictionary qua `to_dataFrame` không?
6. [ ] Cập nhật tick Realtime cho nến 1D đã có hàm ép giờ về 0h (`setHours(0,0,0,0)`) để ghim nến chưa?
