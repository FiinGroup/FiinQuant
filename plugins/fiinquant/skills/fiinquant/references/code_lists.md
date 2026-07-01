---
name: Code List
description: Tham chiếu cho danh sách các mã ngành, mã chỉ số có thể được dùng để truyền vào biến tickers của các hàm thuộc thư viện FiinQuant.
---

# 1. Danh sách các Index có thể truyền vào được các hàm lấy dữ liệu lịch sử và realtime
'VNINDEX', 'VN30', 'HNXIndex', 'HNX30', 'UpcomIndex', 'VNXALL', 'FLEADTRI', 'HNX30TRI', 'VN100', 'VN100TRI', 'VN30TRI', 'VNALL', 'VNALLTRI', 'VNCOND', 'VNCONS', 'VNDIAMOND', 'VNDTRI', 'VNENE', 'VNFIN', 'VNFINLEAD', 'VNFINSELECT', 'VNFSTRI', 'VNHEAL', 'VNIND', 'VNIT', 'VNMAT', 'VNMID', 'VNMIDCAPTRI', 'VNREAL', 'VNSI', 'VNSMALLTRI', 'VNSML', 'VNUTI', 'VNX50'

**Lưu ý**: Đối với các hàm lấy dữ liệu lịch sử, buộc phải điền case sensitive y hệt như trên, còn đối với các hàm realtime các chỉ số được truyền vào cần phải được viết hoa toàn bộ.

# 2. Danh sách các ngành, mã ngành có thể truyền vào được các hàm lấy dữ liệu lịch sửa và realtime

| Tên phân ngành                                                    | Biến tên phân ngành truyền vào các hàm          | ICB Code truyền vào hàm TickerList |
|-------------------------------------------------------------------|-------------------------------------------------|------------------------------------|
| Dầu khí L1                                                        | OIL_AND_GAS_L1                                  | 0001                               |
| Dầu khí L2                                                        | OIL_AND_GAS_L2                                  | 0500                               |
| Sản xuất Dầu khí L3                                               | OIL_AND_GAS_PRODUCERS_L3                        | 0530                               |
| Sản xuất và Khai thác dầu khí L4                                  | EXPLORATION_AND_PRODUCTION_L4                   | 0533                               |
| Tổ hợp Dầu khí L4                                                 | INTEGRATED_OIL_AND_GAS_L4                       | 0537                               |
| Thiết bị, Dịch vụ và Phân phối Dầu khí L3                         | OIL_EQUIPMENT_SERVICES_AND_DISTRIBUTION_L3      | 0570                               |
| Thiết bị và Dịch vụ Dầu khí L4                                    | OIL_EQUIPMENT_AND_SERVICES_L4                   | 0573                               |
| Ống dẫn Dầu L4                                                    | PIPELINES_L4                                    | 0577                               |
| Nguyên vật liệu L1                                                | BASIC_MATERIALS_L1                              | 1000                               |
| Hóa chất L2                                                       | CHEMICALS_L2                                    | 1300                               |
| Hóa chất L3                                                       | CHEMICALS_L3                                    | 1350                               |
| Nhựa, cao su & sợi L4                                             | COMMODITY_CHEMICALS_L4                          | 1353                               |
| Sản phẩm hóa dầu, Nông dược & Hóa chất khác L4                    | SPECIALTY_CHEMICALS_L4                          | 1357                               |
| Tài nguyên Cơ bản L2                                              | BASIC_RESOURCES_L2                              | 1700                               |
| Lâm nghiệp và Giấy L3                                             | FORESTRY_AND_PAPER_L3                           | 1730                               |
| Lâm sản và Chế biến gỗ L4                                         | FORESTRY_L4                                     | 1733                               |
| Sản xuất giấy L4                                                  | PAPER_L4                                        | 1737                               |
| Kim loại L3                                                       | INDUSTRIAL_METALS_AND_MINING_L3                 | 1750                               |
| Nhôm L4                                                           | ALUMINUM_L4                                     | 1753                               |
| Kim Loại màu L4                                                   | NONFERROUS_METALS_L4                            | 1755                               |
| Thép và sản phẩm thép L4                                          | STEEL_L4                                        | 1757                               |
| Khai khoáng L3                                                    | MINING_L3                                       | 1770                               |
| Khai thác Than L4                                                 | COAL_L4                                         | 1771                               |
| Đá quý và Kim cương L4                                            | DIAMONDS_AND_GEMSTONES_L4                       | 1773                               |
| Khai khoáng L4                                                    | GENERAL_MINING_L4                               | 1775                               |
| Khai thác vàng L4                                                 | GOLD_MINING_L4                                  | 1777                               |
| Bạch kim & Kim loại quý khác L4                                   | PLATINUM_AND_PRECIOUS_METALS_L4                 | 1779                               |
| Công nghiệp L1                                                    | INDUSTRIALS_L1                                  | 2000                               |
| Xây dựng và Vật liệu L2                                           | CONSTRUCTION_AND_MATERIALS_L2                   | 2300                               |
| Xây dựng và Vật liệu L3                                           | CONSTRUCTION_AND_MATERIALS_L3                   | 2350                               |
| Vật liệu xây dựng & Nội thất L4                                   | BUILDING_MATERIALS_AND_FIXTURES_L4              | 2353                               |
| Xây dựng L4                                                       | HEAVY_CONSTRUCTION_L4                           | 2357                               |
| Hàng & Dịch vụ Công nghiệp L2                                     | INDUSTRIAL_GOODS_AND_SERVICES_L2                | 2700                               |
| Hàng không & Quốc phòng L3                                        | AEROSPACE_AND_DEFENSE_L3                        | 2710                               |
| Công nghiệp hàng không L4                                         | AEROSPACE_L4                                    | 2713                               |
| Quốc phòng L4                                                     | DEFENSE_L4                                      | 2717                               |
| Hàng công nghiệp L3                                               | GENERAL_INDUSTRIALS_L3                          | 2720                               |
| Containers & Đóng gói L4                                          | CONTAINERS_AND_PACKAGING_L4                     | 2723                               |
| Công nghiệp phức hợp L4                                           | DIVERSIFIED_INDUSTRIALS_L4                      | 2727                               |
| Điện tử & Thiết bị điện L3                                        | ELECTRONIC_AND_ELECTRICAL_EQUIPMENT_L3          | 2730                               |
| Hàng điện & điện tử L4                                            | ELECTRICAL_COMPONENTS_AND_EQUIPMENT_L4          | 2733                               |
| Thiết bị điện L4                                                  | ELECTRONIC_EQUIPMENT_L4                         | 2737                               |
| Công nghiệp nặng L3                                               | INDUSTRIAL_ENGINEERING_L3                       | 2750                               |
| Xe tải & Đóng tàu L4                                              | COMMERCIAL_VEHICLES_AND_TRUCKS_L4               | 2753                               |
| Máy công nghiệp L4                                                | INDUSTRIAL_MACHINERY_L4                         | 2757                               |
| Vận tải L3                                                        | INDUSTRIAL_TRANSPORTATION_L3                    | 2770                               |
| Chuyển phát nhanh L4                                              | DELIVERY_SERVICES_L4                            | 2771                               |
| Vận tải Thủy L4                                                   | MARINE_TRANSPORTATION_L4                        | 2773                               |
| Đường sắt L4                                                      | RAILROADS_L4                                    | 2775                               |
| Kho bãi, hậu cần và bảo dưỡng L4                                  | TRANSPORTATION_SERVICES_L4                      | 2777                               |
| Dịch vụ vận tải L4                                                | TRUCKING_L4                                     | 2779                               |
| Tư vấn & Hỗ trợ Kinh doanh L3                                     | SUPPORT_SERVICES_L3                             | 2790                               |
| Tư vấn & Hỗ trợ KD L4                                             | BUSINESS_SUPPORT_SERVICES_L4                    | 2791                               |
| Đào tạo & Việc làm L4                                             | BUSINESS_TRAINING_AND_EMPLOYMENT_AGENCIES_L4    | 2793                               |
| Quản lý Tài chính L4                                              | FINANCIAL_ADMINISTRATION_L4                     | 2795                               |
| Nhà cung cấp thiết bị L4                                          | INDUSTRIAL_SUPPLIERS_L4                         | 2797                               |
| Chất thải & Môi trường L4                                         | WASTE_AND_DISPOSAL_SERVICES_L4                  | 2799                               |
| Hàng Tiêu dùng L1                                                 | CONSUMER_GOODS_L1                               | 3000                               |
| Ô tô và phụ tùng L2                                               | AUTOMOBILES_AND_PARTS_L2                        | 3300                               |
| Ô tô và phụ tùng L3                                               | AUTOMOBILES_AND_PARTS_L3                        | 3350                               |
| Sản xuất ô tô L4                                                  | AUTOMOBILES_L4                                  | 3353                               |
| Phụ tùng ô tô L4                                                  | AUTO_PARTS_L4                                   | 3355                               |
| Lốp xe L4                                                         | TIRES_L4                                        | 3357                               |
| Thực phẩm và đồ uống L2                                           | FOOD_AND_BEVERAGE_L2                            | 3500                               |
| Bia và đồ uống L3                                                 | BEVERAGES_L3                                    | 3530                               |
| Sản xuất bia L4                                                   | BREWERS_L4                                      | 3533                               |
| Vang & Rượu mạnh L4                                               | DISTILLERS_AND_VINTNERS_L4                      | 3535                               |
| Đồ uống & giải khát L4                                            | SOFT_DRINKS_L4                                  | 3537                               |
| Sản xuất thực phẩm L3                                             | FOOD_PRODUCERS_L3                               | 3570                               |
| Nuôi trồng nông & hải sản L4                                      | FARMING_AND_FISHING_L4                          | 3573                               |
| Thực phẩm L4                                                      | FOOD_PRODUCTS_L4                                | 3577                               |
| Hàng cá nhân & Gia dụng L2                                        | PERSONAL_AND_HOUSEHOLD_GOODS_L2                 | 3700                               |
| Hàng gia dụng L3                                                  | HOUSEHOLD_GOODS_AND_HOME_CONSTRUCTION_L3        | 3720                               |
| Đồ gia dụng lâu bền L4                                            | DURABLE_HOUSEHOLD_PRODUCTS_L4                   | 3722                               |
| Đồ gia dụng một lần L4                                            | NONDURABLE_HOUSEHOLD_PRODUCTS_L4                | 3724                               |
| Thiết bị gia dụng L4                                              | FURNISHINGS_L4                                  | 3726                               |
| Xây nhà L4                                                        | HOME_CONSTRUCTION_L4                            | 3728                               |
| Hàng hóa giải trí L3                                              | LEISURE_GOODS_L3                                | 3740                               |
| Điện tử tiêu dùng L4                                              | CONSUMER_ELECTRONICS_L4                         | 3743                               |
| Sản phẩm nghệ thuật L4                                            | RECREATIONAL_PRODUCTS_L4                        | 3745                               |
| Đồ chơi L4                                                        | TOYS_L4                                         | 3747                               |
| Hàng cá nhân L3                                                   | PERSONAL_GOODS_L3                               | 3760                               |
| Hàng May mặc L4                                                   | CLOTHING_AND_ACCESSORIES_L4                     | 3763                               |
| Giầy dép L4                                                       | FOOTWEAR_L4                                     | 3765                               |
| Hàng cá nhân L4                                                   | PERSONAL_PRODUCTS_L4                            | 3767                               |
| Thuốc lá L3                                                       | TOBACCO_L3                                      | 3780                               |
| Thuốc lá L4                                                       | TOBACCO_L4                                      | 3785                               |
| Dược phẩm và Y tế L1                                              | HEALTH_CARE_L1                                  | 4000                               |
| Y tế L2                                                           | HEALTH_CARE_L2                                  | 4500                               |
| Thiết bị và Dịch vụ Y tế L3                                       | HEALTH_CARE_EQUIPMENT_AND_SERVICES_L3           | 4530                               |
| Chăm sóc y tế L4                                                  | HEALTH_CARE_PROVIDERS_L4                        | 4533                               |
| Thiết bị y tế L4                                                  | MEDICAL_EQUIPMENT_L4                            | 4535                               |
| Dụng cụ y tế L4                                                   | MEDICAL_SUPPLIES_L4                             | 4537                               |
| Dược phẩm L3                                                      | PHARMACEUTICALS_AND_BIOTECHNOLOGY_L3            | 4570                               |
| Công nghệ sinh học L4                                             | BIOTECHNOLOGY_L4                                | 4573                               |
| Dược phẩm L4                                                      | PHARMACEUTICALS_L4                              | 4577                               |
| Dịch vụ Tiêu dùng L1                                              | CONSUMER_SERVICES_L1                            | 5000                               |
| Bán lẻ L2                                                         | RETAIL_L2                                       | 5300                               |
| Phân phối thực phẩm & dược phẩm L3                                | FOOD_AND_DRUG_RETAILERS_L3                      | 5330                               |
| Phân phối dược phẩm L4                                            | DRUG_RETAILERS_L4                               | 5333                               |
| Phân phối thực phẩm L4                                            | FOOD_RETAILERS_AND_WHOLESALERS_L4               | 5337                               |
| Bán lẻ L3                                                         | GENERAL_RETAILERS_L3                            | 5370                               |
| Bán lẻ hàng may mặc L4                                            | APPAREL_RETAILERS_L4                            | 5371                               |
| Bán lẻ phức hợp L4                                                | BROADLINE_RETAILERS_L4                          | 5373                               |
| Phân phối nội thất L4                                             | HOME_IMPROVEMENT_RETAILERS_L4                   | 5375                               |
| Dịch vụ tiêu dùng chuyên ngành L4                                 | SPECIALIZED_CONSUMER_SERVICES_L4                | 5377                               |
| Phân phối hàng chuyên dụng L4                                     | SPECIALTY_RETAILERS_L4                          | 5379                               |
| Truyền thông L2                                                   | MEDIA_L2                                        | 5500                               |
| Truyền thông L3                                                   | MEDIA_L3                                        | 5550                               |
| Giải trí & Truyền thông L4                                        | BROADCASTING_AND_ENTERTAINMENT_L4               | 5553                               |
| Dịch vụ truyền thông L4                                           | MEDIA_AGENCIES_L4                               | 5555                               |
| Sách, ấn bản & sản phẩm văn hóa L4                                | PUBLISHING_L4                                   | 5557                               |
| Du lịch và Giải trí L2                                            | TRAVEL_AND_LEISURE_L2                           | 5700                               |
| Du lịch & Giải trí L3                                             | TRAVEL_AND_LEISURE_L3                           | 5750                               |
| Dịch vụ hàng không L4                                             | AIRLINES_L4                                     | 5751                               |
| Gambling L4                                                       | GAMBLING_L4                                     | 5752                               |
| Khách sạn L4                                                      | HOTELS_L4                                       | 5753                               |
| Dịch vụ giải trí L4                                               | RECREATIONAL_SERVICES_L4                        | 5755                               |
| Nhà hàng và quán bar L4                                           | RESTAURANTS_AND_BARS_L4                         | 5757                               |
| Vận tải hành khách & Du lịch L4                                   | TRAVEL_AND_TOURISM_L4                           | 5759                               |
| Viễn thông L1                                                     | TELECOMMUNICATIONS_L1                           | 6000                               |
| Viễn thông L2                                                     | TELECOMMUNICATIONS_L2                           | 6500                               |
| Viễn thông cố định L3                                             | FIXED_LINE_TELECOMMUNICATIONS_L3                | 6530                               |
| Viễn thông cố định L4                                             | FIXED_LINE_TELECOMMUNICATIONS_L4                | 6535                               |
| Viễn thông di động L3                                             | MOBILE_TELECOMMUNICATIONS_L3                    | 6570                               |
| Viễn thông di động L4                                             | MOBILE_TELECOMMUNICATIONS_L4                    | 6575                               |
| Tiện ích Cộng đồng L1                                             | UTILITIES_L1                                    | 7000                               |
| Điện, nước & xăng dầu khí đốt L2                                  | UTILITIES_L2                                    | 7500                               |
| Sản xuất & Phân phối Điện L3                                      | ELECTRICITY_L3                                  | 7530                               |
| Sản xuất & Phân phối Điện L4                                      | CONVENTIONAL_ELECTRICITY_L4                     | 7535                               |
| Nước & Khí đốt L3                                                 | GAS_WATER_AND_MULTI-UTILITIES_L3                | 7570                               |
| Phân phối xăng dầu & khí đốt L4                                   | GAS_DISTRIBUTION_L4                             | 7573                               |
| Tiện ích khác L4                                                  | MULTIUTILITIES_L4                               | 7575                               |
| Nước L4                                                           | WATER_L4                                        | 7577                               |
| Tài chính L1                                                      | FINANCIALS_L1                                   | 8000                               |
| Ngân hàng L2                                                      | BANKS_L2                                        | 8300                               |
| Ngân hàng L1                                                      | BANKS_L1                                        | 8301                               |
| Ngân hàng L3                                                      | BANKS_L3                                        | 8350                               |
| Ngân hàng L4                                                      | BANKS_L4                                        | 8355                               |
| Bảo hiểm L2                                                       | INSURANCE_L2                                    | 8500                               |
| Bảo hiểm phi nhân thọ L3                                          | NONLIFE_INSURANCE_L3                            | 8530                               |
| Bảo hiểm phức hợp L4                                              | FULL_LINE_INSURANCE_L4                          | 8532                               |
| Môi giới bảo hiểm L4                                              | INSURANCE_BROKERS_L4                            | 8534                               |
| Bảo hiểm phi nhân thọ L4                                          | PROPERTY_AND_CASUALTY_INSURANCE_L4              | 8536                               |
| Tái bảo hiểm L4                                                   | REINSURANCE_L4                                  | 8538                               |
| Bảo hiểm nhân thọ L3                                              | LIFE_INSURANCE_L3                               | 8570                               |
| Bảo hiểm nhân thọ L4                                              | LIFE_INSURANCE_L4                               | 8575                               |
| Bất động sản L2                                                   | REAL_ESTATE_L2                                  | 8600                               |
| Bất động sản L3                                                   | REAL_ESTATE_INVESTMENT_AND_SERVICES_L3          | 8630                               |
| Bất động sản L4                                                   | REAL_ESTATE_HOLDING_AND_DEVELOPMENT_L4          | 8633                               |
| Tư Vấn, Định giá, Môi giới Bất động sản L4                        | REAL_ESTATE_SERVICES_L4                         | 8637                               |
| Quỹ ủy thác BĐS L3                                                | REAL_ESTATE_INVESTMENT_TRUSTS_L3                | 8670                               |
| Quỹ ủy thác BĐS L4                                                | REAL_ESTATE_INVESTMENT_TRUSTS_L4                | 8677                               |
| Dịch vụ tài chính L2                                              | FINANCIAL_SERVICES_L2                           | 8700                               |
| Dịch vụ tài chính L3                                              | FINANCIAL_SERVICES_L3                           | 8770                               |
| Quản lý tài sản L4                                                | ASSET_MANAGERS_L4                               | 8771                               |
| Tài chính cá nhân L4                                              | CONSUMER_FINANCE_L4                             | 8773                               |
| Tài chính đặc biệt L4                                             | SPECIALTY_FINANCE_L4                            | 8775                               |
| Môi giới chứng khoán L4                                           | INVESTMENT_SERVICES_L4                          | 8777                               |
| Cầm cố L4                                                         | MORTGAGE_FINANCE_L4                             | 8779                               |
| Quỹ đầu tư L3                                                     | EQUITY_INVESTMENT_INSTRUMENTS_L3                | 8980                               |
| Quỹ đầu tư L4                                                     | EQUITY_INVESTMENT_INSTRUMENTS_L4                | 8985                               |
| Công nghệ Thông tin L1                                            | TECHNOLOGY_L1                                   | 9000                               |
| Công nghệ Thông tin L2                                            | TECHNOLOGY_L2                                   | 9500                               |
| Phần mềm & Dịch vụ Máy tính L3                                    | SOFTWARE_AND_COMPUTER_SERVICES_L3               | 9530                               |
| Dịch vụ Máy tính L4                                               | COMPUTER_SERVICES_L4                            | 9533                               |
| Internet L4                                                       | INTERNET_L4                                     | 9535                               |
| Phần mềm L4                                                       | SOFTWARE_L4                                     | 9537                               |
| Thiết bị và Phần cứng L3                                          | TECHNOLOGY_HARDWARE_AND_EQUIPMENT_L3            | 9570                               |
| Phần cứng L4                                                      | COMPUTER_HARDWARE_L4                            | 9572                               |
| Thiết bị văn phòng L4                                             | ELECTRONIC_OFFICE_EQUIPMENT_L4                  | 9574                               |
| Bán dẫn L4                                                        | SEMICONDUCTORS_L4                               | 9576                               |
| Thiết bị viễn thông L4                                            | TELECOMMUNICATIONS_EQUIPMENT_L4                 | 9578                               |
| N/A L4 L4                                                         | N/A_L4_L4                                       | OTHER                              |
| Sản xuất và Khai thác dầu khí L5                                  | EXPLORATION_AND_PRODUCTION_L5                   | 05331                              |
| Tổ hợp Dầu khí L5                                                 | INTEGRATED_OIL_AND_GAS_L5                       | 05371                              |
| Thiết bị và Dịch vụ Dầu khí L5                                    | OIL_EQUIPMENT_AND_SERVICES_L5                   | 05731                              |
| Ống dẫn Dầu L5                                                    | PIPELINES_L5                                    | 05771                              |
| Năng lượng thay thế L3                                            | ALTERNATIVE_FUELS_L3                            | 0580                               |
| Thiết bị năng lượng tái chế L4                                    | RENEWABLE_ENERGY_EQUIPMENT_L4                   | 0583                               |
| Thiết bị năng lượng tái chế L5                                    | RENEWABLE_ENERGY_EQUIPMENT_L5                   | 05831                              |
| Nhiên liệu thay thế L4                                            | ALTERNATIVE_FUELS_L4                            | 0587                               |
| Nhiên liệu thay thế L5                                            | ALTERNATIVE_FUELS_L5                            | 05871                              |
| Nhựa L5                                                           | PLASTICS_L5                                     | 13531                              |
| Cao su L5                                                         | RUBBER_L5                                       | 13532                              |
| Sợi tổng hợp L5                                                   | SYNTHETIC_FIBERS_L5                             | 13533                              |
| Hóa chất cơ bản bán buôn L5                                       | COMMODITY_CHEMICALS_WHOLESALE_L5                | 13534                              |
| Hóa chất hàng hóa khác L5                                         | OTHER_COMMODITY_CHEMICALS_L5                    | 13571                              |
| Phân bón L5                                                       | FERTILIZER_L5                                   | 13572                              |
| Thuốc trừ sâu L5                                                  | PESTICIDE_L5                                    | 13573                              |
| Hóa chất nông nghiệp Bán buôn L5                                  | AGRICULTURAL_CHEMICALS_WHOLESALE_L5             | 13574                              |
| Lâm sản và Chế biến gỗ L5                                         | FORESTRY_L5                                     | 17331                              |
| Sản xuất giấy L5                                                  | PAPER_L5                                        | 17371                              |
| Nhôm L5                                                           | ALUMINUM_L5                                     | 17531                              |
| Kim Loại màu L5                                                   | NONFERROUS_METALS_L5                            | 17551                              |
| Sản xuất, chế biến thép L5                                        | PRODUCERS_L5                                    | 17571                              |
| Thương mại (Bán buôn) sắt thép L5                                 | METAL_MERCHANT_WHOLESALERS_L5                   | 17572                              |
| Khai thác Than L5                                                 | COAL_L5                                         | 17711                              |
| Đá quý và Kim cương L5                                            | DIAMONDS_AND_GEMSTONES_L5                       | 17731                              |
| Khai khoáng L5                                                    | GENERAL_MINING_L5                               | 17751                              |
| Khai thác vàng L5                                                 | GOLD_MINING_L5                                  | 17771                              |
| Bạch kim & Kim loại quý khác L5                                   | PLATINUM_AND_PRECIOUS_METALS_L5                 | 17791                              |
| Vật liệu xây dựng khác L5                                         | OTHER_CONSTRUCTION_MATERIALS_L5                 | 23531                              |
| Xi măng L5                                                        | CEMENT_L5                                       | 23532                              |
| Sản xuất bê tông L5                                               | CONCRET_MANUFACTURING_L5                        | 23533                              |
| Sản xuất gạch L5                                                  | BRICK_MANUFACTURING_L5                          | 23534                              |
| Sản xuất gạch ốp lát & Vật liệu lát L5                            | TILE_AND_PAVING_MATERIAL_MANUFACTURING_L5       | 23535                              |
| Khai thác đá L5                                                   | ROCK_MINING_L5                                  | 23536                              |
| Sơn và chất phủ L5                                                | PAINT_L5                                        | 23537                              |
| Vật liệu xây dựng bán buôn L5                                     | CONSTRUCTION_MATERIAL_WHOLESALE_L5              | 23538                              |
| Xây dựng L5                                                       | HEAVY_CONSTRUCTION_L5                           | 23571                              |
| Hàng không L5                                                     | AEROSPACE_L5                                    | 27131                              |
| Quốc phòng L5                                                     | DEFENSE_L5                                      | 27171                              |
| Thùng chứa và bao bì khác L5                                      | OTHER_CONTAINERS_AND_PACKAGING_L5               | 27231                              |
| Bao bì, đóng gói thủy tinh L5                                     | GLASS_CONTAINERS_AND_PACKAGING_L5               | 27232                              |
| Bao bì, đóng gói kim loại L5                                      | METAL_CONTAINERS_AND_PACKAGING_L5               | 27233                              |
| Bao bì, đóng gói bằng nhựa L5                                     | PLASTIC_CONTAINERS_AND_PACKAGING_L5             | 27234                              |
| Bao bì, đóng gói từ gỗ L5                                         | WOOD_CONTAINER_AND_PACKAGING_L5                 | 27235                              |
| Bao bì, đóng gói từ giấy L5                                       | PAPER_PACKAGING_L5                              | 27236                              |
| Vật liệu bao bì, đóng gói bán buôn L5                             | CONTAINER_AND_PACKAGING_MATERIAL_WHOLESALE_L5   | 27237                              |
| Công nghiệp phức hợp L5                                           | DIVERSIFIED_INDUSTRIALS_L5                      | 27271                              |
| Hàng điện & điện tử L5                                            | ELECTRICAL_COMPONENTS_AND_EQUIPMENT_L5          | 27331                              |
| Thiết bị điện L5                                                  | ELECTRONIC_EQUIPMENT_L5                         | 27371                              |
| Xe tải & Đóng tàu L5                                              | COMMERCIAL_VEHICLES_AND_TRUCKS_L5               | 27531                              |
| Máy công nghiệp L5                                                | INDUSTRIAL_MACHINERY_L5                         | 27571                              |
| Chuyển phát nhanh L5                                              | DELIVERY_SERVICES_L5                            | 27711                              |
| Vận tải nội địa L5                                                | INLAND_WATER_FREIGHT_L5                         | 27731                              |
| Vận tải quốc tế L5                                                | DEEP_SEA_FREIGHT_L5                             | 27732                              |
| Đường sắt L5                                                      | RAILROADS_L5                                    | 27751                              |
| Cảng hàng không L5                                                | AIRPORT_L5                                      | 27771                              |
| Bến xe khách L5                                                   | BUS/_CAR_STATION_L5                             | 27772                              |
| Dịch vụ Sân bay L5                                                | AIRPORT_SERVICES_L5                             | 27773                              |
| Dịch vụ cảng biển, cảng sông L5                                   | MARINE_PORT_SERVICES_L5                         | 27774                              |
| Dịch vụ kho bãi L5                                                | LOGISTICS_L5                                    | 27775                              |
| Hỗ trợ vận tải L5                                                 | SUPPORT_ACTIVITIES_FOR_TRANSPORTATION_L5        | 27776                              |
| Vận tải hàng lạnh L5                                              | COLD_TRUCKING_L5                                | 27791                              |
| Vận tải hàng khô L5                                               | DRY_TRUCKING_L5                                 | 27792                              |
| Tư vấn & Hỗ trợ KD L5                                             | BUSINESS_SUPPORT_SERVICES_L5                    | 27911                              |
| Đào tạo & Việc làm L5                                             | BUSINESS_TRAINING_AND_EMPLOYMENT_AGENCIES_L5    | 27933                              |
| Quản lý Tài chính L5                                              | FINANCIAL_ADMINISTRATION_L5                     | 27951                              |
| Nhà cung cấp thiết bị L5                                          | INDUSTRIAL_SUPPLIERS_L5                         | 27971                              |
| Chất thải & Môi trường L5                                         | WASTE_AND_DISPOSAL_SERVICES_L5                  | 27991                              |
| Sản xuất ô tô L5                                                  | AUTOMOBILES_L5                                  | 33531                              |
| Phụ tùng ô tô L5                                                  | AUTO_PARTS_L5                                   | 33551                              |
| Lốp xe L5                                                         | TIRES_L5                                        | 33571                              |
| Sản xuất bia L5                                                   | BREWERS_L5                                      | 35331                              |
| Vang & Rượu mạnh L5                                               | DISTILLERS_AND_VINTNERS_L5                      | 35351                              |
| Đồ uống không cồn khác L5                                         | OTHER_NON-ALCOHOLIC_BEVERAGES_L5                | 35371                              |
| Trà L5                                                            | TEA_L5                                          | 35372                              |
| Cafe L5                                                           | COFFEE_L5                                       | 35373                              |
| Đồ uống có ga mềm L5                                              | CARBONATED_SOFT_DRINKS_L5                       | 35374                              |
| Nước ngũ cốc (đậu nành, đậu phộng, vv) L5                         | CEREALS_JUICE_L5                                | 35375                              |
| Nước trái cây L5                                                  | FRUIT_DRINKS_L5                                 | 35376                              |
| Nước đóng chai L5                                                 | BOTTLED_WATER_AND_ICE_L5                        | 35377                              |
| Nuôi trồng thủy hải sản L5                                        | FISHING_L5                                      | 35731                              |
| Chăn nuôi gia súc, gia cầm L5                                     | PIG_BEEF_AND_VEAL_FARMING_L5                    | 35732                              |
| Trồng ngũ cốc, rau, trái cây & hạt L5                             | GRAIN_(CROP)_VEGETABLE_FRUIT_AND_NUT_FARMING_L5 | 35733                              |
| Hạt, cây giống thương mại L5                                      | COMMERCIAL_NURSERIES_L5                         | 35734                              |
| Trồng Cà phê, trà, ca cao L5                                      | COFFEE_TEA_AND_COCOA_FARMING_L5                 | 35735                              |
| Trồng mía L5                                                      | SUGARCANE_FARMING_L5                            | 35736                              |
| Thức ăn gia súc L5                                                | ANIMAL_FEED_L5                                  | 35737                              |
| Bán buôn, thu mua nông thủy sản L5                                | FISHING_AND_FARMING_WHOLESALE_L5                | 35738                              |
| Nông trại và nuôi trồng khác L5                                   | OTHER_FISHING_AND_FARMING_L5                    | 35739                              |
| Sô cô la, Bánh kẹo, bánh mỳ L5                                    | BREAD_CRACKER_OR_CHOCOLATE_CONFECTIONERY_L5     | 35771                              |
| Suất ăn công nghiệp L5                                            | READY_MADE_MEALS_L5                             | 357710                             |
| Thực phẩm khác L5                                                 | OTHER_FOOD_L5                                   | 357711                             |
| Trái cây và rau quả chế biến L5                                   | FRUIT_AND_VEGETABLE_PROCESSING_L5               | 35772                              |
| Động vật giết mổ và chế biến L5                                   | ANIMAL_SLAUGHTERING_AND_PROCESSING_L5           | 35773                              |
| Hải sản chế biến và đóng gói L5                                   | SEAFOOD_PRODUCT_PREPARATION_AND_PACKAGING_L5    | 35774                              |
| Thực phẩm chế biến L5                                             | PROCESSED_FOOD_L5                               | 35775                              |
| Sản phẩm từ sữa L5                                                | DAIRY_PRODUCTS_L5                               | 35776                              |
| Tinh bột, rau có chất béo L5                                      | STARCH_VEGETABLE_FAT_L5                         | 35777                              |
| Đường L5                                                          | SUGAR_L5                                        | 35778                              |
| Nguyên liệu chế biến, dầu ăn, gia vị (bột nở, hương liệu, etc) L5 | FOOD_INGREDIENT_SPICES_L5                       | 35779                              |
| Đồ gia dụng lâu bền L5                                            | DURABLE_HOUSEHOLD_PRODUCTS_L5                   | 37221                              |
| Đồ gia dụng một lần L5                                            | NONDURABLE_HOUSEHOLD_PRODUCTS_L5                | 37241                              |
| Thiết bị gia dụng L5                                              | FURNISHINGS_L5                                  | 37261                              |
| Xây nhà L5                                                        | HOME_CONSTRUCTION_L5                            | 37281                              |
| Điện tử tiêu dùng L5                                              | CONSUMER_ELECTRONICS_L5                         | 37431                              |
| Sản phẩm nghệ thuật L5                                            | RECREATIONAL_PRODUCTS_L5                        | 37451                              |
| Đồ chơi L5                                                        | TOYS_L5                                         | 37471                              |
| Hàng May mặc L5                                                   | CLOTHING_AND_ACCESSORIES_L5                     | 37631                              |
| Giầy dép L5                                                       | FOOTWEAR_L5                                     | 37651                              |
| Hàng cá nhân L5                                                   | PERSONAL_PRODUCTS_L5                            | 37671                              |
| Thuốc lá L5                                                       | TOBACCO_L5                                      | 37851                              |
| Chăm sóc y tế L5                                                  | HEALTH_CARE_PROVIDERS_L5                        | 45331                              |
| Thiết bị y tế L5                                                  | MEDICAL_EQUIPMENT_L5                            | 45351                              |
| Dụng cụ y tế L5                                                   | MEDICAL_SUPPLIES_L5                             | 45371                              |
| Công nghệ sinh học L5                                             | BIOTECHNOLOGY_L5                                | 45731                              |
| Dược phẩm L5                                                      | PHARMACEUTICALS_L5                              | 45771                              |
| Phân phối dược phẩm L5                                            | DRUG_RETAILERS_L5                               | 53331                              |
| Phân phối thực phẩm L5                                            | FOOD_RETAILERS_AND_WHOLESALERS_L5               | 53371                              |
| Bán lẻ hàng may mặc L5                                            | APPAREL_RETAILERS_L5                            | 53711                              |
| Siêu thị L5                                                       | SUPERMARKET_L5                                  | 53731                              |
| Cửa hàng tiện dụng L5                                             | CONVENIENCE_STORES_L5                           | 53732                              |
| Đại siêu thị L5                                                   | HYPERMARKET_L5                                  | 53733                              |
| Online L5                                                         | ONLINE_L5                                       | 53734                              |
| Các dịch vụ kinh doanh bán lẻ khác L5                             | OTHER_RETAILERS_L5                              | 53735                              |
| Phân phối nội thất L5                                             | HOME_IMPROVEMENT_RETAILERS_L5                   | 53751                              |
| Dịch vụ tiêu dùng chuyên ngành L5                                 | SPECIALIZED_CONSUMER_SERVICES_L5                | 53771                              |
| Phân phối hàng chuyên dụng L5                                     | SPECIALTY_RETAILERS_L5                          | 53791                              |
| Giải trí & Truyền thông L5                                        | BROADCASTING_AND_ENTERTAINMENT_L5               | 55531                              |
| Dịch vụ truyền thông L5                                           | MEDIA_AGENCIES_L5                               | 55551                              |
| Sách, ấn bản & sản phẩm văn hóa L5                                | PUBLISHING_L5                                   | 55571                              |
| Dịch vụ Hàng không L5                                             | AIRLINES_L5                                     | 57511                              |
| Gambling L5                                                       | GAMBLING_L5                                     | 57521                              |
| Khách sạn, resort L5                                              | HOTELS_AND_RESORTS_L5                           | 57531                              |
| Dịch vụ giải trí L5                                               | RECREATIONAL_SERVICES_L5                        | 57551                              |
| Nhà hàng và quán bar L5                                           | RESTAURANTS_AND_BARS_L5                         | 57571                              |
| Vận tải hành khách đường bộ L5                                    | ROAD_PASSENGER_TRANSPORT_L5                     | 57591                              |
| Vận tải hành khách đường thủy L5                                  | MARINE_PASSENGER_L5                             | 57592                              |
| Công ty du lịch L5                                                | TOURISM_L5                                      | 57593                              |
| Viễn thông cố định L5                                             | FIXED_LINE_TELECOMMUNICATIONS_L5                | 65351                              |
| Viễn thông di động L5                                             | MOBILE_TELECOMMUNICATIONS_L5                    | 65751                              |
| Sản xuất & Phân phối Điện L5                                      | CONVENTIONAL_ELECTRICITY_L5                     | 75351                              |
| Phân phối xăng dầu & khí đốt L5                                   | GAS_DISTRIBUTION_L5                             | 75731                              |
| Tiện ích khác L5                                                  | MULTIUTILITIES_L5                               | 75751                              |
| Nước L5                                                           | WATER_L5                                        | 75771                              |
| Ngân hàng thương mại truyền thống L5                              | TRADITIONAL_COMMERCIAL_BANKS_L5                 | 83551                              |
| Fin tech L5                                                       | FIN_TECH_L5                                     | 83552                              |
| Bảo hiểm phức hợp L5                                              | FULL_LINE_INSURANCE_L5                          | 85321                              |
| Môi giới bảo hiểm L5                                              | INSURANCE_BROKERS_L5                            | 85341                              |
| Bảo hiểm phi nhân thọ L5                                          | PROPERTY_AND_CASUALTY_INSURANCE_L5              | 85361                              |
| Tái bảo hiểm L5                                                   | REINSURANCE_L5                                  | 85381                              |
| Bảo hiểm nhân thọ L5                                              | LIFE_INSURANCE_L5                               | 85751                              |
| Phát triển & vận hành Bất động sản khác L5                        | OTHER_REAL_ESTATE_DEVELOPMENT_AND_OPERATIONS_L5 | 86331                              |
| Văn phòng cho thuê L5                                             | OFFICE_REAL_ESTATE_DEVELOPMENT_L5               | 86332                              |
| Bất động sản công nghiệp L5                                       | INDUSTRIAL_REAL_ESTATE_DEVELOPMENT_L5           | 86333                              |
| Bất động sản dân cư L5                                            | RESIDENTIAL_REAL_ESTATE_DEVELOPMENT_L5          | 86334                              |
| Dịch vụ Bất động sản khác L5                                      | OTHER_REAL_ESTATE_SERVICES_L5                   | 86371                              |
| Dịch vụ Bất động sản thương mại L5                                | OFFICE_REAL_ESTATE_SERVICES_L5                  | 86372                              |
| Dịch vụ Bất động sản bán lẻ L5                                    | RETAIL_REAL_ESTATE_SERVICES_L5                  | 86373                              |
| Dịch vụ Bất động sản Công nghiệp L5                               | INDUSTRIAL_REAL_ESTATE_SERVICES_L5              | 86374                              |
| Dịch vụ Bất động sản dân cư L5                                    | RESIDENTIAL_REAL_ESTATE_SERVICES_L5             | 86375                              |
| Quỹ ủy thác BĐS L5                                                | REAL_ESTATE_INVESTMENT_TRUSTS_L5                | 86771                              |
| Quản lý tài sản L5                                                | ASSET_MANAGERS_L5                               | 87711                              |
| Tài chính cá nhân L5                                              | CONSUMER_FINANCE_L5                             | 87731                              |
| Tài chính đặc biệt L5                                             | SPECIALTY_FINANCE_L5                            | 87751                              |
| Môi giới chứng khoán L5                                           | INVESTMENT_SERVICES_L5                          | 87771                              |
| Cầm cố L5                                                         | MORTGAGE_FINANCE_L5                             | 87791                              |
| Quỹ đầu tư L5                                                     | EQUITY_INVESTMENT_INSTRUMENTS_L5                | 89851                              |
| Dịch vụ Máy tính L5                                               | COMPUTER_SERVICES_L5                            | 95331                              |
| Internet L5                                                       | INTERNET_L5                                     | 95351                              |
| Phần mềm L5                                                       | SOFTWARE_L5                                     | 95371                              |
| Phần cứng L5                                                      | COMPUTER_HARDWARE_L5                            | 95721                              |
| Thiết bị văn phòng L5                                             | ELECTRONIC_OFFICE_EQUIPMENT_L5                  | 95741                              |
| Bán dẫn L5                                                        | SEMICONDUCTORS_L5                               | 95761                              |
| Thiết bị viễn thông L5                                            | TELECOMMUNICATIONS_EQUIPMENT_L5                 | 95781                              |
| N/A L5 L5                                                         | N/A_L5_L5                                       | OTHER5                             |
| N/A L1 L1                                                         | N/A_L1_L1                                       | OTHER1                             |
| N/A L2 L2                                                         | N/A_L2_L2                                       | OTHER2                             |
| N/A L3 L3                                                         | N/A_L3_L3                                       | OTHER3                             |