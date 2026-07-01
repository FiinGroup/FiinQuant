---
name: Bộ lọc cổ phiếu
description: Lọc nhanh danh sách cổ phiếu dựa trên các điều kiện định nghĩa sẵn như chỉ số chính, báo cáo tài chính, sàn giao dịch và ngành nghề, hỗ trợ phân tích đầu tư, xây dựng chiến lược screening và tạo danh sách cổ phiếu theo tiêu chí định lượng trong FiinQuantX.
---

# 10. Bộ lọc cổ phiếu

**Tên hàm:** `client.StockScreening().get(...)`

**Mục đích:**
Hàm được sử dụng để lọc nhanh danh sách cổ phiếu dựa trên các điều kiện định nghĩa sẵn, thay vì phải tự xử lý và tính toán dữ liệu từ đầu.

Hàm này đặc biệt hữu ích cho:
- Phân tích đầu tư
- Xây dựng chiến lược screening
- Tạo danh sách cổ phiếu theo tiêu chí định lượng (quant screening)

**Tham số:**

| Tên tham số | Mô tả | Kiểu dữ liệu | Mặc định | Bắt buộc |
|---|---|---|---|---|
| filter | Bộ lọc, là list các điều kiện, mỗi điều kiện là một dict, chi tiết mô tả các tham số trong dict xem phần **Cấu trúc tham số filter** bên dưới | list |  | Có |
| screenerDate | Ngày sàng lọc, định dạng `"%Y-%m-%d"` | str | `datetime.now()` | Không |
| exchanges | Danh sách các sàn cần lọc cổ phiếu | list | Tất cả các sàn | Không |
| sectors | Danh sách các ngành cần lọc cổ phiếu, nhập theo mã ngành như `BANKS_L2`, `OIL_AND_GAS_L2`, `REAL_ESTATE_L2`, `CHEMICALS_L2` | list | Tất cả các ngành | Không |

**Cấu trúc tham số filter**:
List các điều kiện, mỗi điều kiện là một dict.
Dưới đây là cách truyền tham số filter, có 2 nhóm là nhóm các tiêu chí thuộc chỉ số chính (VD: lọc các cổ phiếu có Free Float, % Thay đổi giá gần nhất nằm trong khoảng ...) và nhóm tiêu chí thuộc báo cáo tài chính, chỉ số tài chính (VD: lọc các cổ phiếu có doanh thu thuần, lợi nhuận, P/E, ROE trong khoảng ... hoặc lợi nhuận năm nay cao nhất trong vòng 4 năm đổ lại, v.v.)

```python
filters = [
    {
        # Bộ lọc nhóm chỉ số chính
        "indicatorName": "<string: '% Free Float' | 'Free Float' | 'Số cổ phiếu niêm yết' | ...>",
        "conditionValues": [
            <from_value>,
            <to_value>
        ]
        # conditionValues:
        # - List gồm 2 phần tử: [từ giá trị, đến giá trị]
        # - Có thể dùng None nếu không giới hạn
        # Ví dụ:
        # [100000, 200000]
        # [100000000, 200000000]
        # [100000, None]
        # [0.1, 0.3]  # tương đương 10% - 30%
    },

    {
        # Bộ lọc nhóm báo cáo tài chính và chỉ số tài chính
        "indicatorName": "<string: '3. Doanh thu thuần bán hàng và cung cấp dịch vụ' | '11. Lợi nhuận thuần từ hoạt động kinh doanh' | '18. Lợi nhuận sau thuế TNDN' | P/E cơ bản (TTM) | ROE % (TTM) | ROA % (TTM) >",
        "conditionValues": [
            <from_value>,
            <to_value>
        ],
        # conditionValues:
        # - Có thể [None, None] nếu không muốn dùng filter này
        # Ví dụ:
        # [100000, 200000]
        # [100000, None]
        # [0.1, 0.3]
        # [None, None]
        "interimCode": "<string: 'Yearly' | 'Quarterly' | 'TTM'>",
        # Yearly  = báo cáo năm
        # Quarterly = báo cáo quý
        # TTM = nếu chỉ số cần lọc là TTM
        "indicatorInterimId": "<string>",
        # Nếu Yearly:  '2025', '2024', ...
        # Nếu Quarterly: 'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025'
        # Neesyu TTM: 5 quý gần nhất (VD: 'Q4-2024', 'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025'), '3_Recent_Continuous_TTM', '5_Recent_Continuous_TTM'
        "additionalCondition": {
            # (Optional) - có thể bỏ nếu không dùng
            "operator": "<string: '<' | '>' | '>=' | '<=' | '='>",
            "interimCode": "<string: 'Last_Interim' | '3_Recent_Continuous_{Year/Quarter}' | '5_Recent_Continuous_{Year/Quarter}'>",
            # Last_Interim: So sánh kỳ được chọn với kỳ trước đó
            # 3_Recent_Continuous_{Year/Quarter}: So sánh kỳ được chọn với Max/Min/Avg của 3 kỳ liên tiếp gần nhất
            # 5_Recent_Continuous_{Year/Quarter}: So sánh kỳ được chọn với Max/Min/Avg của 5 kỳ liên tiếp gần nhất
            "function": "<string: 'Max' | 'Min' | 'Avg'>"
            # Không áp dụng nếu interimCode = 'Last_Interim'
        }
    }
]
```

Danh sách các chỉ tiêu lọc được phép điền vào key \"indicatorName\":
- Nhóm chỉ số chính: Free Float, % Free Float, Số cổ phiếu niêm yết, Số CP lưu hành hiện thời, Số cổ phiếu quỹ, Khối lượng khối ngoại sở hữu gần nhất, Khối lượng khối ngoại còn lại, Khối lượng khối ngoại sở hữu tối đa, Tỷ lệ sở hữu khối ngoại, Tỷ lệ sở hữu nhà nước, Giá đóng cửa gần nhất, Giá mở cửa gần nhất, Giá cao nhất gần nhất, Giá thấp nhất gần nhất, Khối lượng gần nhất, Giá trị gần nhất, Khối lượng mua chủ động nhất, Khối lượng bán chủ động gần nhất, Khối lượng đặt mua gần nhất, Khối lượng đặt bán gần nhất, Room khối ngoại còn lại (%), Khối lượng khối ngoại mua gần nhất, Khối lượng khối ngoại bán gần nhất, Giá trị khối ngoại mua gần nhất, Giá trị khối ngoại bán gần nhất, Giá trị cá nhân trong nước mua gần nhất, Giá trị cá nhân trong nước bán gần nhất, Giá trị tổ chức trong nước mua gần nhất, Giá trị tổ chức trong nước bán gần nhất, Giá trị cá nhân nước ngoài mua gần nhất, Giá trị cá nhân nước ngoài bán gần nhất, Giá trị tổ chức nước ngoài mua gần nhất, Giá trị tổ chức nước ngoài bán gần nhất, Beta 6 tháng điều chỉnh, Beta 2 năm điều chỉnh, Beta 6 tháng, Beta 2 năm, % Thay đổi giá gần nhất, % Thay đổi giá 1 tuần, % Thay đổi giá 2 tuần, % Thay đổi giá 1 tháng, % Thay đổi giá 2 tháng, % Thay đổi giá 3 tháng, % Thay đổi giá 6 tháng, % Thay đổi giá 9 tháng, % Thay đổi giá 1 năm, % Thay đổi giá từ đầu năm, % Thay đổi giá 52 tuần, Giá cao nhất 1 tuần, Giá cao nhất 2 tuần, Giá cao nhất 1 tháng, Giá cao nhất 2 tháng, Giá cao nhất 3 tháng, Giá cao nhất 6 tháng, Giá cao nhất 9 tháng, Giá cao nhất 1 năm, Giá cao nhất từ đầu năm, Giá cao nhất 52 tuần, Giá thấp nhất 1 tuần, Giá thấp nhất 2 tuần, Giá thấp nhất 1 tháng, Giá thấp nhất 2 tháng, Giá thấp nhất 3 tháng, Giá thấp nhất 6 tháng, Giá thấp nhất 9 tháng, Giá thấp nhất 1 năm, Giá thấp nhất từ đầu năm, Giá thấp nhất 52 tuần, Giá trung bình (VWAP) 1 tuần, Giá trung bình (VWAP) 2 tuần, Giá trung bình (VWAP) 1 tháng, Giá trung bình (VWAP) 2 tháng, Giá trung bình (VWAP) 3 tháng, Giá trung bình (VWAP) 6 tháng, Giá trung bình (VWAP) 9 tháng, Giá trung bình (VWAP) 1 năm, Giá trung bình (VWAP) từ đầu năm, Giá trung bình (VWAP) 52 tuần, Khối lượng trung bình 1 tuần, Khối lượng trung bình 2 tuần, Khối lượng trung bình 1 tháng, Khối lượng trung bình 2 tháng, Khối lượng trung bình 3 tháng, Khối lượng trung bình 6 tháng, Khối lượng trung bình 9 tháng, Khối lượng trung bình 1 năm, Khối lượng trung bình từ đầu năm, Khối lượng trung bình 52 tuần, Số CP lưu hành hiện thời (TTM), "Giá trị sổ sách/ cổ phiếu " (chỉ số hàng ngày), "Doanh số/ cổ phiếu " (chỉ số hàng ngày), "EPS cơ bản " (chỉ số hàng ngày), "EPS pha loãng " (chỉ số hàng ngày), "Tốc độ tăng trưởng EPS (YoY) ", "EPS dự báo " (chỉ số hàng ngày), "P/E cơ bản " (chỉ số hàng ngày), "P/E pha loãng " (chỉ số hàng ngày), "P/E dự báo " (chỉ số hàng ngày), "P/B " (chỉ số hàng ngày), "P/S " (chỉ số hàng ngày), "P/ Tangible Book " (chỉ số hàng ngày), "P/ Cash Flow " (chỉ số hàng ngày), "Vốn hóa thị trường " (chỉ số hàng ngày), "Giá trị doanh nghiệp " (chỉ số hàng ngày), "Giá trị doanh nghiệp/ Doanh số " (chỉ số hàng ngày), "Giá trị doanh nghiệp/ EBITDA " (chỉ số hàng ngày), "Giá trị doanh nghiệp/ EBIT " (chỉ số hàng ngày)


- Nhóm báo cáo tài chính: I. TÀI SẢN NGẮN HẠN, 1. Tiền và các khoản tương đương tiền, 2. Đầu tư tài chính ngắn hạn, 3. Các khoản phải thu ngắn hạn, 4. Hàng tồn kho, 5. Tài sản ngắn hạn khác, II. TÀI SẢN DÀI HẠN, 1. Các khoản phải thu dài hạn, 2. Tài sản cố định, 3. Bất động sản đầu tư, 4. Tài sản dở dang dài hạn, 5. Đầu tư tài chính dài hạn, 7. Tài sản dài hạn khác, 1. Doanh thu bán hàng & cung cấp dịch vụ, 3. Doanh thu thuần bán hàng và cung cấp dịch vụ, 5. Lợi nhuận gộp về bán hàng và cung cấp dịch vụ, 11. Lợi nhuận thuần từ hoạt động kinh doanh, 16. Tổng lợi nhuận kế toán trước thuế, 18. Lợi nhuận sau thuế TNDN

- Nhóm chỉ số tài chính: Giá trị sổ sách/ cổ phiếu (TTM), Giá trị sổ sách/ cổ phiếu (Y), Doanh số/ cổ phiếu (TTM), Doanh số/ cổ phiếu (Y), EPS cơ bản (TTM), EPS cơ bản (Y), EPS pha loãng (TTM), EPS pha loãng (Y), Tốc độ tăng trưởng EPS (YoY) (TTM), EPS dự báo (TTM), EPS dự báo (Y), Dòng tiền tự do (TTM), Dòng tiền tự do (Y), P/E cơ bản (TTM), P/E pha loãng (TTM), P/E cơ bản (Y), P/E pha loãng (Y), P/E dự báo (TTM), P/E dự báo (Y), P/B (TTM), P/B (Y), P/S (TTM), P/S (Y), P/ Tangible Book (TTM), P/ Tangible Book (Y), P/ Cash Flow (TTM), P/ Cash Flow (Y), Vốn hóa thị trường (TTM), Vốn hóa thị trường (Y), Giá trị doanh nghiệp (TTM), Giá trị doanh nghiệp (Y), Giá trị doanh nghiệp/ Doanh số (TTM), Giá trị doanh nghiệp/ Doanh số (Y), Giá trị doanh nghiệp/ EBITDA (TTM), Giá trị doanh nghiệp/ EBITDA (Y), Giá trị doanh nghiệp/ EBIT (TTM), Giá trị doanh nghiệp/ EBIT (Y), ROE % (TTM), ROCE % (TTM), ROCE % (Y), ROA % (TTM), ROA % (Y), ROA trước dự phòng % (TTM), ROA trước dự phòng % (Y), ROIC % (TTM), ROIC % (Y), Hệ số quay vòng phải thu khách hàng (TTM), Hệ số quay vòng phải thu khách hàng (Y), Thời gian trung bình thu tiền khách hàng (TTM), Thời gian trung bình thu tiền khách hàng (Y), Hệ số quay vòng hàng tồn kho (TTM), Hệ số quay vòng hàng tồn kho (Y)

**Giá trị trả về (Returns):**
- Trả về một `DataFrame`
- Mỗi dòng là một mã cổ phiếu thỏa mãn điều kiện lọc
- Các cột kết quả sẽ bao gồm thông tin cơ bản của doanh nghiệp và các cột dữ liệu động tương ứng với điều kiện lọc được truyền vào

**Thuộc tính dữ liệu:**

| Tên thuộc tính | Mô tả | Kiểu dữ liệu |
|---|---|---|
| Mã CK | Các mã chứng khoán thỏa mãn điều kiện bộ lọc | str |
| Tên công ty | Tên gọi doanh nghiệp đầy đủ của các mã chứng khoán tương ứng | str |
| Sàn | Sàn giao dịch mà các mã chứng khoán tương ứng niêm yết | str |
| Ngành L2 | Tên ngành cấp 2 của các doanh nghiệp tương ứng | str |
| Các cột động tùy theo bộ lọc | Số liệu chỉ số hoặc báo cáo tài chính tương ứng của từng mã chứng khoán thỏa mãn điều kiện lọc | float |

**Ví dụ sử dụng 1:**
Lọc ra các cổ phiếu thuộc sàn HOSE và thuộc các lĩnh vực Hóa chất cấp 2, Bất động sản cấp 2 có tỷ lệ `% Free Float` trong khoảng từ `0.1` đến `0.5` và số cổ phiếu niêm yết trong khoảng từ `10` đến `200` triệu.

```python
from FiinQuantX import FiinSession

username = "REPLACE_WITH_YOUR_USERNAME"
password = "REPLACE_WITH_YOUR_PASSWORD"

client = FiinSession(username=username, password=password).login()

filter = [
    {
        "indicatorName": "% Free Float",
        "conditionValues": [0.1, 0.5]
    },
    {
        "indicatorName": "Số cổ phiếu niêm yết",
        "conditionValues": [10000000, 200000000]
    }
]

data = client.StockScreening().get(
    filter=filter,
    screenerDate="2026-03-17",
    exchanges=["HOSE"],
    sectors=["CHEMICALS_L2", "REAL_ESTATE_L2"]
)

print(data)
```
**Output mẫu 1:**
| Mã CK | Tên công ty       | Sàn  | Ngành L2     | % Free Float 2026-03-17 | Số cổ phiếu niêm yết 2026-03-17 |
|------|-------------------|------|--------------|--------------------------|---------------------------------|
| PHR  | Cao su Phước Hòa  | HOSE | Hóa chất     | 0.3500                   | 135499200.0                     |
| SZC  | Sonadezi Châu Đức | HOSE | Bất động sản | 0.4000                   | 179985860.0                     |
| ...  | ...               | ...  | ...          | ...                      | ...                             |
| BRC  | Cao su Bến Thành  | HOSE | Hóa chất     | 0.1300                   | 12375000.0                      |

**Ví dụ sử dụng 2:**
Lọc ra các cổ phiếu thuộc sàn HOSE và thuộc các lĩnh vực Hóa chất cấp 2, Bất động sản cấp 2 có Doanh thu thuần bán hàng và cung cấp dịch vụ trong cả năm 2025 lớn hơn giá trị doanh thu cao nhất trong 3 năm gần nhất liên tục, đồng thời Doanh thu thuần bán hàng và cung cấp dịch vụ của riêng quý 4 năm 2025 đạt trên 10.000 tỷ.

```python
from FiinQuantX import FiinSession

username = "REPLACE_WITH_YOUR_USERNAME"
password = "REPLACE_WITH_YOUR_PASSWORD"

client = FiinSession(username=username, password=password).login()

filter = [
    {
        "indicatorName": "3. Doanh thu thuần bán hàng và cung cấp dịch vụ",
        "interimCode": "Yearly",
        "indicatorInterimId": "2025",
        "conditionValues": [None, None],
        "additionalCondition": {
            "interimCode": "3_Recent_Continuous_Year",
            "operator": ">",
            "function": "Max"
        }
    },
    {
        "indicatorName": "3. Doanh thu thuần bán hàng và cung cấp dịch vụ",
        "interimCode": "Quarterly",
        "indicatorInterimId": "Q4-2025",
        "conditionValues": [10000000000000, None]
    }
]

data = client.StockScreening().get(
    filter=filter,
    screenerDate="2026-03-17",
    exchanges=["HOSE"],
    sectors=["CHEMICALS_L2", "REAL_ESTATE_L2"]
)

print(data)
```

**Output mẫu 2:**
| Mã CK | Tên công ty | Sàn  | Ngành L2     | 3. Doanh thu thuần bán hàng và cung cấp dịch vụ 2025 | 3. Doanh thu thuần bán hàng và cung cấp dịch vụ 3 năm liên tiếp trước kỳ sàng lọc Lớn nhất của 2025 | 3. Doanh thu thuần bán hàng và cung cấp dịch vụ Q4-2025 |
|------|-------------|------|--------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| VIC  | VinGroup    | HOSE | Bất động sản | 3.3277E+14                                           | 1.89068E+14                                                                                            | 1.63159E+14                                              |
| VHM  | Vinhomes    | HOSE | Bất động sản | 1.54102E+14                                          | 1.03557E+14                                                                                            | 1.0301E+14                                               |