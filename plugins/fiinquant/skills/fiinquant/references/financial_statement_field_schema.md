---
description: "FiinQuantX BCTC Field Schema - Danh sách đầy đủ field theo companyType (auto-generated)"
tags: "schema, fields, bctc, financial-statement"
---

# 05. BCTC Field Schema Reference

> **Auto-generated** từ dữ liệu thực tế Q4/2024.
> Mã đại diện: **HPG** (MANUFACTURING), **VJC** (OTHER), **BID** (BANKING), **SSI** (SECURITIES), **BVH** (INSURANCE).
>
> **Cách dùng khi extract dữ liệu thô (không dùng `fields`):**
> Dữ liệu nằm trong `financialStatement.<stmtKey>[0].<path>` — sau normalize 2 lần thì path trở thành tên cột.
> **Khuyến nghị:** Dùng `fields=[<leafKey>]` để API trả về cột phẳng mà không cần biết đường dẫn đầy đủ.

---

## Quick Reference — `fields=` Hay Dùng Nhất

| Chỉ tiêu | `fields=` value | companyType hỗ trợ |
|---|---|---|
| Lợi nhuận sau thuế | `netProfitAfterTax` | ALL |
| Tổng tài sản | `totalAssets` | ALL |
| Vốn chủ sở hữu | `totalEquity` | ALL |
| Tổng nợ | `totalLiabilities` | ALL |
| Doanh thu thuần | `netRevenue` | MANUFACTURING, OTHER |
| Thu nhập lãi thuần | `netInterestIncome` | BANKING |
| Tổng DT hoạt động | `totalOperatingRevenue` | SECURITIES |
| DT thuần HĐBH | `netRevenueFromInsuranceBusiness` | INSURANCE |
| LN gộp | `grossProfit` | MFG, OTHER, SECURITIES |
| LN trước thuế | `accountingProfitBeforeTax` | ALL |
| CF từ HĐKD | `netCashFromOperatingActivities` | ALL |
| CF từ HĐ đầu tư | `netCashFromInvestingActivities` | ALL |
| CF từ HĐ tài chính | `netCashFromFinancingActivities` | ALL |
| Tiền cuối kỳ | `cashAndCashEquivalentsAtTheEndOfPeriod` | ALL |
| EPS cơ bản | `epsBasic` | ALL |

---

## KQKD — Income Statement (`statement='incomestatement'`)

### MANUFACTURING — MANUFACTURING (HPG, VNM, FPT...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `accountingProfitBeforeTax` | `accountingProfitBeforeTax` | ✅ KEY |
| `costOfSales` | `costOfSales` |  |
| `earningsPerShare` | `earningsPerShare` |  |
| `earningsPerShare.epsBasic` | `epsBasic` |  |
| `earningsPerShare.epsDiluted` | `epsDiluted` |  |
| `grossProfit` | `grossProfit` | ✅ KEY |
| `netOperatingProfit` | `netOperatingProfit` |  |
| `netProfitAfterTax` | `netProfitAfterTax` | ✅ KEY |
| `operatingIncomeExpenses` | `operatingIncomeExpenses` |  |
| `operatingIncomeExpenses.financialExpenses` | `financialExpenses` |  |
| `operatingIncomeExpenses.financialExpenses.interestExpenses` | `interestExpenses` |  |
| `operatingIncomeExpenses.financialExpenses.totalFinancialExpenses` | `totalFinancialExpenses` |  |
| `operatingIncomeExpenses.financialIncome` | `financialIncome` |  |
| `operatingIncomeExpenses.generalAndAdminExpenses` | `generalAndAdminExpenses` |  |
| `operatingIncomeExpenses.sellingExpenses` | `sellingExpenses` |  |
| `operatingIncomeExpenses.shareOfProfitInAssociates` | `shareOfProfitInAssociates` |  |
| `otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `otherIncomeExpenses.netOtherIncomeExpenses` | `netOtherIncomeExpenses` |  |
| `otherIncomeExpenses.otherExpenses` | `otherExpenses` |  |
| `otherIncomeExpenses.otherIncome` | `otherIncome` |  |
| `profitAttribution` | `profitAttribution` |  |
| `profitAttribution.attributableToNonControllingInterest` | `attributableToNonControllingInterest` |  |
| `profitAttribution.attributableToParentCompany` | `attributableToParentCompany` |  |
| `revenue` | `revenue` |  |
| `revenue.deductions` | `deductions` |  |
| `revenue.grossRevenue` | `grossRevenue` |  |
| `revenue.netRevenue` | `netRevenue` | ✅ KEY |
| `taxExpenses` | `taxExpenses` |  |
| `taxExpenses.currentIncomeTaxExpense` | `currentIncomeTaxExpense` |  |
| `taxExpenses.deferredIncomeTaxExpense` | `deferredIncomeTaxExpense` |  |
| `taxExpenses.totalTaxExpenses` | `totalTaxExpenses` |  |

### OTHER — OTHER (VJC, VHM, VIC...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `accountingProfitBeforeTax` | `accountingProfitBeforeTax` | ✅ KEY |
| `costOfSales` | `costOfSales` |  |
| `earningsPerShare` | `earningsPerShare` |  |
| `earningsPerShare.epsBasic` | `epsBasic` |  |
| `earningsPerShare.epsDiluted` | `epsDiluted` |  |
| `grossProfit` | `grossProfit` | ✅ KEY |
| `netOperatingProfit` | `netOperatingProfit` |  |
| `netProfitAfterTax` | `netProfitAfterTax` | ✅ KEY |
| `operatingIncomeExpenses` | `operatingIncomeExpenses` |  |
| `operatingIncomeExpenses.financialExpenses` | `financialExpenses` |  |
| `operatingIncomeExpenses.financialExpenses.interestExpenses` | `interestExpenses` |  |
| `operatingIncomeExpenses.financialExpenses.totalFinancialExpenses` | `totalFinancialExpenses` |  |
| `operatingIncomeExpenses.financialIncome` | `financialIncome` |  |
| `operatingIncomeExpenses.generalAndAdminExpenses` | `generalAndAdminExpenses` |  |
| `operatingIncomeExpenses.sellingExpenses` | `sellingExpenses` |  |
| `operatingIncomeExpenses.shareOfProfitInAssociates` | `shareOfProfitInAssociates` |  |
| `otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `otherIncomeExpenses.netOtherIncomeExpenses` | `netOtherIncomeExpenses` |  |
| `otherIncomeExpenses.otherExpenses` | `otherExpenses` |  |
| `otherIncomeExpenses.otherIncome` | `otherIncome` |  |
| `profitAttribution` | `profitAttribution` |  |
| `profitAttribution.attributableToNonControllingInterest` | `attributableToNonControllingInterest` |  |
| `profitAttribution.attributableToParentCompany` | `attributableToParentCompany` |  |
| `revenue` | `revenue` |  |
| `revenue.deductions` | `deductions` |  |
| `revenue.grossRevenue` | `grossRevenue` |  |
| `revenue.netRevenue` | `netRevenue` | ✅ KEY |
| `taxExpenses` | `taxExpenses` |  |
| `taxExpenses.currentIncomeTaxExpense` | `currentIncomeTaxExpense` |  |
| `taxExpenses.deferredIncomeTaxExpense` | `deferredIncomeTaxExpense` |  |
| `taxExpenses.totalTaxExpenses` | `totalTaxExpenses` |  |

### BANKING — BANKING (BID, VCB, ACB...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `accountingProfitBeforeTax` | `accountingProfitBeforeTax` | ✅ KEY |
| `dividendsIncome` | `dividendsIncome` |  |
| `earningsPerShare` | `earningsPerShare` |  |
| `earningsPerShare.epsBasic` | `epsBasic` |  |
| `earningsPerShare.epsDiluted` | `epsDiluted` |  |
| `feeAndCommissionIncome` | `feeAndCommissionIncome` |  |
| `feeAndCommissionIncome.feesAndCommissionExpenses` | `feesAndCommissionExpenses` |  |
| `feeAndCommissionIncome.feesAndCommissionIncome` | `feesAndCommissionIncome` |  |
| `feeAndCommissionIncome.netFeeAndCommissionIncome` | `netFeeAndCommissionIncome` |  |
| `interestIncome` | `interestIncome` |  |
| `interestIncome.interestAndSimilarExpenses` | `interestAndSimilarExpenses` |  |
| `interestIncome.interestAndSimilarIncome` | `interestAndSimilarIncome` |  |
| `interestIncome.netInterestIncome` | `netInterestIncome` | ✅ KEY |
| `netProfitAfterTax` | `netProfitAfterTax` | ✅ KEY |
| `operatingExpenses` | `operatingExpenses` |  |
| `operatingProfitBeforeProvision` | `operatingProfitBeforeProvision` |  |
| `otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `otherIncomeExpenses.netOtherIncomeExpenses` | `netOtherIncomeExpenses` |  |
| `otherIncomeExpenses.otherExpenses` | `otherExpenses` |  |
| `otherIncomeExpenses.otherIncome` | `otherIncome` |  |
| `profitAttribution` | `profitAttribution` |  |
| `profitAttribution.attributableToParentCompany` | `attributableToParentCompany` |  |
| `profitAttribution.nonControllingInterest` | `nonControllingInterest` |  |
| `provisionForCreditLosses` | `provisionForCreditLosses` |  |
| `taxExpenses` | `taxExpenses` |  |
| `taxExpenses.currentIncomeTaxExpense` | `currentIncomeTaxExpense` |  |
| `taxExpenses.deferredIncomeTaxExpense` | `deferredIncomeTaxExpense` |  |
| `taxExpenses.totalTaxExpenses` | `totalTaxExpenses` |  |
| `totalOperatingIncome` | `totalOperatingIncome` |  |
| `tradingAndInvestmentIncome` | `tradingAndInvestmentIncome` |  |
| `tradingAndInvestmentIncome.netGainLossFromForeignCurrencyAndGold` | `netGainLossFromForeignCurrencyAndGold` |  |
| `tradingAndInvestmentIncome.netGainLossFromInvestmentSecurities` | `netGainLossFromInvestmentSecurities` |  |
| `tradingAndInvestmentIncome.netGainLossFromTradingSecurities` | `netGainLossFromTradingSecurities` |  |

### SECURITIES — SECURITIES (SSI, VND, HCM...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `comprehensiveIncome` | `comprehensiveIncome` |  |
| `comprehensiveIncome.attributableToNonControllingInterests` | `attributableToNonControllingInterests` |  |
| `comprehensiveIncome.attributableToShareholders` | `attributableToShareholders` |  |
| `comprehensiveIncome.totalComprehensiveIncome` | `totalComprehensiveIncome` |  |
| `earningsPerShare` | `earningsPerShare` |  |
| `earningsPerShare.epsBasic` | `epsBasic` |  |
| `earningsPerShare.epsDiluted` | `epsDiluted` |  |
| `earningsPerShare.netIncomeAvailableToCommonShareholders` | `netIncomeAvailableToCommonShareholders` |  |
| `financialExpenses` | `financialExpenses` |  |
| `financialExpenses.interestExpenses` | `interestExpenses` |  |
| `financialExpenses.lossFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures` | `lossFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures` |  |
| `financialExpenses.otherInvestmentExpenses` | `otherInvestmentExpenses` |  |
| `financialExpenses.provisionForInvestmentLoss` | `provisionForInvestmentLoss` |  |
| `financialExpenses.realizedAndUnrealizedLossFromChangesInForeignExchangesRates` | `realizedAndUnrealizedLossFromChangesInForeignExchangesRates` |  |
| `financialExpenses.shareOfProfitLossFromJointVentures` | `shareOfProfitLossFromJointVentures` |  |
| `financialExpenses.totalFinancialExpenses` | `totalFinancialExpenses` |  |
| `financialIncome` | `financialIncome` |  |
| `financialIncome.dividendInterestFromDemandDeposits` | `dividendInterestFromDemandDeposits` |  |
| `financialIncome.gainFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures` | `gainFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures` |  |
| `financialIncome.otherInvestmentIncome` | `otherInvestmentIncome` |  |
| `financialIncome.realizedAndUnrealizedGainFromChangesInForeignExchangesRates` | `realizedAndUnrealizedGainFromChangesInForeignExchangesRates` |  |
| `financialIncome.totalFinancialIncome` | `totalFinancialIncome` |  |
| `generalAndAdministrativeExpenses` | `generalAndAdministrativeExpenses` |  |
| `grossProfit` | `grossProfit` | ✅ KEY |
| `operatingExpenses` | `operatingExpenses` |  |
| `operatingExpenses.expensesForBrokerageServices` | `expensesForBrokerageServices` |  |
| `operatingExpenses.expensesForFinancialAdvisoryActivities` | `expensesForFinancialAdvisoryActivities` |  |
| `operatingExpenses.expensesForProprietaryTradingActivities` | `expensesForProprietaryTradingActivities` |  |
| `operatingExpenses.expensesForSecuritiesCustodianServices` | `expensesForSecuritiesCustodianServices` |  |
| `operatingExpenses.expensesForSecuritiesInvestmentAdvisoryServices` | `expensesForSecuritiesInvestmentAdvisoryServices` |  |
| `operatingExpenses.expensesForUnderwritingAndIssuanceAgencyServices` | `expensesForUnderwritingAndIssuanceAgencyServices` |  |
| `operatingExpenses.lossFromAvailableForSaleAFSFinancialAssets` | `lossFromAvailableForSaleAFSFinancialAssets` |  |
| `operatingExpenses.lossFromDerivative` | `lossFromDerivative` |  |
| `operatingExpenses.lossFromFinancialAssetsAtFVTPL` | `lossFromFinancialAssetsAtFVTPL` |  |
| `operatingExpenses.lossFromFinancialAssetsAtFVTPL.lossFromDisposalOfFinancialAssetsAtFVTPL` | `lossFromDisposalOfFinancialAssetsAtFVTPL` |  |
| `operatingExpenses.lossFromFinancialAssetsAtFVTPL.lossFromRevaluationOfFinancialAssetsAtFVTPL` | `lossFromRevaluationOfFinancialAssetsAtFVTPL` |  |
| `operatingExpenses.lossFromFinancialAssetsAtFVTPL.totalLossFromFinancialAssetsAtFVTPL` | `totalLossFromFinancialAssetsAtFVTPL` |  |
| `operatingExpenses.lossFromFinancialAssetsAtFVTPL.transactionCostOfAcquisitionOfFinancialAssetsAtFVTPL` | `transactionCostOfAcquisitionOfFinancialAssetsAtFVTPL` |  |
| `operatingExpenses.lossFromHeldToMaturityInvestments` | `lossFromHeldToMaturityInvestments` |  |
| `operatingExpenses.otherExpenses` | `otherExpenses` |  |
| `operatingExpenses.otherExpenses.totalOtherExpenses` | `totalOtherExpenses` |  |
| `operatingExpenses.provisionExpenseForInvestmentLosses` | `provisionExpenseForInvestmentLosses` |  |
| `operatingExpenses.totalOperatingExpenses` | `totalOperatingExpenses` |  |
| `operatingIncome` | `operatingIncome` |  |
| `operatingIncome.gainFromAvailableForSaleAFSFinancialAssets` | `gainFromAvailableForSaleAFSFinancialAssets` |  |
| `operatingIncome.gainFromDerivative` | `gainFromDerivative` |  |
| `operatingIncome.gainFromFinancialAssetsAtFVTPL` | `gainFromFinancialAssetsAtFVTPL` |  |
| `operatingIncome.gainFromFinancialAssetsAtFVTPL.dividendsAndInterestFromFVTPL` | `dividendsAndInterestFromFVTPL` |  |
| `operatingIncome.gainFromFinancialAssetsAtFVTPL.gainFromDisposalOfFinancialAssetsAtFVTPL` | `gainFromDisposalOfFinancialAssetsAtFVTPL` |  |
| `operatingIncome.gainFromFinancialAssetsAtFVTPL.gainFromRevaluationOfFinancialAssetsAtFVTPL` | `gainFromRevaluationOfFinancialAssetsAtFVTPL` |  |
| `operatingIncome.gainFromFinancialAssetsAtFVTPL.totalGainFromFinancialAssetsAtFVTPL` | `totalGainFromFinancialAssetsAtFVTPL` |  |
| `operatingIncome.gainFromHeldToMaturityInvestments` | `gainFromHeldToMaturityInvestments` |  |
| `operatingIncome.gainFromLoansAndReceivables` | `gainFromLoansAndReceivables` |  |
| `operatingIncome.revenueFromBrokerageServices` | `revenueFromBrokerageServices` |  |
| `operatingIncome.revenueFromFinancialAdvisoryServices` | `revenueFromFinancialAdvisoryServices` |  |
| `operatingIncome.revenueFromOtherOperatingActivities` | `revenueFromOtherOperatingActivities` |  |
| `operatingIncome.revenueFromSecuritiesCustodianServices` | `revenueFromSecuritiesCustodianServices` |  |
| `operatingIncome.revenueFromStockInvestmentAdvisoryServices` | `revenueFromStockInvestmentAdvisoryServices` |  |
| `operatingIncome.revenueFromUnderwritingServices` | `revenueFromUnderwritingServices` |  |
| `operatingIncome.totalOperatingRevenue` | `totalOperatingRevenue` | ✅ KEY |
| `operatingProfit` | `operatingProfit` |  |
| `otherComprehensiveIncomeAfterTax` | `otherComprehensiveIncomeAfterTax` |  |
| `otherComprehensiveIncomeAfterTax.gainLossDistributedFromInvestmentsInSubsidiariesAssociatesAndJointVentures` | `gainLossDistributedFromInvestmentsInSubsidiariesAssociatesAndJointVentures` |  |
| `otherComprehensiveIncomeAfterTax.gainLossFromForeignExchangeDifferenceOfOverseasOperations` | `gainLossFromForeignExchangeDifferenceOfOverseasOperations` |  |
| `otherComprehensiveIncomeAfterTax.gainLossFromRevaluationOfAvailableForSalesFinancialAssets` | `gainLossFromRevaluationOfAvailableForSalesFinancialAssets` |  |
| `otherComprehensiveIncomeAfterTax.gainLossFromRevaluationOfDerivatives` | `gainLossFromRevaluationOfDerivatives` |  |
| `otherComprehensiveIncomeAfterTax.gainLossFromRevaluationOfFixedAssetsUsingFairValueModel` | `gainLossFromRevaluationOfFixedAssetsUsingFairValueModel` |  |
| `otherComprehensiveIncomeAfterTax.gainLossFromValuationOfDerivatives` | `gainLossFromValuationOfDerivatives` |  |
| `otherComprehensiveIncomeAfterTax.preDistributedGainLossFromInvestmentsInSubsidiariesAssociatesAndJointVentures` | `preDistributedGainLossFromInvestmentsInSubsidiariesAssociatesAndJointVentures` |  |
| `otherComprehensiveIncomeAfterTax.totalOtherComprehensiveIncome` | `totalOtherComprehensiveIncome` |  |
| `otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `otherIncomeExpenses.netOtherIncomeExpenses` | `netOtherIncomeExpenses` |  |
| `otherIncomeExpenses.otherExpenses` | `otherExpenses` |  |
| `otherIncomeExpenses.otherIncome` | `otherIncome` |  |
| `profitAfterTax` | `profitAfterTax` |  |
| `profitAfterTax.netProfitAfterTax` | `netProfitAfterTax` | ✅ KEY |
| `profitAfterTax.profitAfterTaxAfterAppropriations` | `profitAfterTaxAfterAppropriations` |  |
| `profitAfterTax.profitAfterTaxAttributableToNoncontrollingInterest` | `profitAfterTaxAttributableToNoncontrollingInterest` |  |
| `profitAfterTax.profitAfterTaxAttributableToTheParentCompanyOwners` | `profitAfterTaxAttributableToTheParentCompanyOwners` |  |
| `profitBeforeTax` | `profitBeforeTax` |  |
| `profitBeforeTax.accountingProfitBeforeTax` | `accountingProfitBeforeTax` | ✅ KEY |
| `profitBeforeTax.realizedProfitBeforeTax` | `realizedProfitBeforeTax` |  |
| `profitBeforeTax.unrealizedProfitBeforeTax` | `unrealizedProfitBeforeTax` |  |
| `sellingExpenses` | `sellingExpenses` |  |
| `taxExpenses` | `taxExpenses` |  |
| `taxExpenses.currentIncomeTaxExpense` | `currentIncomeTaxExpense` |  |
| `taxExpenses.deferredIncomeTaxExpense` | `deferredIncomeTaxExpense` |  |
| `taxExpenses.totalIncomeTaxExpenses` | `totalIncomeTaxExpenses` |  |

### INSURANCE — INSURANCE (BVH, BMI, PTI...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `accountingProfitBeforeTax` | `accountingProfitBeforeTax` | ✅ KEY |
| `bankingActivities` | `bankingActivities` |  |
| `bankingActivities.expensesBanking` | `expensesBanking` |  |
| `bankingActivities.incomeBanking` | `incomeBanking` |  |
| `bankingActivities.netOperatingIncomeBanking` | `netOperatingIncomeBanking` |  |
| `catastropheReserveExpenses` | `catastropheReserveExpenses` |  |
| `changeInCatastropheReserve` | `changeInCatastropheReserve` |  |
| `changeInClaimReserve` | `changeInClaimReserve` |  |
| `changeInClaimReserve.directAndInwardReserveChange` | `directAndInwardReserveChange` |  |
| `changeInClaimReserve.outwardReserveChange` | `outwardReserveChange` |  |
| `changeInClaimReserve.totalChangeInClaimReserve` | `totalChangeInClaimReserve` |  |
| `changeInMathematicsReserves` | `changeInMathematicsReserves` |  |
| `claimAndMaturityPaymentExpenses` | `claimAndMaturityPaymentExpenses` |  |
| `claimExpensesReinsuranceAssumed` | `claimExpensesReinsuranceAssumed` |  |
| `claimExpensesRetainedRisks` | `claimExpensesRetainedRisks` |  |
| `commissionAndOtherIncome` | `commissionAndOtherIncome` |  |
| `commissionAndOtherIncome.commissionOnReinsuranceCeded` | `commissionOnReinsuranceCeded` |  |
| `commissionAndOtherIncome.otherIncome` | `otherIncome` |  |
| `commissionAndOtherIncome.otherIncome.otherActivitiesIncome` | `otherActivitiesIncome` |  |
| `commissionAndOtherIncome.otherIncome.reinsuranceAssumedIncome` | `reinsuranceAssumedIncome` |  |
| `commissionAndOtherIncome.otherIncome.reinsuranceCededIncome` | `reinsuranceCededIncome` |  |
| `commissionAndOtherIncome.otherIncome.totalOtherIncome` | `totalOtherIncome` |  |
| `commissionAndOtherIncome.totalCommissionAndOtherIncome` | `totalCommissionAndOtherIncome` |  |
| `deductions` | `deductions` |  |
| `deductions.recoveriesReinsuranceCeded` | `recoveriesReinsuranceCeded` |  |
| `deductions.salvages` | `salvages` |  |
| `deductions.subrogationRecoveries` | `subrogationRecoveries` |  |
| `deductions.totalDeductions` | `totalDeductions` |  |
| `earningsPerShare` | `earningsPerShare` |  |
| `earningsPerShare.epsBasic` | `epsBasic` |  |
| `earningsPerShare.epsDiluted` | `epsDiluted` |  |
| `equalisationReserve` | `equalisationReserve` |  |
| `financialActivities` | `financialActivities` |  |
| `financialActivities.financialExpenses` | `financialExpenses` |  |
| `financialActivities.financialIncome` | `financialIncome` |  |
| `financialActivities.profitFinancialActivities` | `profitFinancialActivities` |  |
| `gainLossJointVentures` | `gainLossJointVentures` |  |
| `generalAndAdminExpenses` | `generalAndAdminExpenses` |  |
| `generalAndAdminExpenses.bankingOperation` | `bankingOperation` |  |
| `generalAndAdminExpenses.insuranceOperation` | `insuranceOperation` |  |
| `generalAndAdminExpenses.otherOperations` | `otherOperations` |  |
| `generalAndAdminExpenses.totalGeneralAndAdmin` | `totalGeneralAndAdmin` |  |
| `grossInsuranceOperatingProfit` | `grossInsuranceOperatingProfit` |  |
| `increaseInUnearnedPremiumReserveAndTechnical` | `increaseInUnearnedPremiumReserveAndTechnical` |  |
| `insurancePremium` | `insurancePremium` |  |
| `insurancePremium.changeInUnearnedPremiumReserve` | `changeInUnearnedPremiumReserve` |  |
| `insurancePremium.directWrittenPremium` | `directWrittenPremium` |  |
| `insurancePremium.reinsurancePremiumAssumed` | `reinsurancePremiumAssumed` |  |
| `insurancePremium.totalRevenueFromInsurancePremium` | `totalRevenueFromInsurancePremium` |  |
| `netInsurancePremium` | `netInsurancePremium` |  |
| `netRevenueFromInsuranceBusiness` | `netRevenueFromInsuranceBusiness` | ✅ KEY |
| `operatingProfitFromInsuranceOperation` | `operatingProfitFromInsuranceOperation` |  |
| `operatingProfitFromInsuranceOperation.gainLossFromLifeInsurance` | `gainLossFromLifeInsurance` |  |
| `operatingProfitFromInsuranceOperation.gainLossFromNonLifeInsurance` | `gainLossFromNonLifeInsurance` |  |
| `operatingProfitFromInsuranceOperation.netOperatingProfitFromInsuranceOperation` | `netOperatingProfitFromInsuranceOperation` |  |
| `otherActivities` | `otherActivities` |  |
| `otherActivities.expensesFromOtherActivities` | `expensesFromOtherActivities` |  |
| `otherActivities.incomeFromOtherActivities` | `incomeFromOtherActivities` |  |
| `otherActivities.netOperatingIncomeOther` | `netOperatingIncomeOther` |  |
| `otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `otherIncomeExpenses.netOtherIncomeExpenses` | `netOtherIncomeExpenses` |  |
| `otherIncomeExpenses.otherExpenses` | `otherExpenses` |  |
| `otherIncomeExpenses.otherIncome` | `otherIncome` |  |
| `otherInsuranceOperatingExpenses` | `otherInsuranceOperatingExpenses` |  |
| `otherInsuranceOperatingExpenses.directInsuranceExpenses` | `directInsuranceExpenses` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses` | `otherUnderwritingExpenses` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.commissions` | `commissions` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.fullyIndemnifiedGoods` | `fullyIndemnifiedGoods` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.lossAdjustingAndRiskAssessment` | `lossAdjustingAndRiskAssessment` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.others` | `others` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.riskMinimization` | `riskMinimization` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.sellingExpenses` | `sellingExpenses` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.thirdPartyRecourse` | `thirdPartyRecourse` |  |
| `otherInsuranceOperatingExpenses.otherUnderwritingExpenses.totalOtherUnderwritingExpenses` | `totalOtherUnderwritingExpenses` |  |
| `otherInsuranceOperatingExpenses.reinsuranceAssumedExpenses` | `reinsuranceAssumedExpenses` |  |
| `otherInsuranceOperatingExpenses.reinsuranceCededExpenses` | `reinsuranceCededExpenses` |  |
| `otherInsuranceOperatingExpenses.totalOtherExpenses` | `totalOtherExpenses` |  |
| `profitAfterTax` | `profitAfterTax` |  |
| `profitAfterTax.attributableToNonControllingInterests` | `attributableToNonControllingInterests` |  |
| `profitAfterTax.attributableToParentCompany` | `attributableToParentCompany` |  |
| `profitAfterTax.netProfitAfterTax` | `netProfitAfterTax` | ✅ KEY |
| `realEstateActivities` | `realEstateActivities` |  |
| `realEstateActivities.costRealEstate` | `costRealEstate` |  |
| `realEstateActivities.realEstateInvestmentProfits` | `realEstateInvestmentProfits` |  |
| `realEstateActivities.revenueRealEstate` | `revenueRealEstate` |  |
| `recoveriesFromReinsuranceCeded` | `recoveriesFromReinsuranceCeded` |  |
| `reinsurancePremiumCeded` | `reinsurancePremiumCeded` |  |
| `reinsurancePremiumCeded.cededPremiumRefunds` | `cededPremiumRefunds` |  |
| `reinsurancePremiumCeded.changeInUnearnedCededPremiumReserve` | `changeInUnearnedCededPremiumReserve` |  |
| `reinsurancePremiumCeded.otherCededPremiumDeductions` | `otherCededPremiumDeductions` |  |
| `reinsurancePremiumCeded.reinsurancePremiumCeded` | `reinsurancePremiumCeded` |  |
| `reinsurancePremiumCeded.totalReinsurancePremiumCeded` | `totalReinsurancePremiumCeded` |  |
| `sellingExpenses` | `sellingExpenses` |  |
| `taxExpenses` | `taxExpenses` |  |
| `taxExpenses.currentIncomeTaxExpense` | `currentIncomeTaxExpense` |  |
| `taxExpenses.deferredIncomeTaxExpense` | `deferredIncomeTaxExpense` |  |
| `taxExpenses.totalTaxExpenses` | `totalTaxExpenses` |  |
| `totalDirectInsuranceExpenses` | `totalDirectInsuranceExpenses` |  |
| `totalInsuranceClaimSettlementExpenses` | `totalInsuranceClaimSettlementExpenses` |  |

---

## Cân đối Kế toán — Balance Sheet (`statement='balancesheet'`)

### MANUFACTURING — MANUFACTURING (HPG, VNM, FPT...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `assets` | `assets` |  |
| `assets.currentAssets` | `currentAssets` |  |
| `assets.currentAssets.cashAndCashEquivalents` | `cashAndCashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.cash` | `cash` |  |
| `assets.currentAssets.cashAndCashEquivalents.cashEquivalents` | `cashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.totalCashAndCashEquivalents` | `totalCashAndCashEquivalents` |  |
| `assets.currentAssets.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.allowanceForImpairment` | `allowanceForImpairment` |  |
| `assets.currentAssets.inventories.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.totalInventories` | `totalInventories` |  |
| `assets.currentAssets.otherCurrentAssets` | `otherCurrentAssets` |  |
| `assets.currentAssets.otherCurrentAssets.deductibleValueAddedTax` | `deductibleValueAddedTax` |  |
| `assets.currentAssets.otherCurrentAssets.governmentBondRepurchaseAgreement` | `governmentBondRepurchaseAgreement` |  |
| `assets.currentAssets.otherCurrentAssets.other` | `other` |  |
| `assets.currentAssets.otherCurrentAssets.prepayments` | `prepayments` |  |
| `assets.currentAssets.otherCurrentAssets.taxAndOrderReceivables` | `taxAndOrderReceivables` |  |
| `assets.currentAssets.otherCurrentAssets.totalOtherCurrentAssets` | `totalOtherCurrentAssets` |  |
| `assets.currentAssets.shortTermInvestments` | `shortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.currentAssets.shortTermInvestments.provisionForTradingSecurities` | `provisionForTradingSecurities` |  |
| `assets.currentAssets.shortTermInvestments.totalShortTermInvestments` | `totalShortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.tradingSecurities` | `tradingSecurities` |  |
| `assets.currentAssets.shortTermReceivables` | `shortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.advancesToSuppliers` | `advancesToSuppliers` |  |
| `assets.currentAssets.shortTermReceivables.allowanceForDoubtfulReceivables` | `allowanceForDoubtfulReceivables` |  |
| `assets.currentAssets.shortTermReceivables.otherReceivables` | `otherReceivables` |  |
| `assets.currentAssets.shortTermReceivables.pendingAssetsShortage` | `pendingAssetsShortage` |  |
| `assets.currentAssets.shortTermReceivables.receivablesUnderConstructionContracts` | `receivablesUnderConstructionContracts` |  |
| `assets.currentAssets.shortTermReceivables.shortTermInternalReceivables` | `shortTermInternalReceivables` |  |
| `assets.currentAssets.shortTermReceivables.shortTermLoans` | `shortTermLoans` |  |
| `assets.currentAssets.shortTermReceivables.totalShortTermReceivables` | `totalShortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.tradeReceivables` | `tradeReceivables` |  |
| `assets.currentAssets.totalCurrentAssets` | `totalCurrentAssets` | ✅ KEY |
| `assets.longTermAssets` | `longTermAssets` |  |
| `assets.longTermAssets.fixedAssets` | `fixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets` | `financeLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.totalFinanceLeaseFixedAssets` | `totalFinanceLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets` | `intangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.accumulatedAmortisation` | `accumulatedAmortisation` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.totalIntangibleFixedAssets` | `totalIntangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets` | `tangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.totalTangibleFixedAssets` | `totalTangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.totalFixedAssets` | `totalFixedAssets` |  |
| `assets.longTermAssets.investmentProperty` | `investmentProperty` |  |
| `assets.longTermAssets.investmentProperty.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.investmentProperty.cost` | `cost` |  |
| `assets.longTermAssets.investmentProperty.totalInvestmentProperty` | `totalInvestmentProperty` |  |
| `assets.longTermAssets.longTermAssetsInProgress` | `longTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.constructionInProgress` | `constructionInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.longTermWorkInProgress` | `longTermWorkInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.totalLongTermAssetsInProgress` | `totalLongTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermInvestments` | `longTermInvestments` |  |
| `assets.longTermAssets.longTermInvestments.equityInvestmentsInOthers` | `equityInvestmentsInOthers` |  |
| `assets.longTermAssets.longTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.longTermAssets.longTermInvestments.investmentsInJointVentures` | `investmentsInJointVentures` |  |
| `assets.longTermAssets.longTermInvestments.investmentsInSubsidiaries` | `investmentsInSubsidiaries` |  |
| `assets.longTermAssets.longTermInvestments.provisionForLongTermInvestments` | `provisionForLongTermInvestments` |  |
| `assets.longTermAssets.longTermInvestments.totalLongTermInvestments` | `totalLongTermInvestments` |  |
| `assets.longTermAssets.longTermReceivables` | `longTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.capitalAtAffiliatedUnits` | `capitalAtAffiliatedUnits` |  |
| `assets.longTermAssets.longTermReceivables.longTermAdvancesToSuppliers` | `longTermAdvancesToSuppliers` |  |
| `assets.longTermAssets.longTermReceivables.longTermCustomerReceivables` | `longTermCustomerReceivables` |  |
| `assets.longTermAssets.longTermReceivables.longTermIntercompanyReceivables` | `longTermIntercompanyReceivables` |  |
| `assets.longTermAssets.longTermReceivables.longTermLoanReceivables` | `longTermLoanReceivables` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables` | `otherLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.provisionForDoubtfulLongTermReceivables` | `provisionForDoubtfulLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.totalLongTermReceivables` | `totalLongTermReceivables` |  |
| `assets.longTermAssets.otherLongTermAssets` | `otherLongTermAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.deferredTaxAssets` | `deferredTaxAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.goodWill` | `goodWill` |  |
| `assets.longTermAssets.otherLongTermAssets.longTermSparePartsAndEquipment` | `longTermSparePartsAndEquipment` |  |
| `assets.longTermAssets.otherLongTermAssets.other` | `other` |  |
| `assets.longTermAssets.otherLongTermAssets.prepayments` | `prepayments` |  |
| `assets.longTermAssets.otherLongTermAssets.totalOtherLongTermAssets` | `totalOtherLongTermAssets` |  |
| `assets.longTermAssets.totalLongTermAssets` | `totalLongTermAssets` | ✅ KEY |
| `assets.totalAssets` | `totalAssets` | ✅ KEY |
| `resources` | `resources` |  |
| `resources.equity` | `equity` |  |
| `resources.equity.fundsAndOtherSources` | `fundsAndOtherSources` |  |
| `resources.equity.fundsAndOtherSources.fixedAssetFunding` | `fixedAssetFunding` |  |
| `resources.equity.fundsAndOtherSources.fundingSources` | `fundingSources` |  |
| `resources.equity.fundsAndOtherSources.totalOtherFunds` | `totalOtherFunds` |  |
| `resources.equity.ownersEquity` | `ownersEquity` |  |
| `resources.equity.ownersEquity.assetRevaluationSurplus` | `assetRevaluationSurplus` |  |
| `resources.equity.ownersEquity.constructionInvestmentCapital` | `constructionInvestmentCapital` |  |
| `resources.equity.ownersEquity.convertibleBondOptions` | `convertibleBondOptions` |  |
| `resources.equity.ownersEquity.developmentInvestmentFund` | `developmentInvestmentFund` |  |
| `resources.equity.ownersEquity.foreignExchangeDifferences` | `foreignExchangeDifferences` |  |
| `resources.equity.ownersEquity.nonControllingInterests` | `nonControllingInterests` |  |
| `resources.equity.ownersEquity.otherEquityFunds` | `otherEquityFunds` |  |
| `resources.equity.ownersEquity.otherOwnersCapital` | `otherOwnersCapital` |  |
| `resources.equity.ownersEquity.preferredShares` | `preferredShares` |  |
| `resources.equity.ownersEquity.reorganizationSupportFund` | `reorganizationSupportFund` |  |
| `resources.equity.ownersEquity.retainedEarnings` | `retainedEarnings` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsCurrent` | `retainedEarningsCurrent` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsPrevious` | `retainedEarningsPrevious` |  |
| `resources.equity.ownersEquity.retainedEarnings.totalRetainedEarnings` | `totalRetainedEarnings` |  |
| `resources.equity.ownersEquity.shareCapital` | `shareCapital` |  |
| `resources.equity.ownersEquity.sharePremium` | `sharePremium` |  |
| `resources.equity.ownersEquity.totalOwnersEquity` | `totalOwnersEquity` |  |
| `resources.equity.ownersEquity.treasuryShares` | `treasuryShares` |  |
| `resources.equity.totalEquity` | `totalEquity` | ✅ KEY |
| `resources.liabilities` | `liabilities` |  |
| `resources.liabilities.currentLiabilities` | `currentLiabilities` |  |
| `resources.liabilities.currentLiabilities.accountsPayableToSuppliers` | `accountsPayableToSuppliers` |  |
| `resources.liabilities.currentLiabilities.advancesFromCustomers` | `advancesFromCustomers` |  |
| `resources.liabilities.currentLiabilities.bonusAndWelfareFund` | `bonusAndWelfareFund` |  |
| `resources.liabilities.currentLiabilities.borrowings` | `borrowings` |  |
| `resources.liabilities.currentLiabilities.constructionContractPayablesByProgress` | `constructionContractPayablesByProgress` |  |
| `resources.liabilities.currentLiabilities.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `resources.liabilities.currentLiabilities.otherPayables` | `otherPayables` |  |
| `resources.liabilities.currentLiabilities.payableToEmployees` | `payableToEmployees` |  |
| `resources.liabilities.currentLiabilities.priceStabilizationFund` | `priceStabilizationFund` |  |
| `resources.liabilities.currentLiabilities.shortTermInternalPayables` | `shortTermInternalPayables` |  |
| `resources.liabilities.currentLiabilities.shortTermPayableExpenses` | `shortTermPayableExpenses` |  |
| `resources.liabilities.currentLiabilities.shortTermProvisionForPayables` | `shortTermProvisionForPayables` |  |
| `resources.liabilities.currentLiabilities.shortTermUnearnedRevenue` | `shortTermUnearnedRevenue` |  |
| `resources.liabilities.currentLiabilities.taxPayables` | `taxPayables` |  |
| `resources.liabilities.currentLiabilities.totalCurrentLiabilities` | `totalCurrentLiabilities` | ✅ KEY |
| `resources.liabilities.longTermLiabilities` | `longTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.borrowings` | `borrowings` |  |
| `resources.liabilities.longTermLiabilities.convertibleBonds` | `convertibleBonds` |  |
| `resources.liabilities.longTermLiabilities.deferredTaxLiabilities` | `deferredTaxLiabilities` |  |
| `resources.liabilities.longTermLiabilities.internalCapitalContributionPayables` | `internalCapitalContributionPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermAccusedExpenses` | `longTermAccusedExpenses` |  |
| `resources.liabilities.longTermLiabilities.longTermAdvancesFromCustomers` | `longTermAdvancesFromCustomers` |  |
| `resources.liabilities.longTermLiabilities.longTermInternalPayables` | `longTermInternalPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermProvisionForPayables` | `longTermProvisionForPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermTradePayables` | `longTermTradePayables` |  |
| `resources.liabilities.longTermLiabilities.longTermUnearnedRevenue` | `longTermUnearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities.otherLongTermPayables` | `otherLongTermPayables` |  |
| `resources.liabilities.longTermLiabilities.preferredShares` | `preferredShares` |  |
| `resources.liabilities.longTermLiabilities.scienceAndTechnologyDevelopmentFund` | `scienceAndTechnologyDevelopmentFund` |  |
| `resources.liabilities.longTermLiabilities.totalLongTermLiabilities` | `totalLongTermLiabilities` | ✅ KEY |
| `resources.liabilities.totalLiabilities` | `totalLiabilities` | ✅ KEY |
| `resources.totalResources` | `totalResources` |  |

### OTHER — OTHER (VJC, VHM, VIC...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `assets` | `assets` |  |
| `assets.currentAssets` | `currentAssets` |  |
| `assets.currentAssets.cashAndCashEquivalents` | `cashAndCashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.cash` | `cash` |  |
| `assets.currentAssets.cashAndCashEquivalents.cashEquivalents` | `cashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.totalCashAndCashEquivalents` | `totalCashAndCashEquivalents` |  |
| `assets.currentAssets.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.provisionForInventoryDevaluation` | `provisionForInventoryDevaluation` |  |
| `assets.currentAssets.inventories.totalInventories` | `totalInventories` |  |
| `assets.currentAssets.otherCurrentAssets` | `otherCurrentAssets` |  |
| `assets.currentAssets.otherCurrentAssets.deductibleVAT` | `deductibleVAT` |  |
| `assets.currentAssets.otherCurrentAssets.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `assets.currentAssets.otherCurrentAssets.other` | `other` |  |
| `assets.currentAssets.otherCurrentAssets.prepayments` | `prepayments` |  |
| `assets.currentAssets.otherCurrentAssets.taxReceivables` | `taxReceivables` |  |
| `assets.currentAssets.otherCurrentAssets.totalOtherCurrentAssets` | `totalOtherCurrentAssets` |  |
| `assets.currentAssets.shortTermInvestments` | `shortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.currentAssets.shortTermInvestments.provisionForDiminutionOfTradingSecurities` | `provisionForDiminutionOfTradingSecurities` |  |
| `assets.currentAssets.shortTermInvestments.totalShortTermInvestments` | `totalShortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.tradingSecurities` | `tradingSecurities` |  |
| `assets.currentAssets.shortTermReceivables` | `shortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.otherReceivables` | `otherReceivables` |  |
| `assets.currentAssets.shortTermReceivables.pendingAssetHandling` | `pendingAssetHandling` |  |
| `assets.currentAssets.shortTermReceivables.provisionForDoubtfulShortTermReceivables` | `provisionForDoubtfulShortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.shortTermAdvancesToSuppliers` | `shortTermAdvancesToSuppliers` |  |
| `assets.currentAssets.shortTermReceivables.shortTermInternalReceivables` | `shortTermInternalReceivables` |  |
| `assets.currentAssets.shortTermReceivables.shortTermLoansReceivables` | `shortTermLoansReceivables` |  |
| `assets.currentAssets.shortTermReceivables.shortTermReceivablesAccordingToConstructionProgress` | `shortTermReceivablesAccordingToConstructionProgress` |  |
| `assets.currentAssets.shortTermReceivables.shortTermReceivablesFromCustomers` | `shortTermReceivablesFromCustomers` |  |
| `assets.currentAssets.shortTermReceivables.totalShortTermReceivables` | `totalShortTermReceivables` |  |
| `assets.currentAssets.totalCurrentAssets` | `totalCurrentAssets` | ✅ KEY |
| `assets.longTermAssets` | `longTermAssets` |  |
| `assets.longTermAssets.fixedAssets` | `fixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets` | `financeLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.totalFinanceLeaseFixedAssets` | `totalFinanceLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets` | `intangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.accumulatedAmortisation` | `accumulatedAmortisation` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.totalIntangibleFixedAssets` | `totalIntangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets` | `tangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.totalTangibleFixedAssets` | `totalTangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.totalFixedAssets` | `totalFixedAssets` |  |
| `assets.longTermAssets.investmentProperty` | `investmentProperty` |  |
| `assets.longTermAssets.investmentProperty.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.investmentProperty.cost` | `cost` |  |
| `assets.longTermAssets.investmentProperty.totalInvestmentProperty` | `totalInvestmentProperty` |  |
| `assets.longTermAssets.longTermAssetsInProgress` | `longTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.longTermAssetsInProgress` | `longTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.longTermWorkInProgressCosts` | `longTermWorkInProgressCosts` |  |
| `assets.longTermAssets.longTermAssetsInProgress.totalLongTermAssetsInProgress` | `totalLongTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermInvestments` | `longTermInvestments` |  |
| `assets.longTermAssets.longTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.longTermAssets.longTermInvestments.investmentInJointVenturesAndAssociates` | `investmentInJointVenturesAndAssociates` |  |
| `assets.longTermAssets.longTermInvestments.investmentInOtherEntities` | `investmentInOtherEntities` |  |
| `assets.longTermAssets.longTermInvestments.investmentInSubsidiaries` | `investmentInSubsidiaries` |  |
| `assets.longTermAssets.longTermInvestments.provisionForLongTermFinancialInvestments` | `provisionForLongTermFinancialInvestments` |  |
| `assets.longTermAssets.longTermInvestments.totalLongTermInvestments` | `totalLongTermInvestments` |  |
| `assets.longTermAssets.longTermReceivables` | `longTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.capitalInAffiliatedUnits` | `capitalInAffiliatedUnits` |  |
| `assets.longTermAssets.longTermReceivables.internalLongTermReceivables` | `internalLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.longTermAdvancesToSuppliers` | `longTermAdvancesToSuppliers` |  |
| `assets.longTermAssets.longTermReceivables.longTermLoansReceivables` | `longTermLoansReceivables` |  |
| `assets.longTermAssets.longTermReceivables.longTermReceivablesFromCustomers` | `longTermReceivablesFromCustomers` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables` | `otherLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.provisionForDoubtfulLongTermReceivables` | `provisionForDoubtfulLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.totalLongTermReceivables` | `totalLongTermReceivables` |  |
| `assets.longTermAssets.otherLongTermAssets` | `otherLongTermAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.deferredTaxAssets` | `deferredTaxAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.goodWill` | `goodWill` |  |
| `assets.longTermAssets.otherLongTermAssets.longTermEquipmentMaterialsAndSpareParts` | `longTermEquipmentMaterialsAndSpareParts` |  |
| `assets.longTermAssets.otherLongTermAssets.other` | `other` |  |
| `assets.longTermAssets.otherLongTermAssets.prepayments` | `prepayments` |  |
| `assets.longTermAssets.otherLongTermAssets.totalOtherLongTermAssets` | `totalOtherLongTermAssets` |  |
| `assets.longTermAssets.totalLongTermAssets` | `totalLongTermAssets` | ✅ KEY |
| `assets.totalAssets` | `totalAssets` | ✅ KEY |
| `resources` | `resources` |  |
| `resources.equity` | `equity` |  |
| `resources.equity.fundsAndOtherSources` | `fundsAndOtherSources` |  |
| `resources.equity.fundsAndOtherSources.fixedAssetFunding` | `fixedAssetFunding` |  |
| `resources.equity.fundsAndOtherSources.fundingSources` | `fundingSources` |  |
| `resources.equity.fundsAndOtherSources.totalOtherFunds` | `totalOtherFunds` |  |
| `resources.equity.ownersEquity` | `ownersEquity` |  |
| `resources.equity.ownersEquity.assetRevaluationSurplus` | `assetRevaluationSurplus` |  |
| `resources.equity.ownersEquity.constructionInvestmentCapital` | `constructionInvestmentCapital` |  |
| `resources.equity.ownersEquity.convertibleBondOptions` | `convertibleBondOptions` |  |
| `resources.equity.ownersEquity.developmentInvestmentFund` | `developmentInvestmentFund` |  |
| `resources.equity.ownersEquity.foreignExchangeDifferences` | `foreignExchangeDifferences` |  |
| `resources.equity.ownersEquity.nonControllingInterests` | `nonControllingInterests` |  |
| `resources.equity.ownersEquity.otherEquityFunds` | `otherEquityFunds` |  |
| `resources.equity.ownersEquity.otherOwnersCapital` | `otherOwnersCapital` |  |
| `resources.equity.ownersEquity.reorganizationSupportFund` | `reorganizationSupportFund` |  |
| `resources.equity.ownersEquity.retainedEarnings` | `retainedEarnings` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsCurrent` | `retainedEarningsCurrent` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsPrevious` | `retainedEarningsPrevious` |  |
| `resources.equity.ownersEquity.retainedEarnings.totalRetainedEarnings` | `totalRetainedEarnings` |  |
| `resources.equity.ownersEquity.shareCapital` | `shareCapital` |  |
| `resources.equity.ownersEquity.shareCapital.commonShares` | `commonShares` |  |
| `resources.equity.ownersEquity.shareCapital.preferredShares` | `preferredShares` |  |
| `resources.equity.ownersEquity.shareCapital.totalShareCapital` | `totalShareCapital` |  |
| `resources.equity.ownersEquity.sharePremium` | `sharePremium` |  |
| `resources.equity.ownersEquity.totalOwnersEquity` | `totalOwnersEquity` |  |
| `resources.equity.ownersEquity.treasuryShares` | `treasuryShares` |  |
| `resources.equity.totalEquity` | `totalEquity` | ✅ KEY |
| `resources.liabilities` | `liabilities` |  |
| `resources.liabilities.currentLiabilities` | `currentLiabilities` |  |
| `resources.liabilities.currentLiabilities.bonusAndWelfareFund` | `bonusAndWelfareFund` |  |
| `resources.liabilities.currentLiabilities.borrowings` | `borrowings` |  |
| `resources.liabilities.currentLiabilities.constructionContractProgressPayables` | `constructionContractProgressPayables` |  |
| `resources.liabilities.currentLiabilities.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `resources.liabilities.currentLiabilities.internalPayables` | `internalPayables` |  |
| `resources.liabilities.currentLiabilities.otherShortTermPayables` | `otherShortTermPayables` |  |
| `resources.liabilities.currentLiabilities.payablesToEmployees` | `payablesToEmployees` |  |
| `resources.liabilities.currentLiabilities.priceStabilizationFund` | `priceStabilizationFund` |  |
| `resources.liabilities.currentLiabilities.provisionForShortTermLiabilities` | `provisionForShortTermLiabilities` |  |
| `resources.liabilities.currentLiabilities.shortTermAccruedExpenses` | `shortTermAccruedExpenses` |  |
| `resources.liabilities.currentLiabilities.shortTermAdvancesFromCustomers` | `shortTermAdvancesFromCustomers` |  |
| `resources.liabilities.currentLiabilities.shortTermAdvancesToSuppliers` | `shortTermAdvancesToSuppliers` |  |
| `resources.liabilities.currentLiabilities.taxesAndPayablesToState` | `taxesAndPayablesToState` |  |
| `resources.liabilities.currentLiabilities.totalCurrentLiabilities` | `totalCurrentLiabilities` | ✅ KEY |
| `resources.liabilities.currentLiabilities.unearnedRevenue` | `unearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities` | `longTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.borrowings` | `borrowings` |  |
| `resources.liabilities.longTermLiabilities.convertibleBonds` | `convertibleBonds` |  |
| `resources.liabilities.longTermLiabilities.deferredIncomeTaxPayable` | `deferredIncomeTaxPayable` |  |
| `resources.liabilities.longTermLiabilities.longTermAccruedExpenses` | `longTermAccruedExpenses` |  |
| `resources.liabilities.longTermLiabilities.longTermAdvancesFromCustomers` | `longTermAdvancesFromCustomers` |  |
| `resources.liabilities.longTermLiabilities.longTermInternalPayables` | `longTermInternalPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermTradePayables` | `longTermTradePayables` |  |
| `resources.liabilities.longTermLiabilities.longTermUnearnedRevenue` | `longTermUnearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities.otherLongTermPayables` | `otherLongTermPayables` |  |
| `resources.liabilities.longTermLiabilities.preferredShares` | `preferredShares` |  |
| `resources.liabilities.longTermLiabilities.provisionForLongTermLiabilities` | `provisionForLongTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.scienceAndTechnologyDevelopmentFund` | `scienceAndTechnologyDevelopmentFund` |  |
| `resources.liabilities.longTermLiabilities.totalLongTermLiabilities` | `totalLongTermLiabilities` | ✅ KEY |
| `resources.liabilities.totalLiabilities` | `totalLiabilities` | ✅ KEY |
| `resources.totalResources` | `totalResources` |  |

### BANKING — BANKING (BID, VCB, ACB...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `assets` | `assets` |  |
| `assets.balancesWithTheStateBankOfVietnam` | `balancesWithTheStateBankOfVietnam` |  |
| `assets.cashOnHandGoldAndGemstones` | `cashOnHandGoldAndGemstones` |  |
| `assets.debtPurchases` | `debtPurchases` |  |
| `assets.debtPurchases.allowanceForDebtPurchases` | `allowanceForDebtPurchases` |  |
| `assets.debtPurchases.debtPurchases` | `debtPurchases` |  |
| `assets.depositsWithAndLoansToOtherCreditInstitutions` | `depositsWithAndLoansToOtherCreditInstitutions` |  |
| `assets.depositsWithAndLoansToOtherCreditInstitutions.allowanceForCreditLosses` | `allowanceForCreditLosses` |  |
| `assets.depositsWithAndLoansToOtherCreditInstitutions.depositsWithOtherInstitutions` | `depositsWithOtherInstitutions` |  |
| `assets.depositsWithAndLoansToOtherCreditInstitutions.loansToOtherInstitutions` | `loansToOtherInstitutions` |  |
| `assets.depositsWithAndLoansToOtherCreditInstitutions.totalDepositsWithAndLoansToOtherCreditInstitutions` | `totalDepositsWithAndLoansToOtherCreditInstitutions` |  |
| `assets.derivativesAndOtherFinancialAssets` | `derivativesAndOtherFinancialAssets` |  |
| `assets.fixedAssets` | `fixedAssets` |  |
| `assets.fixedAssets.financeLeaseFixedAssets` | `financeLeaseFixedAssets` |  |
| `assets.fixedAssets.financeLeaseFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.fixedAssets.financeLeaseFixedAssets.cost` | `cost` |  |
| `assets.fixedAssets.financeLeaseFixedAssets.totalFinanceLeaseFixedAssets` | `totalFinanceLeaseFixedAssets` |  |
| `assets.fixedAssets.intangibleFixedAssets` | `intangibleFixedAssets` |  |
| `assets.fixedAssets.intangibleFixedAssets.accumulatedAmortisation` | `accumulatedAmortisation` |  |
| `assets.fixedAssets.intangibleFixedAssets.cost` | `cost` |  |
| `assets.fixedAssets.intangibleFixedAssets.totalIntangibleFixedAssets` | `totalIntangibleFixedAssets` |  |
| `assets.fixedAssets.tangibleFixedAssets` | `tangibleFixedAssets` |  |
| `assets.fixedAssets.tangibleFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.fixedAssets.tangibleFixedAssets.cost` | `cost` |  |
| `assets.fixedAssets.tangibleFixedAssets.totalTangibleFixedAssets` | `totalTangibleFixedAssets` |  |
| `assets.fixedAssets.totalFixedAssets` | `totalFixedAssets` |  |
| `assets.heldForTradingSecurities` | `heldForTradingSecurities` |  |
| `assets.heldForTradingSecurities.allowanceForLossesOnHeldForTradingSecurities` | `allowanceForLossesOnHeldForTradingSecurities` |  |
| `assets.heldForTradingSecurities.heldForTradingSecurities` | `heldForTradingSecurities` |  |
| `assets.heldForTradingSecurities.totalHeldForTradingSecurities` | `totalHeldForTradingSecurities` |  |
| `assets.investmentProperty` | `investmentProperty` |  |
| `assets.investmentProperty.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.investmentProperty.cost` | `cost` |  |
| `assets.investmentProperty.totalInvestmentProperty` | `totalInvestmentProperty` |  |
| `assets.investmentSecurities` | `investmentSecurities` |  |
| `assets.investmentSecurities.allowanceForLossesOnInvestmentSecurities` | `allowanceForLossesOnInvestmentSecurities` |  |
| `assets.investmentSecurities.availableForSaleSecurities` | `availableForSaleSecurities` |  |
| `assets.investmentSecurities.heldToMaturitySecurities` | `heldToMaturitySecurities` |  |
| `assets.investmentSecurities.totalInvestmentSecurities` | `totalInvestmentSecurities` |  |
| `assets.loansToCustomers` | `loansToCustomers` |  |
| `assets.loansToCustomers.allowanceForCreditLosses` | `allowanceForCreditLosses` |  |
| `assets.loansToCustomers.loansToCustomers` | `loansToCustomers` |  |
| `assets.loansToCustomers.totalLoansToCustomers` | `totalLoansToCustomers` |  |
| `assets.longTermInvestments` | `longTermInvestments` |  |
| `assets.longTermInvestments.investmentInSubsidiaries` | `investmentInSubsidiaries` |  |
| `assets.longTermInvestments.investmentsInAssociates` | `investmentsInAssociates` |  |
| `assets.longTermInvestments.investmentsInJointVenture` | `investmentsInJointVenture` |  |
| `assets.longTermInvestments.otherLongTermInvestments` | `otherLongTermInvestments` |  |
| `assets.longTermInvestments.provisionForLongTermInvestments` | `provisionForLongTermInvestments` |  |
| `assets.longTermInvestments.totalLongTermInvestments` | `totalLongTermInvestments` |  |
| `assets.otherAssets` | `otherAssets` |  |
| `assets.otherAssets.accruedInterestAndFeeReceivables` | `accruedInterestAndFeeReceivables` |  |
| `assets.otherAssets.allowanceForLosses` | `allowanceForLosses` |  |
| `assets.otherAssets.deferredTaxAssets` | `deferredTaxAssets` |  |
| `assets.otherAssets.goodwill` | `goodwill` |  |
| `assets.otherAssets.other` | `other` |  |
| `assets.otherAssets.receivables` | `receivables` |  |
| `assets.otherAssets.totalOtherAssets` | `totalOtherAssets` |  |
| `assets.totalAssets` | `totalAssets` | ✅ KEY |
| `resources` | `resources` |  |
| `resources.equity` | `equity` |  |
| `resources.equity.capital` | `capital` |  |
| `resources.equity.capital.charterCapital` | `charterCapital` |  |
| `resources.equity.capital.ownersOtherCapital` | `ownersOtherCapital` |  |
| `resources.equity.capital.preferredShares` | `preferredShares` |  |
| `resources.equity.capital.sharePremium` | `sharePremium` |  |
| `resources.equity.capital.totalCapital` | `totalCapital` |  |
| `resources.equity.capital.treasuryShares` | `treasuryShares` |  |
| `resources.equity.exchangeRateDifferences` | `exchangeRateDifferences` |  |
| `resources.equity.nonControllingInterests` | `nonControllingInterests` |  |
| `resources.equity.reserves` | `reserves` |  |
| `resources.equity.retainedProfits` | `retainedProfits` |  |
| `resources.equity.retainedProfits.totalRetainedProfits` | `totalRetainedProfits` |  |
| `resources.equity.revaluationSurplus` | `revaluationSurplus` |  |
| `resources.equity.totalEquity` | `totalEquity` | ✅ KEY |
| `resources.liabilities` | `liabilities` |  |
| `resources.liabilities.depositsAndBorrowings` | `depositsAndBorrowings` |  |
| `resources.liabilities.depositsAndBorrowings.borrowingsFromOtherInstitutions` | `borrowingsFromOtherInstitutions` |  |
| `resources.liabilities.depositsAndBorrowings.depositsAndBorrowingsFromOtherInstitutions` | `depositsAndBorrowingsFromOtherInstitutions` |  |
| `resources.liabilities.depositsAndBorrowings.depositsFromOtherInstitutions` | `depositsFromOtherInstitutions` |  |
| `resources.liabilities.depositsFromCustomers` | `depositsFromCustomers` |  |
| `resources.liabilities.derivativesAndOtherFinancialLiabilities` | `derivativesAndOtherFinancialLiabilities` |  |
| `resources.liabilities.dueToTheGovernmentAndTheStateBankOfVietnam` | `dueToTheGovernmentAndTheStateBankOfVietnam` |  |
| `resources.liabilities.fundsAndEntrustedInvestmentsReceivedFromTheGovernmentInternationalAndOtherCreditInstitutions` | `fundsAndEntrustedInvestmentsReceivedFromTheGovernmentInternationalAndOtherCreditInstitutions` |  |
| `resources.liabilities.otherLiabilities` | `otherLiabilities` |  |
| `resources.liabilities.otherLiabilities.accruedInterestPayable` | `accruedInterestPayable` |  |
| `resources.liabilities.otherLiabilities.allowanceForLosses` | `allowanceForLosses` |  |
| `resources.liabilities.otherLiabilities.other` | `other` |  |
| `resources.liabilities.otherLiabilities.taxPayables` | `taxPayables` |  |
| `resources.liabilities.otherLiabilities.totalOtherLiabilities` | `totalOtherLiabilities` |  |
| `resources.liabilities.totalLiabilities` | `totalLiabilities` | ✅ KEY |
| `resources.liabilities.valuablePapersIssued` | `valuablePapersIssued` |  |
| `resources.totalResources` | `totalResources` |  |

### SECURITIES — SECURITIES (SSI, VND, HCM...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `assets` | `assets` |  |
| `assets.currentAssets` | `currentAssets` |  |
| `assets.currentAssets.financialAssets` | `financialAssets` |  |
| `assets.currentAssets.financialAssets.advancesToSuppliers` | `advancesToSuppliers` |  |
| `assets.currentAssets.financialAssets.availableForSaleFinancialAssets` | `availableForSaleFinancialAssets` |  |
| `assets.currentAssets.financialAssets.cashAndCashEquivalents` | `cashAndCashEquivalents` |  |
| `assets.currentAssets.financialAssets.cashAndCashEquivalents.cash` | `cash` |  |
| `assets.currentAssets.financialAssets.cashAndCashEquivalents.cashEquivalents` | `cashEquivalents` |  |
| `assets.currentAssets.financialAssets.cashAndCashEquivalents.totalCashAndCashEquivalents` | `totalCashAndCashEquivalents` |  |
| `assets.currentAssets.financialAssets.financialAssetsAtFairValueThroughProfitOrLoss` | `financialAssetsAtFairValueThroughProfitOrLoss` |  |
| `assets.currentAssets.financialAssets.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.currentAssets.financialAssets.internalReceivables` | `internalReceivables` |  |
| `assets.currentAssets.financialAssets.loans` | `loans` |  |
| `assets.currentAssets.financialAssets.otherReceivables` | `otherReceivables` |  |
| `assets.currentAssets.financialAssets.provisionForImpairmentOfFinancialAssetsAndMortgageAssets` | `provisionForImpairmentOfFinancialAssetsAndMortgageAssets` |  |
| `assets.currentAssets.financialAssets.provisionForImpairmentOfReceivables` | `provisionForImpairmentOfReceivables` |  |
| `assets.currentAssets.financialAssets.receivables` | `receivables` |  |
| `assets.currentAssets.financialAssets.receivables.receivablesAndAccrualsFromDividendInterestIncome` | `receivablesAndAccrualsFromDividendInterestIncome` |  |
| `assets.currentAssets.financialAssets.receivables.receivablesAndAccrualsFromDividendInterestIncome.accrualsForUndueDividendAndInterestIncome` | `accrualsForUndueDividendAndInterestIncome` |  |
| `assets.currentAssets.financialAssets.receivables.receivablesAndAccrualsFromDividendInterestIncome.dueOrOverdueReceivablesDividendInterest` | `dueOrOverdueReceivablesDividendInterest` |  |
| `assets.currentAssets.financialAssets.receivables.receivablesAndAccrualsFromDividendInterestIncome.totalReceivablesAndAccrualsFromDividendInterestIncome` | `totalReceivablesAndAccrualsFromDividendInterestIncome` |  |
| `assets.currentAssets.financialAssets.receivables.receivablesFromDisposalOfFinancialAssets` | `receivablesFromDisposalOfFinancialAssets` |  |
| `assets.currentAssets.financialAssets.receivables.totalReceivables` | `totalReceivables` |  |
| `assets.currentAssets.financialAssets.receivablesFromSecuritiesTransactionErrors` | `receivablesFromSecuritiesTransactionErrors` |  |
| `assets.currentAssets.financialAssets.receivablesFromServicesProvidedByCompany` | `receivablesFromServicesProvidedByCompany` |  |
| `assets.currentAssets.financialAssets.totalFinancialAssets` | `totalFinancialAssets` |  |
| `assets.currentAssets.otherCurrentAssets` | `otherCurrentAssets` |  |
| `assets.currentAssets.otherCurrentAssets.advances` | `advances` |  |
| `assets.currentAssets.otherCurrentAssets.deductibleValueAddedTax` | `deductibleValueAddedTax` |  |
| `assets.currentAssets.otherCurrentAssets.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `assets.currentAssets.otherCurrentAssets.officeSuppliesToolsAndMaterials` | `officeSuppliesToolsAndMaterials` |  |
| `assets.currentAssets.otherCurrentAssets.otherCurrentAssetsDetails` | `otherCurrentAssetsDetails` |  |
| `assets.currentAssets.otherCurrentAssets.provisionForImpairmentOfOtherCurrentAssets` | `provisionForImpairmentOfOtherCurrentAssets` |  |
| `assets.currentAssets.otherCurrentAssets.shortTermDepositsCollateralsAndPledges` | `shortTermDepositsCollateralsAndPledges` |  |
| `assets.currentAssets.otherCurrentAssets.shortTermPrepaidExpenses` | `shortTermPrepaidExpenses` |  |
| `assets.currentAssets.otherCurrentAssets.taxesAndStateReceivables` | `taxesAndStateReceivables` |  |
| `assets.currentAssets.otherCurrentAssets.totalOtherCurrentAssets` | `totalOtherCurrentAssets` |  |
| `assets.currentAssets.totalCurrentAssets` | `totalCurrentAssets` | ✅ KEY |
| `assets.longTermAssets` | `longTermAssets` |  |
| `assets.longTermAssets.constructionInProgress` | `constructionInProgress` |  |
| `assets.longTermAssets.fixedAssets` | `fixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets` | `financeLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.totalFinanceLeaseFixedAssets` | `totalFinanceLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets` | `intangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.accumulatedAmortisation` | `accumulatedAmortisation` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel` | `revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.totalIntangibleFixedAssets` | `totalIntangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets` | `tangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.totalTangibleFixedAssets` | `totalTangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.totalFixedAssets` | `totalFixedAssets` |  |
| `assets.longTermAssets.investmentProperties` | `investmentProperties` |  |
| `assets.longTermAssets.investmentProperties.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.investmentProperties.cost` | `cost` |  |
| `assets.longTermAssets.investmentProperties.revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel` | `revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel` |  |
| `assets.longTermAssets.investmentProperties.totalInvestmentProperties` | `totalInvestmentProperties` |  |
| `assets.longTermAssets.longTermFinancialAssets` | `longTermFinancialAssets` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments` | `longTermInvestments` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments.investmentInJointVenturesAndAssociates` | `investmentInJointVenturesAndAssociates` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments.investmentInSubsidiaries` | `investmentInSubsidiaries` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments.otherLongTermInvestments` | `otherLongTermInvestments` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermInvestments.totalLongTermInvestments` | `totalLongTermInvestments` |  |
| `assets.longTermAssets.longTermFinancialAssets.longTermReceivables` | `longTermReceivables` |  |
| `assets.longTermAssets.longTermFinancialAssets.provisionForImpairmentOfLongTermInvestments` | `provisionForImpairmentOfLongTermInvestments` |  |
| `assets.longTermAssets.longTermFinancialAssets.totalLongTermFinancialAssets` | `totalLongTermFinancialAssets` |  |
| `assets.longTermAssets.otherLongTermAssets` | `otherLongTermAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.deferredIncomeTaxAssets` | `deferredIncomeTaxAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.goodwill` | `goodwill` |  |
| `assets.longTermAssets.otherLongTermAssets.longTermDepositsCollateralsAndPledges` | `longTermDepositsCollateralsAndPledges` |  |
| `assets.longTermAssets.otherLongTermAssets.longTermEquipmentMaterialAndSpareParts` | `longTermEquipmentMaterialAndSpareParts` |  |
| `assets.longTermAssets.otherLongTermAssets.longTermPrepaidExpenses` | `longTermPrepaidExpenses` |  |
| `assets.longTermAssets.otherLongTermAssets.otherLongTermAssetsDetails` | `otherLongTermAssetsDetails` |  |
| `assets.longTermAssets.otherLongTermAssets.paymentForSettlementAssistanceFund` | `paymentForSettlementAssistanceFund` |  |
| `assets.longTermAssets.otherLongTermAssets.totalOtherLongTermAssets` | `totalOtherLongTermAssets` |  |
| `assets.longTermAssets.provisionForImpairmentOfLongTermAssets` | `provisionForImpairmentOfLongTermAssets` |  |
| `assets.longTermAssets.totalLongTermAssets` | `totalLongTermAssets` | ✅ KEY |
| `assets.totalAssets` | `totalAssets` | ✅ KEY |
| `resources` | `resources` |  |
| `resources.equity` | `equity` |  |
| `resources.equity.ownersEquity` | `ownersEquity` |  |
| `resources.equity.ownersEquity.differencesFromRevaluationOfAssetsAtFairValue` | `differencesFromRevaluationOfAssetsAtFairValue` |  |
| `resources.equity.ownersEquity.foreignExchangeRateDifferences` | `foreignExchangeRateDifferences` |  |
| `resources.equity.ownersEquity.nonControllingInterests` | `nonControllingInterests` |  |
| `resources.equity.ownersEquity.ownerFundsReserve` | `ownerFundsReserve` |  |
| `resources.equity.ownersEquity.ownerFundsReserve.charterCapitalSupplementaryReserve` | `charterCapitalSupplementaryReserve` |  |
| `resources.equity.ownersEquity.ownerFundsReserve.otherOwnerFunds` | `otherOwnerFunds` |  |
| `resources.equity.ownersEquity.shareCapital` | `shareCapital` |  |
| `resources.equity.ownersEquity.shareCapital.capitalContribution` | `capitalContribution` |  |
| `resources.equity.ownersEquity.shareCapital.capitalContribution.ordinaryShares` | `ordinaryShares` |  |
| `resources.equity.ownersEquity.shareCapital.capitalContribution.preferredShares` | `preferredShares` |  |
| `resources.equity.ownersEquity.shareCapital.capitalContribution.totalCapitalContribution` | `totalCapitalContribution` |  |
| `resources.equity.ownersEquity.shareCapital.convertibleBondOption` | `convertibleBondOption` |  |
| `resources.equity.ownersEquity.shareCapital.otherOwnerCapital` | `otherOwnerCapital` |  |
| `resources.equity.ownersEquity.shareCapital.sharePremium` | `sharePremium` |  |
| `resources.equity.ownersEquity.shareCapital.totalShareCapital` | `totalShareCapital` |  |
| `resources.equity.ownersEquity.shareCapital.treasuryShares` | `treasuryShares` |  |
| `resources.equity.ownersEquity.totalOwnersEquity` | `totalOwnersEquity` |  |
| `resources.equity.ownersEquity.undistributedProfit` | `undistributedProfit` |  |
| `resources.equity.ownersEquity.undistributedProfit.realizedProfit` | `realizedProfit` |  |
| `resources.equity.ownersEquity.undistributedProfit.totalUndistributedProfit` | `totalUndistributedProfit` |  |
| `resources.equity.ownersEquity.undistributedProfit.unrealizedProfit` | `unrealizedProfit` |  |
| `resources.equity.totalEquity` | `totalEquity` | ✅ KEY |
| `resources.fundingSourcesAndOtherFunds` | `fundingSourcesAndOtherFunds` |  |
| `resources.liabilities` | `liabilities` |  |
| `resources.liabilities.currentLiabilities` | `currentLiabilities` |  |
| `resources.liabilities.currentLiabilities.bondsRepurchaseTransactions` | `bondsRepurchaseTransactions` |  |
| `resources.liabilities.currentLiabilities.bonusAndWelfareFund` | `bonusAndWelfareFund` |  |
| `resources.liabilities.currentLiabilities.constructionContractInProgressPayables` | `constructionContractInProgressPayables` |  |
| `resources.liabilities.currentLiabilities.convertibleBondsShortTerm` | `convertibleBondsShortTerm` |  |
| `resources.liabilities.currentLiabilities.employeeBenefits` | `employeeBenefits` |  |
| `resources.liabilities.currentLiabilities.issuedBondsShortTerm` | `issuedBondsShortTerm` |  |
| `resources.liabilities.currentLiabilities.otherShortTermPayables` | `otherShortTermPayables` |  |
| `resources.liabilities.currentLiabilities.payablesDueToFinancialAssetErrors` | `payablesDueToFinancialAssetErrors` |  |
| `resources.liabilities.currentLiabilities.payablesFromSecuritiesTransactions` | `payablesFromSecuritiesTransactions` |  |
| `resources.liabilities.currentLiabilities.payablesToEmployees` | `payablesToEmployees` |  |
| `resources.liabilities.currentLiabilities.paymentSupportFund` | `paymentSupportFund` |  |
| `resources.liabilities.currentLiabilities.provisionForShortTermLiabilities` | `provisionForShortTermLiabilities` |  |
| `resources.liabilities.currentLiabilities.shortTermAccruedExpenses` | `shortTermAccruedExpenses` |  |
| `resources.liabilities.currentLiabilities.shortTermAdvanceFromCustomers` | `shortTermAdvanceFromCustomers` |  |
| `resources.liabilities.currentLiabilities.shortTermBorrowingsAndFinancialLeases` | `shortTermBorrowingsAndFinancialLeases` |  |
| `resources.liabilities.currentLiabilities.shortTermBorrowingsAndFinancialLeases.shortTermBorrowings` | `shortTermBorrowings` |  |
| `resources.liabilities.currentLiabilities.shortTermBorrowingsAndFinancialLeases.shortTermFinanceLeaseLiabilities` | `shortTermFinanceLeaseLiabilities` |  |
| `resources.liabilities.currentLiabilities.shortTermBorrowingsAndFinancialLeases.totalShortTermBorrowingsAndFinancialLeases` | `totalShortTermBorrowingsAndFinancialLeases` |  |
| `resources.liabilities.currentLiabilities.shortTermDepositsAndCollateralReceived` | `shortTermDepositsAndCollateralReceived` |  |
| `resources.liabilities.currentLiabilities.shortTermFinanceLeasePayables` | `shortTermFinanceLeasePayables` |  |
| `resources.liabilities.currentLiabilities.shortTermInternalPayables` | `shortTermInternalPayables` |  |
| `resources.liabilities.currentLiabilities.shortTermTradePayables` | `shortTermTradePayables` |  |
| `resources.liabilities.currentLiabilities.shortTermUnearnedRevenue` | `shortTermUnearnedRevenue` |  |
| `resources.liabilities.currentLiabilities.statutoryObligation` | `statutoryObligation` |  |
| `resources.liabilities.currentLiabilities.totalCurrentLiabilities` | `totalCurrentLiabilities` | ✅ KEY |
| `resources.liabilities.longTermLiabilities` | `longTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.convertibleBonds` | `convertibleBonds` |  |
| `resources.liabilities.longTermLiabilities.deferredIncomeTaxPayable` | `deferredIncomeTaxPayable` |  |
| `resources.liabilities.longTermLiabilities.issuedBondsLongTerm` | `issuedBondsLongTerm` |  |
| `resources.liabilities.longTermLiabilities.longTermAccruedExpenses` | `longTermAccruedExpenses` |  |
| `resources.liabilities.longTermLiabilities.longTermAdvanceFromCustomers` | `longTermAdvanceFromCustomers` |  |
| `resources.liabilities.longTermLiabilities.longTermBorrowingsAndFinancialLeases` | `longTermBorrowingsAndFinancialLeases` |  |
| `resources.liabilities.longTermLiabilities.longTermBorrowingsAndFinancialLeases.longTermBorrowings` | `longTermBorrowings` |  |
| `resources.liabilities.longTermLiabilities.longTermBorrowingsAndFinancialLeases.longTermFinanceLeaseLiabilities` | `longTermFinanceLeaseLiabilities` |  |
| `resources.liabilities.longTermLiabilities.longTermBorrowingsAndFinancialLeases.totalLongTermBorrowingsAndFinancialLeases` | `totalLongTermBorrowingsAndFinancialLeases` |  |
| `resources.liabilities.longTermLiabilities.longTermCollateralsReceived` | `longTermCollateralsReceived` |  |
| `resources.liabilities.longTermLiabilities.longTermFinanceLeasePayables` | `longTermFinanceLeasePayables` |  |
| `resources.liabilities.longTermLiabilities.longTermInternalPayables` | `longTermInternalPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermTradePayables` | `longTermTradePayables` |  |
| `resources.liabilities.longTermLiabilities.longTermUnearnedRevenue` | `longTermUnearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities.otherLongTermPayables` | `otherLongTermPayables` |  |
| `resources.liabilities.longTermLiabilities.provisionForInvestorCompensation` | `provisionForInvestorCompensation` |  |
| `resources.liabilities.longTermLiabilities.provisionForLongTermLiabilities` | `provisionForLongTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.scienceAndTechnologyDevelopmentFund` | `scienceAndTechnologyDevelopmentFund` |  |
| `resources.liabilities.longTermLiabilities.totalLongTermLiabilities` | `totalLongTermLiabilities` | ✅ KEY |
| `resources.liabilities.totalLiabilities` | `totalLiabilities` | ✅ KEY |
| `resources.totalResources` | `totalResources` |  |

### INSURANCE — INSURANCE (BVH, BMI, PTI...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `assets` | `assets` |  |
| `assets.currentAssets` | `currentAssets` |  |
| `assets.currentAssets.cashAndCashEquivalents` | `cashAndCashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.cash` | `cash` |  |
| `assets.currentAssets.cashAndCashEquivalents.cashEquivalents` | `cashEquivalents` |  |
| `assets.currentAssets.cashAndCashEquivalents.totalCashAndCashEquivalents` | `totalCashAndCashEquivalents` |  |
| `assets.currentAssets.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.inventories` | `inventories` |  |
| `assets.currentAssets.inventories.provisionForInventoryDevaluation` | `provisionForInventoryDevaluation` |  |
| `assets.currentAssets.inventories.totalInventories` | `totalInventories` |  |
| `assets.currentAssets.otherCurrentAssets` | `otherCurrentAssets` |  |
| `assets.currentAssets.otherCurrentAssets.deductibleVAT` | `deductibleVAT` |  |
| `assets.currentAssets.otherCurrentAssets.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `assets.currentAssets.otherCurrentAssets.other` | `other` |  |
| `assets.currentAssets.otherCurrentAssets.prepaidExpenses` | `prepaidExpenses` |  |
| `assets.currentAssets.otherCurrentAssets.prepaidExpenses.otherPrepaidExpenses` | `otherPrepaidExpenses` |  |
| `assets.currentAssets.otherCurrentAssets.prepaidExpenses.totalPrepaidExpenses` | `totalPrepaidExpenses` |  |
| `assets.currentAssets.otherCurrentAssets.prepaidExpenses.unallocatedCommissionExpenses` | `unallocatedCommissionExpenses` |  |
| `assets.currentAssets.otherCurrentAssets.taxesAndStateReceivables` | `taxesAndStateReceivables` |  |
| `assets.currentAssets.otherCurrentAssets.totalOtherCurrentAssets` | `totalOtherCurrentAssets` |  |
| `assets.currentAssets.reinsuranceAssets` | `reinsuranceAssets` |  |
| `assets.currentAssets.reinsuranceAssets.reinsuranceCededClaimsReserve` | `reinsuranceCededClaimsReserve` |  |
| `assets.currentAssets.reinsuranceAssets.reinsuranceCededUnearnedPremiumReserve` | `reinsuranceCededUnearnedPremiumReserve` |  |
| `assets.currentAssets.reinsuranceAssets.totalReinsuranceAssets` | `totalReinsuranceAssets` |  |
| `assets.currentAssets.shortTermInvestments` | `shortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.currentAssets.shortTermInvestments.provisionForTradingSecurities` | `provisionForTradingSecurities` |  |
| `assets.currentAssets.shortTermInvestments.totalShortTermInvestments` | `totalShortTermInvestments` |  |
| `assets.currentAssets.shortTermInvestments.tradingSecurities` | `tradingSecurities` |  |
| `assets.currentAssets.shortTermReceivables` | `shortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.advancesToSuppliers` | `advancesToSuppliers` |  |
| `assets.currentAssets.shortTermReceivables.internalReceivables` | `internalReceivables` |  |
| `assets.currentAssets.shortTermReceivables.otherShortTermReceivables` | `otherShortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.provisionForDoubtfulShortTermReceivables` | `provisionForDoubtfulShortTermReceivables` |  |
| `assets.currentAssets.shortTermReceivables.receivablesFromCustomers` | `receivablesFromCustomers` |  |
| `assets.currentAssets.shortTermReceivables.receivablesFromCustomers.fromInsuranceActivities` | `fromInsuranceActivities` |  |
| `assets.currentAssets.shortTermReceivables.receivablesFromCustomers.otherReceivables` | `otherReceivables` |  |
| `assets.currentAssets.shortTermReceivables.receivablesFromCustomers.totalReceivablesFromCustomers` | `totalReceivablesFromCustomers` |  |
| `assets.currentAssets.shortTermReceivables.shortTermLoansReceivables` | `shortTermLoansReceivables` |  |
| `assets.currentAssets.shortTermReceivables.totalShortTermReceivables` | `totalShortTermReceivables` |  |
| `assets.currentAssets.totalCurrentAssets` | `totalCurrentAssets` | ✅ KEY |
| `assets.longTermAssets` | `longTermAssets` |  |
| `assets.longTermAssets.fixedAssets` | `fixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets` | `financeLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.financeLeaseFixedAssets.totalFinanceLeaseFixedAssets` | `totalFinanceLeaseFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets` | `intangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.accumulatedAmortisation` | `accumulatedAmortisation` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.intangibleFixedAssets.totalIntangibleFixedAssets` | `totalIntangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets` | `tangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.cost` | `cost` |  |
| `assets.longTermAssets.fixedAssets.tangibleFixedAssets.totalTangibleFixedAssets` | `totalTangibleFixedAssets` |  |
| `assets.longTermAssets.fixedAssets.totalFixedAssets` | `totalFixedAssets` |  |
| `assets.longTermAssets.investmentProperties` | `investmentProperties` |  |
| `assets.longTermAssets.investmentProperties.accumulatedDepreciation` | `accumulatedDepreciation` |  |
| `assets.longTermAssets.investmentProperties.cost` | `cost` |  |
| `assets.longTermAssets.investmentProperties.totalInvestmentProperties` | `totalInvestmentProperties` |  |
| `assets.longTermAssets.longTermAssetsInProgress` | `longTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.longTermAssetsInProgress` | `longTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermAssetsInProgress.longTermWorkInProgressCosts` | `longTermWorkInProgressCosts` |  |
| `assets.longTermAssets.longTermAssetsInProgress.totalLongTermAssetsInProgress` | `totalLongTermAssetsInProgress` |  |
| `assets.longTermAssets.longTermInvestments` | `longTermInvestments` |  |
| `assets.longTermAssets.longTermInvestments.heldToMaturityInvestments` | `heldToMaturityInvestments` |  |
| `assets.longTermAssets.longTermInvestments.investmentsInJointVenturesAndAssociates` | `investmentsInJointVenturesAndAssociates` |  |
| `assets.longTermAssets.longTermInvestments.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `assets.longTermAssets.longTermInvestments.investmentsInSubsidiaries` | `investmentsInSubsidiaries` |  |
| `assets.longTermAssets.longTermInvestments.provisionForLongTermFinancialInvestments` | `provisionForLongTermFinancialInvestments` |  |
| `assets.longTermAssets.longTermInvestments.totalLongTermInvestments` | `totalLongTermInvestments` |  |
| `assets.longTermAssets.longTermReceivables` | `longTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.capitalInAffiliatedUnits` | `capitalInAffiliatedUnits` |  |
| `assets.longTermAssets.longTermReceivables.internalLongTermReceivables` | `internalLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.longTermReceivablesFromCustomers` | `longTermReceivablesFromCustomers` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables` | `otherLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables.insuranceDeposits` | `insuranceDeposits` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables.otherLongTermReceivables` | `otherLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.otherLongTermReceivables.totalOtherLongTermReceivables` | `totalOtherLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.provisionForDoubtfulLongTermReceivables` | `provisionForDoubtfulLongTermReceivables` |  |
| `assets.longTermAssets.longTermReceivables.totalLongTermReceivables` | `totalLongTermReceivables` |  |
| `assets.longTermAssets.otherLongTermAssets` | `otherLongTermAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.deferredTaxAssets` | `deferredTaxAssets` |  |
| `assets.longTermAssets.otherLongTermAssets.goodwill` | `goodwill` |  |
| `assets.longTermAssets.otherLongTermAssets.other` | `other` |  |
| `assets.longTermAssets.otherLongTermAssets.prepayments` | `prepayments` |  |
| `assets.longTermAssets.otherLongTermAssets.totalOtherLongTermAssets` | `totalOtherLongTermAssets` |  |
| `assets.longTermAssets.totalLongTermAssets` | `totalLongTermAssets` | ✅ KEY |
| `assets.totalAssets` | `totalAssets` | ✅ KEY |
| `resources` | `resources` |  |
| `resources.equity` | `equity` |  |
| `resources.equity.ownersEquity` | `ownersEquity` |  |
| `resources.equity.ownersEquity.assetRevaluationSurplus` | `assetRevaluationSurplus` |  |
| `resources.equity.ownersEquity.developmentInvestmentFund` | `developmentInvestmentFund` |  |
| `resources.equity.ownersEquity.foreignExchangeDifferences` | `foreignExchangeDifferences` |  |
| `resources.equity.ownersEquity.nonControllingInterests` | `nonControllingInterests` |  |
| `resources.equity.ownersEquity.otherEquityFunds` | `otherEquityFunds` |  |
| `resources.equity.ownersEquity.otherOwnersCapital` | `otherOwnersCapital` |  |
| `resources.equity.ownersEquity.preferredShares` | `preferredShares` |  |
| `resources.equity.ownersEquity.reorganizationSupportFund` | `reorganizationSupportFund` |  |
| `resources.equity.ownersEquity.retainedEarnings` | `retainedEarnings` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsCurrent` | `retainedEarningsCurrent` |  |
| `resources.equity.ownersEquity.retainedEarnings.retainedEarningsPrevious` | `retainedEarningsPrevious` |  |
| `resources.equity.ownersEquity.retainedEarnings.totalRetainedEarnings` | `totalRetainedEarnings` |  |
| `resources.equity.ownersEquity.shareCapital` | `shareCapital` |  |
| `resources.equity.ownersEquity.shareCapital.paidInCapital` | `paidInCapital` |  |
| `resources.equity.ownersEquity.shareCapital.totalShareCapital` | `totalShareCapital` |  |
| `resources.equity.ownersEquity.sharePremium` | `sharePremium` |  |
| `resources.equity.ownersEquity.totalOwnersEquity` | `totalOwnersEquity` |  |
| `resources.equity.ownersEquity.treasuryShares` | `treasuryShares` |  |
| `resources.equity.provisionStatutory` | `provisionStatutory` |  |
| `resources.equity.totalEquity` | `totalEquity` | ✅ KEY |
| `resources.liabilities` | `liabilities` |  |
| `resources.liabilities.currentLiabilities` | `currentLiabilities` |  |
| `resources.liabilities.currentLiabilities.bonusAndWelfareFund` | `bonusAndWelfareFund` |  |
| `resources.liabilities.currentLiabilities.governmentBondRepurchaseTransactions` | `governmentBondRepurchaseTransactions` |  |
| `resources.liabilities.currentLiabilities.internalPayables` | `internalPayables` |  |
| `resources.liabilities.currentLiabilities.otherShortTermPayables` | `otherShortTermPayables` |  |
| `resources.liabilities.currentLiabilities.payablesToEmployees` | `payablesToEmployees` |  |
| `resources.liabilities.currentLiabilities.priceStabilizationFund` | `priceStabilizationFund` |  |
| `resources.liabilities.currentLiabilities.provisionForShortTermLiabilities` | `provisionForShortTermLiabilities` |  |
| `resources.liabilities.currentLiabilities.shortTermAccruedExpenses` | `shortTermAccruedExpenses` |  |
| `resources.liabilities.currentLiabilities.shortTermAdvancesFromCustomers` | `shortTermAdvancesFromCustomers` |  |
| `resources.liabilities.currentLiabilities.shortTermBorrowingsAndFinanceLeases` | `shortTermBorrowingsAndFinanceLeases` |  |
| `resources.liabilities.currentLiabilities.shortTermTradePayables` | `shortTermTradePayables` |  |
| `resources.liabilities.currentLiabilities.shortTermTradePayables.insuranceOperationPayables` | `insuranceOperationPayables` |  |
| `resources.liabilities.currentLiabilities.shortTermTradePayables.totalShortTermTradePayables` | `totalShortTermTradePayables` |  |
| `resources.liabilities.currentLiabilities.shortTermTradePayables.tradeAndServicePayables` | `tradeAndServicePayables` |  |
| `resources.liabilities.currentLiabilities.taxesAndPayablesToState` | `taxesAndPayablesToState` |  |
| `resources.liabilities.currentLiabilities.totalCurrentLiabilities` | `totalCurrentLiabilities` | ✅ KEY |
| `resources.liabilities.currentLiabilities.unearnedCommissionIncome` | `unearnedCommissionIncome` |  |
| `resources.liabilities.currentLiabilities.unearnedRevenue` | `unearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities` | `longTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.deferredIncomeTaxPayable` | `deferredIncomeTaxPayable` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision` | `insuranceBusinessProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.catastropheProvision` | `catastropheProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.claimsProvision` | `claimsProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.dividendProvision` | `dividendProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.equalizationProvision` | `equalizationProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.interestRateCommitmentProvision` | `interestRateCommitmentProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.mathematicalProvision` | `mathematicalProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.other` | `other` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.resilienceProvision` | `resilienceProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.totalInsuranceBusinessProvision` | `totalInsuranceBusinessProvision` |  |
| `resources.liabilities.longTermLiabilities.insuranceBusinessProvision.unearnedPremiumProvision` | `unearnedPremiumProvision` |  |
| `resources.liabilities.longTermLiabilities.longTermBorrowings` | `longTermBorrowings` |  |
| `resources.liabilities.longTermLiabilities.longTermDepositAndMortgage` | `longTermDepositAndMortgage` |  |
| `resources.liabilities.longTermLiabilities.longTermInternalPayables` | `longTermInternalPayables` |  |
| `resources.liabilities.longTermLiabilities.longTermTradePayables` | `longTermTradePayables` |  |
| `resources.liabilities.longTermLiabilities.longTermUnearnedRevenue` | `longTermUnearnedRevenue` |  |
| `resources.liabilities.longTermLiabilities.otherLongTermPayables` | `otherLongTermPayables` |  |
| `resources.liabilities.longTermLiabilities.provisionForLongTermLiabilities` | `provisionForLongTermLiabilities` |  |
| `resources.liabilities.longTermLiabilities.scienceAndTechnologyDevelopmentFund` | `scienceAndTechnologyDevelopmentFund` |  |
| `resources.liabilities.longTermLiabilities.totalLongTermLiabilities` | `totalLongTermLiabilities` | ✅ KEY |
| `resources.liabilities.totalLiabilities` | `totalLiabilities` | ✅ KEY |
| `resources.totalResources` | `totalResources` |  |

---

## Lưu chuyển Tiền tệ — Cash Flow (`statement='cashflow'`)

### MANUFACTURING — MANUFACTURING (HPG, VNM, DPM...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `cashAndCashEquivalentsAtTheBeginningOfPeriod` | `cashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod` | `cashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashFlowsFromFinancingActivities` | `cashFlowsFromFinancingActivities` |  |
| `cashFlowsFromFinancingActivities.dividendsPaid` | `dividendsPaid` |  |
| `cashFlowsFromFinancingActivities.financeLeasePrincipalPayments` | `financeLeasePrincipalPayments` |  |
| `cashFlowsFromFinancingActivities.netCashFromFinancingActivities` | `netCashFromFinancingActivities` | ✅ KEY |
| `cashFlowsFromFinancingActivities.paymentsForShareReturnsAndRepurchases` | `paymentsForShareReturnsAndRepurchases` |  |
| `cashFlowsFromFinancingActivities.proceedsFromIssueOfShares` | `proceedsFromIssueOfShares` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans` | `proceedsFromLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans` | `repaymentOfLoans` |  |
| `cashFlowsFromInvestingActivities` | `cashFlowsFromInvestingActivities` |  |
| `cashFlowsFromInvestingActivities.collectionOfLoansSalesOfDebtInstruments` | `collectionOfLoansSalesOfDebtInstruments` |  |
| `cashFlowsFromInvestingActivities.dividendsAndInterestReceived` | `dividendsAndInterestReceived` |  |
| `cashFlowsFromInvestingActivities.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.loansGrantedPurchasesOfDebtInstruments` | `loansGrantedPurchasesOfDebtInstruments` |  |
| `cashFlowsFromInvestingActivities.netCashFromInvestingActivities` | `netCashFromInvestingActivities` | ✅ KEY |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfFixedAssets` | `proceedsFromDisposalOfFixedAssets` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDivestmentInOtherEntities` | `proceedsFromDivestmentInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.purchasesOfFixedAndLongTermAssets` | `purchasesOfFixedAndLongTermAssets` |  |
| `cashFlowsFromOperatingActivities` | `cashFlowsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments` | `adjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.amortisationOfGoodwill` | `amortisationOfGoodwill` |  |
| `cashFlowsFromOperatingActivities.adjustments.depreciationAndAmortisation` | `depreciationAndAmortisation` |  |
| `cashFlowsFromOperatingActivities.adjustments.interestExpense` | `interestExpense` |  |
| `cashFlowsFromOperatingActivities.adjustments.otherAdjustments` | `otherAdjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.profitLossFromInvestingActivities` | `profitLossFromInvestingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments.provisions` | `provisions` |  |
| `cashFlowsFromOperatingActivities.adjustments.unrealisedForeignExchangeGainLoss` | `unrealisedForeignExchangeGainLoss` |  |
| `cashFlowsFromOperatingActivities.netCashFromOperatingActivities` | `netCashFromOperatingActivities` | ✅ KEY |
| `cashFlowsFromOperatingActivities.netProfitBeforeTax` | `netProfitBeforeTax` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges` | `operatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInInventories` | `changesInInventories` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPayables` | `changesInPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPrepaidExpenses` | `changesInPrepaidExpenses` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables` | `changesInReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInTradingSecurities` | `changesInTradingSecurities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.incomeTaxPaid` | `incomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.interestPaid` | `interestPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.netOperatingProfitBeforeChanges` | `netOperatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPaymentsOnOperatingActivities` | `otherPaymentsOnOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceiptsFromOperatingActivities` | `otherReceiptsFromOperatingActivities` |  |
| `effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `netCashFlow` | `netCashFlow` | ✅ KEY |

### OTHER — OTHER (VJC, VHM, VIC...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `cashAndCashEquivalentsAtTheBeginningOfPeriod` | `cashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod` | `cashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashFlowsFromFinancingActivities` | `cashFlowsFromFinancingActivities` |  |
| `cashFlowsFromFinancingActivities.dividendsPaid` | `dividendsPaid` |  |
| `cashFlowsFromFinancingActivities.financeLeasePrincipalPayments` | `financeLeasePrincipalPayments` |  |
| `cashFlowsFromFinancingActivities.netCashFromFinancingActivities` | `netCashFromFinancingActivities` | ✅ KEY |
| `cashFlowsFromFinancingActivities.paymentsForShareReturnsAndRepurchases` | `paymentsForShareReturnsAndRepurchases` |  |
| `cashFlowsFromFinancingActivities.proceedsFromIssueOfShares` | `proceedsFromIssueOfShares` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans` | `proceedsFromLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans` | `repaymentOfLoans` |  |
| `cashFlowsFromInvestingActivities` | `cashFlowsFromInvestingActivities` |  |
| `cashFlowsFromInvestingActivities.collectionOfLoansSalesOfDebtInstruments` | `collectionOfLoansSalesOfDebtInstruments` |  |
| `cashFlowsFromInvestingActivities.dividendsAndInterestReceived` | `dividendsAndInterestReceived` |  |
| `cashFlowsFromInvestingActivities.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.loansGrantedPurchasesOfDebtInstruments` | `loansGrantedPurchasesOfDebtInstruments` |  |
| `cashFlowsFromInvestingActivities.netCashFromInvestingActivities` | `netCashFromInvestingActivities` | ✅ KEY |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfFixedAssets` | `proceedsFromDisposalOfFixedAssets` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDivestmentInOtherEntities` | `proceedsFromDivestmentInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.purchasesOfFixedAndLongTermAssets` | `purchasesOfFixedAndLongTermAssets` |  |
| `cashFlowsFromOperatingActivities` | `cashFlowsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments` | `adjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.amortisationOfGoodwill` | `amortisationOfGoodwill` |  |
| `cashFlowsFromOperatingActivities.adjustments.depreciationAndAmortisation` | `depreciationAndAmortisation` |  |
| `cashFlowsFromOperatingActivities.adjustments.interestExpense` | `interestExpense` |  |
| `cashFlowsFromOperatingActivities.adjustments.otherAdjustments` | `otherAdjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.profitLossFromInvestingActivities` | `profitLossFromInvestingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments.provisions` | `provisions` |  |
| `cashFlowsFromOperatingActivities.adjustments.unrealisedForeignExchangeGainLoss` | `unrealisedForeignExchangeGainLoss` |  |
| `cashFlowsFromOperatingActivities.netCashFromOperatingActivities` | `netCashFromOperatingActivities` | ✅ KEY |
| `cashFlowsFromOperatingActivities.netProfitBeforeTax` | `netProfitBeforeTax` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges` | `operatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInInventories` | `changesInInventories` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPayables` | `changesInPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPrepaidExpenses` | `changesInPrepaidExpenses` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables` | `changesInReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInTradingSecurities` | `changesInTradingSecurities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.incomeTaxPaid` | `incomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.interestPaid` | `interestPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.netOperatingProfitBeforeChanges` | `netOperatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPaymentsOnOperatingActivities` | `otherPaymentsOnOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceiptsFromOperatingActivities` | `otherReceiptsFromOperatingActivities` |  |
| `effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `netCashFlow` | `netCashFlow` | ✅ KEY |

### BANKING — BANKING (BID, VCB, ACB...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `cashAndCashEquivalentsAtTheBeginningOfPeriod` | `cashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod` | `cashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashFlowsFromFinancingActivities` | `cashFlowsFromFinancingActivities` |  |
| `cashFlowsFromFinancingActivities.dividendsPaid` | `dividendsPaid` |  |
| `cashFlowsFromFinancingActivities.netCashFromFinancingActivities` | `netCashFromFinancingActivities` | ✅ KEY |
| `cashFlowsFromFinancingActivities.paymentsForRedemptionOfBonds` | `paymentsForRedemptionOfBonds` |  |
| `cashFlowsFromFinancingActivities.proceedsFromConvertibleBonds` | `proceedsFromConvertibleBonds` |  |
| `cashFlowsFromFinancingActivities.proceedsFromIssueOfShares` | `proceedsFromIssueOfShares` |  |
| `cashFlowsFromFinancingActivities.proceedsFromSellingTreasuryShares` | `proceedsFromSellingTreasuryShares` |  |
| `cashFlowsFromFinancingActivities.purchaseOfTreasuryShares` | `purchaseOfTreasuryShares` |  |
| `cashFlowsFromInvestingActivities` | `cashFlowsFromInvestingActivities` |  |
| `cashFlowsFromInvestingActivities.dividendsAndInterestReceived` | `dividendsAndInterestReceived` |  |
| `cashFlowsFromInvestingActivities.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.netCashFromInvestingActivities` | `netCashFromInvestingActivities` | ✅ KEY |
| `cashFlowsFromInvestingActivities.paymentsForPurchasesOfFixedAssetsAndOtherLongTermAssets` | `paymentsForPurchasesOfFixedAssetsAndOtherLongTermAssets` |  |
| `cashFlowsFromInvestingActivities.paymentsOnDisposalOfFixedAssets` | `paymentsOnDisposalOfFixedAssets` |  |
| `cashFlowsFromInvestingActivities.paymentsOnDisposalOfInvestmentProperties` | `paymentsOnDisposalOfInvestmentProperties` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfFixedAssets` | `proceedsFromDisposalOfFixedAssets` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfInvestmentProperties` | `proceedsFromDisposalOfInvestmentProperties` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDivestmentInOtherEntities` | `proceedsFromDivestmentInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.purchasesOfInvestmentProperties` | `purchasesOfInvestmentProperties` |  |
| `cashFlowsFromOperatingActivities` | `cashFlowsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.cashFlowFromOperatingActivitiesBeforeChangesInOperatingAssetsAndLiabilities` | `cashFlowFromOperatingActivitiesBeforeChangesInOperatingAssetsAndLiabilities` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets` | `changesInOperatingAssets` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.changeInLoansToCustomers` | `changeInLoansToCustomers` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.changesInDepositsAndLoansToOtherCreditInstitutions` | `changesInDepositsAndLoansToOtherCreditInstitutions` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.changesInHeldForTradingSecuritiesAndInvestmentSecurities` | `changesInHeldForTradingSecuritiesAndInvestmentSecurities` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.changesInOtherOperatingAssets` | `changesInOtherOperatingAssets` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.derivativesAndOtherFinancialAssets` | `derivativesAndOtherFinancialAssets` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingAssets.provisionForLoanLosses` | `provisionForLoanLosses` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities` | `changesInOperatingLiabilities` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInDepositsAndBorrowingsToOtherCreditInstitutions` | `changesInDepositsAndBorrowingsToOtherCreditInstitutions` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInDepositsFromCustomers` | `changesInDepositsFromCustomers` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInDerivativesAndOtherFinancialLiabilities` | `changesInDerivativesAndOtherFinancialLiabilities` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInFundsFromGovAndInstitutions` | `changesInFundsFromGovAndInstitutions` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInLoansFromStateAndSBV` | `changesInLoansFromStateAndSBV` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInOtherOperatingLiabilities` | `changesInOtherOperatingLiabilities` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.changesInValuablePapersIssued` | `changesInValuablePapersIssued` |  |
| `cashFlowsFromOperatingActivities.changesInOperatingLiabilities.paymentFromReserves` | `paymentFromReserves` |  |
| `cashFlowsFromOperatingActivities.corporateIncomeTaxPaid` | `corporateIncomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.interestAndSimilarExpensesPaid` | `interestAndSimilarExpensesPaid` |  |
| `cashFlowsFromOperatingActivities.interestAndSimilarIncomeReceived` | `interestAndSimilarIncomeReceived` |  |
| `cashFlowsFromOperatingActivities.netCashFromOperatingActivities` | `netCashFromOperatingActivities` | ✅ KEY |
| `cashFlowsFromOperatingActivities.netFeeAndCommissionIncomeReceived` | `netFeeAndCommissionIncomeReceived` |  |
| `cashFlowsFromOperatingActivities.netReceiptsFromTradingActivities` | `netReceiptsFromTradingActivities` |  |
| `cashFlowsFromOperatingActivities.otherIncomeExpenses` | `otherIncomeExpenses` |  |
| `cashFlowsFromOperatingActivities.receiptsFromDebtsWrittenOff` | `receiptsFromDebtsWrittenOff` |  |
| `cashFlowsFromOperatingActivities.salariesAndOperatingExpensesPaid` | `salariesAndOperatingExpensesPaid` |  |
| `effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `netCashFlow` | `netCashFlow` | ✅ KEY |

### SECURITIES — SECURITIES (SSI, VND, HCM...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `cashAndCashEquivalentsAtTheBeginningOfPeriod` | `cashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheBeginningOfPeriod.cash` | `cash` |  |
| `cashAndCashEquivalentsAtTheBeginningOfPeriod.cashEquivalents` | `cashEquivalents` |  |
| `cashAndCashEquivalentsAtTheBeginningOfPeriod.effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `cashAndCashEquivalentsAtTheBeginningOfPeriod.totalCashAndCashEquivalentsAtTheBeginningOfPeriod` | `totalCashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod` | `cashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod.cash` | `cash` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod.cashEquivalents` | `cashEquivalents` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod.effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod.totalCashAndCashEquivalentsAtTheEndOfPeriod` | `totalCashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod` | `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit` | `cashAndBankDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.customersGeneralDeposit` | `customersGeneralDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.depositForSecuritiesClearing` | `depositForSecuritiesClearing` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers` | `depositsOfSecuritiesIssuers` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers.issuingOrganizationDepositWithTerm` | `issuingOrganizationDepositWithTerm` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers.totalDepositsOfSecuritiesIssuers` | `totalDepositsOfSecuritiesIssuers` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod` | `investorDepositSecuritiesCompanyMethod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod.investorDepositWithTerm` | `investorDepositWithTerm` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod.totalInvestorDepositSecuritiesCompanyMethod` | `totalInvestorDepositSecuritiesCompanyMethod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashAndBankDeposit.totalCashAndBankDeposit` | `totalCashAndBankDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.cashEquivalent` | `cashEquivalent` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod.totalCashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod` | `totalCashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod` | `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit` | `cashAndBankDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.customersGeneralDeposit` | `customersGeneralDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.depositForSecuritiesClearing` | `depositForSecuritiesClearing` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers` | `depositsOfSecuritiesIssuers` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers.issuingOrganizationDepositWithTerm` | `issuingOrganizationDepositWithTerm` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.depositsOfSecuritiesIssuers.totalDepositsOfSecuritiesIssuers` | `totalDepositsOfSecuritiesIssuers` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod` | `investorDepositSecuritiesCompanyMethod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod.investorDepositWithTerm` | `investorDepositWithTerm` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.investorDepositSecuritiesCompanyMethod.totalInvestorDepositSecuritiesCompanyMethod` | `totalInvestorDepositSecuritiesCompanyMethod` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashAndBankDeposit.totalCashAndBankDeposit` | `totalCashAndBankDeposit` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.cashEquivalent` | `cashEquivalent` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod.totalCashAndCashEquivalentsOfCustomersAtTheEndOfPeriod` | `totalCashAndCashEquivalentsOfCustomersAtTheEndOfPeriod` |  |
| `cashFlowsFromBrokerageAndTrustActivities` | `cashFlowsFromBrokerageAndTrustActivities` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashInflowFromCurrentAccountOfClients` | `cashInflowFromCurrentAccountOfClients` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashInflowFromMandatedSales` | `cashInflowFromMandatedSales` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashInflowFromSecuritiesBroking` | `cashInflowFromSecuritiesBroking` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashInflowOnLoanFromSettlementAssistanceFund` | `cashInflowOnLoanFromSettlementAssistanceFund` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashOutflowFromCurrentAccountOfClients` | `cashOutflowFromCurrentAccountOfClients` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashOutflowFromMandatedSales` | `cashOutflowFromMandatedSales` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashOutflowFromSecuritiesPurchase` | `cashOutflowFromSecuritiesPurchase` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashOutflowOnRepayingFromSettlementAssistanceFund` | `cashOutflowOnRepayingFromSettlementAssistanceFund` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashPaidForDepositoryFee` | `cashPaidForDepositoryFee` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashPaidForThePurposeOfClientsTransactionSettlement` | `cashPaidForThePurposeOfClientsTransactionSettlement` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashPaidForThePurposeOfMandatedInvestmentOfClients` | `cashPaidForThePurposeOfMandatedInvestmentOfClients` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashPaidOnTransactionErrors` | `cashPaidOnTransactionErrors` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashPaidToIssuingOrganizations` | `cashPaidToIssuingOrganizations` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashReceivedForPurposeOfTransactionsOfClients` | `cashReceivedForPurposeOfTransactionsOfClients` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashReceivedForThePurposeOfMandatedInvestmentOfClients` | `cashReceivedForThePurposeOfMandatedInvestmentOfClients` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashReceivedFromIssuingOrganizations` | `cashReceivedFromIssuingOrganizations` |  |
| `cashFlowsFromBrokerageAndTrustActivities.cashReceivedOnTransactionErrors` | `cashReceivedOnTransactionErrors` |  |
| `cashFlowsFromBrokerageAndTrustActivities.netCashFromBrokerageAndTrustActivities` | `netCashFromBrokerageAndTrustActivities` |  |
| `cashFlowsFromFinancingActivities` | `cashFlowsFromFinancingActivities` |  |
| `cashFlowsFromFinancingActivities.dividendsPaid` | `dividendsPaid` |  |
| `cashFlowsFromFinancingActivities.financeLeasePrincipalPayments` | `financeLeasePrincipalPayments` |  |
| `cashFlowsFromFinancingActivities.netCashFromFinancingActivities` | `netCashFromFinancingActivities` | ✅ KEY |
| `cashFlowsFromFinancingActivities.paymentsForShareReturnsAndRepurchases` | `paymentsForShareReturnsAndRepurchases` |  |
| `cashFlowsFromFinancingActivities.proceedsFromIssueOfShares` | `proceedsFromIssueOfShares` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans` | `proceedsFromLoans` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans.otherLoans` | `otherLoans` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans.settlementAssistanceFund` | `settlementAssistanceFund` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans.totalProceedsFromLoans` | `totalProceedsFromLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans` | `repaymentOfLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans.financialAssetsLoans` | `financialAssetsLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans.otherLoans` | `otherLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans.settlementAssistanceFund` | `settlementAssistanceFund` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans.totalRepaymentOfLoans` | `totalRepaymentOfLoans` |  |
| `cashFlowsFromInvestingActivities` | `cashFlowsFromInvestingActivities` |  |
| `cashFlowsFromInvestingActivities.collectionOfLoansAndProceedsFromSalesOfDebtsInstruments` | `collectionOfLoansAndProceedsFromSalesOfDebtsInstruments` |  |
| `cashFlowsFromInvestingActivities.dividendsAndInterestReceived` | `dividendsAndInterestReceived` |  |
| `cashFlowsFromInvestingActivities.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.loansGrantedAndPurchasesOfDebtInstruments` | `loansGrantedAndPurchasesOfDebtInstruments` |  |
| `cashFlowsFromInvestingActivities.netCashFromInvestingActivities` | `netCashFromInvestingActivities` | ✅ KEY |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfFixedAssetsAndInvestmentPropertiesAndOtherLongTermAssets` | `proceedsFromDisposalOfFixedAssetsAndInvestmentPropertiesAndOtherLongTermAssets` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDivestmentInOtherEntities` | `proceedsFromDivestmentInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.purchasesAndConstructionOfFixedAssetsAndInvestmentPropertiesAndOtherLongTermAssets` | `purchasesAndConstructionOfFixedAssetsAndInvestmentPropertiesAndOtherLongTermAssets` |  |
| `cashFlowsFromOperatingActivities` | `cashFlowsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments` | `adjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.accruedExpenses` | `accruedExpenses` |  |
| `cashFlowsFromOperatingActivities.adjustments.amortisationOfGoodwill` | `amortisationOfGoodwill` |  |
| `cashFlowsFromOperatingActivities.adjustments.depreciationAndAmortisation` | `depreciationAndAmortisation` |  |
| `cashFlowsFromOperatingActivities.adjustments.interestExpense` | `interestExpense` |  |
| `cashFlowsFromOperatingActivities.adjustments.interestIncomeAndDividend` | `interestIncomeAndDividend` |  |
| `cashFlowsFromOperatingActivities.adjustments.otherAdjustments` | `otherAdjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.profitLossFromInvestingActivities` | `profitLossFromInvestingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments.provisions` | `provisions` |  |
| `cashFlowsFromOperatingActivities.adjustments.totalAdjustments` | `totalAdjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.unrealisedForeignExchangeGainLoss` | `unrealisedForeignExchangeGainLoss` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue` | `decreaseInNonMonetaryRevenue` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue.gainFromAFSReclassification` | `gainFromAFSReclassification` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue.gainFromRevaluationOfFinancialAssetsAtFVTPL` | `gainFromRevaluationOfFinancialAssetsAtFVTPL` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue.otherGains` | `otherGains` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue.reversalOfProvision` | `reversalOfProvision` |  |
| `cashFlowsFromOperatingActivities.decreaseInNonMonetaryRevenue.totalDecreaseInNonMonetaryRevenue` | `totalDecreaseInNonMonetaryRevenue` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses` | `increaseInNonMonetaryExpenses` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.lossFromRevaluationOfFinancialAssetsAtFVTPL` | `lossFromRevaluationOfFinancialAssetsAtFVTPL` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.lossOnAFSReclassification` | `lossOnAFSReclassification` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.lossOnHeldToMaturityInvestments` | `lossOnHeldToMaturityInvestments` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.lossOnLoansGiven` | `lossOnLoansGiven` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.otherLoss` | `otherLoss` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.provisionForLongTermInvestments` | `provisionForLongTermInvestments` |  |
| `cashFlowsFromOperatingActivities.increaseInNonMonetaryExpenses.totalIncreaseInNonMonetaryExpenses` | `totalIncreaseInNonMonetaryExpenses` |  |
| `cashFlowsFromOperatingActivities.netCashFromOperatingActivities` | `netCashFromOperatingActivities` | ✅ KEY |
| `cashFlowsFromOperatingActivities.netProfitBeforeTax` | `netProfitBeforeTax` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges` | `operatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInAvailableForSaleFinancialAssets` | `changesInAvailableForSaleFinancialAssets` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInEmployeesWelfareContributions` | `changesInEmployeesWelfareContributions` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInFVTPLFinancialAssets` | `changesInFVTPLFinancialAssets` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInHeldToMaturityInvestments` | `changesInHeldToMaturityInvestments` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInLoansGiven` | `changesInLoansGiven` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInOtherAssets` | `changesInOtherAssets` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInOtherPayables` | `changesInOtherPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInOtherReceivables` | `changesInOtherReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPayableExpensesExcludingInterest` | `changesInPayableExpensesExcludingInterest` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPayableFromFinancialAssetTransactionError` | `changesInPayableFromFinancialAssetTransactionError` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPayablesToEmployees` | `changesInPayablesToEmployees` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPrepaidExpenses` | `changesInPrepaidExpenses` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivableFromInterestOfFinancialAssets` | `changesInReceivableFromInterestOfFinancialAssets` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivableFromSellingFinancialAssets` | `changesInReceivableFromSellingFinancialAssets` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivableFromServicesRendered` | `changesInReceivableFromServicesRendered` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivableFromTransactionErrors` | `changesInReceivableFromTransactionErrors` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInTaxAndPayablesToAuthority` | `changesInTaxAndPayablesToAuthority` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInTradePayables` | `changesInTradePayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.incomeTaxPaid` | `incomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.interestExpensesPaid` | `interestExpensesPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.netOperatingProfitBeforeChanges` | `netOperatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPayments` | `otherPayments` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPayments.businessIncomeTaxPaid` | `businessIncomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPayments.interestPaid` | `interestPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPayments.otherExpenses` | `otherExpenses` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPayments.totalOtherPayments` | `totalOtherPayments` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceipts` | `otherReceipts` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceipts.interestReceived` | `interestReceived` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceipts.otherReceivables` | `otherReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceipts.totalOtherReceipts` | `totalOtherReceipts` |  |
| `netCashFlow` | `netCashFlow` | ✅ KEY |

### INSURANCE — INSURANCE (BVH, BMI, PTI...)

| Field Path | Leaf Key | Ghi chú |
|---|---|---|
| `cashAndCashEquivalentsAtTheBeginningOfPeriod` | `cashAndCashEquivalentsAtTheBeginningOfPeriod` |  |
| `cashAndCashEquivalentsAtTheEndOfPeriod` | `cashAndCashEquivalentsAtTheEndOfPeriod` |  |
| `cashFlowsFromFinancingActivities` | `cashFlowsFromFinancingActivities` |  |
| `cashFlowsFromFinancingActivities.dividendsPaid` | `dividendsPaid` |  |
| `cashFlowsFromFinancingActivities.financeLeasePrincipalPayments` | `financeLeasePrincipalPayments` |  |
| `cashFlowsFromFinancingActivities.netCashFromFinancingActivities` | `netCashFromFinancingActivities` | ✅ KEY |
| `cashFlowsFromFinancingActivities.paymentsForShareReturnsAndRepurchases` | `paymentsForShareReturnsAndRepurchases` |  |
| `cashFlowsFromFinancingActivities.proceedsFromIssueOfShares` | `proceedsFromIssueOfShares` |  |
| `cashFlowsFromFinancingActivities.proceedsFromLoans` | `proceedsFromLoans` |  |
| `cashFlowsFromFinancingActivities.repaymentOfLoans` | `repaymentOfLoans` |  |
| `cashFlowsFromInvestingActivities` | `cashFlowsFromInvestingActivities` |  |
| `cashFlowsFromInvestingActivities.collectionOfLoansAndProceedsFromSalesOfDebtsInstruments` | `collectionOfLoansAndProceedsFromSalesOfDebtsInstruments` |  |
| `cashFlowsFromInvestingActivities.dividendsAndInterestReceived` | `dividendsAndInterestReceived` |  |
| `cashFlowsFromInvestingActivities.investmentsInOtherEntities` | `investmentsInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.loansGrantedAndDebtInstrumentsPurchased` | `loansGrantedAndDebtInstrumentsPurchased` |  |
| `cashFlowsFromInvestingActivities.netCashFromInvestingActivities` | `netCashFromInvestingActivities` | ✅ KEY |
| `cashFlowsFromInvestingActivities.proceedsFromDisposalOfFixedAndLongTermAssets` | `proceedsFromDisposalOfFixedAndLongTermAssets` |  |
| `cashFlowsFromInvestingActivities.proceedsFromDivestmentInOtherEntities` | `proceedsFromDivestmentInOtherEntities` |  |
| `cashFlowsFromInvestingActivities.purchasesAndConstructionOfFixedAndLongTermAssets` | `purchasesAndConstructionOfFixedAndLongTermAssets` |  |
| `cashFlowsFromOperatingActivities` | `cashFlowsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments` | `adjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.amortisationOfGoodwill` | `amortisationOfGoodwill` |  |
| `cashFlowsFromOperatingActivities.adjustments.depreciationAndAmortisation` | `depreciationAndAmortisation` |  |
| `cashFlowsFromOperatingActivities.adjustments.interestIncomeAndDividend` | `interestIncomeAndDividend` |  |
| `cashFlowsFromOperatingActivities.adjustments.otherAdjustments` | `otherAdjustments` |  |
| `cashFlowsFromOperatingActivities.adjustments.profitLossFromInvestingActivities` | `profitLossFromInvestingActivities` |  |
| `cashFlowsFromOperatingActivities.adjustments.provisions` | `provisions` |  |
| `cashFlowsFromOperatingActivities.adjustments.repoAndInterestExpenses` | `repoAndInterestExpenses` |  |
| `cashFlowsFromOperatingActivities.adjustments.unrealisedForeignExchangeGainLoss` | `unrealisedForeignExchangeGainLoss` |  |
| `cashFlowsFromOperatingActivities.netCashFromOperatingActivities` | `netCashFromOperatingActivities` | ✅ KEY |
| `cashFlowsFromOperatingActivities.netProfitBeforeTax` | `netProfitBeforeTax` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges` | `operatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInInventories` | `changesInInventories` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInPrepaidExpenses` | `changesInPrepaidExpenses` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables` | `changesInReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.grossWrittenPremiumReceivables` | `grossWrittenPremiumReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.interCompanyReceivablesPayables` | `interCompanyReceivablesPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.otherReceivablesFromInsurance` | `otherReceivablesFromInsurance` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.reinsuranceAssumedReceivables` | `reinsuranceAssumedReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.reinsuranceCededReceivables` | `reinsuranceCededReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInReceivables.totalChangesInReceivables` | `totalChangesInReceivables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.changesInTradingSecurities` | `changesInTradingSecurities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.corporateIncomeTaxPaid` | `corporateIncomeTaxPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.interestPaid` | `interestPaid` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.netOperatingProfitBeforeChanges` | `netOperatingProfitBeforeChanges` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherPaymentsOnOperatingActivities` | `otherPaymentsOnOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.otherReceiptsFromOperatingActivities` | `otherReceiptsFromOperatingActivities` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax` | `payablesExcludingInterestAndTax` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.grossWrittenPremiumPayables` | `grossWrittenPremiumPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.otherPayablesFromInsurance` | `otherPayablesFromInsurance` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.payablesToEmployees` | `payablesToEmployees` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.reinsuranceAssumedPayables` | `reinsuranceAssumedPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.reinsuranceCededPayables` | `reinsuranceCededPayables` |  |
| `cashFlowsFromOperatingActivities.operatingProfitBeforeChanges.payablesExcludingInterestAndTax.totalChangesInPayables` | `totalChangesInPayables` |  |
| `effectOfForeignExchangeDifferences` | `effectOfForeignExchangeDifferences` |  |
| `netCashFlow` | `netCashFlow` | ✅ KEY |

---
