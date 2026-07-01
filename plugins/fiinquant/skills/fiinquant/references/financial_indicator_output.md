---
name: Mẫu dữ liệu chỉ số báo cáo tài chính
description: List các dictionary, trong đó mỗi dictionary sẽ tương ứng với data của 1 kỳ báo cáo, dưới đây là mô tả.
---

- Loại hình doanh nghiệp: CTCK, NH, BH, CTY
- Doanh nghiệp mẫu: HPG, SSI, VCB, BVH

# 1. Doanh nghiệp sản xuất
```json
[
    {
        "ratios": {
            "ActivityRatio": {
                "TotalAssetTurnover": 0.67360875,
                "FixedAssetTurnover": 1.99746402,
                "DaysOfSalesOutstanding": 13.60541001,
                "DaysOfInventoryOnHand": 122.5495936,
                "NumberOfDaysOfPayables": 40.08278741,
                "CashConversionCycle": 96.0722162
            },
            "LiquidityRatio": {
                "CashRatio": 0.0915603,
                "QuickRatio": 0.19322565,
                "CurrentRatio": 1.15219669
            },
            "SolvencyRatio": {
                "DebtToEquityRatio": 0.72363689,
                "LiabilitiesToEquityRatio": 0.95808709,
                "FinancialLeverageRatio": 1.95808709,
                "EBITInterestCoverage": 6.38933934
            },
            "ProfitabilityRatio": {
                "GrossProfitMargin": 0.13321475,
                "EBITMargin": 0.10525161,
                "NetProfitMargin": 0.08656522,
                "ROA": 0.05831798,
                "ROE": 0.11073185,
                "ROIC": 0.07400689
            },
            "ValuationRatios": {
                "MarketCap": 171419505360000.0,
                "BookValuePerShare": 17878.67325004,
                "BasicEPS": 1879.45178193,
                "PriceToBook": 1.49899266,
                "PriceToEarning": 14.25947729,
                "PriceToSales": 1.23452066,
                "EVtoEBITDA": 11.50865884,
                "PriceToCashFlow": -31.95073084
            },
            "Growth": {
                "NetRevenueGrowthYoY": 0.16731045,
                "EBTgrowthYoY": 0.75721531
            },
            "Revenue": 140561387448572.0,
            "AttributeToParentCompany": 12021443836074.0,
            "EBIT": 14614724419648.0
        },
        "ticker": "HPG",
        "year": 2024
    }
]
```

# 2. Ngân hàng
```json
[
    {
        "ratios": {
            "CapitalAdequacyComponent": {
                "CAR": 0.1216
            },
            "AssetQualityComponent": {
                "ProblemLoansAndLeasesCalculatedAsPercentageOfGrossLoans": 0.00963568,
                "LoanLossReservesToNPLs": 2.23310969,
                "LoanLossProvisionsCalculatedAsPercentageOfGrossLoansToCustomer": 0.02151753,
                "ProvisionChargesToLoans": 0.00177474,
                "CASARatio": 0.3497396
            },
            "EfficiencyComponent": {
                "NonInterestIncomeToNetInterestIncome": 0.23775086,
                "CostToIncomeRatio": 0.3357811
            },
            "LiquidityAndAssetsComponent": {
                "LDRPercentage": 0.80842175
            },
            "ProfitabilityComponent": {
                "NIM": 0.02860674,
                "AverageYieldOnEarningAssets": 0.04844275,
                "AverageCostOfFinancing": 0.02196457,
                "PreprovisionROA": 0.02320723,
                "PreprovisionROE": 0.25215852
            },
            "GrowthComponent": {
                "AverageLoansGrowthPercentageYoY": 0.14201639,
                "AverageDepositGrowthPercentageYoY": 0.08523855,
                "InterestincomeGrowthPercentageYoY": 0.03341086
            },
            "NetInterestIncome": 55405735000000.0,
            "AttributeToParentCompany": 33831386000000.0
        },
        "ticker": "VCB",
        "year": 2024
    }
]
```

# 3. Doanh nghiệp chứng khoán
```json
[
    {
        "ratios": {
            "ActivityRatio": {
                "TotalAssetTurnover": 0.11950069,
                "FixedAssetTurnover": 58.64222268
            },
            "LiquidityRatio": {
                "CashRatio": 1.48353629,
                "QuickRatio": 1.50071706,
                "CurrentRatio": 1.52217267
            },
            "SolvencyRatio": {
                "DebtToEquityRatio": 1.696148,
                "LiabilitiesToEquityRatio": 1.74008499,
                "FinancialLeverageRatio": 2.74008499,
                "EBITInterestCoverage": 3.28043821
            },
            "ProfitabilityRatio": {
                "GrossProfitMargin": 0.61450887,
                "EBITMargin": 0.57913078,
                "NetProfitMargin": 0.33356968,
                "ROA": 0.0397205,
                "ROE": 0.11391035,
                "ROIC": 0.05747587
            },
            "ValuationRatios": {
                "MarketCap": 61174361045700.0,
                "BookValuePerShare": 13583.44192478,
                "BasicEPS": 1443.59448452,
                "PriceToBook": 2.2932332,
                "PriceToEarning": 21.57808189,
                "PriceToSales": 7.17227762,
                "EVtoEBITDA": 21.11853306,
                "PriceToCashFlow": -239.98858965
            },
            "Growth": {
                "NetRevenueGrowthYoY": 0.19162418,
                "EBTgrowthYoY": 0.24396847
            },
            "Revenue": 8529279575474.0,
            "AttributeToParentCompany": 2835023120364.0,
            "EBIT": 4939568329540.0
        },
        "ticker": "SSI",
        "year": 2024
    }
]
```

# 4. Doanh nghiệp bảo hiểm
```json
[
    {
        "ratios": {
            "ActivityRatio": {
                "TotalAssetTurnover": 0.16858292,
                "FixedAssetTurnover": 43.51112659
            },
            "LiquidityRatio": {
                "CashRatio": 0.12547497,
                "QuickRatio": 0.40792562,
                "CurrentRatio": 2.96829948
            },
            "SolvencyRatio": {
                "DebtToEquityRatio": 0.12349318,
                "LiabilitiesToEquityRatio": 9.66313889,
                "FinancialLeverageRatio": 10.66313889
            },
            "ProfitabilityRatio": {
                "GrossProfitMargin": -0.0243354,
                "EBITMargin": -0.20190535,
                "NetProfitMargin": 0.05509778,
                "ROA": 0.00893434,
                "ROE": 0.09603442,
                "ROIC": -0.25415179
            },
            "ValuationRatios": {
                "MarketCap": 51814128927200.0,
                "BookValuePerShare": 30433.59705579,
                "BasicEPS": 2843.09875562,
                "PriceToBook": 2.29351791,
                "PriceToEarning": 24.55067727,
                "PriceToSales": 1.3011049,
                "EVtoEBITDA": -7.06284986,
                "PriceToCashFlow": -15.60598111
            },
            "Growth": {
                "NetRevenueGrowthYoY": -0.0065436,
                "EBTgrowthYoY": 0.17660793
            },
            "Revenue": 42669681559583.0,
            "AttributeToParentCompany": 2110496926600.0,
            "EBIT": -8040512078455.0
        },
        "ticker": "BVH",
        "year": 2024
    }
]
```