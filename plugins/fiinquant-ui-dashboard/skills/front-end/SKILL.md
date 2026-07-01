---
name: ui-ux-finquant-dashboard
description: "UI/UX design intelligence specialized for financial dashboards, trading platforms, and data-driven interfaces powered by FiinQuant. Includes 50+ styles optimized for data density, 161 color palettes for financial contexts (bull/bear, risk levels), 57 font pairings for numeric readability, 25+ advanced chart types (candlestick, heatmap, order book, time-series), and 99 UX guidelines tailored for real-time analytics. Supports 10 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, HTML/CSS). Actions: design, build, optimize, refactor, and review high-performance financial UI. Focus on dashboards, trading terminals, portfolio tracking, and analytics platforms using FiinQuant data APIs."
---

# UI/UX FinQuant Dashboard - Design Intelligence

Comprehensive design guide specialized for financial dashboards, trading platforms, and data-intensive interfaces. Designed to support products leveraging FiinQuant market data, including real-time analytics, portfolio tracking, and investment decision tools.

Includes:
- 50+ UI styles adapted for **high-density financial data**
- 161 color palettes optimized for **market semantics (bull/bear, volatility, risk tiers)**
- 57 font pairings focused on **numeric clarity and tabular alignment**
- 25+ chart types (candlestick, OHLC, heatmap, depth chart, time-series, correlation matrix)
- 99 UX guidelines tailored for **real-time, high-frequency interaction environments**
- Cross-platform support across 10 modern UI stacks

## When to Apply

This Skill should be used when designing data-heavy financial interfaces, especially those involving **FiinQuant datasets** derived from `fiinquant` folder such as stock prices, financial ratios, market signals, or portfolio analytics.

### Must Use

This Skill must be invoked in the following situations:

- Designing **financial dashboards** (market overview, portfolio, risk monitoring)
- Building **trading interfaces** (order placement, order book, price ladder, charting tools)
- Creating **data visualization layers** (time-series, candlestick, heatmap, comparative charts)
- Structuring **information hierarchy for investment decisions**
- Designing UI for **real-time or near real-time data updates**
- Optimizing **data tables with large datasets** (sorting, filtering, pagination, virtualization)
- Applying **color systems aligned with financial meaning** (green/red neutrality, accessibility-safe palettes)
- Ensuring **high readability of numbers, ratios, and financial metrics**
- Designing **alert systems** (price alerts, risk thresholds, abnormal signals)
- Reviewing UI for **latency perception and responsiveness**

### Recommended

This Skill is recommended in the following situations:

- Dashboard feels **cluttered or overwhelming due to too much data**
- Users struggle to **interpret charts or financial indicators**
- Need to improve **decision-making speed for investors**
- Aligning UI across **web trading platform & mobile trading app**
- Designing **multi-panel layouts (terminal-style UI like Bloomberg/TradingView)**
- Enhancing **data storytelling using FiinQuant insights**
- Pre-launch optimization for **financial SaaS / analytics products**

### Skip

This Skill is not needed in the following situations:

- Pure backend processing of financial data
- API integration without UI layer
- Quantitative modeling without visualization
- Infrastructure or data pipeline work
- Non-visual analytics scripts

**Decision criteria**: If the task impacts how financial data is visualized, interpreted, or interacted with in a UI, especially using FiinQuant → use this Skill.

## Rule Categories by Priority (Financial UI Context)

| Priority | Category | Impact | Domain | Key Checks (Must Have) | Anti-Patterns (Avoid) |
|----------|----------|--------|--------|------------------------|------------------------|
| 1 | Data Readability | CRITICAL | `ux` | Tabular alignment, Monospace/Tabular nums, Clear decimal precision | Misaligned numbers, Inconsistent units |
| 2 | Real-time Feedback | CRITICAL | `ux` | Live updates, Delta indicators, Loading states | Data flickering, No update indicators |
| 3 | Accessibility | CRITICAL | `ux` | Colorblind-safe red/green, Contrast 4.5:1, Alt text | Pure red/green reliance |
| 4 | Chart Integrity | HIGH | `chart` | Correct scale, Time continuity, Zoom/pan | Distorted axes, Misleading visuals |
| 5 | Layout Density | HIGH | `ux` | Information grouping, Collapsible panels | Overcrowded dashboards |
| 6 | Interaction Speed | HIGH | `ux` | Keyboard shortcuts, Quick actions | Multi-step trading flows |
| 7 | Color Semantics | MEDIUM | `color` | Bull/bear consistency, Risk color tiers | Arbitrary colors |
| 8 | Typography | MEDIUM | `typography` | Numeric clarity, 16px+, consistent units | Small unreadable metrics |
| 9 | Alerts & Signals | HIGH | `ux` | Clear thresholds, priority levels | Noise, over-alerting |
| 10 | Performance | HIGH | `ux` | Virtualization, efficient rendering | Laggy charts, heavy DOM |

## Quick Reference

### 1. Data Readability & Numerical Integrity (CRITICAL)

- `tabular-numbers` — Use tabular/monospaced figures for prices, volumes, and % changes
- `decimal-consistency` — Keep consistent decimal precision per asset class
- `unit-clarity` — Always show units (VND, %, millions, billions, lots)
- `column-alignment` — Right-align all numeric columns
- `delta-visibility` — Show change using color + symbol (+/−, ▲▼) + value
- `no-rounding-loss` — Avoid rounding that affects investment decisions
- ❌ Anti-pattern: misaligned numbers, inconsistent decimals, missing units

### 2. Real-time Data & Market Feedback (CRITICAL)

- `live-update` — FiinQuant data must support clear streaming or polling updates
- `price-flash` — Highlight price changes (green/red flash for 300–800ms)
- `latency-indicator` — Indicate data status (Real-time / Delayed / Snapshot)
- `market-status` — Show trading state (ATO / ATC / Closed / Break)
- `loading-state` — Use skeletons for tables and charts
- `error-recovery` — Provide retry for data disconnections
- ❌ Anti-pattern: static data with no indication of update status

### 3. Accessibility (Financial Context) (CRITICAL)

- `colorblind-safe` — Never rely on red/green only → add icons or labels
- `contrast-finance` — Maintain ≥4.5:1 contrast for readability
- `keyboard-trading` — Support keyboard interactions for power users
- `aria-live-prices` — Announce price updates for screen readers
- ❌ Anti-pattern: color-only meaning for gain/loss

### 4. Chart Integrity & Financial Visualization (HIGH)

- `chart-type-correct`
    + Candlestick → price movement
    + Line → trend
    + Bar → volume
    + Heatmap → market overview
- `time-continuity` — Maintain consistent time axis
- `zoom-pan` — Smooth zoom & pan (TradingView-like)
- `indicator-layer` — Overlay indicators (MA, RSI, MACD) clearly
- `tooltip-precision` — Show full OHLC data
- `crosshair` — Enable precise crosshair tracking
- ❌ Anti-pattern: misleading scales or distorted axes

### 5. Layout Density & Information Hierarchy (HIGH)

- `terminal-layout` — Use multi-panel trading terminal layout
- `grouping` — Group by Market / Portfolio / Orders
- `collapsible-panels` — Allow panels to collapse/expand
- `focus-zone` — Prioritize chart or price table as primary focus
- `progressive-reveal` — Hide advanced features by default
- ❌ Anti-pattern: overcrowded dashboards

### 6. Interaction Speed & Trading Efficiency (HIGH)

- `one-click-actions` — Enable trading in ≤1–2 steps
- `keyboard-shortcuts` — Quick Buy/Sell/Cancel actions
- `order-confirmation` — Clear confirmation for critical trades
- `instant-feedback` — UI feedback within 100ms
- `undo-cancel` — Fast cancel/undo actions
- ❌ Anti-pattern: multi-step, slow trading flows

### 7. Color System for Financial Meaning (MEDIUM)

- `bull-bear-system`
    + Up: green
    + Down: red
    + Neutral: gray
- `intensity-scale` — Color intensity reflects magnitude of change
- `risk-color` — Use yellow/orange/red for risk levels
- `dark-mode-optimized` — Prefer dark mode for trading environments
- ❌ Anti-pattern: arbitrary brand colors overriding financial meaning

### 8. Typography for Financial Data (MEDIUM)

- `numeric-priority` — Numbers take visual priority over text
- `font-choice` — Use highly readable fonts (Inter, Roboto Mono, IBM Plex)
- `size-hierarchy`
    + Price → largest
    + Change % → medium
    + Metadata → small
- `line-height-tight` — Compact spacing for dense tables
- ❌ Anti-pattern: decorative fonts or poor numeric readability

### 9. Alerts, Signals & Risk UX (HIGH)

- `alert-priority` — Define levels (info / warning / critical)
- `price-alert` — Alerts based on price or % thresholds
- `risk-warning` — Highlight margin or drawdown risks
- `notification-center` — Centralized alert management
- `no-alert-spam` — Avoid excessive alerts
- ❌ Anti-pattern: alert fatigue

### 10. Performance for Data-heavy UI (HIGH)

- `virtualized-table` — Virtualize tables with 100+ rows
- `efficient-render` — Avoid full re-render on updates
- `websocket-stream` — Prefer streaming over polling
- `chart-optimization` — Avoid rendering excessive data points directly
- `debounce-updates` — Control UI update frequency
- ❌ Anti-pattern: laggy scrolling or chart rendering

### 11. Data Table (Stock Screener / Market Watch)

- `sticky-header` — Keep headers fixed
- `column-resize` — Allow column resizing
- `sort-filter` — Advanced sorting & filtering
- `row-highlight` — Highlight watchlist stocks
- `infinite-scroll` — Load more data progressively
- ❌ Anti-pattern: long static tables without navigation

### 12. Trading-specific Components

- `order-book` — Clear bid/ask depth visualization
- `price-ladder` — Structured price steps
- `order-ticket` — Minimal, fast order form
- `portfolio-card` — Clear P&L visualization
- `watchlist` — Personalized tracking
- `heatmap-market` — Market overview visualization