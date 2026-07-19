---
name: fiinquant
description: Giới thiệu và hướng dẫn cài đặt thư viện FiinQuantX — thư viện dữ liệu tài chính Python cho thị trường chứng khoán Việt Nam.
---

# FiinQuant Skill

FiinQuantX là thư viện dữ liệu và công cụ phân tích dành cho Python, giúp các nhà đầu tư, nhà phân tích và lập trình viên dễ dàng truy cập, xử lý và phân tích dữ liệu tài chính một cách nhanh chóng và chính xác.

> Nội dung phần dưới đây căn cứ [tài liệu FiinQuant](https://fiinquant.vn/Home/Document) (iframe [docs.fiinquant.vn](https://docs.fiinquant.vn/)).

## Điểm nổi bật

### Dữ liệu giao dịch nguồn chính thống

FiinQuant tích hợp trực tiếp dữ liệu thị trường từ các sở giao dịch (HOSE, HNX, UPCOM) theo thời gian thực, đảm bảo tính chính xác, minh bạch và đáng tin cậy cho các ứng dụng phân tích, giao dịch và nghiên cứu.

### Kết nối WebSocket realtime

FiinQuant hỗ trợ kết nối WebSocket ổn định và hiệu suất cao, cho phép:

* Nhận dữ liệu tick-by-tick hoặc cập nhật theo batch (VD: 1s, 5s, 1min)
* Push dữ liệu tự động vào dashboard, bot, hệ thống cảnh báo
* Đồng bộ liên tục với dữ liệu lịch sử để phục vụ các hệ thống phức tạp

WebSocket tích hợp cho module giá lẫn module sổ lệnh.

### Dữ liệu tổng hợp sẵn theo từng phút

Hệ thống hỗ trợ dữ liệu tick by tick cho đến từng phút với đầy đủ timeframe 1' 5' 15' 1h 4h 1D cho phép người dùng gọi trực tiếp, không cần duy trì hệ thống server để lưu các dữ liệu lịch sử

### Sẵn sàng kết hợp dữ liệu lịch sử và realtime

FiinQuant cung cấp sẵn các hàm merge và đồng bộ dữ liệu lịch sử và realtime, giúp việc phát triển chiến lược, kiểm thử mô hình (backtest) và triển khai giao dịch dễ dàng và mượt mà.

### **Dữ liệu dòng tiền thông minh – realtime & lịch sử**

Bao gồm các chỉ báo chủ động như:

* BU-SD: Giá trị mua bán ròng của nhà đầu tư tổ chức/chủ động.
* NĐTNN: Hoạt động của nhà đầu tư nước ngoài realtime và theo chuỗi thời gian.

=> Hữu ích cho việc xác định dòng tiền lớn và xu hướng thị trường ngắn hạn – trung hạn.

### Tích hợp bộ chỉ báo phân tích kỹ thuật (TA) phổ biến

Thư viện tích hợp sẵn các bộ chỉ báo như:

* MA, EMA, RSI, MACD, Bollinger Bands
* Breakout Signals, Divergence
* Volume Profile và các nhóm chỉ báo hành vi thị trường

### Hàm tài chính nâng cao dành cho nhà đầu tư chuyên nghiệp

FiinQuant cung cấp nhiều hàm tiện ích sẵn sàng triển khai:

* Stock prediction: Dự báo xu hướng giá cổ phiếu bằng ML
* Similar chart: Tìm kiếm cổ phiếu có mô hình tương đồng
* Rebalance index: Tái cơ cấu danh mục chỉ số theo định kỳ hoặc tín hiệu
* Factor models: Phân tích yếu tố ảnh hưởng đến hiệu suất cổ phiếu
* Cập nhật định kỳ liên tục các mô hình tài chính khác

> **Sử dụng thư viện FiinQuant không đơn thuần là công cụ truy xuất dữ liệu, còn là sử dụng hệ sinh thái các công cụ định lượng được xây dựng sẵn dành cho các nhà đầu tư.**

## 1. Cài đặt và Cấu hình (Setup & Initialization)
**Lệnh cài đặt thư viện:**
```bash
pip install --extra-index-url https://fiinquant.github.io/fiinquantx/simple fiinquantx
```

**Lệnh cập nhật thư viện khi có phiên bản mới:**
```bash
pip install --upgrade --extra-index-url https://fiinquant.github.io/fiinquantx/simple fiinquantx
```

**Quan trọng: kiểm tra version signalrcore:**
```bash
pip show signalrcore
```
Nếu signalrcore version >= 1.0.0 thực hiện gỡ bỏ và cài lại các bản 0.9.x để đảm bảo có thể chạy được các hàm lấy dữ liệu realtime

> **Lưu ý quan trọng:** KHÔNG ĐẶT TÊN CÁC FILE SCRIPT PYTHON TRÙNG VỚI TÊN THƯ VIỆN (ví dụ: không đặt tên file là `FiinQuant.py` hay `FiinQuantX.py`).

## 2. Đăng nhập

```python
from FiinQuantX import FiinSession

client = FiinSession(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
).login()
```
**Các trường dữ liệu:**
| Field | Mô tả |
|-------|-------|
| username | Tên đăng nhập của người dùng |
| password | Mật khẩu của người dùng |

**Mã lỗi thường gặp khi đăng nhập tài khoản:**

| Tên phương thức | Mã lỗi | Mô tả |
|-----------------|--------|-------|
| User does not exist (Tài khoản không tồn tại) | 400 | Người dùng nhập sai username. |
| Incorrect password (Mật khẩu không đúng) | 400 | Người dùng nhập sai password. |

Khi đăng nhập không thành công, các lệnh gọi dữ liệu sau đó có thể báo lỗi phía thư viện, ví dụ: `NameError: Please login before calling data`.

### Quản lý thông tin đăng nhập và phiên làm việc

- Không ghi tên đăng nhập hoặc mật khẩu trực tiếp vào mã nguồn được chia sẻ. Nên đọc thông tin xác thực từ biến môi trường hoặc hệ thống quản lý bí mật.
- Đăng nhập một lần và tái sử dụng `client` trong vòng đời tiến trình hoặc worker. Không đăng nhập lại khi đổi mã, đổi khung thời gian hoặc thực hiện từng yêu cầu dữ liệu lịch sử.
- Với ứng dụng web hoặc mobile, chỉ backend hoặc sidecar được đăng nhập FiinQuantX. Không gửi thông tin xác thực xuống trình duyệt hay nhúng thông tin này trong JavaScript.
- Với hệ thống nhiều worker hoặc nhiều replica, cần quản lý tổng số luồng realtime của toàn hệ thống theo hạn mức tài khoản.

Xem thêm [Quản lý kết nối và tối ưu hiệu năng](2.6-connection-lifecycle-performance.md) để phân biệt historical request, realtime stream và cách tổ chức kết nối cho ứng dụng chạy dài hạn.

---
