---
name: Mẫu dữ liệu BCTC hợp nhất
description: List các dictionary, trong đó mỗi dictionary sẽ tương ứng với data của 1 kỳ báo cáo, dưới đây là mô tả.
---

- Loại hình doanh nghiệp: CTCK, NH, BH, CTY
- Doanh nghiệp mẫu: HPG, SSI, VCB, BVH

# 1. Bảng cân đối kế toán

## 1.1. Doanh nghiệp sản xuất
```json
[	
    {	
        "ticker": "HPG",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "balanceSheet": [	
                {	
                    "assets": {	
                        "totalAssets": 224489707553981,	
                        "currentAssets": {	
                            "shortTermInvestments": {	
                                "totalShortTermInvestments": 18974716730905,     	
                                "tradingSecurities": 0,	
                                "heldToMaturityInvestments": 18974716730905,     	
                                "provisionForTradingSecurities": 0	
                            },	
                            "shortTermReceivables": {	
                                "tradeReceivables": 4352135419872,	
                                "shortTermInternalReceivables": 0,	
                                "receivablesUnderConstructionContracts": 0,      	
                                "advancesToSuppliers": 2118824427004,	
                                "allowanceForDoubtfulReceivables": -159993736285,	
                                "pendingAssetsShortage": 379714580,	
                                "shortTermLoans": 87461616439,	
                                "otherReceivables": 1248992845378,	
                                "totalShortTermReceivables": 7647800286988       	
                            },	
                            "inventories": {	
                                "allowanceForImpairment": -101069892341,	
                                "inventories": 46192292081813,	
                                "totalInventories": 46091222189472	
                            },	
                            "totalCurrentAssets": 86674276272995,	
                            "cashAndCashEquivalents": {	
                                "totalCashAndCashEquivalents": 6887646139852,    	
                                "cashEquivalents": 3968114193944,	
                                "cash": 2919531945908	
                            },	
                            "otherCurrentAssets": {	
                                "taxAndOrderReceivables": 10074967536,	
                                "other": 0,	
                                "governmentBondRepurchaseAgreement": 0,	
                                "prepayments": 426149499088,	
                                "totalOtherCurrentAssets": 7072890925778,        	
                                "deductibleValueAddedTax": 6636666459154	
                            }	
                        },	
                        "longTermAssets": {	
                            "otherLongTermAssets": {	
                                "other": 0,	
                                "deferredTaxAssets": 254671208385,	
                                "prepayments": 4269141694868,	
                                "longTermSparePartsAndEquipment": 429422385383,	
                                "totalOtherLongTermAssets": 5016848415359,	
                                "goodWill": 63613126723	
                            },	
                            "totalLongTermAssets": 137815431280986,	
                            "longTermAssetsInProgress": {	
                                "constructionInProgress": 63655857440382,	
                                "totalLongTermAssetsInProgress": 63750717325406,	
                                "longTermWorkInProgress": 94859885024	
                            },	
                            "longTermInvestments": {	
                                "provisionForLongTermInvestments": 0,	
                                "heldToMaturityInvestments": 136500000000,	
                                "totalLongTermInvestments": 136500000000,	
                                "equityInvestmentsInOthers": 0,	
                                "investmentsInSubsidiaries": 0,	
                                "investmentsInJointVentures": 0	
                            },	
                            "fixedAssets": {	
                                "intangibleAssets": {	
                                    "cost": 367057604707,	
                                    "accumulatedAmortisation": -182841626241,	
                                    "totalIntangibleAssets": 184215978466	
                                },	
                                "financeLeaseFixedAssets": {	
                                    "cost": 0,	
                                    "totalFinanceLeaseFixedAssets": 0,	
                                    "accumulatedDepreciation": 0	
                                },	
                                "totalFixedAssets": 67428366953514,	
                                "tangibleFixedAssets": {	
                                    "cost": 108146566348954,	
                                    "totalTangibleFixedAssets": 67244150975048,	
                                    "accumulatedDepreciation": -40902415373906	
                                }	
                            },	
                            "longTermReceivables": {	
                                "longTermCustomerReceivables": 0,	
                                "longTermAdvancesToSuppliers": 82805287792,	
                                "capitalAtAffiliatedUnits": 0,	
                                "otherLongTermReceivables": 840594835822,	
                                "provisionForDoubtfulLongTermReceivables": 0,	
                                "longTermIntercompanyReceivables": 0,	
                                "longTermLoanReceivables": 0,	
                                "totalLongTermReceivables": 923400123614	
                            },	
                            "investmentProperty": {	
                                "cost": 860549015615,	
                                "accumulatedDepreciation": -300950552522,	
                                "totalInvestmentProperty": 559598463093	
                            }	
                        }	
                    },	
                    "resources": {	
                        "totalResources": 224489707553981,	
                        "liabilities": {	
                            "currentLiabilities": {	
                                "otherPayables": 188076845190,	
                                "shortTermPayableExpenses": 682112072502,	
                                "advancesFromCustomers": 739178306553,	
                                "bonusAndWelfareFund": 1027310381825,	
                                "totalCurrentLiabilities": 75225243262689,	
                                "shortTermUnearnedRevenue": 11060479431,	
                                "accountsPayableToSuppliers": 14046841160127,	
                                "payableToEmployees": 890893543298,	
                                "governmentBondRepurchaseTransactions": 0,	
                                "borrowings": 55882686213459,	
                                "priceStabilizationFund": 0,	
                                "shortTermInternalPayables": 0,	
                                "shortTermProvisionForPayables": 13672830889,	
                                "taxPayables": 1743411429415,	
                                "constructionContractPayablesByProgress": 0	
                            },	
                            "totalLiabilities": 109842249570282,	
                            "longTermLiabilities": {	
                                "internalCapitalContributionPayables": 0,	
                                "longTermUnearnedRevenue": 0,	
                                "preferredShares": 0,	
                                "deferredTaxLiabilities": 29268483140,	
                                "scienceAndTechnologyDevelopmentFund": 0,	
                                "convertibleBonds": 0,	
                                "longTermAccusedExpenses": 1143692237207,	
                                "longTermProvisionForPayables": 67495546940,	
                                "longTermInternalPayables": 0,	
                                "otherLongTermPayables": 12476505170,	
                                "borrowings": 27080443256096,	
                                "totalLongTermLiabilities": 34617006307593,	
                                "longTermTradePayables": 6283630279040,	
                                "longTermAdvancesFromCustomers": 0	
                            }	
                        },	
                        "equity": {	
                            "ownersEquity": {	
                                "convertibleBondOptions": 0,	
                                "preferredShares": 0,	
                                "totalOwnersEquity": 114647457983699,	
                                "treasuryShares": 0,	
                                "foreignExchangeDifferences": 0,	
                                "otherOwnersCapital": 0,	
                                "reorganizationSupportFund": 0,	
                                "nonControllingInterests": 290990632368,	
                                "sharePremium": 0,	
                                "shareCapital": 63962502000000,	
                                "assetRevaluationSurplus": 0,	
                                "developmentInvestmentFund": 794841242128,	
                                "constructionInvestmentCapital": 0,	
                                "otherEquityFunds": 0,	
                                "retainedEarnings": {	
                                    "retainedEarningsCurrent": 11974873561074,	
                                    "retainedEarningsPrevious": 37624250548129,	
                                    "totalRetainedEarnings": 49599124109203	
                                }	
                            },	
                            "totalEquity": 114647457983699,	
                            "fundsAndOtherSources": {	
                                "fixedAssetFunding": 0,	
                                "totalOtherFunds": 0,	
                                "fundingSources": 0	
                            }	
                        }	
                    }	
                }	
            ]	
        },	
        "companyType": "MANUFACTURING",	
        "businessTypeId": 3	
    }	
]	
```

## 1.2. Ngân hàng
```json
[	
    {	
        "ticker": "VCB",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "balanceSheet": [	
                {	
                    "assets": {	
                        "derivativesAndOtherFinancialAssets": 1314434000000,	
                        "otherAssets": {	
                            "goodwill": 0,	
                            "other": 6516040000000,	
                            "totalOtherAssets": 30402348000000,	
                            "deferredTaxAssets": 991748000000,	
                            "receivables": 14040294000000,	
                            "accruedInterestAndFeeReceivables": 8868303000000,	
                            "allowanceForLosses": -14037000000	
                        },	
                        "totalAssets": 2085873522000000,	
                        "loansToCustomers": {	
                            "loansToCustomers": 1449198899000000,	
                            "totalLoansToCustomers": 1418015724000000,	
                            "allowanceForCreditLosses": -31183175000000	
                        },	
                        "cashOnHandGoldAndGemstones": 14268064000000,	
                        "balancesWithTheStateBankOfVietnam": 49340493000000,	
                        "heldForTradingSecurities": {	
                            "totalHeldForTradingSecurities": 4876237000000,	
                            "heldForTradingSecurities": 4908527000000,	
                            "allowanceForLossesOnHeldForTradingSecurities": -32290000000	
                        },	
                        "investmentSecurities": {	
                            "availableForSaleSecurities": 86799901000000,	
                            "heldToMaturitySecurities": 80829540000000,	
                            "totalInvestmentSecurities": 167383349000000,	
                            "allowanceForLossesOnInvestmentSecurities": -246092000000   	
                        },	
                        "fixedAssets": {	
                            "intangibleAssets": {	
                                "cost": 5072735000000,	
                                "accumulatedAmortisation": -2510437000000,	
                                "totalIntangibleAssets": 2562298000000	
                            },	
                            "financeLeaseFixedAssets": {	
                                "cost": 0,	
                                "totalFinanceLeaseFixedAssets": 0,	
                                "accumulatedDepreciation": 0	
                            },	
                            "totalFixedAssets": 8092877000000,	
                            "tangibleFixedAssets": {	
                                "cost": 15808302000000,	
                                "totalTangibleFixedAssets": 5530579000000,	
                                "accumulatedDepreciation": -10277723000000	
                            }	
                        },	
                        "longTermInvestment": {	
                            "otherLongTermInvestments": 1528922000000,	
                            "investmentsInJointVenture": 763736000000,	
                            "provisionForLongTermInvestments": -75000000000,	
                            "investmentInSubsidiaries": 0,	
                            "investmentsInAssociates": 10440000000,	
                            "totalLongTermInvestment": 2228098000000	
                        },	
                        "debtPurchases": {	
                            "allowanceForDebtPurchases": 0,	
                            "debtPurchases": 0	
                        },	
                        "depositsWithAndLoansToOtherCreditInstitutions": {	
                            "totalDepositsWithAndLoansToOtherCreditInstitutions": 389951898000000,	
                            "depositsWithOtherInstitutions": 384031890000000,	
                            "allowanceForCreditLosses": -1000000000000,	
                            "loansToOtherInstitutions": 6920008000000	
                        },	
                        "investmentProperty": {	
                            "cost": 0,	
                            "accumulatedDepreciation": 0,	
                            "totalInvestmentProperty": 0	
                        }	
                    },	
                    "resources": {	
                        "totalResources": 2085873522000000,	
                        "liabilities": {	
                            "fundsAndEntrustedInvestmentsReceivedFromTheGovernmentInternationalAndOtherCreditInstitutions": 529000000,	
                            "depositsFromCustomers": 1514664850000000,	
                            "otherLiabilities": {	
                                "other": 24112345000000,	
                                "accruedInterestPayable": 13990276000000,	
                                "totalOtherLiabilities": 38102621000000,	
                                "taxPayables": 0,	
                                "allowanceForLosses": 0	
                            },	
                            "derivativesAndOtherFinancialLiabilities": 0,	
                            "valuablePapersIssued": 24125059000000,	
                            "totalLiabilities": 1889664354000000,	
                            "dueToTheGovernmentAndTheStateBankOfVietnam": 78237337000000,	
                            "depositsAndBorrowings": {	
                                "borrowingsFromOtherInstitutions": 11362577000000,	
                                "depositsFromOtherInstitutions": 223171381000000,	
                                "depositsAndBorrowingsFromOtherInstitutions": 234533958000000	
                            }	
                        },	
                        "equity": {	
                            "totalEquity": 196209168000000,	
                            "capital": {	
                                "totalCapital": 61696139000000,	
                                "preferredShares": 0,	
                                "charterCapital": 55890913000000,	
                                "treasuryShares": 0,	
                                "sharePremium": 4995389000000,	
                                "ownersOtherCapital": 809837000000	
                            },	
                            "retainedProfits": {	
                                "totalRetainedProfits": 98332086000000	
                            },	
                            "reserves": 37052974000000,	
                            "nonControllingInterests": 96261000000,	
                            "revaluationSurplus": 0,	
                            "exchangeRateDifferences": -968292000000	
                        }	
                    }	
                }	
            ]	
        },	
        "companyType": "BANKING",	
        "businessTypeId": 1	
    }	
]	
```

## 1.3. Doanh nghiệp chứng khoán
```json
[	
    {	
        "ticker": "SSI",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "balanceSheet": [	
                {	
                    "assets": {	
                        "totalAssets": 73507302559722,	
                        "currentAssets": {	
                            "totalCurrentAssets": 70932391912367,	
                            "financialAssets": {	
                                "loans": 21998601885375,	
                                "totalFinancialAssets": 70813502224578,	
                                "provisionForImpairmentOfReceivables": -232039957803,	
                                "otherReceivables": 210104950765,	
                                "availableForSaleFinancialAssets": 562332851822,	
                                "provisionForImpairmentOfFinancialAssetsAndMortgageAssets": -55101823874,     	
                                "receivablesFromServicesProvidedByCompany": 30201748046,	
                                "financialAssetsAtFairValueThroughProfitOrLoss": 42438121481401,	
                                "receivables": {	
                                    "receivablesAndAccrualsFromDividendInterestIncome": {	
                                        "totalReceivablesAndAccrualsFromDividendInterestIncome": 292847293114,	
                                        "dueOrOverdueReceivablesDividendInterest": 0,	
                                        "accrualsForUndueDividendAndInterestIncome": 292847293114	
                                    },	
                                    "totalReceivables": 800614271922,	
                                    "receivablesFromDisposalOfFinancialAssets": 507766978808	
                                },	
                                "receivablesFromSecuritiesTransactionErrors": 0,	
                                "heldToMaturityInvestments": 3893901724895,	
                                "advancesToSuppliers": 927764853829,	
                                "cashAndCashEquivalents": {	
                                    "totalCashAndCashEquivalents": 239000238200,	
                                    "cashEquivalents": 30030246575,	
                                    "cash": 208969991625	
                                },	
                                "internalReceivables": 0	
                            },	
                            "otherCurrentAssets": {	
                                "shortTermDepositsCollateralsAndPledges": 772112130,	
                                "taxesAndStateReceivables": 55944865,	
                                "governmentBondRepurchaseTransactions": 0,	
                                "advances": 20927597892,	
                                "provisionForImpairmentOfOtherCurrentAssets": 0,	
                                "totalOtherCurrentAssets": 118889687789,	
                                "shortTermPrepaidExpenses": 54860667972,	
                                "otherCurrentAssetsDetails": 41677606235,	
                                "deductibleValueAddedTax": 0,	
                                "officeSuppliesToolsAndMaterials": 595758695	
                            }	
                        },	
                        "longTermAssets": {	
                            "totalLongTermAssets": 2574910647355,	
                            "otherLongTermAssets": {	
                                "deferredIncomeTaxAssets": 24001105881,	
                                "longTermDepositsCollateralsAndPledges": 31205273582,	
                                "longTermPrepaidExpenses": 21614788489,	
                                "paymentForSettlementAssistanceFund": 20000000000,	
                                "otherLongTermAssetsDetails": 33312364248,	
                                "totalOtherLongTermAssets": 130133532200,	
                                "longTermEquipmentMaterialAndSpareParts": 0,	
                                "goodWill": 0	
                            },	
                            "constructionInProgress": 387623333376,	
                            "provisionForImpairmentOfLongTermAssets": 0,	
                            "investmentProperties": {	
                                "revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel": 0,	
                                "cost": 287459600028,	
                                "totalInvestmentProperties": 200196436698,	
                                "accumulatedDepreciation": -87263163330	
                            },	
                            "longTermFinancialAssets": {	
                                "totalLongTermFinancialAssets": 1625606669387,	
                                "longTermInvestments": {	
                                    "otherLongTermInvestments": 0,	
                                    "investmentInJointVenturesAndAssociates": 687490406131,	
                                    "investmentInSubsidiaries": 0,	
                                    "totalLongTermInvestments": 1625606669387,	
                                    "heldToMaturityInvestments": 938116263256	
                                },	
                                "provisionForImpairmentOfLongTermInvestments": 0,	
                                "longTermReceivables": 0	
                            },	
                            "fixedAssets": {	
                                "intangibleFixedAssets": {	
                                    "revaluationOfFixedAssetsInFinancialLeaseUsingFairValueModel": 0,	
                                    "cost": 313999554731,	
                                    "accumulatedAmortisation": -201155598936,	
                                    "totalIntangibleAssets": 112843955795	
                                },	
                                "financeLeaseFixedAssets": {	
                                    "cost": 0,	
                                    "totalFinanceLeaseFixedAssets": 0,	
                                    "accumulatedDepreciation": 0	
                                },	
                                "totalFixedAssets": 231350675694,	
                                "tangibleFixedAssets": {	
                                    "cost": 408360121790,	
                                    "totalTangibleFixedAssets": 118506719899,	
                                    "accumulatedDepreciation": -289853401891	
                                }	
                            }	
                        }	
                    },	
                    "resources": {	
                        "totalResources": 73507302559722,	
                        "fundingSourcesAndOtherFunds": 0,	
                        "liabilities": {	
                            "currentLiabilities": {	
                                "shortTermDepositsAndCollateralReceived": 362313180,	
                                "otherShortTermPayables": 18037472054,	
                                "payablesToEmployees": 93761808205,	
                                "convertibleBondsShortTerm": 0,	
                                "totalCurrentLiabilities": 46599438522989,	
                                "shortTermFinanceLeasePayables": 0,	
                                "bonusAndWelfareFund": 356533362422,	
                                "paymentSupportFund": 0,	
                                "issuedBondsShortTerm": 0,	
                                "shortTermUnearnedRevenue": 1299798330,	
                                "shortTermAccruedExpenses": 67847177428,	
                                "bondsRepurchaseTransactions": 0,	
                                "constructionContractInProgressPayables": 0,	
                                "payablesDueToFinancialAssetErrors": 0,	
                                "shortTermTradePayables": 103075387679,	
                                "shortTermAdvanceFromCustomers": 26490726300,	
                                "provisionForShortTermLiabilities": 0,	
                                "payablesFromSecuritiesTransactions": 227883634106,	
                                "shortTermInternalPayables": 0,	
                                "shortTermBorrowingsAndFinancialLeases": {	
                                    "totalShortTermBorrowingsAndFinancialLeases": 45501969699137,	
                                    "shortTermBorrowings": 45501969699137,	
                                    "shortTermFinanceLeaseLiabilities": 0	
                                },	
                                "employeeBenefits": 884019653,	
                                "statutoryObligation": 201293124495	
                            },	
                            "totalLiabilities": 46680651947954,	
                            "longTermLiabilities": {	
                                "issuedBondsLongTerm": 0,	
                                "deferredIncomeTaxPayable": 26650541290,	
                                "provisionForInvestorCompensation": 0,	
                                "longTermFinanceLeasePayables": 0,	
                                "longTermUnearnedRevenue": 54562883675,	
                                "longTermAccruedExpenses": 0,	
                                "scienceAndTechnologyDevelopmentFund": 0,	
                                "convertibleBonds": 0,	
                                "longTermBorrowingsAndFinancialLeases": {	
                                    "totalLongTermBorrowingsAndFinancialLeases": 0,	
                                    "longTermFinanceLeaseLiabilities": 0,	
                                    "longTermBorrowings": 0	
                                },	
                                "longTermInternalPayables": 0,	
                                "longTermCollateralsReceived": 0,	
                                "otherLongTermPayables": 0,	
                                "totalLongTermLiabilities": 81213424965,	
                                "provisionForLongTermLiabilities": 0,	
                                "longTermTradePayables": 0,	
                                "longTermAdvanceFromCustomers": 0	
                            }	
                        },	
                        "equity": {	
                            "ownersEquity": {	
                                "shareCapital": {	
                                    "otherOwnerCapital": 0,	
                                    "totalShareCapital": 20713065094108,	
                                    "capitalContribution": {	
                                        "ordinaryShares": 19638639180000,	
                                        "preferredShares": 0,	
                                        "totalCapitalContribution": 19638639180000	
                                    },	
                                    "convertibleBondOption": 0,	
                                    "treasuryShares": -19115006409,	
                                    "sharePremium": 1093540920517	
                                },	
                                "totalOwnersEquity": 26826650611768,	
                                "differencesFromRevaluationOfAssetsAtFairValue": 31690477740,	
                                "undistributedProfit": {	
                                    "realizedProfit": 6025186849191,	
                                    "totalUndistributedProfit": 5856098315938,	
                                    "unrealizedProfit": -169088533253	
                                },	
                                "ownerFundsReserve": {	
                                    "charterCapitalSupplementaryReserve": 3000000000,	
                                    "otherOwnerFunds": 0	
                                },	
                                "ForeignExchangeRateDifferences": 72177590546,	
                                "nonControllingInterests": 150619133436	
                            },	
                            "totalEquity": 26826650611768	
                        }	
                    }	
                }	
            ]	
        },	
        "companyType": "SECURITIES",	
        "businessTypeId": 3	
    }	
]	
```

## 1.4. Doanh nghiệp bảo hiểm
```json
[	
    {	
        "ticker": "BVH",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "balanceSheet": [	
                {	
                    "assets": {	
                        "totalAssets": 251286326838124,	
                        "currentAssets": {	
                            "reinsuranceAssets": {	
                                "reinsuranceCededClaimsReserve": 1871236613709,	
                                "reinsuranceCededUnearnedPremiumReserve": 1686897782968,  	
                                "totalReinsuranceAssets": 3558134396677	
                            },	
                            "shortTermInvestments": {	
                                "totalShortTermInvestments": 103898039030526,	
                                "tradingSecurities": 3660368511864,	
                                "heldToMaturityInvestments": 100440649810502,	
                                "provisionForTradingSecurities": -202979291840	
                            },	
                            "shortTermReceivables": {	
                                "receivablesFromCustomers": {	
                                    "fromInsuranceActivities": 1265479668075,	
                                    "totalReceivablesFromCustomers": 7892192217650,       	
                                    "otherReceivables": 6626712549575	
                                },	
                                "otherShortTermReceivables": 311080060298,	
                                "shortTermLoansReceivables": 3547995002349,	
                                "provisionForDoubtfulShortTermReceivables": -247913748321,	
                                "advancesToSuppliers": 32063030043,	
                                "totalShortTermReceivables": 11535416562019,	
                                "internalReceivables": 0	
                            },	
                            "inventories": {	
                                "inventories": 100479759917,	
                                "totalInventories": 100479759917,	
                                "provisionForInventoryDevaluation": 0	
                            },	
                            "totalCurrentAssets": 121226741291519,	
                            "cashAndCashEquivalents": {	
                                "totalCashAndCashEquivalents": 1464088127113,	
                                "cashEquivalents": 190000000000,	
                                "cash": 1274088127113	
                            },	
                            "otherCurrentAssets": {	
                                "deductibleVAT": 36415365,	
                                "taxesAndStateReceivables": 4809122226,	
                                "other": 5199723492,	
                                "governmentBondRepurchaseTransactions": 0,	
                                "prepaidExpenses": {	
                                    "totalPrepaidExpenses": 660538154184,	
                                    "unallocatedCommissionExpenses": 581867688103,	
                                    "otherPrepaidExpenses": 78670466081	
                                },	
                                "totalOtherCurrentAssets": 670583415267	
                            }	
                        },	
                        "longTermAssets": {	
                            "totalLongTermAssets": 130059585546605,	
                            "otherLongTermAssets": {	
                                "goodwill": 0,	
                                "other": 26098348989,	
                                "deferredTaxAssets": 7855743207,	
                                "prepayments": 181047015237,	
                                "totalOtherLongTermAssets": 215001107433	
                            },	
                            "investmentProperties": {	
                                "cost": 191327232874,	
                                "totalInvestmentProperties": 109961268939,	
                                "accumulatedDepreciation": -81365963935	
                            },	
                            "longTermAssetsInProgress": {	
                                "totalLongTermAssetsInProgress": 131645367989,	
                                "longTermAssetsInProgress": 131645367989,	
                                "longTermWorkInProgressCosts": 0	
                            },	
                            "longTermInvestments": {	
                                "investmentsInOtherEntities": 1279365243151,	
                                "provisionForLongTermFinancialInvestments": -62506533483,	
                                "totalLongTermInvestments": 127645423169640,	
                                "heldToMaturityInvestments": 123543648618749,	
                                "investmentsInSubsidiaries": 0,	
                                "investmentsInJointVenturesAndAssociates": 2884915841223	
                            },	
                            "fixedAssets": {	
                                "intangibleAssets": {	
                                    "cost": 1840590207970,	
                                    "accumulatedAmortisation": -822369186322,	
                                    "totalIntangibleAssets": 1018221021648	
                                },	
                                "financeLeaseFixedAssets": {	
                                    "cost": 0,	
                                    "totalFinanceLeaseFixedAssets": 0,	
                                    "accumulatedDepreciation": 0	
                                },	
                                "totalFixedAssets": 1890638249670,	
                                "tangibleFixedAssets": {	
                                    "cost": 2726029379554,	
                                    "totalTangibleFixedAssets": 872417228022,	
                                    "accumulatedDepreciation": -1853612151532	
                                }	
                            },	
                            "longTermReceivables": {	
                                "longTermReceivablesFromCustomers": 0,	
                                "internalLongTermReceivables": 0,	
                                "otherLongTermReceivables": {	
                                    "otherLongTermReceivables": 0,	
                                    "totalOtherLongTermReceivables": 66916382934,	
                                    "insuranceDeposits": 66916382934	
                                },	
                                "provisionForDoubtfulLongTermReceivables": 0,	
                                "capitalInAffiliatedUnits": 0,	
                                "totalLongTermReceivables": 66916382934	
                            }	
                        }	
                    },	
                    "resources": {	
                        "totalResources": 251286326838124,	
                        "liabilities": {	
                            "currentLiabilities": {	
                                "otherShortTermPayables": 395628174229,	
                                "payablesToEmployees": 1702090155645,	
                                "taxesAndPayablesToState": 211453081628,	
                                "totalCurrentLiabilities": 40840468409215,	
                                "bonusAndWelfareFund": 0,	
                                "shortTermAccruedExpenses": 141601337253,	
                                "shortTermBorrowingsAndFinanceLeases": 2910226356811,	
                                "governmentBondRepurchaseTransactions": 32123608859706,	
                                "internalPayables": 0,	
                                "shortTermTradePayables": {	
                                    "insuranceOperationPayables": 2370393614148,	
                                    "tradeAndServicePayables": 63568872587,	
                                    "totalShortTermTradePayables": 2433962486735	
                                },	
                                "unearnedCommissionIncome": 382055501051,	
                                "provisionForShortTermLiabilities": 0,	
                                "priceStabilizationFund": 260153881426,	
                                "unearnedRevenue": 258502574731,	
                                "shortTermAdvancesFromCustomers": 21186000000	
                            },	
                            "totalLiabilities": 227720439778201,	
                            "longTermLiabilities": {	
                                "deferredIncomeTaxPayable": 2731324749,	
                                "longTermInternalPayables": 0,	
                                "longTermUnearnedRevenue": 0,	
                                "otherLongTermPayables": 303139567653,	
                                "longTermBorrowings": 0,	
                                "totalLongTermLiabilities": 186879971368986,	
                                "provisionForLongTermLiabilities": 0,	
                                "longTermTradePayables": 0,	
                                "scienceAndTechnologyDevelopmentFund": 0,	
                                "insuranceBusinessProvision": {	
                                    "catastropheProvision": 186907656143,	
                                    "interestRateCommitmentProvision": 16741736693139,	
                                    "other": 0,	
                                    "resilienceProvision": 0,	
                                    "totalInsuranceBusinessProvision": 186574100476584,	
                                    "mathematicalProvision": 5451808363226,	
                                    "equalizationProvision": 412275456267,	
                                    "unearnedPremiumProvision": 157148585024401,	
                                    "dividendProvision": 3521002598958,	
                                    "claimsProvision": 3111784684450	
                                },	
                                "longTermDepositAndMortgage": 0	
                            }	
                        },	
                        "equity": {	
                            "ownersEquity": {	
                                "preferredShares": 0,	
                                "totalOwnersEquity": 23565887059923,	
                                "treasuryShares": 0,	
                                "foreignExchangeDifferences": 15445192000,	
                                "otherOwnersCapital": 0,	
                                "reorganizationSupportFund": 0,	
                                "nonControllingInterests": 974335175004,	
                                "sharePremium": 7310458742807,	
                                "shareCapital": {	
                                    "totalShareCapital": 7423227640000,	
                                    "paidInCapital": 7423227640000	
                                },	
                                "assetRevaluationSurplus": 0,	
                                "developmentInvestmentFund": 2933853033569,	
                                "otherEquityFunds": 103568802818,	
                                "retainedEarnings": {	
                                    "retainedEarningsCurrent": 2007200429930,	
                                    "totalRetainedEarnings": 4007066089089,	
                                    "retainedEarningsPrevious": 1999865659159	
                                }	
                            },	
                            "totalEquity": 23565887059923,	
                            "provisionStatutory": 797932384636	
                        }	
                    }	
                }	
            ]	
        },	
        "companyType": "INSURANCE",	
        "businessTypeId": 1	
    }	
]	
```

# 2. Báo cáo kết quả hoạt động kinh doanh

## 2.1. Doanh nghiệp sản xuất
```json
[	
    {	
        "ticker": "HPG",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "incomeStatement": [	
                {	
                    "earningsPerShare": {	
                        "epsDiluted": 0,	
                        "epsBasic": 0	
                    },	
                    "taxExpenses": {	
                        "currentIncomeTaxExpense": -503217741562,        	
                        "totalTaxExpenses": -477081785345,	
                        "deferredIncomeTaxExpense": 26135956217	
                    },	
                    "netOperatingProfit": 3302799103110,	
                    "costOfSales": -30126073473488,	
                    "revenue": {	
                        "netRevenue": 34490982426689,	
                        "deductions": -741215175825,	
                        "grossRevenue": 35232197602514	
                    },	
                    "netProfitAfterTax": 2809594315351,	
                    "operatingIncomeExpenses": {	
                        "financialExpenses": {	
                            "totalFinancialExpenses": -1015139809937,    	
                            "interestExpenses": -562492663846	
                        },	
                        "sellingExpenses": -230212058532,	
                        "generalAndAdminExpenses": -517318083678,        	
                        "shareOfProfitInAssociates": 0,	
                        "financialIncome": 700560102056	
                    },	
                    "profitAttribution": {	
                        "attributableToParentCompany": 2808645369171,    	
                        "attributableToNonControllingInterest": 948946180	
                    },	
                    "otherIncomeExpenses": {	
                        "otherIncome": 225300683318,	
                        "otherExpenses": -241423685732,	
                        "netOtherIncomeExpenses": -16123002414	
                    },	
                    "grossProfit": 4364908953201,	
                    "netProfitBeforeTax": 3286676100696	
                }	
            ]	
        },	
        "companyType": "MANUFACTURING",	
        "businessTypeId": 3	
    }	
]	
```

## 2.2. Ngân hàng
```json
[	
    {	
        "ticker": "VCB",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "incomeStatement": [	
                {	
                    "tradingAndInvestmentIncome": {	
                        "netGainLossFromInvestmentSecurities": 2735000000,	
                        "netGainLossFromTradingSecurities": 4472000000,	
                        "netGainLossFromForeignCurrencyAndGold": 1586183000000	
                    },	
                    "earningsPerShare": {	
                        "epsDiluted": 0,	
                        "epsBasic": 1050	
                    },	
                    "taxExpenses": {	
                        "currentIncomeTaxExpense": -2274403000000,	
                        "totalTaxExpenses": -2132756000000,	
                        "deferredIncomeTaxExpense": 141647000000	
                    },	
                    "operatingExpenses": -7040188000000,	
                    "interestIncome": {	
                        "interestAndSimilarIncome": 23581262000000,	
                        "netInterestIncome": 13842332000000,	
                        "interestAndSimilarExpenses": -9738930000000	
                    },	
                    "operatingProfitBeforeProvision": 10670348000000,	
                    "provisionForCreditLosses": 32329000000,	
                    "profitAttribution": {	
                        "attributableToParentCompany": 8565378000000,	
                        "nonControllingInterest": -4543000000	
                    },	
                    "netProfitBeforeTax": 10702677000000,	
                    "feeAndCommissionIncome": {	
                        "feesAndCommissionIncome": 3368816000000,	
                        "netFeeAndCommissionIncome": 923783000000,	
                        "feesAndCommissionExpenses": -2445033000000	
                    },	
                    "totalOperatingIncome": 17710536000000,	
                    "netProfitAfterTax": 8569921000000,	
                    "dividendsIncome": 66378000000,	
                    "otherIncomeExpenses": {	
                        "otherIncome": 1833975000000,	
                        "otherExpenses": -549322000000,	
                        "netOtherIncomeExpenses": 1284653000000	
                    }	
                }	
            ]	
        },	
        "companyType": "BANKING",	
        "businessTypeId": 1	
    }	
]	
```

## 2.3. Doanh nghiệp chứng khoán
```json
[	
    {	
        "ticker": "SSI",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "incomeStatement": [	
                {	
                    "operatingIncome": {	
                        "revenueFromOtherOperatingActivities": 159228084869,	
                        "revenueFromBrokerageServices": 319081080523,	
                        "revenueFromStockInvestmentAdvisoryServices": 5076593090,      	
                        "gainFromLoansAndReceivables": 570733012956,	
                        "revenueFromUnderwritingServices": 9645301369,	
                        "revenueFromFinancialAdvisoryServices": 9909312725,	
                        "totalOperatingRevenue": 2221274987684,	
                        "gainFromFinancialAssetsAtFVTPL": {	
                            "dividendsAndInterestFromFVTPL": 458116449700,	
                            "gainFromDisposalOfFinancialAssetsAtFVTPL": 533797567725,  	
                            "gainFromRevaluationOfFinancialAssetsAtFVTPL": 77445924780,	
                            "totalGainFromFinancialAssetsAtFVTPL": 1069359942205       	
                        },	
                        "gainFromHeldToMaturityInvestments": 70365036207,	
                        "gainFromAvailableForSaleAFSFinancialAssets": -1920489739,     	
                        "gainFromDerivative": 0,	
                        "revenueFromSecuritiesCustodianServices": 9797113479	
                    },	
                    "earningsPerShare": {	
                        "netIncomeAvailableToCommonShareholders": 0,	
                        "dilutedEarningsPerShare": 0,	
                        "basicEarningsPerShare": 0	
                    },	
                    "taxExpenses": {	
                        "currentIncomeTaxExpense": -132825428063,	
                        "totalIncomeTaxExpenses": -116405977346,	
                        "deferredIncomeTaxExpense": 16419450717	
                    },	
                    "generalAndAdministrativeExpenses": -92749211365,	
                    "sellingExpenses": 0,	
                    "operatingExpenses": {	
                        "otherExpenses": {	
                            "totalOtherExpenses": -122952284234	
                        },	
                        "totalOperatingExpenses": -1205443690595,	
                        "expensesForSecuritiesInvestmentAdvisoryServices": -4615364040,	
                        "provisionExpenseForInvestmentLosses": -34746394527,	
                        "expensesForSecuritiesCustodianServices": -10506493998,        	
                        "expensesForBrokerageServices": -311643887858,	
                        "lossFromDerivative": 0,	
                        "expensesForProprietaryTradingActivities": -40974083587,       	
                        "lossFromHeldToMaturityInvestments": 0,	
                        "expensesForFinancialAdvisoryActivities": -9731408322,	
                        "lossFromFinancialAssetsAtFVTPL": {	
                            "totalLossFromFinancialAssetsAtFVTPL": -661210512559,	
                            "lossFromRevaluationOfFinancialAssetsAtFVTPL": -357736593994,	
                            "transactionCostOfAcquisitionOfFinancialAssetsAtFVTPL": -3721644754,	
                            "lossFromDisposalOfFinancialAssetsAtFVTPL": -299752273811	
                        },	
                        "expensesForUnderwritingAndIssuanceAgencyServices": -9063261470,	
                        "lossFromAvailableForSaleAFSFinancialAssets": 0	
                    },	
                    "otherIncomeAndExpenses": {	
                        "otherOperatingIncome": 746639592,	
                        "netOtherIncomeOrExpenses": -1340488587,	
                        "otherOperatingExpenses": -2087128179	
                    },	
                    "otherComprehensiveIncomeAfterTax": {	
                        "gainLossFromValuationOfDerivatives": 0,	
                        "totalOtherComprehensiveIncome": 9245392000,	
                        "gainLossDistributedFromInvestmentsInSubsidiariesAssociatesAndJointVentures": 0,	
                        "gainLossFromRevaluationOfAvailableForSalesFinancialAssets": 9245392000,	
                        "preDistributedGainLossFromInvestmentsInSubsidiariesAssociatesAndJointVentures": 0,	
                        "gainLossFromRevaluationOfDerivatives": 0,	
                        "gainLossFromForeignExchangeDifferenceOfOverseasOperations": 0,	
                        "gainLossFromRevaluationOfFixedAssetsUsingFairValueModel": 0	
                    },	
                    "profitBeforeTax": {	
                        "accountingProfitBeforeTax": 554769762801,	
                        "unrealizedProfitBeforeTax": -270310131826,	
                        "realizedProfitBeforeTax": 825079894627	
                    },	
                    "financialIncome": {	
                        "gainFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures": 0,	
                        "totalFinancialIncome": 43964730178,	
                        "otherInvestmentIncome": 27178025374,	
                        "realizedAndUnrealizedGainFromChangesInForeignExchangesRates": 10168314028,	
                        "dividendInterestFromDemandDeposits": 6618390776	
                    },	
                    "comprehensiveIncome": {	
                        "totalComprehensiveIncome": 447609177455,	
                        "attributableToShareholders": 447609177455,	
                        "attributableToNonControllingInterests": 0	
                    },	
                    "profitAfterTax": {	
                        "profitAfterTaxAfterAppropriations": 0,	
                        "netProfitAfterTax": 438363785455,	
                        "profitAfterTaxAttributableToNoncontrollingInterest": 10625619023,	
                        "profitAfterTaxAttributableToTheParentCompanyOwners": 427738166432	
                    },	
                    "financialExpenses": {	
                        "totalFinancialExpenses": -410936564514,	
                        "interestExpenses": -405752832021,	
                        "shareOfProfitLossFromJointVentures": 0,	
                        "otherInvestmentExpenses": -2073184310,	
                        "provisionForInvestmentLoss": 0,	
                        "realizedAndUnrealizedLossFromChangesInForeignExchangesRates": -3110548183,	
                        "lossFromDisposalsOrSalesOfInvestmentsInSubsidiariesAssociatesAndJointVentures": 0	
                    },	
                    "grossProfit": 1015831297089,	
                    "operatingProfit": 556110251388	
                }	
            ]	
        },	
        "companyType": "SECURITIES",	
        "businessTypeId": 3	
    }	
]	
```

## 2.4. Doanh nghiệp bảo hiểm
```json
[	
    {	
        "ticker": "BVH",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "incomeStatement": [	
                {	
                    "catastropheReserveExpenses": 0,	
                    "changeInClaimReserve": {	
                        "outwardReserveChange": -340255471042,	
                        "totalChangeInClaimReserve": -48478760054,	
                        "directAndInwardReserveChange": 291776710988        	
                    },	
                    "deductions": {	
                        "subrogationRecoveries": 0,	
                        "totalDeductions": 1185344534,	
                        "salvages": 1185344534,	
                        "recoveriesReinsuranceCeded": 0	
                    },	
                    "profitBeforeTax": 698671288788,	
                    "changeInCatastropheReserve": -13043873653,	
                    "otherInsuranceOperatingExpenses": {	
                        "directInsuranceExpenses": 0,	
                        "totalOtherExpenses": -895651685256,	
                        "reinsuranceAssumedExpenses": 0,	
                        "otherUnderwritingExpenses": {	
                            "riskMinimization": 0,	
                            "lossAdjustingAndRiskAssessment": 0,	
                            "commissions": -600541584531,	
                            "sellingExpenses": 0,	
                            "totalOtherUnderwritingExpenses": -895651685256,	
                            "thirdPartyRecourse": 0,	
                            "fullyIndemnifiedGoods": 0,	
                            "others": -295110100725	
                        },	
                        "reinsuranceCededExpenses": 0	
                    },	
                    "gainLossJointVentures": 35957841680,	
                    "profitAfterTax": {	
                        "attributableToParentCompany": 560335389500,        	
                        "netProfitAfterTax": 575011518636,	
                        "attributableToNonControllingInterests": 14676129136	
                    },	
                    "claimAndMaturityPaymentExpenses": -5320087494877,      	
                    "reinsurancePremiumCeded": {	
                        "otherCededPremiumDeductions": 0,	
                        "changeInUnearnedCededPremiumReserve": 1090256117,  	
                        "totalReinsurancePremiumCeded": -882898418406,      	
                        "cededPremiumRefunds": 0,	
                        "reinsurancePremiumCeded": -883988674523	
                    },	
                    "earningsPerShare": {	
                        "ePSDiluted": 0,	
                        "ePSBasic": 755	
                    },	
                    "taxExpenses": {	
                        "currentIncomeTaxExpense": -118793503363,	
                        "totalTaxExpenses": -123659770152,	
                        "deferredIncomeTaxExpense": -4866266789	
                    },	
                    "insurancePremium": {	
                        "reinsurancePremiumAssumed": 64803201619,	
                        "changeInUnearnedPremiumReserve": -46123818050,	
                        "totalRevenueFromInsurancePremium": 11165344381246,	
                        "directWrittenPremium": 11146664997677	
                    },	
                    "otherActivities": {	
                        "incomeFromOtherActivities": 98264493429,	
                        "expensesFromOtherActivities": -124231299550,	
                        "netOperatingIncomeOther": -25966806121	
                    },	
                    "grossInsuranceOperatingProfit": 67149647564,	
                    "generalAndAdminExpenses": {	
                        "otherOperations": 0,	
                        "bankingOperation": 0,	
                        "insuranceOperation": -1560836151613,	
                        "totalGeneralAndAdmin": -1560836151613	
                    },	
                    "sellingExpenses": -409320319252,	
                    "equalisationReserve": 0,	
                    "netInsurancePremium": 10282445962840,	
                    "recoveriesFromReinsuranceCeded": 455031247569,	
                    "commissionAndOtherIncome": {	
                        "otherIncome": {	
                            "totalOtherIncome": 0,	
                            "reinsuranceAssumedIncome": 0,	
                            "reinsuranceCededIncome": 0,	
                            "otherActivitiesIncome": 0	
                        },	
                        "totalCommissionAndOtherIncome": 184933662369,	
                        "commissionOnReinsuranceCeded": 184933662369	
                    },	
                    "financialActivities": {	
                        "profitFinancialActivities": 2579764071055,	
                        "financialExpenses": -629539261479,	
                        "financialIncome": 3209303332534	
                    },	
                    "netRevenueFromInsuranceBusiness": 10467379625209,	
                    "claimExpensesReinsuranceAssumed": -32006260964,	
                    "totalDirectInsuranceExpenses": -10400229977645,	
                    "realEstateActivities": {	
                        "costRealEstate": 0,	
                        "revenueRealEstate": 0,	
                        "realEstateInvestmentProfits": 0	
                    },	
                    "changeInMathematicsReserves": -4547178494944,	
                    "totalInsuranceClaimSettlementExpenses": -9491534418736,	
                    "operatingProfitFromInsuranceOperation": {	
                        "netOperatingProfitFromInsuranceOperation": -1903006823301,	
                        "gainLossFromNonLifeInsurance": -1903006823301,	
                        "gainLossFromLifeInsurance": 0	
                    },	
                    "bankingActivities": {	
                        "expensesBanking": 0,	
                        "netOperatingIncomeBanking": 0,	
                        "incomeBanking": 0	
                    },	
                    "increaseInUnearnedPremiumReserveAndTechnical": 0,	
                    "otherIncomeExpenses": {	
                        "otherIncome": 13474172215,	
                        "otherExpenses": -1551166740,	
                        "netOtherIncome": 11923005475	
                    },	
                    "claimExpensesRetainedRisks": -4895877163738	
                }	
            ]	
        },	
        "companyType": "INSURANCE",	
        "businessTypeId": 1	
    }	
]	
```

# 3. Báo cáo lưu chuyển tiền tệ

## 3.1. Doanh nghiệp sản xuất
```json
[	
    {	
        "ticker": "HPG",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "cashFlow": [	
                {	
                    "cashAndCashEquivalentsAtTheEndOfPeriod": 6887646139852,      	
                    "cashAndCashEquivalentsAtTheBeginningOfPeriod": 8500998079280,	
                    "cashFlowsFromInvestingActivities": {	
                        "proceedsFromDisposalOfFixedAssets": 443699573180,        	
                        "purchasesOfFixedAndLongTermAssets": -7257089099480,      	
                        "proceedsFromDivestmentInOtherEntities": 31246619001,     	
                        "investmentsInOtherEntities": 0,	
                        "netCashFromInvestingActivities": -9083163490691,	
                        "loansGrantedPurchasesOfDebtInstruments": -6360476824332,	
                        "dividendsAndInterestReceived": 187519990129,	
                        "collectionOfLoansSalesOfDebtInstruments": 3871936250811  	
                    },	
                    "effectOfForeignExchangeDifferences": 5563161728,	
                    "netCashFlow": -1618915101156,	
                    "cashFlowsFromOperatingActivities": {	
                        "operatingProfitBeforeChanges": {	
                            "changesInReceivables": 971968926351,	
                            "operatingProfitBeforeChanges": 4955838305029,        	
                            "changesInPrepaidExpenses": 129299221688,	
                            "changesInTradingSecurities": 0,	
                            "changesInPayables": 4023222874211,	
                            "incomeTaxPaid": -51647870077,	
                            "otherPaymentsOnOperatingActivities": -194420019511,  	
                            "changesInInventories": -6209983876378,	
                            "otherReceiptsFromOperatingActivities": 447272727,    	
                            "interestPaid": -529644932828	
                        },	
                        "adjustments": {	
                            "depreciationAndAmortisation": 1693028331093,	
                            "provisions": -61035121811,	
                            "unrealisedForeignExchangeGainLoss": 227751228845,    	
                            "amortisationOfGoodwill": 12295891969,	
                            "otherAdjustments": 0,	
                            "profitLossFromInvestingActivities": -765370789609,   	
                            "interestExpense": 562492663846	
                        },	
                        "netCashFromOperatingActivities": 3095079901212,	
                        "profitBeforeTax": 3286676100696	
                    },	
                    "cashFlowsFromFinancingActivities": {	
                        "proceedsFromIssueOfShares": 103000000000,	
                        "dividendsPaid": -2343960741,	
                        "netCashFromFinancingActivities": 4369168488323,	
                        "proceedsFromLoans": 42414841815225,	
                        "repaymentOfLoans": -38146312226161,	
                        "financeLeasePrincipalPayments": 0,	
                        "paymentsForShareReturnsAndRepurchases": -17140000	
                    }	
                }	
            ]	
        },	
        "companyType": "MANUFACTURING",	
        "businessTypeId": 3	
    }	
]	
```

## 3.2. Ngân hàng
```json
[	
    {	
        "ticker": "VCB",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "cashFlow": [	
                {	
                    "cashAndCashEquivalentsAtTheEndOfPeriod": 430614185000000,	
                    "cashAndCashEquivalentsAtTheBeginningOfPeriod": 314023125000000,	
                    "cashFlowsFromInvestingActivities": {	
                        "proceedsFromDisposalOfInvestmentProperties": 0,	
                        "proceedsFromDisposalOfFixedAssets": 5492000000,	
                        "purchasesOfInvestmentProperties": 0,	
                        "proceedsFromDivestmentInOtherEntities": 0,	
                        "paymentsOnDisposalOfInvestmentProperties": 0,	
                        "investmentsInOtherEntities": 0,	
                        "paymentsForPurchasesOfFixedAssetsAndOtherLongTermAssets": -531176000000,	
                        "paymentsOnDisposalOfFixedAssets": -809000000,	
                        "netCashFromInvestingActivities": -501783000000,	
                        "dividendsAndInterestReceived": 24710000000	
                    },	
                    "effectOfForeignExchangeDifferences": 0,	
                    "netCashFlow": 116591060000000,	
                    "cashFlowsFromOperatingActivities": {	
                        "netFeeAndCommissionIncomeReceived": 570544000000,	
                        "interestAndSimilarIncomeReceived": 23060402000000,	
                        "interestAndSimilarExpensesPaid": -9657477000000,	
                        "netReceiptsFromTradingActivities": 1303964000000,	
                        "cashFlowFromOperatingActivitiesBeforeChangesInOperatingAssetsAndLiabilities": 10425121000000,	
                        "netCashFromOperatingActivities": 117112806000000,	
                        "changesInOperatingLiabilities": {	
                            "changesInDepositsAndBorrowingsToOtherCreditInstitutions": 17273590000000,	
                            "changesInDerivativesAndOtherFinancialLiabilities": -116988000000,	
                            "changesInFundsFromGovAndInstitutions": 527000000,	
                            "paymentFromReserves": -646942000000,	
                            "changesInDepositsFromCustomers": 84593830000000,	
                            "changesInLoansFromStateAndSBV": 41944064000000,	
                            "changesInValuablePapersIssued": -2776436000000,	
                            "changesInOtherOperatingLiabilities": 2376448000000	
                        },	
                        "changesInOperatingAssets": {	
                            "derivativesAndOtherFinancialAssets": -1314434000000,	
                            "changeInLoansToCustomers": -48047224000000,	
                            "changesInDepositsAndLoansToOtherCreditInstitutions": 6503970000000,	
                            "changesInHeldForTradingSecuritiesAndInvestmentSecurities": 2299942000000,	
                            "provisionForLoanLosses": -3877864000000,	
                            "changesInOtherOperatingAssets": 8475202000000	
                        },	
                        "corporateIncomeTaxPaid": -81798000000,	
                        "otherIncomeExpenses": -343813000000,	
                        "salariesAndOperatingExpensesPaid": -6050484000000,	
                        "receiptsFromDebtsWrittenOff": 1623783000000	
                    },	
                    "cashFlowsFromFinancingActivities": {	
                        "paymentsForRedemptionOfBonds": 0,	
                        "proceedsFromIssueOfShares": 0,	
                        "proceedsFromConvertibleBonds": 0,	
                        "dividendsPaid": -19963000000,	
                        "netCashFromFinancingActivities": -19963000000,	
                        "purchaseOfTreasuryShares": 0,	
                        "proceedsFromSellingTreasuryShares": 0	
                    }	
                }	
            ]	
        },	
        "companyType": "BANKING",	
        "businessTypeId": 1	
    }	
]	
```

## 3.3. Doanh nghiệp chứng khoán
```json
[	
    {	
        "ticker": "SSI",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "cashFlow": [	
                {	
                    "cashAndCashEquivalentsAtTheEndOfPeriod": {	
                        "cashEquivalents": 30030246575,	
                        "totalCashAndCashEquivalentsAtTheEndOfPeriod": 239000238200,	
                        "effectOfForeignExchangeDifferences": 2174347516,	
                        "cash": 206795644109	
                    },	
                    "cashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod": {	
                        "cashEquivalent": 0,	
                        "totalCashAndCashEquivalentsOfCustomersAtTheBeginningOfPeriod": 6343236859628,	
                        "effectOfForeignExchangeDifferences": 0,	
                        "cashAndBankDeposit": {	
                            "investorDepositSecuritiesCompanyMethod": {	
                                "investorDepositWithTerm": 0,	
                                "totalInvestorDepositSecuritiesCompanyMethod": 6319318004994	
                            },	
                            "depositsOfSecuritiesIssuers": {	
                                "totalDepositsOfSecuritiesIssuers": 11708460936,	
                                "issuingOrganizationDepositWithTerm": 0	
                            },	
                            "depositForSecuritiesClearing": 0,	
                            "customersGeneralDeposit": 12210393698,	
                            "totalCashAndBankDeposit": 6343236859628	
                        }	
                    },	
                    "cashAndCashEquivalentsOfCustomersAtTheEndOfPeriod": {	
                        "cashEquivalent": 0,	
                        "totalCashAndCashEquivalentsOfCustomersAtTheEndOfPeriod": 4941400793936,      	
                        "effectOfForeignExchangeDifferences": 0,	
                        "cashAndBankDeposit": {	
                            "investorDepositSecuritiesCompanyMethod": {	
                                "investorDepositWithTerm": 0,	
                                "totalInvestorDepositSecuritiesCompanyMethod": 4919023915622	
                            },	
                            "depositsOfSecuritiesIssuers": {	
                                "totalDepositsOfSecuritiesIssuers": 11297197134,	
                                "issuingOrganizationDepositWithTerm": 0	
                            },	
                            "depositForSecuritiesClearing": 0,	
                            "customersGeneralDeposit": 11079681180,	
                            "totalCashAndBankDeposit": 4941400793936	
                        }	
                    },	
                    "cashAndCashEquivalentsAtTheBeginningOfPeriod": {	
                        "cashEquivalents": 0,	
                        "effectOfForeignExchangeDifferences": 512993328,	
                        "cash": 660773688392,	
                        "totalCashAndCashEquivalentsAtTheBeginningOfPeriod": 661286681720	
                    },	
                    "cashFlowsFromInvestingActivities": {	
                        "proceedsFromDisposalOfFixAssetsAndInvestmentPropertiesAndOtherLongTermAssets": 83484415636,	
                        "collectionOfLoansAndProceedsFromSalesOfDebtsInstruments": 0,	
                        "proceedsFromDivestmentInOtherEntities": 0,	
                        "purchasesAndConstructionOfFixedAssetsAndInvestmentPropertiesAndOtherLongTermAssets": -290162312537,	
                        "investmentsInOtherEntities": -820000000000,	
                        "netCashFromInvestingActivities": -1026677896901,	
                        "dividendsAndInterestReceived": 0,	
                        "loansGrantedAndPurchasesOfDebtInstruments": 0	
                    },	
                    "cashFlowsFromBrokerageAndTrustActivities": {	
                        "cashReceivedForThePurposeOfMandatedInvestmentOfClients": -50024721687,	
                        "cashPaidOnTransactionErrors": 0,	
                        "cashInflowFromMandatedSales": 0,	
                        "cashInflowFromCurrentAccountOfClients": 0,	
                        "cashPaidForThePurposeOfClientsTransactionSettlement": -167590257153513,	
                        "cashReceivedOnTransactionErrors": 0,	
                        "cashOutflowFromCurrentAccountOfClients": 0,	
                        "cashInflowOnLoanFromSettlementAssistanceFund": 0,	
                        "cashOutflowFromSecuritiesPurchase": -106053636536510,	
                        "cashPaidForDepositoryFee": -8838075903,	
                        "cashInflowFromSecuritiesBroking": 112446988164988,	
                        "cashOutflowFromMandatedSales": 0,	
                        "cashPaidForThePurposeOfMandatedInvestmentOfClients": 0,	
                        "netCashFromBrokerageAndTrustActivities": -1401836065692,	
                        "cashReceivedForPurposeOfTransactionsOfClients": 160188523820216,	
                        "cashReceivedFromIssuingOrganizations": 1128179917000,	
                        "cashOutflowOnRepayingFromSettlementAssistanceFund": 0,	
                        "cashPaidToIssuingOrganizations": -1462771480283	
                    },	
                    "netCashFlow": -422286443520,	
                    "cashFlowsFromOperatingActivities": {	
                        "decreaseInNonMonetaryRevenue": {	
                            "reversalOfProvision": 0,	
                            "gainFromRevaluationOfFinancialAssetsAtFVTPL": -77445924780,	
                            "totalDecreaseInNonMonetaryRevenue": -77445924780,	
                            "gainFromAFSReclassification": 0,	
                            "otherGains": 0	
                        },	
                        "operatingProfitBeforeChanges": {	
                            "operatingProfitBeforeChanges": -6542795640146,	
                            "changesInPrepaidExpenses": -5864781300,	
                            "changesInTaxAndPayablesToAuthority": 17167054630,	
                            "changesInFVTPLFinancialAssets": -5337039144331,	
                            "changesInAvailableForSaleFinancialAssets": 3235887200,	
                            "changesInTradePayables": -94364324227,	
                            "interestExpensesPaid": -386222868753,	
                            "incomeTaxPaid": -173297277481,	
                            "changesInPayableExpensesExcludingInterest": -26530110226,	
                            "changesInOtherReceivables": -402214172791,	
                            "changesInOtherAssets": 90249742232,	
                            "changesInPayableFromFinancialAssetTransactionError": 0,	
                            "changesInHeldToMaturityInvestments": 1596096206907,	
                            "changesInPayablesToEmployees": 45161121770,	
                            "changesInLoansGiven": -2500301689956,	
                            "otherPayments": {	
                                "otherExpenses": -2918076634,	
                                "totalOtherPayments": -2918076634,	
                                "businessIncomeTaxPaid": 0,	
                                "interestPaid": 0	
                            },	
                            "changesInReceivableFromSellingFinancialAssets": -276145542000,	
                            "changesInEmployeesWelfareContributions": -190110604,	
                            "changesInReceivableFromInterestOfFinancialAssets": 0,	
                            "changesInReceivableFromTransactionErrors": 0,	
                            "changesInOtherPayables": -115346181038,	
                            "otherReceipts": {	
                                "interestReceived": 0,	
                                "totalOtherReceipts": 1036691380044,	
                                "otherReceivables": 1036691380044	
                            },	
                            "changesInReceivableFromServicesRendered": -10962753588	
                        },	
                        "adjustments": {	
                            "depreciationAndAmortisation": 23294171773,	
                            "provisions": 34762788174,	
                            "totalAdjustments": -664031531181,	
                            "unrealisedForeignExchangeGainLoss": -9980537388,	
                            "interestIncomeAndDividend": -1026919751205,	
                            "amortisationOfGoodwill": 0,	
                            "accruedExpenses": 0,	
                            "otherAdjustments": 2956074154,	
                            "profitLossFromInvestingActivities": -93897108710,	
                            "interestExpense": 405752832021	
                        },	
                        "netCashFromOperatingActivities": -6369727968576,	
                        "increaseInNonMonetaryExpenses": {	
                            "lossOnHeldToMaturityInvestments": 0,	
                            "otherLoss": 2035000000,	
                            "provisionForLongTermInvestments": 0,	
                            "lossFromRevaluationOfFinancialAssetsAtFVTPL": 357736593994,	
                            "lossOnAFSReclassification": 0,	
                            "lossOnLoansGiven": 3770736,	
                            "totalIncreaseInNonMonetaryExpenses": 359775364730	
                        },	
                        "netProfitBeforeTax": 554769762801	
                    },	
                    "cashFlowsFromFinancingActivities": {	
                        "proceedsFromIssueOfShares": 2263708005000,	
                        "dividendsPaid": -1505372068000,	
                        "netCashFromFinancingActivities": 6974119421957,	
                        "repaymentOfLoans": {	
                            "financialAssetsLoans": 0,	
                            "otherLoans": -66794440486399,	
                            "totalRepaymentOfLoans": -66794440486399,	
                            "settlementAssistanceFund": 0	
                        },	
                        "proceedsFromLoans": {	
                            "otherLoans": 73010223971356,	
                            "settlementAssistanceFund": 0,	
                            "totalProceedsFromLoans": 73010223971356	
                        },	
                        "financeLeasePrincipalPayments": 0,	
                        "paymentsForShareReturnsAndRepurchases": 0	
                    }	
                }	
            ]	
        },	
        "companyType": "SECURITIES",	
        "businessTypeId": 3	
    }	
]		
```

## 3.4. Doanh nghiệp bảo hiểm
```json
[	
    {	
        "ticker": "BVH",	
        "year": 2024,	
        "quarter": 4,	
        "reportType": "consolidated",	
        "audited": true,	
        "financialStatement": {	
            "cashFlow": [	
                {	
                    "cashAndCashEquivalentsAtTheEndOfPeriod": 1464088127113,	
                    "cashAndCashEquivalentsAtTheBeginningOfPeriod": 2492005463163,	
                    "cashFlowsFromInvestingActivities": {	
                        "collectionOfLoansAndProceedsFromSalesOfDebtsInstruments": 16547744977558,	
                        "loansGrantedAndDebtInstrumentsPurchased": -31477820550999,	
                        "purchasesAndConstructionOfFixedAndLongTermAssets": -43750705265,	
                        "proceedsFromDisposalOfFixedAndLongTermAssets": 431618182,	
                        "proceedsFromDivestmentInOtherEntities": 0,	
                        "investmentsInOtherEntities": -245308499,	
                        "netCashFromInvestingActivities": -12031799087740,	
                        "dividendsAndInterestReceived": 2941840881283	
                    },	
                    "effectOfForeignExchangeDifferences": 190850472,	
                    "netCashFlow": -1028108186522,	
                    "cashFlowsFromOperatingActivities": {	
                        "operatingProfitBeforeChanges": {	
                            "changesInReceivables": {	
                                "reinsuranceAssumedReceivables": 0,	
                                "otherReceivablesFromInsurance": 1238632024209,	
                                "reinsuranceCededReceivables": 0,	
                                "interCompanyReceivablesPayables": 0,	
                                "totalChangesInReceivables": 1238632024209,	
                                "grossWrittenPremiumReceivables": 0	
                            },	
                            "payablesExcludingInterestAndTax": {	
                                "grossWrittenPremiumPayables": 0,	
                                "reinsuranceCededPayables": 0,	
                                "payablesToEmployees": 0,	
                                "otherPayablesFromInsurance": -481523964546,	
                                "reinsuranceAssumedPayables": 0,	
                                "totalChangesInPayables": -481523964546	
                            },	
                            "operatingProfitBeforeChanges": 2236492652239,	
                            "changesInPrepaidExpenses": -121078201649,	
                            "changesInTradingSecurities": 23790361850,	
                            "otherPaymentsOnOperatingActivities": -13300685403,	
                            "changesInInventories": -8633811127,	
                            "corporateIncomeTaxPaid": -119757549110,	
                            "otherReceiptsFromOperatingActivities": 0,	
                            "interestPaid": -31640508878	
                        },	
                        "adjustments": {	
                            "depreciationAndAmortisation": 114024389779,	
                            "provisions": 4332402833531,	
                            "unrealisedForeignExchangeGainLoss": 6037995155,	
                            "interestIncomeAndDividend": 0,	
                            "amortisationOfGoodwill": 0,	
                            "otherAdjustments": 0,	
                            "profitLossFromInvestingActivities": -3235181137860,	
                            "repoAndInterestExpenses": 320537282846	
                        },	
                        "netCashFromOperatingActivities": 2722980317585,	
                        "netProfitBeforeTax": 698671288788	
                    },	
                    "cashFlowsFromFinancingActivities": {	
                        "proceedsFromIssueOfShares": 0,	
                        "dividendsPaid": -767074656367,	
                        "netCashFromFinancingActivities": 8280710583633,	
                        "proceedsFromLoans": 12228301080000,	
                        "repaymentOfLoans": -3180515840000,	
                        "financeLeasePrincipalPayments": 0,	
                        "paymentsForShareReturnsAndRepurchases": 0	
                    }	
                }	
            ]	
        },	
        "companyType": "INSURANCE",	
        "businessTypeId": 1	
    }	
]	
```