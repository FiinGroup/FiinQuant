---
name: dnse-order-placement
description: Hướng dẫn xây dựng giao diện và workflow đặt lệnh chứng khoán qua DNSE bằng FiinQuant API. Đọc file này khi hệ thống cần xây dựng/thiết kế UI, luồng xử lý hoặc tích hợp tính năng đăng nhập OTP, bảo mật token, và tính năng đặt lệnh.
---

# Hướng dẫn Xây dựng luồng Đặt Lệnh thông qua DNSE bằng FiinQuant API

Skill này cung cấp workflow chuẩn và các yêu cầu về mặt giao diện, backend khi triển khai tính năng đặt lệnh chứng khoán qua broker DNSE.

## 1. Đăng nhập FiinQuant & Broker DNSE

Để thực hiện giao dịch, hệ thống yêu cầu đăng nhập hai lớp: FiinQuant session và DNSE Broker session. Khi khởi tạo phiên bản đăng nhập, hệ thống sẽ yêu cầu mã OTP được gửi nội bộ. Chi tiết các hàm xem tại phần `Nhóm 6 — Đặt lệnh giao dịch` ở file skill `fiinquant/SKILL.md`

### Đoạn mã xử lý chuẩn:

```python
# 1. Đăng nhập FiinSession
fq_username = "REPLACE_WITH_YOUR_FIINQUANT_USERNAME"
fq_password = "REPLACE_WITH_YOUR_FIINQUANT_PASSWORD"
client = FiinSession(username=fq_username, password=fq_password).login()

# 2. Đăng nhập DNSE Broker với Smart OTP
dnse_username = "REPLACE_WITH_YOUR_DNSE_USERNAME"
dnse_password = "REPLACE_WITH_YOUR_DNSE_PASSWORD"
client_order = client.FiinQuantConnector(broker='DNSE', username=dnse_username, password=dnse_password, smart_otp=True).login()
```

### ⚠️ Lưu ý Quan Trọng dành cho Backend & UI:
- **Tương tác OTP qua Terminal**: Khi chạy thông số `smart_otp=True`, tại terminal sẽ xuất hiện prompt `Input OTP:`. Quy trình này chặn luồng xử lý cho đến khi nhập xong. 
  - **Yêu cầu UI**: Cần cung cấp một giao diện (Modal/Form) để người dùng nhập OTP.
  - **Yêu cầu Backend**: Backend phải có cơ chế nhận mã OTP từ giao diện truyền xuống và pipe (gửi) trực tiếp vào luồng `stdin` (terminal) của tiến trình khởi chạy đoạn code trên để hoàn thành đăng nhập.
- **Bảo mật `trading_token......json`**:
  - Sau khi xác thực OTP thành công, thư mục chạy project (trên server) sẽ xuất hiện file có định dạng `trading_token......json`.
  - File này được SDK đọc ngầm trong khoảng 8 tiếng tiếp theo giúp hệ thống tự động thực thi các lệnh mua/bán mà không cần lấy lại OTP.
  - Sau 8 tiếng, file này mất hiệu lực.
  - **Khuyến cáo**: Server host ứng dụng web (Backend) tuyệt đối phải **giữ bí mật file này**, thêm vào `.gitignore` (nếu có push lên git), không được expose quyền truy cập download/xem từ phía Frontend hoặc bất kì public API nào.

---

## 2. Hiển thị Thông tin Tài khoản và Tiểu khoản

Tiếp theo, ứng dụng cần lấy ra được các thông tin tài khoản để người dùng biết mình đang dùng tài khoản nào.

### A. Hiển thị thông tin chủ tài khoản (Account Info)

```python
account_info = client_order.get_account_info()
print(account_info.summary())
```
**Mẫu dữ liệu trả về**:
```json
{
    "id": "0001006289",
    "investor_id": "0001006289",
    "name": "DANG THANH THUY",
    "error": null,
    "status_code": 200
}
```
**Hướng dẫn UI**: Hiển thị tên hiển thị người dùng (trong trường `name`) ở góc giao diện (ví dụ: góc trên cùng bên phải) để thể hiện session hiện tại là của ai.

### B. Hiển thị các Tiểu khoản (Sub Accounts)

Một User có thể có cả tài khoản thường và tài khoản phái sinh.

```python
sub_accounts = client_order.get_sub_accounts()
for account in sub_accounts.accounts:
    print(account.summary())
```
**Mẫu dữ liệu trả về**:
```json
// Tài khoản Cơ Sở (Thường)
{
    "id": "0001177757",
    "investor_id": "0001006289",
    "custody_code": "064C500006",
    "derivative_account": false,
    "derivative_status": null,
    "status_code": 200
}

// Tài khoản Phái Sinh
{
    "id": "0001009212",
    "investor_id": "0001006289",
    "custody_code": "064C500006",
    "derivative_account": true,
    "derivative_status": "ACTIVE",
    "status_code": 200
}
```
**Hướng dẫn UI**:
- Phải tạo một danh sách chọn tiểu khoản cho người dùng. 
- Dựa vào trường `derivative_account` (True/False) mà phân biệt nhãn "Tài khoản thường" hay "Tài khoản phái sinh". 
- Khi người dùng click chọn 1 tài khoản, phải **lưu trữ lại giá trị `id` của tài khoản đó (Ví dụ: '0001009212') vào bộ nhớ (state/store)** để truyền xuống các bước kế tiếp.

---

## 3. Hiển thị Chọn Gói Vay (Loan Packages) Dựa Theo Tiểu Khoản

Dựa vào việc người dùng chọn **Tài khoản thường** hay **Tài khoản phái sinh** ở Bước 2, phía frontend sẽ gọi API lấy thông tin gói vay tương ứng và hiển thị cấu trúc Button cho họ chọn.

### A. Đối với Tài Khoản Thường (Cơ sở)

```python
loan_packages = client_order.get_loan_packages(account_id='0001009212') # account_id lấy từ bước 2
for i in loan_packages:
    print(i.summary())
```
**Mẫu dữ liệu**:
```json
{
    "id": 7905,
    "type": "M", // M: Margin, N: Normal
    "initial_rate": 0.5,
    "maintenance_rate": 0.4,
    "interest_rate": 0.12,
    "preferential_interest_rate": 0.12,
    "allow_extend": true,
    "allow_early_payment": true,
    "buy_fee": 0.0007,
    "sell_fee": 0.0007,
    "tickers": ["ACB", "BCC", "BID", ...],
    "error": null,
    "status_code": 200,
    "num_tickers": 19
}
```
**Hướng dẫn UI**:
- Generate các **Buttons** đóng vai trò chọn Gói Vay cho người dùng.
- Trên Button hiển thị động các thông số sau (nếu key có giá trị hợp lệ mới show):
  - `type`: Loại gói vay (M = Margin / Ký Quỹ, N = Normal / Thông Thường).
  - `initial_rate`: Tỷ lệ vay ban đầu.
  - `maintenance_rate`: Tỷ lệ duy trì (nếu tỷ lệ thực tiễn thấp hơn mức này, tài khoản sẽ bị call margin).
  - `interest_rate`: Lãi suất vay ký quỹ (%/năm).
  - `preferential_interest_rate`: Lãi suất ưu đãi.
  - `buy_fee`: Phí giao dịch Mua.
  - `sell_fee`: Phí giao dịch Bán.
- Khi Click button, phải **lưu lại giá trị `id` của gói vay đã chọn** vào state (ví dụ `loan_id = '7905'`).

### B. Đối với Tài Khoản Phái Sinh

```python
der_loans = client_order.get_derivative_loan_packages(account_id='0001009212') # account_id lấy từ bước 2
for i in der_loans:
    print(i.summary())
```
**Mẫu dữ liệu**:
```json
{
    "id": 2278,
    "initial_rate": 0.1848,
    "maintenance_rate": 0.1771,
    "liquid_rate": 0.1731,
    "trading_fee": 500.0,
    "trading_fee_daily_close": 500.0,
    "symbol_types": ["V100F1M", "V100F2M", "VN30F1M", "VN30F1Q", "VN30F2M", "VN30F2Q"],
    "error": null,
    "status_code": 200,
    "num_symbol_types": 6
}
```
**Hướng dẫn UI**:
- Generate các **Buttons** chọn Gói vay Phái sinh.
- Hiển thị các thông tin:
  - `initial_rate`: Tỷ lệ ký quỹ ban đầu.
  - `maintenance_rate`: Tỷ lệ duy trì ký quỹ.
  - `liquid_rate`: Tỷ lệ xử lý (mức Call margin bắt buộc đóng vị thế).
  - `trading_fee`: Phí giao dịch cố định.
  - `trading_fee_daily_close`: Phí giao dịch cố định hàng ngày (nếu có).
- Khi Click button, **lưu lại giá trị `id` của gói vay đã chọn** vào state.

---

## 4. Thực thi Đặt Lệnh (Place Order)

Khi người dùng đã chọn đầy đủ Tài khoản, Gói vay và nhập thông số (Mã CK, Loại Lệnh, Số lượng, Giá), hệ thống sẽ tiến hành gửi lệnh.

```python
# 1. Khởi tạo đối tượng orderbook với account_id và loan_id người dùng đã chọn
orderbook = client_order.get_orderbook(
    account_id='0001009212', # ID tiểu khoản được chọn ở Bước 2
    loan_id='13720' # ID gói vay được chọn ở Bước 3
)

# 2. Đặt lệnh bằng hàm place_order
order = orderbook.place_order(
    ticker='HPG',         # Mã cổ phiếu nhập trên form
    side='buy',           # UI Map: Người nhấn nút 'Mua' -> side='buy', 'Bán' -> side='sell'
    order_type='LO',      # Loại lệnh: LO, ATO, ATC, ...
    quantity=1000,        # Khối lượng nhập
    price=27000           # Mức giá nhập
)

# 3. Kết quả trả về
print(order.summary())
```
**Hướng dẫn UI**:
- Thiết kế riêng rẽ Button MUA (thường màu Xanh) và BÁN (thường màu Đỏ).
- Truyền đúng giá trị `side='buy'` khi gọi action của button Mua và `side='sell'` khi bấm nút Bán.
- Có hiển thị modal thông báo kết quả trả về từ `order.summary()` để người dùng biết thành công hay thất bại.
- **Xử lý Loại lệnh (`order_type`) & Logic nhập Giá (`price`)**:
  - Giao diện cần Dropdown/Radio để chọn loại lệnh. **Lưu ý: Tài khoản phái sinh sẽ KHÔNG có lệnh PLO và MP**.
  - **LO**: Mua/bán tại mức giá xác định hoặc tốt hơn. 👉 **Được phép** nhập giá mua/bán.
  - **MP**: Mua/bán ngay tại giá tốt nhất hiện có trên thị trường, nếu không khớp hết sẽ chuyển thành LO tại mức giá tiếp theo. 👉 **Không được phép** nhập giá.
  - **MTL**: Giống MP nhưng có cơ chế giữ lại phần chưa khớp. 👉 **Không được phép** nhập giá.
  - **MOK**: Phải khớp toàn bộ ngay lập tức. 👉 **Không được phép** nhập giá.
  - **MAK**: Khớp được bao nhiêu thì khớp, phần còn lại sẽ hủy ngay. 👉 **Không được phép** nhập giá.
  - **ATO**: Dùng trong phiên xác định giá mở cửa. Chỉ cho phép chọn trong phiên ATO. 👉 **Không được phép** nhập giá.
  - **ATC**: Dùng trong phiên xác định giá đóng cửa. Chỉ cho phép chọn trong phiên ATC. 👉 **Không được phép** nhập giá.
  - **PLO**: Chỉ cho dùng Giao dịch sau giờ (14h45–15h). Giá sẽ lấy bằng giá đóng cửa (ATC). Chỉ khớp nếu có đối ứng. 👉 **Được phép** nhập giá mua/bán.
  - *(Khi user chọn thay đổi loại lệnh trên UI, cần chủ động disable hoặc khóa ô nhập `price`/cho phép `price` tương ứng như rule trên).*
