# FiinQuant Skill Package

FiinQuant Skill Package cung cấp bộ hướng dẫn kỹ thuật và tài liệu tham chiếu
cho các workflow sử dụng **FiinQuant** trên thị trường chứng khoán Việt Nam
(HOSE, HNX, UPCOM).

Package tập trung vào việc chuẩn hóa cách gọi hàm, tham số, dữ liệu trả về và
các tình huống triển khai thường gặp khi làm việc với FiinQuant. Nội dung được
tổ chức theo cơ chế progressive disclosure: file `SKILL.md` đóng vai trò điều
phối, còn chi tiết từng nhóm chức năng nằm trong thư mục `references/`.

## Nội dung chính

- Dữ liệu danh mục: mã chứng khoán, rổ chỉ số, ngành, vốn hóa, room ngoại,
  free-float và giá trần/sàn.
- Dữ liệu giao dịch: realtime, lịch sử, OHLCV, order book, dữ liệu tick và quản lý vòng đời kết nối.
- Phân tích cơ bản: báo cáo tài chính, chỉ số tài chính, P/E, P/B và định giá.
- Thống kê thị trường: độ rộng thị trường và seasonality.
- Công cụ danh mục: rebalance, RRG và portfolio workflow.
- Giao dịch: đăng nhập, tài khoản, sức mua/bán, đặt/sửa/hủy lệnh và vị thế.
- Phân tích kỹ thuật: trend, momentum, volatility, volume, money flow,
  support/resistance, Fibonacci và chart pattern.
- Stock screening theo bộ lọc dữ liệu FiinQuant.

## Phiên bản FiinQuant

Bộ reference được rà theo FiinQuant bản mới nhất tại thời điểm kiểm chứng gần
nhất: **2026-06-08**.

Repo không pin version FiinQuant. Khi triển khai, cài hoặc cập nhật package từ
index chính thức:

```bash
pip install --extra-index-url https://fiinquant.github.io/FiinQuant/simple FiinQuant
pip install --upgrade --extra-index-url https://fiinquant.github.io/FiinQuant/simple FiinQuant
```

Lưu ý realtime: nếu `signalrcore` >= 1.0.0 gây lỗi tương thích, dùng bản 0.9.x
theo hướng dẫn trong
`plugins/fiinquant/skills/fiinquant/references/0-installation-introduction.md`.

## Cấu trúc repo

```text
.
├── plugins/
│   ├── fiinquant/
│   │   └── skills/
│   │       ├── fiinquant/
│   │       │   ├── SKILL.md
│   │       │   └── references/
│   │       └── fiinquant-ui-errors/
│   ├── fiinquant-trading-chart/
│   │   └── skills/trading-chart-data/
│   ├── fiinquant-ui-dashboard/
│   │   └── skills/front-end/
│   └── fiinquant-dnse-order/
│       └── skills/dnse-order-placement/
├── evals/
└── scripts/build_packages.sh
```

## Đóng gói

Tạo các gói skill trong thư mục `dist/`:

```bash
bash scripts/build_packages.sh
```

Mỗi file zip chứa một thư mục top-level và file `SKILL.md` ở gốc thư mục đó.

## Cài đặt

### Codex

Codex đọc skill từ thư mục user-level hoặc repo-level.

Cài cho một máy cá nhân:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R plugins/fiinquant/skills/fiinquant "$HOME/.agents/skills/"
cp -R plugins/fiinquant/skills/fiinquant-ui-errors "$HOME/.agents/skills/"
cp -R plugins/fiinquant-trading-chart/skills/trading-chart-data "$HOME/.agents/skills/"
cp -R plugins/fiinquant-ui-dashboard/skills/front-end "$HOME/.agents/skills/"
cp -R plugins/fiinquant-dnse-order/skills/dnse-order-placement "$HOME/.agents/skills/"
```

Cài theo từng repo:

```bash
mkdir -p .agents/skills
cp -R /path/to/fiinquant/plugins/fiinquant/skills/fiinquant .agents/skills/
```

Sau khi copy, mở phiên làm việc mới hoặc restart Codex nếu skill chưa xuất hiện.
Có thể gọi trực tiếp bằng tên skill, ví dụ `$fiinquant`.

### Skill-Compatible Clients

Với môi trường hỗ trợ upload skill dạng zip, chạy:

```bash
bash scripts/build_packages.sh
```

Upload `dist/fiinquant.zip` cho bộ core. Các gói bổ trợ:

- `dist/fiinquant-ui-errors.zip`: hướng dẫn xử lý lỗi UI khi tích hợp FiinQuant.
- `dist/trading-chart-data.zip`: workflow biểu đồ realtime.
- `dist/front-end.zip`: guideline UI dashboard tài chính.
- `dist/dnse-order-placement.zip`: workflow đặt lệnh DNSE.

### Marketplace Plugin

Bản repo này được giữ ở dạng skill package trung tính. Nếu cần phát hành theo
marketplace hoặc one-click plugin cho một nền tảng cụ thể, nên tạo package riêng
kèm metadata của nền tảng đó.

## Kiểm thử

Kiểm tra toàn vẹn bộ test:

```bash
python3 evals/run_eval.py
```

Điều kiện trước khi phát hành:

- Bộ test route phủ đủ 10/10 nhóm hàm.
- Tất cả reference trong test phải tồn tại.
- Không có secret, token, password hoặc file phiên giao dịch trong repo.
- Khi FiinQuant thay đổi API, cần rà lại reference và chạy lại bộ test.

## Bảo mật

- Không lưu token, OTP, password hoặc file phiên giao dịch trong git.
- Secret vận hành nên truyền qua biến môi trường hoặc hệ thống quản lý secret.
- File dạng `*token*.json`, `*trading_token*.json`, `.env` và thư mục `secrets/`
  đã được đưa vào `.gitignore`.

## License

Apache License 2.0. See `LICENSE`.
