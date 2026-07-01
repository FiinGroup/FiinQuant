---
name: Hướng dẫn cách dùng bộ lọc cổ phiếu
description: Mô tả, hướng dẫn chi tiết các dùng tham số filter của hàm `client.StockScreening().get(params)` ở mục `core/stock_screening.md`.
---

**Cấu trúc tổng thể**: Bộ lọc là list các điều kiện, mỗi điều kiện là một dict.

**Chi tiết cách dùng**: Dưới đây là cách truyền tham số filter, có 2 nhóm là nhóm các tiêu chí thuộc chỉ số (VD: lọc các cổ phiếu có Free Float, % Thay đổi giá gần nhất nằm trong khoảng ...) và nhóm tiêu chí thuộc báo cáo tài chính (VD: lọc các cổ phiếu có doanh thu thuần, lợi nhuận trong khoảng ... hoặc lợi nhuận năm nay cao nhất trong vòng 4 năm đổ lại, v.v.)

**Nhóm 1: Các tiêu chí thuộc chỉ số**:
```python
filters = [
	{
    "indicatorName":  “<string: ‘% Free Float’ | ‘Free Float’ | ‘Số cổ phiếu niêm yết’ | etc… >”,
    "conditionValues": “<list gồm 2 phần tử thể hiện khoảng giá trị cần lấy trong đó phần tử thứ nhất là "từ giá trị" và phần tử thứ 2 là "đến giá trị", có thể điền None ở 1 trong 2 đầu để biểu hiện việc không có giới hạn đầu trên và đầu dưới. VD : [100000, 200000] | [100000000, 200000000] | [100000, None] | [0.1, 0.3] (đối với các chỉ số dạng % nghĩa là từ 10%-30%) | etc… >” 
    }
]
```

**Nhóm 2: Các tiêu chí thuộc báo cáo tài chính**:
```python
filters = [
	{
        "indicatorName":  “<string: ‘3. Doanh thu thuần bán hàng và cung cấp dịch vụ‘ | ‘11. Lợi nhuận thuần từ hoạt động kinh doanh’ | ‘18. Lợi nhuận sau thuế TNDN’ | etc… >”,
        "conditionValues": “<list gồm 2 phần tử thể hiện khoảng giá trị cần lấy trong đó phần tử thứ nhất là "từ giá trị" và phần tử thứ 2 là "đến giá trị", có thể điền None ở 1 trong 2 đầu để biểu hiện việc không có giới hạn đầu trên và đầu dưới hoặc nếu không muốn dùng bộ lọc này thì để None ở 2 đầu. VD : [100000, 200000] | [100000000, 200000000] | [100000, None] | [0.1, 0.3] (đối với các chỉ số dạng % nghĩa là từ 10%-30% | [None, None] | etc… >”,
        "interimCode": "<string: Sàng lọc theo báo cáo quý hoặc năm, chỉ nhận 1 trong 2 giá trị "Yearly" - báo cáo năm hoặc "Quarterly" - báo cáo quý>",
        "indicatorInterimId":  "<string: Kỳ sàng lọc, với báo cáo năm thì điền string dạng số như '2025', '2024', '2023', v.v.; còn quý thì điền dạng 'Q{số quý 1,2,3,4}-YYYY' như 'Q4-2025', 'Q3-2025', 'Q2-2025', v.v.>",
        "additionalCondition": 
            { # tiêu chí mở rộng có thể dùng nếu cần, nếu không cần dùng thì không cần thêm vào trong danh sách bộ lọc
                "operator": “<string: tiêu chí so sánh, nhận 1 trong 5 toán tử ‘<’|’>’|’>=’|’<=’,’=’ ”,
                "interimCode": "<string: Giá trị so sánh, nhận 1 trong 3 giá trị ’Last_Interim’ - kỳ trước, ’3_Recent_Continuous_{Year/Quarter}’ - 3 kỳ gần nhất liên tiếp, ’5_Recent_Continuous_{Year/Quarter}’ - 5 kỳ gần nhất liên tiếp>",
                "function": "<string: cơ sở so sánh với interimCode (không áp dụng nếu interimCode nhận giá trị ’Last_Interim’), nhận 1 trong 3 giá trị ’Max’, ’Min’, ’Avg’>"
            }
    } # Đối với các bộ lọc thuộc nhóm báo cáo tài chính
]
```

**Danh sách các chỉ tiêu lọc được phép điền vào key "indicatorName":**
- Nhóm chỉ số chính: Free Float, % Free Float, Số cổ phiếu niêm yết, Số CP lưu hành hiện thời, Số cổ phiếu quỹ, Khối lượng khối ngoại sở hữu gần nhất, Khối lượng khối ngoại còn lại, Khối lượng khối ngoại sở hữu tối đa, Tỷ lệ sở hữu khối ngoại, Tỷ lệ sở hữu nhà nước, Giá đóng cửa gần nhất, Giá mở cửa gần nhất, Giá cao nhất gần nhất, Giá thấp nhất gần nhất, Khối lượng gần nhất, Giá trị gần nhất, Khối lượng mua chủ động nhất, Khối lượng bán chủ động gần nhất, Khối lượng đặt mua gần nhất, Khối lượng đặt bán gần nhất, Room khối ngoại còn lại (%), Khối lượng khối ngoại mua gần nhất, Khối lượng khối ngoại bán gần nhất, Giá trị khối ngoại mua gần nhất, Giá trị khối ngoại bán gần nhất, Giá trị cá nhân trong nước mua gần nhất, Giá trị cá nhân trong nước bán gần nhất, Giá trị tổ chức trong nước mua gần nhất, Giá trị tổ chức trong nước bán gần nhất, Giá trị cá nhân nước ngoài mua gần nhất, Giá trị cá nhân nước ngoài bán gần nhất, Giá trị tổ chức nước ngoài mua gần nhất, Giá trị tổ chức nước ngoài bán gần nhất, Beta 6 tháng điều chỉnh, Beta 2 năm điều chỉnh, Beta 6 tháng, Beta 2 năm, % Thay đổi giá gần nhất, % Thay đổi giá 1 tuần, % Thay đổi giá 2 tuần, % Thay đổi giá 1 tháng, % Thay đổi giá 2 tháng, % Thay đổi giá 3 tháng, % Thay đổi giá 6 tháng, % Thay đổi giá 9 tháng, % Thay đổi giá 1 năm, % Thay đổi giá từ đầu năm, % Thay đổi giá 52 tuần, Giá cao nhất 1 tuần, Giá cao nhất 2 tuần, Giá cao nhất 1 tháng, Giá cao nhất 2 tháng, Giá cao nhất 3 tháng, Giá cao nhất 6 tháng, Giá cao nhất 9 tháng, Giá cao nhất 1 năm, Giá cao nhất từ đầu năm, Giá cao nhất 52 tuần, Giá thấp nhất 1 tuần, Giá thấp nhất 2 tuần, Giá thấp nhất 1 tháng, Giá thấp nhất 2 tháng, Giá thấp nhất 3 tháng, Giá thấp nhất 6 tháng, Giá thấp nhất 9 tháng, Giá thấp nhất 1 năm, Giá thấp nhất từ đầu năm, Giá thấp nhất 52 tuần, Giá trung bình (VWAP) 1 tuần, Giá trung bình (VWAP) 2 tuần, Giá trung bình (VWAP) 1 tháng, Giá trung bình (VWAP) 2 tháng, Giá trung bình (VWAP) 3 tháng, Giá trung bình (VWAP) 6 tháng, Giá trung bình (VWAP) 9 tháng, Giá trung bình (VWAP) 1 năm, Giá trung bình (VWAP) từ đầu năm, Giá trung bình (VWAP) 52 tuần, Khối lượng trung bình 1 tuần, Khối lượng trung bình 2 tuần, Khối lượng trung bình 1 tháng, Khối lượng trung bình 2 tháng, Khối lượng trung bình 3 tháng, Khối lượng trung bình 6 tháng, Khối lượng trung bình 9 tháng, Khối lượng trung bình 1 năm, Khối lượng trung bình từ đầu năm, Khối lượng trung bình 52 tuần, Số CP lưu hành hiện thời (TTM), Giá trị sổ sách/ cổ phiếu (TTM), Doanh số/ cổ phiếu (TTM), EPS cơ bản (TTM), EPS pha loãng (TTM), Dòng tiền tự do (TTM), P/E cơ bản (TTM), P/e pha loãng (TTM), P/B (TTM), P/S (TTM), P/ Tangible Book (TTM), P/ Cash Flow (TTM), Vốn hóa thị trường (TTM), Giá trị doanh nghiệp (TTM), Giá trị doanh nghiệp/ Doanh số (TTM), Giá trị doanh nghiệp/ EBITDA (TTM), Giá trị doanh nghiệp/ EBIT (TTM), ROE % (TTM), ROCE % (TTM), ROA % (TTM), ROIC % (TTM), Hệ số quay vòng phải thu khách hàng (TTM), Thời gian trung bình thu tiền khách hàng (TTM), Hệ số quay vòng hàng tồn kho (TTM)
- Nhóm báo cáo tài chính: I. TÀI SẢN NGẮN HẠN, 1. Tiền và các khoản tương đương tiền, 2. Đầu tư tài chính ngắn hạn, 3. Các khoản phải thu ngắn hạn, 4. Hàng tồn kho, 5. Tài sản ngắn hạn khác, II. TÀI SẢN DÀI HẠN, 1. Các khoản phải thu dài hạn, 2. Tài sản cố định, 3. Bất động sản đầu tư, 4. Tài sản dở dang dài hạn, 5. Đầu tư tài chính dài hạn, 7. Tài sản dài hạn khác, 1. Doanh thu bán hàng & cung cấp dịch vụ, 3. Doanh thu thuần bán hàng và cung cấp dịch vụ, 5. Lợi nhuận gộp về bán hàng và cung cấp dịch vụ, 11. Lợi nhuận thuần từ hoạt động kinh doanh, 16. Tổng lợi nhuận kế toán trước thuế, 18. Lợi nhuận sau thuế TNDN