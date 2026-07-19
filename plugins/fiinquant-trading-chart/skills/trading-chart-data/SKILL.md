---
name: tradingchart-data-sync
description: "Implementation guide to build high-performance TradingView-like candlestick charts. Covers: symbol search using client.TickerList, fetching historical data up to latest, integrating real-time tick-by-tick updates for live candle flickering, live candle synthesis/aggregation on the fly without reloading, and backend/frontend caching mechanisms (local storage) for instantaneous symbol switching."
---

# Trading Chart Data & Real-time Sync - Implementation Skill

This skill provides step-by-step instructions and architectural patterns to implement a real-time, high-performance financial chart similar to TradingView.

## 1. Symbol Search & Autocomplete
**Objective**: Build a responsive search interface with suggestions for all market ticker symbols.
- **Source**: Use the `1.1. Danh sách mã theo index` function/API, please review the skill `fiinquant/SKILL.md` to use this function to get the complete list of available market symbols.
- **Implementation**:
  - **Backend**: On startup or periodically, cache the result of `client.TickerList()` in memory. Expose a fuzzy-search or prefix-match endpoint `/api/search?q={query}`.
  - **Frontend**: Create a command-palette or input dropdown that queries this list. Given the small payload size, the frontend should fetch the entire list once on app instantiation, store it in browser state, and perform client-side filtering to achieve zero-latency auto-suggestions.

## 2. Initial Data Load & Timeframes
**Objective**: Draw historical candles up to the current exact moment when a user opens the chart or reloads.
- **Source**: Use the `2.2. Hàm dữ liệu Lịch sử` function/API, please review the skill `fiinquant/SKILL.md` to use this function to fetch the latest historical OHLCV data of each available market symbols.
- **Lưu ý Cực Kỳ Quan Trọng về Lỗi "Nến không đuổi kịp ngày hiện tại"**: Bạn BẮT BUỘC phải truyền tham số `lasted=True`. Tham số này bị đánh vần là `lasted` (chữ d) trong thư viện FiinQuant thay vì `latest`. Mặc định của SDK là `lasted=False`, và nếu bạn để mặc định, biểu đồ sẽ bị cắt bỏ toàn bộ phiên giao dịch hiện tại chưa đóng, khiến nến mới nhất bị trễ hơn ngày thực tế (VD: hiển thị 07/04 trong khi hôm nay 09/04).
- **Functionality**:
  - Support multiple timeframes (1m, 5m, 15m, 30m, 1h, 4h, 1d).
  - Fetch historical OHLCV (Open, High, Low, Close, Volume) data up to the `latest` available timestamp.
- **Implementation**:
  - When the user selects a symbol and timeframe, call the backend API to fetch historical bars.
  - For the first render, request only the latest page required by the viewport, typically 300-500 bars. Load older pages when the user scrolls back or selects a wider date range.
  - Deduplicate identical in-flight requests and discard stale responses after the user switches symbol or timeframe.
  - Draw these bars on the charting library (e.g., Lightweight Charts, D3, or TradingView Lightweight).
  - **Market Hours Check**: If the market is **CLOSED**, this initial data load represents the final state of the chart. Stop here and do not subscribe to real-time data.
  - If the market is **OPEN**, the final bar in this initial historical fetch represents the *current, incomplete* period. It serves as the baseline for real-time updates.
  - **Market Hours**: 
    + HOSE: 9:00 - 11:30 & 13:00 - 14:45 (match order), 14:45 - 15:00 (deal order).
    + HNX & UPCoM: 9:00 - 11:30 & 13:00 - 15:00.

## 3. Real-Time Tick Integration (Live Candle Flickering)
**Objective**: Make the current, active candle jump/update continuously representing real-time market activity.
- **Source**: Subscribe to real-time tick-by-tick data streams via `2.1. Hàm dữ liệu Realtime` function/API, please review the skill `fiinquant/SKILL.md` to use this function. **Condition:** Only connect and subscribe if the market is currently **OPEN**.
- **Lưu ý Quan trọng về Python Websocket Callback:** Hàm đẩy data vào Asyncio Websocket Queue phải chú ý lấy đúng event_loop (`asyncio.run_coroutine_threadsafe(..., loop)`) vì Callback `on_tick` chạy trên background thread. Ngoài ra, TUYỆT ĐỐI phải lấy Dict thông qua `data.to_dataFrame().iloc[0].to_dict()` thay vì `getattr()`.
- **Shared Stream Architecture**:
  - The backend or sidecar owns the authenticated `FiinSession` and realtime stream. Browser code must not contain FiinQuant credentials.
  - Maintain one upstream realtime stream for the union of symbols used by charts, watchlists, alerts, and other active features.
  - Multiplex ticks from that stream to frontend clients through the application's WebSocket layer.
  - Do not create or reconnect an upstream stream when the selected symbol is already in the active subscription set.
  - Debounce subscription changes. If the SDK cannot update tickers on a running stream, stop the old stream completely before starting the replacement.
- **Implementation**:
  - Each incoming tick contains at least `Close`, `MatchVolume`, and `TradingDate`.
  - Locate the **current active candle** (the last one drawn from historical data).
  - On each new tick, apply the following logic:
    - `Close = tick.Close`
    - `High = Math.max(current.High, tick.Close)`
    - `Low = Math.min(current.Low, tick.Close)`
    - `Volume = current.Volume + tick.MatchVolume`
  - Update the chart's current candle via the library's `update()` method so it naturally "flickers" just like a real TradingView terminal.

## 4. Live Candle Synthesis & Aggregation
**Objective**: As time progresses without the user reloading the app, seamlessly construct *new* historical bars out of the live realtime tick data.
- **Lỗi Bị Nuốt Nến (Swallowed Candle Bug)**: Rất nhiều triển khai chỉ cập nhật `currentBar` cho nến cuối cùng lấy từ hàm Lịch Sử (`Fetch_Trading_Data`), dẫn tới việc các Ticks của ngày mới tiếp tục ghi đè lên cây nến của ngày hôm qua (VD: nến 08/04 bị bóp méo bởi dòng giá của ngày 09/04). 
- **Bắt buộc Payload WS phải có Time**: Payload của websockets CẦN phải có thuộc tính `time` (ví dụ: `time.time()` trong trươờng hợp object `data` của FiinQuant Stream không chứa sẵn timestamp).
- **Implementation**:
  - Keep track of the current timeframe's boundary (e.g., for a 1D timeframe, boundary is 00:00 của ngày tiếp theo).
  - When a tick's timestamp crosses the boundary into a new period (`Math.floor(new Date(tick.time * 1000).setHours(0,0,0,0) / 1000) > currentBar.time`):
    - **Finalize** the current candle (nó sẽ đóng băng làm historical bar vĩnh viễn).
    - **Open** a new candle (TargetBar) where:
      - `Open = tick.price`
      - `High = tick.price`
      - `Low = tick.price`
      - `Close = tick.price`
      - `Volume = tick.volume`
      - `time = tickPeriodTime` (chuẩn bị bằng setHours(0,0,0,0) / 1000)
  - Đẩy cây nến mới này (TargetBar) vào hàm `candlestickSeries.update()`. Thư viện `lightweight-charts` sẽ tự động tách nó thành một cột nến hoàn toàn mới trên màn hình.

## 5. Backend Caching & Local Storage for Instant Switching
**Objective**: Guarantee that when a user switches between symbols, historical data loads instantly without noticeable network delay or redundant API calls.
- **Backend Architecture**:
  - The backend server MUST pre-fetch and maintain up-to-date historical data for *all active symbols* in a local cache (e.g., in-memory hash maps, Redis, or local disk array/database).
  - When a frontend requests historical data for a symbol, the backend serves it directly from this local storage overlay, avoiding redundant external API calls to data providers.
- **Frontend Optimization (Local Storage/IndexedDB)**:
  - Cache loaded historical datasets in the browser's IndexedDB.
  - **Switching Flow**:
    1. User picks a new symbol via autocomplete.
    2. Frontend immediately checks IndexedDB and renders cached historical data (yielding a 0ms display).
    3. Frontend asynchronously hits the backend caching layer to fetch any missed delta updates since the last cache timestamp.
    4. Backend serves this delta instantly.
    5. Frontend patches the chart and registers the symbol with the shared subscription registry. It reuses the existing application WebSocket instead of opening a connection per symbol.

## Key Rules for triển khai
- **Rule 1**: Understand that `historicalBars` (array) and `currentLiveBar` (object/pointer) are two distinct entities. Design your state management to handle them clearly.
- **Rule 2**: **NEVER** use polling to refresh the chart. Historical polling is highly inefficient. Real-time chart flickering must exclusively use tick updates.
- **Rule 3**: Correctly implement the time-boundary synthesis algorithm. If the user stays on the chart for an hour, it must smoothly print 60 new 1-minute candles using purely incoming ticks.
- **Rule 4**: Aggressive Caching. Implement both backend local storage caching for all symbols and frontend IndexedDB caching to enable instantaneous, lag-free chart jumping between symbols.
- **Rule 5**: Market Hours Awareness. Do not initiate WebSocket connections, polling, or real-time tick processing outside of active trading hours. Simply load the `latest` historical snapshot representing the closure of the previous session and keep the chart static.
- **Rule 6**: Shared Connection Ownership. Charts, watchlists, and alerts must not create independent upstream realtime streams. Use a shared session, subscription registry, and stream managed by the backend or sidecar.
- **Rule 7**: Follow `fiinquant/references/2.6-connection-lifecycle-performance.md` for session reuse, historical request limits, realtime cleanup, reconnect, and operational monitoring.
