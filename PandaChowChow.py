import quandl
import pandas as pd
import numpy as np

########################################################################################################################
#                      Panda Chow Chow                                                                                 #
#    - Pulls gobal economic data and returns a score based on historical norms,                                        #
#      a high score indicates growth, a low score indicates decline.                                                   #
#                                                                                                                      #
#    - Endogenous Analysis scores a country based on a standalone basis                                                #
#    - Exogenous Analysis scores two countries based on a relative scale to enable                                     #
#      trading that currency as a pair                                                                                 #
#                                                                                                                      #
#    -  Current support for USD, GBP and AUD                                                                           #
#                                                                                                                      #
########################################################################################################################
##All Endogenous Data Goes Here
def USEndoScore():

    def USGDP():
        GDP = (quandl.get("FRED/GDP", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        curGDP = GDP.iloc[-1, -1]
        return (curGDP)

    def USPMI():
        PMI = quandl.get("ISM/MAN_PMI", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=3)
        cPMI = PMI.iloc[-1, -1]
        prevPMI = PMI.iloc[-2, -1]
        maPMI = (cPMI + prevPMI + PMI.iloc[-3, -1]) / 3
        print("Current PMI is {}".format(cPMI))
        if cPMI > 50:
            if cPMI > prevPMI:            
                pmiscore = 7
            elif cPMI < prevPMI:
                if cPMI < maPMI:
                    pmiscore = -10
                elif cPMI > maPMI:
                    pmiscore = 3
        elif cPMI < 50:
            if cPMI > prevPMI:
                pmiscore = -3
            elif cPMI < prevPMI:
                if cPMI > maPMI:
                   pmiscore = 10
                elif cPMI < maPMI:
                    pmiscore = -6
        else:
            pmiscore = 0
        return(pmiscore)

    def USNMPMI():
        NMPMI = quandl.get("ISM/NONMAN_NMI", authtoken="8pyGLCjcAHgwZoTYFnNS", row=3)
        cPMI = NMPMI.iloc[-1, -1]
        prevPMI = NMPMI.iloc[-2, -1]
        maPMI = (cPMI + prevPMI + NMPMI.iloc[-3, -1]) / 3
        print("Current NMPMI is {}".format(cPMI))
        if cPMI > 50:
            if cPMI > prevPMI:            
                pmiscore = 7
            elif cPMI < prevPMI:
                if cPMI < maPMI:
                    pmiscore = -10
                elif cPMI > maPMI:
                    pmiscore = 3
        elif cPMI < 50:
            if cPMI > prevPMI:
                pmiscore = -3
            elif cPMI < prevPMI:
                if cPMI > maPMI:
                    pmiscore = 10
                elif cPMI < maPMI:
                    pmiscore = -6
        else:
            pmiscore = 0
        return(pmiscore)

    def UOMCS():
        MCS = quandl.get("UMICH/SOC1", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        MCS = MCS.iloc[-1, -1]
        print("Current University of Michigan Consumer Expectation Survey is {}".format(MCS))
        if MCS == 55:
            uom = 10
        elif MCS == 56:
            uom = 10
        elif MCS == 57:
            uom = 9
        elif MCS == 58:
            uom = 9
        elif MCS == 59:
            uom = 8
        elif MCS == 60:
            uom = 7
        elif MCS == 61:
            uom = 6
        elif MCS == 62:
            uom = 5
        elif MCS == 63:
            uom = -10
        elif MCS == 64:
            uom = -9
        elif MCS == 65:
            uom = -8
        elif MCS == 66:
            uom = -7
        elif MCS == 67:
            uom = -6
        elif MCS == 68:
            uom = -5
        elif MCS == 69:
            uom = -4
        elif MCS == 70:
            uom = -3
        elif MCS == 71:
            uom = -2
        elif MCS == 72:
            uom = -1
        elif MCS == 73:
            uom = -1
        elif MCS == 74:
            uom = 0
        elif MCS == 75:
            uom = 0
        elif MCS == 76:
            uom = 1
        elif MCS == 77:
            uom = 1
        elif MCS == 78:
            uom = 2
        elif MCS == 79:
            uom = 2
        elif MCS == 80:
            uom = 3
        elif MCS == 81:
            uom = 3
        elif MCS == 82:
            uom = 4
        elif MCS == 83:
            uom = 4
        elif MCS == 84:
            uom = 5
        elif MCS == 85:
            uom = 5
        elif MCS == 86:
            uom = 6
        elif MCS == 87:
            uom = 6
        elif MCS == 88:
            uom = 7
        elif MCS == 89:
            uom = 7
        elif MCS == 90:
            uom = 8
        elif MCS == 91:
            uom = 8
        elif MCS == 92:
            uom = 9
        elif MCS == 93:
            uom = 9
        elif MCS == 94:
            uom = 10
        elif MCS == 95:
            uom = 10
        elif MCS == 96:
            uom = -5
        elif MCS == 97:
            uom = -5
        elif MCS == 98:
            uom = -6
        elif MCS == 99:
            uom = -6
        elif MCS == 100:
            uom = -7
        elif MCS == 101:
            uom = -8
        elif MCS == 102:
            uom = -9
        elif MCS == 103:
            uom = -9
        elif MCS == 104:
            uom = -10
        elif MCS == 105:
            uom = -10
        else:
            uom = 0
        return uom

    def USBuildPermits():
        Permits = quandl.get("FRED/PERMIT", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        cPermits = Permits.iloc[-1, -1]
        print("Current Building Permits are {}".format(cPermits))
        if cPermits <= 400:
            score = 10
        elif cPermits > 400 and cPermits <= 500:
            score = 10
        elif cPermits > 500 and cPermits <= 600:
            score = 10
        elif cPermits > 600 and cPermits <= 700:
            score = 7
        elif cPermits > 700 and cPermits <= 800:
            score = -8
        elif cPermits > 800 and cPermits <= 900:
            score = -5
        elif cPermits > 900 and cPermits <= 1000:
            score = -3
        elif cPermits > 1000 and cPermits <= 1100:
            score = 0
        elif cPermits > 1100 and cPermits <= 1200:
            score = 2
        elif cPermits > 1200 and cPermits <= 1300:
            score = 3
        elif cPermits > 1300 and cPermits <= 1400:
            score = 4
        elif cPermits > 1400 and cPermits <= 1500:
            score = 5
        elif cPermits > 1500 and cPermits <= 1600:
            score = 8
        elif cPermits > 1600 and cPermits <= 1700:
            score = 9
        elif cPermits > 1700 and cPermits <= 1800:
            score = 10
        elif cPermits > 1800 and cPermits <= 1900:
            score = -7
        elif cPermits > 1900 and cPermits <= 2000:
            score = -9
        elif cPermits > 2000 and cPermits <= 2100:
            score = -10
        elif cPermits > 2100 and cPermits <= 2200:
            score = -10
        elif cPermits > 2200 and cPermits <= 2300:
            score = -10
        elif cPermits > 2300:
            score = -10
        else:
            score = 0
        return (score)

    def USM2():
        M2 = (quandl.get("FRED/M2", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=55))
        curM2 = M2.iloc[-1, -1]
        YearM2 = M2.iloc[-53, -1]
        df2 = M2.pct_change() * 100
        weekM2 = df2.iloc[-1, -1]
        print("Weekly M2 change is {0:.2f}".format(weekM2))
        anChange = (curM2 - YearM2) / YearM2 * 100
        print("Annualised M2 change is {0:.2f}%".format(anChange))
        if anChange > 50:
            score == 3
        elif anChange > 40 and anChange <= 50:
            score == 6
        elif anChange > 30 and anChange <= 40:
            score == 10
        elif anChange > 20 and anChange <= 30:
            score == 8
        elif anChange > 15 and anChange <= 20:
            score == 6
        elif anChange > 10 and anChange <= 15:
            score == 4
        elif anChange > 5 and anChange <= 10:
            score = 0
        elif anChange > 0 and anChange <= 5:
            score == -6
        elif anChange > -5 and anChange <= 0:
            score == -8
        elif anChange > -10 and anChange <= -5:
            score == -10
        elif anChange > -15 and anChange <= -10:
            score == 8
        elif anChange <= -15:
            score == 10
        return(score)

    def USFedFunds():
        rate = quandl.get("FRED/FEDFUNDS", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=14)
        currRate = rate.iloc[-1, -1]
        yearAgo = rate.iloc[-13, -1]
        pct_change = rate.pct_change() * 100
        anChange = (currRate - yearAgo) / yearAgo * 100
        print("The current Fed Funds rate is {}%".format(currRate))
        print("The annualised Fed Funds Percentage Change is {0:.2f}%".format(anChange))
        if anChange > 30:
            score = 0
        elif anChange > 20 and anChange <= 30:
            score == -10
        elif anChange > 15 and anChange <= 20:
            score == -9
        elif anChange > 10 and anChange <= 15:
            score == -6
        elif anChange > 5 and anChange <= 10:
            score == -3
        elif anChange > -10 and anChange <= 5:
            score = 0
        elif anChange > -15 and anChange <= -10:
            score == 3
        elif anChange > -20 and anChange <= -15:
            score == 5
        elif anChange > -30 and anChange <= -20:
            score == 7
        elif anChange > -40 and anChange <= -30:
            score == -8
        elif anChange > -50 and anChange <= -40:
            score == -9
        elif anChange <= 50:
            score == -10
        else:
            score = 0
        return(score)

    def USCPIALL():
        CPIall = (quandl.get("FRED/CPIAUCSL", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=14))
        monthlyCPI = (CPIall.iloc[-1, -1] - CPIall.iloc[-2, -1]) / CPIall.iloc[-2, -1] * 100
        annualCPI = (CPIall.iloc[-1, -1] - CPIall.iloc[-13, -1]) / CPIall.iloc[-13, -1] * 100
        print ("Monthly CPI is {0:.2f}%".format(monthlyCPI))
        print("Annualised CPI is {0:.2f}%".format(annualCPI))
        if monthlyCPI > 1.4:
            score = 3
        elif monthlyCPI > 1.2 and monthlyCPI <= 1.4:
            score = 6
        elif monthlyCPI > 1 and monthlyCPI <= 1.2:
            score = 10
        elif monthlyCPI > 0.8 and monthlyCPI <= 1:
            score = 8
        elif monthlyCPI > 0.6 and monthlyCPI <= 0.8:
            score = 6
        elif monthlyCPI > 0.4 and monthlyCPI <= 0.6:
            score = 4
        elif monthlyCPI > 0.3 and monthlyCPI <= 0.4:
            score = 0
        elif monthlyCPI > 0 and monthlyCPI <= 0.3:
            score = 0
        elif monthlyCPI > -0.1 and monthlyCPI <= 0:
            score = -6
        elif monthlyCPI > -0.2 and monthlyCPI <= -0.1:
            score = -8
        elif monthlyCPI > -0.3 and monthlyCPI <= -0.4:
            score = -10
        elif monthlyCPI > -0.4 and monthlyCPI <= -0.5:
            score = 6
        elif monthlyCPI > -0.6 and monthlyCPI <= -0.4:
            score = 8
        elif monthlyCPI <= -0.6:
            score = 10
        else:
            score = 0
        return(score)

    def USCPIEXFE():
        CPIex = (quandl.get("FRED/CPILFESL", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=14))
        monthlyCPI = (CPIex.iloc[-1, -1] - CPIex.iloc[-2, -1]) / CPIex.iloc[-2, -1] * 100
        annualCPI = (CPIex.iloc[-1, -1] - CPIex.iloc[-13, -1]) / CPIex.iloc[-13, -1] * 100
        print ("Monthly CPI ex-food and energy is {0:.2f}%".format(monthlyCPI))
        print("Annualised CPI ex-food and energy is {0:.2f}%".format(annualCPI))
        if monthlyCPI > 1.4:
            score = 3
        elif monthlyCPI > 1.2 and monthlyCPI <= 1.4:
            score = 6
        elif monthlyCPI > 1 and monthlyCPI <= 1.2:
            score = 10
        elif monthlyCPI > 0.8 and monthlyCPI <= 1:
            score = 10
        elif monthlyCPI > 0.6 and monthlyCPI <= 0.8:
            score = 8
        elif monthlyCPI > 0.4 and monthlyCPI <= 0.6:
            score = 6
        elif monthlyCPI > 0.2 and monthlyCPI <= 0.4:
            score = 4
        elif monthlyCPI > 0 and monthlyCPI <= 0.2:
            score = 0
        elif monthlyCPI > -0.05 and monthlyCPI <= 0:
            score = -8
        elif monthlyCPI > -0.1 and monthlyCPI <= -0.05:
            score = -9
        elif monthlyCPI > -0.15 and monthlyCPI <= -0.1:
            score = -10
        elif monthlyCPI > -0.2 and monthlyCPI <= -0.15:
            score = 7
        elif monthlyCPI > -0.25 and monthlyCPI <= -0.2:
            score = 8
        elif monthlyCPI > -0.3 and monthlyCPI <= -0.25:
            score = 9
        elif monthlyCPI > -0.35 and monthlyCPI <= -0.3:
            score = 10
        elif monthlyCPI <= -0.35:
            score = 10
        else:
            score = 0
        return(score)

    def USNFPR():
        NFPR = (quandl.get("FRED/PAYEMS", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=14))
        momNFPR = (NFPR.iloc[-1, -1] - NFPR.iloc[-2, -1]) / NFPR.iloc[-2, -1] * 100
        annualNFPR = (NFPR.iloc[-1, -1] - NFPR.iloc[-13, -1]) / NFPR.iloc[-13, -1] * 100
        print("Month on Month NFPR change is {0:.2f}%".format(momNFPR))
        print("Annualised NFPR change is {0:.2f}%".format(annualNFPR))
        if momNFPR >= 0.5:
            score = 2
        elif momNFPR < 0.5 and momNFPR >= 0.4:
            score = 4
        elif momNFPR < 0.4 and momNFPR >= 0.3:
            score = 7
        elif momNFPR < 0.3 and momNFPR >= 0.2:
            score = 5
        elif momNFPR < 0.2 and momNFPR >= 0.1:
            score = 3
        elif momNFPR < 0.1 and momNFPR >= 0:
            score = -6
        elif momNFPR < 0 and momNFPR >= -0.1:
            score = -8
        elif momNFPR < -0.1 and momNFPR >= -0.2:
            score = -10
        elif momNFPR < -0.2 and momNFPR >= -0.3:
            score = 8
        elif momNFPR < -0.3 and momNFPR >= -0.4:
            score = 10
        elif momNFPR < -0.4:
            score = 10
        else:
            score = 0
        return(score)

    def USDGDP():
        DGDP = quandl.get("FRED/GFDEGDQ188S", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        curDGDP = DGDP.iloc[-1, -1]
        print("Current Debt/GDP Ratio is {0:.2f}".format(curDGDP))
        if curDGDP >= 95:
            score = 10
        elif curDGDP >= 85 and curDGDP < 95:
            score = 9
        elif curDGDP >= 75 and curDGDP < 85:
            score = 8
        elif curDGDP >= 65 and curDGDP < 75:
            score = 7
        elif curDGDP >= 55 and curDGDP < 65:
            score = 6
        elif curDGDP >= 45 and curDGDP < 55:
            score = 5
        elif curDGDP >= 35 and curDGDP < 45:
            score = 4
        elif curDGDP >= 25 and curDGDP < 35:
            score = 3
        elif curDGDP >= 15 and curDGDP < 25:
            score = 2
        elif curDGDP >= 5 and curDGDP < 15:
            score = 1
        elif curDGDP >= 0 and curDGDP < 5:
            score = 0
        elif curDGDP >= -10 and curDGDP < 0:
            score = -1
        elif curDGDP >= -20 and curDGDP < -10:
            score = -2
        elif curDGDP >= -30 and curDGDP < -20:
            score = -3
        elif curDGDP >= -40 and curDGDP < -30:
            score = -4
        elif curDGDP >= -50 and curDGDP < -40:
            score = -5
        elif curDGDP >= -60 and curDGDP < -50:
            score = -6
        elif curDGDP >= -70 and curDGDP < -60:
            score = -7
        elif curDGDP >= -80 and curDGDP < -70:
            score = -8
        elif curDGDP >= -90 and curDGDP < -80:
            score = -9
        elif curDGDP < -90:
            score = -10
        else:
            score = 0
        return (score)

    def USSpendingtoGDP(USGDP):
        Surplus = (quandl.get("FRED/FYFSD", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        curSurp = Surplus.iloc[-1, -1]
        SurplusGDP = (curSurp/USGDP)/10
        print("Current Surplus/Defecit to GDP ratio is {0:.2f}".format(SurplusGDP))
        if SurplusGDP >= -9.5:
            score = 10
        elif SurplusGDP >= -8.5 and SurplusGDP < -9.5:
            score = 9
        elif SurplusGDP >= -7.5 and SurplusGDP < -8.5:
            score = 8
        elif SurplusGDP >= -6.5 and SurplusGDP < -7.5:
            score = 7
        elif SurplusGDP >= -5.5 and SurplusGDP < -6.5:
            score = 6
        elif SurplusGDP >= -4.5 and SurplusGDP < -5.5:
            score = 5
        elif SurplusGDP >= -3.5 and SurplusGDP < -4.5:
            score = 4
        elif SurplusGDP >= -2.5 and SurplusGDP < -3.5:
            score = 3
        elif SurplusGDP >= -1.5 and SurplusGDP < -2.5:
            score = 2
        elif SurplusGDP >= -0.5 and SurplusGDP < -1.5:
            score = 1
        elif SurplusGDP >= 0.5 and SurplusGDP < -0.5:
            score = 0
        elif SurplusGDP >= 1.5 and SurplusGDP < 0.5:
            score = -1
        elif SurplusGDP >=2.5 and SurplusGDP < 1.5:
            score = -2
        elif SurplusGDP >=3.5 and SurplusGDP < 2.5:
            score = -3
        elif SurplusGDP >=4.5 and SurplusGDP < 3.5:
            score = -4
        elif SurplusGDP >=5.5 and SurplusGDP < 4.5:
            score = -5
        elif SurplusGDP >=6.5 and SurplusGDP < 5.5:
            score = -6
        elif SurplusGDP >=7.5 and SurplusGDP < 6.5:
            score = -7
        elif SurplusGDP >=8.5 and SurplusGDP < 7.5:
            score = -8
        elif SurplusGDP >=9.5 and SurplusGDP < 8.5:
            score = -9
        elif SurplusGDP < 9.5:
            score = -10
        else:
            score = 0
        return(score)

    def USInterestasGDP():
        interest = (quandl.get("FRED/FYOIGDA188S", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        currInterest = interest.iloc[-1, -1]
        print("Current Federal Debt Servicing to GDP ratio is {0:.2f}".format(currInterest))
        if currInterest >= 2.5:
            score = -10
        elif currInterest >=2 and currInterest < 2.5:
            score = -8
        elif currInterest >=1.5 and currInterest < 2:
            score = -6
        elif currInterest >=1 and currInterest < 1.5:
            score = -4
        elif currInterest >=0.5 and currInterest < 1:
            score = -2
        else:
            score = 0
        return (score)
        
    def USLiquidityCover():
        federalReceipts = (quandl.get("FRED/FYFR", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        currentReceipt = federalReceipts.iloc[-1, -1]
        federalServicingCost = (quandl.get("FRED/FYOINT", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        currentServicing = federalServicingCost.iloc[-1, -1]
        cover = currentReceipt/currentServicing
        print("Current Liquidity Cover ratio is {0:.2f}".format(cover))
        if cover >= 15:
            score = 10
        elif cover >= 14 and cover <15:
            score = 8
        elif cover >= 13 and cover <14:
            score = 6
        elif cover >= 12 and cover <13:
            score = 4
        elif cover >= 11 and cover <12:
            score = 2
        elif cover >= 10 and cover <11:
            score = 0
        elif cover >= 9 and cover <10:
            score = -1
        elif cover >= 8 and cover <9:
            score = -2
        elif cover >= 7 and cover <8:
            score = -3
        elif cover >= 6 and cover <7:
            score = -4
        elif cover >= 5 and cover <6:
            score = -5
        elif cover >= 4 and cover <5:
            score = -6
        elif cover >= 3 and cover <4:
            score = -7
        elif cover >= 2 and cover <3:
            score = -8
        elif cover >= 1 and cover <2:
            score = -9
        else:
            score = -10
        return (score)

    def USBenchmarkSovereignRates():
        rate = (quandl.get("FRED/DGS10", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        currentRate = rate.iloc[-1, -1]
        print("Current 10 Year rate is {}%".format(currentRate))
        if currentRate >= 16:
            score = -10
        elif currentRate >= 15 and currentRate < 16:
            score = -9
        elif currentRate >= 14 and currentRate < 15:
            score = -8
        elif currentRate >= 13 and currentRate < 14:
            score = -7
        elif currentRate >= 12 and currentRate < 13:
            score = -6
        elif currentRate >= 11 and currentRate < 12:
            score = -5
        elif currentRate >= 10 and currentRate < 11:
            score = -4
        elif currentRate >= 9 and currentRate < 10:
            score = -3
        elif currentRate >= 8 and currentRate < 9:
            score = -2
        elif currentRate >= 7 and currentRate < 8:
            score = -1
        elif currentRate >= 6 and currentRate < 7:
            score = 0
        elif currentRate >= 5 and currentRate < 6:
            score = 2
        elif currentRate >= 4 and currentRate < 5:
            score = 4
        elif currentRate >= 3 and currentRate < 4:
            score = 6
        elif currentRate >= 2 and currentRate < 3:
            score = 8
        else:
            score = 10
        return(score)

    def USCentralBankBS(USGDP):
        BS = (quandl.get("FRED/WALCL", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        curBS = BS.iloc[-1, -1]
        BSasGDP = curBS/USGDP/10
        print("The Fed's Balance Sheet is {0:.2f}% of GDP".format(BSasGDP))
        if BSasGDP >= 95:
            score = 10
        elif BSasGDP >= 85 and BSasGDP < 95:
            score = 9
        elif BSasGDP >= 75 and BSasGDP < 85:
            score = 8
        elif BSasGDP >= 65 and BSasGDP < 75:
            score = 7
        elif BSasGDP >= 55 and BSasGDP < 65:
            score = 6
        elif BSasGDP >= 45 and BSasGDP < 55:
            score = 5
        elif BSasGDP >= 35 and BSasGDP < 45:
            score = 4
        elif BSasGDP >= 25 and BSasGDP < 35:
            score = 3
        elif BSasGDP >= 15 and BSasGDP < 25:
            score = 2
        elif BSasGDP >= 5 and BSasGDP < 15:
            score = 1
        elif BSasGDP >= 0 and BSasGDP < 5:
            score = 0
        elif BSasGDP >= -10 and BSasGDP < 0:
            score = -1
        elif BSasGDP >= -20 and BSasGDP < -10:
            score = -2
        elif BSasGDP >= -30 and BSasGDP < -20:
            score = -3
        elif BSasGDP >= -40 and BSasGDP < -30:
            score = -4
        elif BSasGDP >= -50 and BSasGDP < -40:
            score = -5
        elif BSasGDP >= -60 and BSasGDP < -50:
            score = -6
        elif BSasGDP >= -70 and BSasGDP < -60:
            score = -7
        elif BSasGDP >= -80 and BSasGDP < -70:
            score = -8
        elif BSasGDP >= -90 and BSasGDP < -80:
            score = -9
        elif BSasGDP < 90:
            score = -10
        else:
            score = 0
        return(score)

    print("Summary of US Economic Data: ")
    print("-----------------------------")
    USGDP = USGDP()
    USPMI = USPMI()
    USNMPMI = USNMPMI()
    UOMCS = UOMCS()
    USBuildPermits = USBuildPermits()
    USM2 = USM2()
    USFedFunds = USFedFunds()
    USCPIALL = USCPIALL()
    USCPIEXFE = USCPIEXFE()
    USNFPR = USNFPR()
    USDGDP = USDGDP()
    USSpendingtoGDP = USSpendingtoGDP(USGDP)
    USInterestasGDP = USInterestasGDP()
    USLiquidityCover = USLiquidityCover()
    USBenchmarkSovereignRates = USBenchmarkSovereignRates()
    USCentralBankBS = USCentralBankBS(USGDP)
    
    print("-----------------------------")
    USScore = USPMI + USNMPMI + UOMCS + USBuildPermits + USM2 + USFedFunds + USCPIALL + USCPIEXFE + USNFPR + USDGDP + USSpendingtoGDP
    + USInterestasGDP + USLiquidityCover + USBenchmarkSovereignRates + USCentralBankBS
    USScore = USScore / 16
    print("The current endogenous score for the USD is {}".format(round(USScore, 2)))
    print("\n")

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
def UKEndoScore():    
    def UKGDP():
        try:
            #quandl.get("UKONS/PGDP_ABMI_Q", authtoken="8pyGLCjcAHgwZoTYFnNS") - not up to date, recheck
            data = pd.read_csv("UKGDP.csv")
            data = data["GDP"].iloc[-1]
            return (data)
        except:
            print("No valid GDP data")
            return (Null)

    def UKPMI():
        try:
            data = pd.read_csv("UKDATA.csv")
            data = data["UKPMI"]
            cPMI = data.iloc[-1]
            prevPMI = data.iloc[-2]
            maPMI = (cPMI + prevPMI + data.iloc[-3]) / 3
            print ("Current UK PMI is {}**".format(cPMI))
            if cPMI > 50:
                if cPMI > prevPMI:            
                    pmiscore = 7
                elif cPMI < prevPMI:
                    if cPMI < maPMI:
                        pmiscore = -10
                    elif cPMI > maPMI:
                        pmiscore = 3
            elif cPMI < 50:
                if cPMI > prevPMI:
                    pmiscore = -3
                elif cPMI < prevPMI:
                    if cPMI > maPMI:
                        pmiscore = 10
                    elif cPMI < maPMI:
                        pmiscore = -6
            else:
                pmiscore = 0
            return(pmiscore)
        except:
            print("PMI data is missing")
            return(0)
         
    def UKNMPMI():
        try:
            data = pd.read_csv("UKDATA.csv")
            data = data["UKNPMI"]
            cPMI = data.iloc[-1]
            prevPMI = data.iloc[-2]
            maPMI = (cPMI + prevPMI + data.iloc[-3]) / 3
            print ("Current UK NMPMI is {}**".format(cPMI))
            if cPMI > 50:
                if cPMI > prevPMI:            
                    pmiscore = 7
                elif cPMI < prevPMI:
                    if cPMI < maPMI:
                        pmiscore = -10
                    elif cPMI > maPMI:
                        pmiscore = 3
            elif cPMI < 50:
                if cPMI > prevPMI:
                    pmiscore = -3
                elif cPMI < prevPMI:
                    if cPMI > maPMI:
                        pmiscore = 10
                    elif cPMI < maPMI:
                        pmiscore = -6
            else:
                pmiscore = 0
            return(pmiscore)
        except:
            print("Services PMI data is missing")
            return(0)

    def UKSentiment():
        try:
            data = pd.read_csv("UKDATA.csv")
            data = data["Confidence"]
            current = data.iloc[-1]
            print("Current UK Sentiment is at {}**".format(current))
            if current > 25:
                score = -10
            elif current > 20 and current <= 25:
                score = 10
            elif current > 15 and current <=20:
                score = 8
            elif current > 10 and current <=15:
                score = 7
            elif current> 5 and current <=10:
                score = 6
            elif current > 0 and curren <=5:
                score = 5
            elif current > -5 and current <=0:
                score = 4
            elif current > -10 and current <=-5:
                score = 2
            elif current > -15 and current <=-10:
                score = 0
            elif current >-20 and current <=-15:
                score = -3
            elif current >-25 and current <=-20:
                score = -5
            elif current >-30 and current <=-25:
                score = -7
            elif current >-35 and current <=35:
                score = -10
            elif current <=-35:
                score = 10
            else:
                score = 0
            return(score)
        except:
            print("Consumer Sentiment data is missing")
            return(0)

    def UKConPMI():
        try:
            data = pd.read_csv("UKDATA.csv")
            data = data["ConstructionPMI"]
            cPMI = data.iloc[-1]
            prevPMI = data.iloc[-2]
            maPMI = (cPMI + prevPMI + data.iloc[-3]) / 3
            print ("Current Construction PMI is {}**".format(cPMI))
            if cPMI > 50:
                if cPMI > prevPMI:            
                    pmiscore = 7
                elif cPMI < prevPMI:
                    if cPMI < maPMI:
                        pmiscore = -10
                    elif cPMI > maPMI:
                        pmiscore = 3
            elif cPMI < 50:
                if cPMI > prevPMI:
                    pmiscore = -3
                elif cPMI < prevPMI:
                    if cPMI > maPMI:
                        pmiscore = 10
                    elif cPMI < maPMI:
                        pmiscore = -6
            else:
                pmiscore = 0
            return(pmiscore)
        except:
            print("Construction PMI data is missing")
            return(0)

    def UKM4():
        try:
            data = pd.read_csv("UKDATA.csv")
            data = data["M4"]
            if np.isnan(data.iloc[-1]) == True:
                current = data.iloc[-2]
                previous = data.iloc[-3]
                annual = data.iloc[-14]
            else:
                current = data.iloc[-1]
                previous = data.iloc[-2]
                annual = data.iloc[-13]
            popchange = round((current-previous) / previous * 100, 2)
            anChange = round((current-annual) / annual * 100, 2)
            print("Monthly M4 change is {}**".format(popchange))
            print("Annualised M4 change is {}**".format(anChange))
            return(0)
        except:
            ("M4 Data is missing")
            return(0)

    def UKBOEFunds():
        rate = quandl.get("BOE/IUDBEDR", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=13)
        currRate = rate.iloc[-1, -1]
        yearAgo = rate.iloc[-13, -1]
        pct_change = rate.pct_change() * 100
        anChange = (currRate - yearAgo) / yearAgo * 100
        print("The current Bank of England rate is {}%".format(currRate))
        print("The annualised Bank of England Percentage Change is {0:.2f}%".format(anChange))
        if anChange > 30:
            score = 0
        elif anChange > 20 and anChange <= 30:
            score == -10
        elif anChange > 15 and anChange <= 20:
            score == -9
        elif anChange > 10 and anChange <= 15:
            score == -6
        elif anChange > 5 and anChange <= 10:
            score == -3
        elif anChange > -10 and anChange <= 5:
            score = 0
        elif anChange > -15 and anChange <= -10:
            score == 3
        elif anChange > -20 and anChange <= -15:
            score == 5
        elif anChange > -30 and anChange <= -20:
            score == 7
        elif anChange > -40 and anChange <= -30:
            score == -8
        elif anChange > -50 and anChange <= -40:
            score == -9
        elif anChange <= 50:
            score == -10
        else:
            score = 0
        return(score)

    def UKCPIALL(): 
        CPIall = quandl.get("UKONS/MM23_D7BT_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=13)
        monthlyCPI = (CPIall.iloc[-1, -1] - CPIall.iloc[-2, -1]) / CPIall.iloc[-2, -1] * 100
        annualCPI = (CPIall.iloc[-1, -1] - CPIall.iloc[-13, -1]) / CPIall.iloc[-13, -1] * 100
        print ("Monthly CPI is {0:.2f}%".format(monthlyCPI))
        print("Annualised CPI is {0:.2f}%".format(annualCPI))
        if monthlyCPI > 1.4:
            score = 3
        elif monthlyCPI > 1.2 and monthlyCPI <= 1.4:
            score = 6
        elif monthlyCPI > 1 and monthlyCPI <= 1.2:
            score = 10
        elif monthlyCPI > 0.8 and monthlyCPI <= 1:
            score = 8
        elif monthlyCPI > 0.6 and monthlyCPI <= 0.8:
            score = 6
        elif monthlyCPI > 0.4 and monthlyCPI <= 0.6:
            score = 4
        elif monthlyCPI > 0.3 and monthlyCPI <= 0.4:
            score = 3
        elif monthlyCPI > 0.2 and monthlyCPI <= 0.3:
            score = 2
        elif monthlyCPI > 0.1 and monthlyCPI <= 0.1:
            score = 1
        elif monthlyCPI > 0 and monthlyCPI <= 0.1:
            score = 0
        elif monthlyCPI > -0.1 and monthlyCPI <= 0:
            score = -6
        elif monthlyCPI > -0.2 and monthlyCPI <= -0.1:
            score = -8
        elif monthlyCPI > -0.3 and monthlyCPI <= -0.4:
            score = -10
        elif monthlyCPI > -0.4 and monthlyCPI <= -0.5:
            score = 6
        elif monthlyCPI > -0.6 and monthlyCPI <= -0.4:
            score = 8
        elif monthlyCPI <= -0.6:
            score = 10
        else:
            score = 0
        return(score)

    def UKCPIEXFE():
        CPIex = quandl.get("UKONS/MM23_DKC6_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=13)
        monthlyCPI = (CPIex.iloc[-1, -1] - CPIex.iloc[-2, -1]) / CPIex.iloc[-2, -1] * 100
        annualCPI = (CPIex.iloc[-1, -1] - CPIex.iloc[-13, -1]) / CPIex.iloc[-13, -1] * 100
        print ("Monthly CPI ex-food and energy is {0:.2f}%".format(monthlyCPI))
        print("Annualised CPI ex-food and energy is {0:.2f}%".format(annualCPI))
        if monthlyCPI > 1.35:
            score = 3
        elif monthlyCPI > 1.2 and monthlyCPI <= 1.35:
            score = 6
        elif monthlyCPI > 0.95 and monthlyCPI <= 1.2:
            score = 10
        elif monthlyCPI > 0.8 and monthlyCPI <= 0.95:
            score = 10
        elif monthlyCPI > 0.55 and monthlyCPI <= 0.8:
            score = 8
        elif monthlyCPI > 0.4 and monthlyCPI <= 0.55:
            score = 6
        elif monthlyCPI > 0.13 and monthlyCPI <= 0.4:
            score = 4
        elif monthlyCPI > 0 and monthlyCPI <= 0.13:
            score = 0
        elif monthlyCPI > -0.05 and monthlyCPI <= 0:
            score = -8
        elif monthlyCPI > -0.1 and monthlyCPI <= -0.05:
            score = -9
        elif monthlyCPI > -0.15 and monthlyCPI <= -0.1:
            score = -10
        elif monthlyCPI > -0.2 and monthlyCPI <= -0.15:
            score = 7
        elif monthlyCPI > -0.25 and monthlyCPI <= -0.2:
            score = 8
        elif monthlyCPI > -0.3 and monthlyCPI <= -0.25:
            score = 9
        elif monthlyCPI > -0.35 and monthlyCPI <= -0.3:
            score = 10
        elif monthlyCPI <= -0.35:
            score = 10
        else:
            score = 0
        return(score)

    def UKPPI():
        data = quandl.get("UKONS/MM22_JVZ7_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=14)
        curr = data.iloc[-1, -1]
        prev = data.iloc[-2, -1]
        ann = data.iloc[-13 -1]
        anChange = (float(curr) - float(ann)) / float(ann)
        pchange = (float(curr) - float(prev)) / float(prev)
        print("Monthly UK Producer Price Index is {}%".format(round(pchange, 2)))
        print("The annualised Producer Price Index is {0:.2f}%".format(round(anChange, 2)))
        if pchange > 1:
            score = -10
        elif pchange > 0.9 and pchange <= 1:
            score = 10
        elif pchange > 0.8 and pchange <= 0.9:
            score = 9
        elif pchange > 0.7 and pchange <= 0.8:
            score = 8
        elif pchange > 0.6 and pchange <= 0.7:
            score = 7
        elif pchange > 0.5 and pchange <=0.6:
            score = 6
        elif pchange >0.4 and pchange <= 0.5:
            score = 5
        elif pchange > 0.2 and pchange <=0.4:
            score = 4
        elif pchange > 0.1 and pchange <=0.2:
            score = 3
        elif pchange > 0 and pchange <=0.1:
            score = 1
        elif pchange > -0.1 and pchange <=0:
            score = -1
        elif pchange > -0.2 and pchange <= -0.1:
            score = -3
        elif pchange > -0.3 and pchange <= -0.2:
            score = -4
        elif pchange > -0.4 and pchange <= -0.3:
            score = -5
        elif pchange > -0.5 and pchange <= -0.4:
            score = -6
        elif pchange > -0.6 and pchange <= -0.5:
            score = -8
        elif pchange > -0.7 and pchange <= -0.6:
            score = -10
        elif pchange > -0.8 and pchange <= -0.7:
            score = -10
        elif pchange <= -0.8:
            score = 10
        else:
            score = 0    
        return(score)

    def UKHoursWorked():
        data = (quandl.get("UKONS/LMS_YBUS_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2))
        curr = data.iloc[-1, -1]
        prev = data.iloc[-2, -1]
        if int(curr) > int(prev):
            upordown = ("up")
        else:
            upordown = ("down")
        pchange = (int(curr) - int(prev)) / int(prev)
        print("{} million hours worked in the UK, {} from {} last month".format(curr, upordown, prev))
        print("This is a {0:.2f}% SA change from last month".format(pchange))
        if pchange > 0.9:
            score = -10
        elif pchange > 0.8 and pchange <= 0.9:
            score = 10
        elif pchange > 0.7 and pchange <= 0.8:
            score = 9
        elif pchange > 0.6 and pchange <= 0.7:
            score = 8
        elif pchange > 0.5 and pchange <=0.6:
            score = 6
        elif pchange >0.4 and pchange <= 0.5:
            score = 5
        elif pchange > 0.2 and pchange <=0.4:
            score = 4
        elif pchange > 0.1 and pchange <=0.2:
            score = 3
        elif pchange > 0 and pchange <=0.1:
            score = 1
        elif pchange > -0.1 and pchange <=0:
            score = -1
        elif pchange > -0.2 and pchange <= -0.1:
            score = -3
        elif pchange > -0.3 and pchange <= -0.2:
            score = -4
        elif pchange > -0.4 and pchange <= -0.3:
            score = -5
        elif pchange > -0.5 and pchange <= -0.4:
            score = -6
        elif pchange > -0.6 and pchange <= -0.5:
            score = -8
        elif pchange > -0.7 and pchange <= -0.6:
            score = -10
        elif pchange > -0.8 and pchange <= -0.7:
            score = -10
        elif pchange <= -0.8:
            score = 10
        else:
            score = 0    
        return(score)

    def UKDebtGDP():
        DGDP = quandl.get("UKONS/PUSF_HF6X_Q", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        curDGDP = DGDP.iloc[-1, -1]
        print("Current Debt/GDP Ratio is {0:.2f}".format(curDGDP))
        if curDGDP >= 95:
            score = 10
        elif curDGDP >= 85 and curDGDP < 95:
            score = 9
        elif curDGDP >= 75 and curDGDP < 85:
            score = 8
        elif curDGDP >= 65 and curDGDP < 75:
            score = 7
        elif curDGDP >= 55 and curDGDP < 65:
            score = 6
        elif curDGDP >= 45 and curDGDP < 55:
            score = 5
        elif curDGDP >= 35 and curDGDP < 45:
            score = 4
        elif curDGDP >= 25 and curDGDP < 35:
            score = 3
        elif curDGDP >= 15 and curDGDP < 25:
            score = 2
        elif curDGDP >= 5 and curDGDP < 15:
            score = 1
        elif curDGDP >= 0 and curDGDP < 5:
            score = 0
        elif curDGDP >= -10 and curDGDP < 0:
            score = -1
        elif curDGDP >= -20 and curDGDP < -10:
            score = -2
        elif curDGDP >= -30 and curDGDP < -20:
            score = -3
        elif curDGDP >= -40 and curDGDP < -30:
            score = -4
        elif curDGDP >= -50 and curDGDP < -40:
            score = -5
        elif curDGDP >= -60 and curDGDP < -50:
            score = -6
        elif curDGDP >= -70 and curDGDP < -60:
            score = -7
        elif curDGDP >= -80 and curDGDP < -70:
            score = -8
        elif curDGDP >= -90 and curDGDP < -80:
            score = -9
        elif curDGDP < -90:
            score = -10
        else:
            score = 0
        return (score)

    def UKGovSpendGDP(UKGDP):
        data = quandl.get("UKONS/PUSF_ANLW_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        data = data["Value"]
        data = (data/UKGDP * 100) * 12
        recent = round(data.iloc[-1], 2)
        print("12 Month Average Government Spending to GDP is {}%".format(recent))
        if recent > 1.7:
            score = 10
        elif recent > 1.4 and recent <= 1.7:
            score = 9
        elif recent > 1.1 and recent <= 1.4:
            score = 8
        elif recent > 0.8 and recent <=1.1:
            score = 7
        elif recent >0.5 and recent <= 0.8:
            score = 6
        elif recent > 0.2 and recent <=05.:
            score = 5
        elif recent > -0 and recent <=0.2:
            score = 4
        elif recent >-0.2 and recent <=0:
            score = 3
        elif recent >-0.5 and recent <=-0.2:
            score = 2
        elif recent >-0.8 and recent <=0.5:
            score = 1
        elif recent >-1.1 and recent <=-0.8:
            score = 0
        elif recent >-1.4 and recent <=1.1:
            score = -1
        elif recent >-1.7 and recent <=1.4:
            score = -2
        elif recent >-2 and recent <=-1.7:
            score = -3
        elif recent >-2.3 and recent <=-2:
            score = -5
        elif recent >-2.6 and recent <=-2.3:
            score = -6
        elif recent >-2.9 and recent <=-2.6:
            score = -7
        elif recent >-3.2 and recent <=-2.9:
            score = -8
        elif recent >-3.5 and recent <=-3.2:
            score = -9
        elif recent <=3.5:
            score = -10
        else:
            score=0
        return(score)

    def UKInterestasGDP(UKGDP):
        data = quandl.get("UKONS/PUSF_NMFX_M", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        data = data.iloc[-1]
        interest = float(round(data/int(UKGDP) * 1000, 2))
        print("Interest replayments are {}% of GDP".format(interest))
        if interest > 13:
            score = -10
        elif interest > 10 and interest <=13:
            score = -9
        elif interest > 0:
            score = -(int(interest)+1)
        else:
            score = 0
        return(score)

    def UKTenYear():
        data = quandl.get("CHRIS/LIFFE_R1", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        data = data["Open"]
        current = data.ix[-1, -1]
        print("Current 10 Year GILTS are priced at {}".format(current))
        if current >135:
            score = -10
        elif current > 130 and current <= 135:
            score = -7
        elif current > 125 and current <=130:
            score = -5
        elif current > 120 and current <=125:
            score = -3
        elif current > 115 and current <= 120:
            score = 0
        elif current > 110 and current <=115:
            score = 3
        elif current > 105 and current <=110:
            score = 5
        elif current > 100 and current <=105:
            score = 8
        elif current <=100:
            score = 10
        else:
            score = 0
        return(score)
        
    print("Summary of UK Economic Data:")
    print("-----------------------------")
    UKGDP = UKGDP() # https://www.ons.gov.uk/economy/grossdomesticproductgdp
    UKPMI = UKPMI() # https://uk.investing.com/economic-calendar/manufacturing-pmi-204
    UKNMPMI = UKNMPMI() # https://uk.investing.com/economic-calendar/services-pmi-274
    UKSentiment = UKSentiment() # https://uk.investing.com/economic-calendar/gfk-consumer-confidence-330
    UKConPMI = UKConPMI() # https://uk.investing.com/economic-calendar/construction-pmi-44
    UKM4 = UKM4() # quandl.get("BOE/LPMAUYN", authtoken="8pyGLCjcAHgwZoTYFnNS") or LPMVQJS
    UKBOEFunds = UKBOEFunds()
    UKCPIALL = UKCPIALL()
    UKCPIEXFE = UKCPIEXFE()
    UKPPI = UKPPI()
    UKHoursWorked = UKHoursWorked()
    UKDebtGDP = UKDebtGDP()
    UKGovSpendGDP = UKGovSpendGDP(UKGDP)
    UKInterestasGDP = UKInterestasGDP(UKGDP)
    UKTenYear = UKTenYear()
    print("----------------------------")
    UKScore = UKPMI + UKNMPMI + UKSentiment + UKConPMI + UKBOEFunds + UKCPIALL + UKCPIEXFE + UKPPI + UKHoursWorked + UKDebtGDP
    + UKGovSpendGDP + UKTenYear + UKInterestasGDP
    UKScore = UKScore / 13
    print("The current endogenous score for the GBP is {}".format(round(UKScore, 2)))
    print("")
    print("")

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
def AUDEndoScore():
    def AUGDP():
        GDP = (quandl.get("AUSBS/5206001_KEY_AGGREGATES_A2304402X", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        GDP = (GDP.iloc[-1, -1])
        return (GDP)

    def AUPMI():
        try:
            PMI = pd.read_csv("AUDDATA.csv")
            cPMI = PMI.iloc[0, 1]
            prevPMI = PMI.iloc[1, 1]
            maPMI = (cPMI + prevPMI + PMI.iloc[2, 1]) / 3
            print ("Current Australian PMI is {}**".format(cPMI))
            if cPMI > 50:
                if cPMI > prevPMI:            
                    pmiscore = 7
                elif cPMI < prevPMI:
                    if cPMI < maPMI:
                        pmiscore = -10
                    elif cPMI > maPMI:
                        pmiscore = 3
            elif cPMI < 50:
                if cPMI > prevPMI:
                    pmiscore = -3
                elif cPMI < prevPMI:
                    if cPMI > maPMI:
                       pmiscore = 10
                    elif cPMI < maPMI:
                        pmiscore = -6
            else:
                pmiscore = 0
            return(pmiscore)
        except:
            print("Australian PMI data is missing")
            return(0)

    def AUNMPMI():
        try:
            PMI = pd.read_csv("AUDDATA.csv")
            cPMI = PMI.iloc[0, 2]
            prevPMI = PMI.iloc[1, 2]
            maPMI = (cPMI + prevPMI + PMI.iloc[2, 2]) / 3
            print ("Current Australian NMPMI is {}**".format(cPMI))
            if cPMI > 50:
                if cPMI > prevPMI:            
                    pmiscore = 7
                elif cPMI < prevPMI:
                    if cPMI < maPMI:
                        pmiscore = -10
                    elif cPMI > maPMI:
                        pmiscore = 3
            elif cPMI < 50:
                if cPMI > prevPMI:
                    pmiscore = -3
                elif cPMI < prevPMI:
                    if cPMI > maPMI:
                       pmiscore = 10
                    elif cPMI < maPMI:
                        pmiscore = -6
            else:
                pmiscore = 0
            return(pmiscore)
        except:
            print("Services PMI data is missing")
            return(0)

    def AUSentiment():
        sent = (quandl.get("RBA/H03", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2))
        sent = sent["Consumer sentiment. Units: Index; Series ID: GICWMICS"]
        sent = sent[np.logical_not(np.isnan(sent))]
        sentlist = []
        for data in sent:
            sentlist.append(data)
        csent = sentlist[-1]
        csent = np.round(csent, decimals=2)
        psent = sentlist[-2]
        psent = np.round(psent, decimals=2)
        popchange = np.round((csent-psent) / psent * 100, decimals=2)
        print("Current consumer sentiment is {}".format(csent))
        print("Period on period change for consumer sentiment is {}%".format(popchange))
        if csent < 81:
            score = 10
        elif csent >= 81 and csent < 85:
            score = 9
        elif csent >= 85 and csent < 88:
            score = 8
        elif csent == 88:
            score = -10
        elif csent == 89:
            score = -9
        elif csent == 90:
            score = -8
        elif csent == 91:
            score = -7
        elif csent == 92:
            score = -6
        elif csent == 93:
            score = -5
        elif csent == 94:
            score = -4
        elif csent == 95:
            score = -3
        elif csent == 96:
            score = -2
        elif csent == 97:
            score = -1
        elif csent == 98:
            score = 0
        elif csent == 99:
            score = 1
        elif csent == 100:
            score = 2
        elif csent == 101:
            score = 3
        elif csent == 102 or csent == 103:
            score = 4
        elif csent == 104 or csent == 105:
            score = 5
        elif csent == 106 or csent == 107:
            score = 6
        elif csent == 108 or csent == 109:
            score = 7
        elif csent == 110 or csent == 111:
            score = 8
        elif csent == 112 or csent == 113:
            score = 9
        elif csent == 114 or csent == 115:
            score = 10
        elif csent == 116:
            score = -5
        elif csent == 117:
            score = -6
        elif csent == 118:
            score = -7
        elif csent == 119:
            score = -8
        elif csent == 120:
            score = -9
        elif csent >= 121:
            score = -10
        else:
            score = 0
        return score

    def AUPermits():
        Permits = (quandl.get("RBA/H03", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=6))
        Permits = Permits["Private dwelling approvals trend. Units: '000; Series ID: GISDWPRITR"]
        if np.isnan(Permits.iloc[-1]) == True:
            cPermit = Permits.iloc[-2]
        else:
            cPermit = Permits.iloc[-1]
        if np.isnan(Permits.iloc[-1]) == True:
            pPermit = Permits.iloc[-3]
        else:
            pPermit = Permits.iloc[-2]
        if np.isnan(Permits.iloc[-1]) == True:
            ppPermit = Permits.iloc[-4]
        else:
            ppPermit = Permits.iloc[-3]
        if np.isnan(Permits.iloc[-1]) == True:
            pppPermit = Permits.iloc[-5]
        else:
            pppPermit = Permits.iloc[-4]
        avPermit = (cPermit + pPermit + ppPermit) / 3
        pavPermit = (pPermit + ppPermit + pppPermit) / 3
        popchange = cPermit-pPermit/pPermit
        avchange = avPermit - pavPermit / pavPermit
        print("Total Adjusted Housing Permits were {}".format(cPermit))
        print ("Monthly change is {}%".format(round(popchange,2)))
        if popchange < -6:
            score1 = 10
        elif popchange >= -6 and popchange < -4:
            score1 = -10
        elif popchange >= -4 and popchange < -3:
            score1 = -8
        elif popchange >=-3 and popchange < -2:
            score1 = -5
        elif popchange >=-2 and popchange < -1:
            score1 = -2
        elif popchange >=-1 and popchange < 0:
            score1 = 0
        elif popchange >=0 and popchange < 1:
            score1 = 2
        elif popchange >=1 and popchange < 2:
            score1 = 5
        elif popchange >=2 and popchange < 3:
            score1 = 8
        elif popchange >=3 and popchange < 4:
            score1 = 10
        elif popchange >=4 and popchange <5:
            score1 = 0
        elif popchange >=6:
            score1 = -10
        else:
            score1 = 0
        return score1

    def AUM3():
        M3 = (quandl.get("RBA/D03", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=53))
        M3 = M3["M3: Seasonally adjusted. Units: $ billion; Series ID: DMAM3S"]
        cM3 = M3[-1]
        YearM3 = M3[-53]
        popchange = M3.pct_change() * 100
        print("Weekly M3 change is {0:.2f}".format(popchange[-1]))
        anChange = (cM3 - YearM3) / YearM3 * 100
        print("Annualised M3 change is {0:.2f}%".format(anChange))
        popchange = popchange[-1]
        if popchange < -1.1:
            score = 10
        elif popchange < -1 and popchange >=-1.1:
            score = -10
        elif popchange <-0.9 and popchange >=-1:
            score = -9
        elif popchange < -0.8 and popchange >=-0.9:
            score = -8
        elif popchange < -0.7 and popchange >=-0.8:
            score = -7
        elif popchange < -0.6 and popchange >=-0.7:
            score = -6
        elif popchange < -0.5 and popchange >=-0.6:
            score = -5
        elif popchange < -0.4 and popchange >=-0.5:
            score = -4
        elif popchange < -0.3 and popchange >=-0.4:
            score = -3
        elif popchange < -0.2 and popchange >=-0.3:
            score = -2
        elif popchange < -0 and popchange >=-0.2:
            score = -1
        elif popchange < 0.3 and popchange > 0:
            score = 0
        elif popchange < 0.6 and popchange >=0.3:
            score = 1
        elif popchange < 0.9 and popchange >=0.6:
            score = 2
        elif popchange < 1.2 and popchange >=0.9:
            score = 3
        elif popchange <1.3 and popchange >= 1.2:
            score = 4
        elif popchange <1.4 and popchange >= 1.3:
            score = 5
        elif popchange < 1.6 and popchange >= 1.4:
            score = 8
        elif popchange < 1.8 and popchange >=1.6:
            score = 9
        elif popchange <2 and popchange >=1.8:
            score = 10
        elif popchange >=2.1:
            score = -10
        else:
            score = 10
        return(score)

    def AUCashRate():
        CashRate = (quandl.get("RBA/F01_1", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        CashRate = CashRate["Interbank Overnight Cash Rate. Units: Per cent; Series ID: FIRMMCRI"]
        change = CashRate.pct_change()
        cchange = change.iloc[-1]
        print ("Interbank Overnight Cash Rate Change is {}%".format(cchange))
        if cchange < -10:
            score = 10
        elif cchange <-9 and cchange >=-10:
            score = 9
        elif cchange <-8 and cchange >=-9:
            score = 8
        elif cchange <-7 and cchange >=-8:
            score = 7
        elif cchange <-6 and cchange >=-7:
            score = 6
        elif cchange <-5 and cchange >=-6:
            score = 5
        elif cchange <-4 and cchange >=-5:
            score = 4
        elif cchange <-3 and cchange >=-4:
            score = 3
        elif cchange <-2 and cchange >=-3:
            score = 2
        elif cchange <-1 and cchange >=-2:
            score = 1
        elif cchange <0 and cchange >=-1:
            score = 0
        elif cchange < 1 and cchange >=0:
            score = 0
        elif cchange < 2 and cchange >=1:
            score = -1
        elif cchange < 3 and cchange >=2:
            score = -2
        elif cchange < 4 and cchange >=3:
            score = -3
        elif cchange < 5 and cchange >=4:
            score = -4
        elif cchange < 6 and cchange >=5:
            score = -5
        elif cchange < 7 and cchange >=6:
            score = -6
        elif cchange < 8 and cchange >=7:
            score = -7
        elif cchange < 9 and cchange >=8:
            score = -8
        elif cchange < 10 and cchange >=9:
            score = -9
        elif cchange >=10:
            score = -10
        else:
            score = 0
        return(score)

    def AUCPI():
        data = quandl.get("RBA/G01", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2)
        CPI = data["Year-ended inflation. Units: Per cent; Series ID: GCPIAGYP"]
        cCPI = CPI.iloc[-1]
        prevCPI = CPI.iloc[-2]
        popchange = (cCPI - prevCPI) / prevCPI
        if popchange > 0:
            upordown = ("up")
        else:
            popchange = ("down")
        print("Australian CPI is {}%".format(cCPI))
        print("CPI has gone {} {}% this month".format(upordown, round(popchange, 2)))
        if popchange > 18:
            score = -10
        elif popchange > 16 and popchange <= 18:
            score = 10
        elif popchange > 14 and popchange <= 16:
            score = 9
        elif popchange > 12 and popchange <=14:
            score = 8
        elif popchange > 10 and popchange <=12:
            score = 7
        elif popchange > 9 and popchange <= 10:
            score = 6
        elif popchange > 8 and popchange <=9:
            score = 5
        elif popchange > 7 and popchange <=8:
            score = 4
        elif popchange > 6 and popchange <=7:
            score = 3
        elif popchange > 5 and popchange <=6:
            score = 2
        elif popchange > 4 and popchange <= 5:
            score = 1
        elif popchange > 3 and popchange <= 4:
            score = 0
        elif popchange > 2 and popchange <=3:
            score = -1
        elif popchange > 1 and popchange <=2:
            score = -1
        elif popchange > 0 and popchange <=1:
            score = -2
        elif popchange > -1 and popchange <= 0:
            score= -3
        elif popchange > -2 and popchange <=-1:
            score = -4
        elif popchange >-3 and popchange <=-2:
            score = -5
        elif popchange >-4 and popchange <=-3:
            score = -6
        elif popchange >-5 and popchange <=-4:
            score = -7
        elif popchange >-6 and popchange <=-5:
            score = -8
        elif popchange >-7 and popchange <=-6:
            score = -10
        elif popchange >=-8:
            score = 10
        else:
            score = 0
        return(score)

    def AUexCPI():
        data = quandl.get("RBA/G01", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2)
        exCPI = data["Year-ended tradables inflation excluding volatile items and tobacco. Units: Per cent; Series ID: GCPITXVIYP"]
        cexCPI = exCPI.iloc[-1]
        if exCPI.iloc[-2] != 0:
            prevexCPI = exCPI.iloc[-2]
        else:
            prevexCPI = 0.001
        popchange = (cexCPI - prevexCPI) / prevexCPI * 100
        if popchange > 0:
            upordown = ("up")
        else:
            upordown = ("down")
        print("Australian CPI ex-volatile items is {}%, {} from {}%".format(cexCPI, upordown, prevexCPI))
        if popchange > 404:
            score = -10
        elif popchange > 375 and popchange <=404:
            score = 10
        elif popchange > 350 and popchange <= 375:
            score = 9
        elif popchange > 325 and popchange <= 350:
            score = 8
        elif popchange > 275 and popchange <=325:
            score = 7
        elif popchange > 225 and popchange <=275:
            score = 6
        elif popchange > 200 and popchange <= 225:
            score = 5
        elif popchange > 175 and popchange <=200:
            score = 4
        elif popchange > 125 and popchange <=175:
            score = 3
        elif popchange > 75 and popchange <=125:
            score = 2
        elif popchange > 50 and popchange <= 75:
            score = 1
        elif popchange > -15 and popchange <=50:
            score = 0
        elif popchange > -50 and popchange <=-15:
            score = -1
        elif popchange > -100 and popchange <=-50:
            score = -2
        elif popchange > -150 and popchange <=-50:
            score = -3
        elif popchange > -175 and popchange <=-150:
            score = -4
        elif popchange > -200 and popchange <=-175:
            score = -5
        elif popchange > -250 and popchange <=-200:
            score = -6
        elif popchange > -300 and popchange <=-250:
            score = -7
        elif popchange >-350 and popchange <=-300:
            score = -8
        elif popchange >-375 and popchange <=-350:
            score =-9
        elif popchange >-400 and popchange <=-375:
            score = -10
        elif popchange <= -400:
            score = 10
        else:
            score = 0
        return(score)

    def AUEPR():
        data = quandl.get("RBA/H05", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2)
        EPR = data["Participation rate. Units: Per cent; Series ID: GLFSPRSA"]
        cEPR = EPR.iloc[-1]
        prevEPR = EPR.iloc[-2]
        EPRchange = round(((cEPR-prevEPR)/prevEPR * 100),2)
        print("Monthly Employment Participation Rate has changed by {}%".format(EPRchange))
        if EPRchange > 1:
            score = -10
        elif EPRchange > 0.9 and EPRchange <=1:
            score = 10
        elif EPRchange > 0.8 and EPRchange <=0.9:
            score = 9
        elif EPRchange > 0.7 and EPRchange <=0.8:
            score = 8
        elif EPRchange > 0.6 and EPRchange <=0.7:
            score = 7
        elif EPRchange > 0.5 and EPRchange <=0.6:
            score = 6
        elif EPRchange > 0.4 and EPRchange <=0.5:
            score = 5
        elif EPRchange > 0.3 and EPRchange <=0.4:
            score = 4
        elif EPRchange > 0.2 and EPRchange <=0.3:
            score = 3
        elif EPRchange > 0.1 and EPRchange <=0.2:
            score = 2
        elif EPRchange > 0 and EPRchange <= 0.1:
            score = 1
        elif EPRchange > -0.1 and EPRchange <= 0:
            score = -1
        elif EPRchange > -0.2 and EPRchange <= 0.1:
            score = -2
        elif EPRchange > -0.3 and EPRchange <= 0.2:
            score = -3
        elif EPRchange > -0.4 and EPRchange <= 0.3:
            score = -4
        elif EPRchange > -0.5 and EPRchange <= 0.4:
            score = -5
        elif EPRchange > -0.6 and EPRchange <= 0.5:
            score = -6
        elif EPRchange > -0.7 and EPRchange <= 0.6:
            score = -7
        elif EPRchange > -0.8 and EPRchange <= 0.7:
            score = -8
        elif EPRchange > -0.9 and EPRchange <= 0.8:
            score = -9
        elif EPRchange > -1 and EPRchange <= 0.9:
            score = -10
        elif EPRchange <=1:
            score = 10
        else:
            score=0
        return(score)

    def tenBond():
        data = quandl.get("RBA/F02", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        data = data["Australian Government 10 year bond. Units: Per cent per annum; Series ID: FCMYGBAG10D"]
        cBond = data.iloc[-1]
        print("10 Year Bonds rates are {}%".format(cBond))
        if cBond > 5.25:
            score = 10
        elif cBond > 5 and cBond <=5.25:
            score = -10
        elif cBond >4.75 and cBond <=5:
            score = -8
        elif cBond >4.5 and cBond <=4.75:
            score = -6
        elif cBond >4.25 and cBond <=4.5:
            score = -4
        elif cBond >4 and cBond <=4.25:
            score = -3
        elif cBond > 3.75 and cBond <=4:
            score = -2
        elif cBond >3.5 and cBond <=3.75:
            score = -1
        elif cBond > 3.25 and cBond <=3.5:
            score=0
        elif cBond >3 and cBond <=3.25:
            score = 1
        elif cBond >2.75 and cBond<=3:
            score = 2
        elif cBond >2.5 and cBond <=2.75:
            score = 3
        elif cBond >2.25 and cBond <=2.5:
            score = 4
        elif cBond >2 and cBond <=2.25:
            score = 5
        elif cBond > 1.75 and cBond <=2:
            score = 6
        elif cBond > 1.5 and cBond <=1.75:
            score =7
        elif cBond > 1.25 and cBond <=1.5:
            score = 8
        elif cBond > 1 and cBond <= 1.25:
            score = 9
        elif cBond >0.75 and cBond <=1:
            score = 10
        elif cBond <=0.77:
            score = -10
        else:
            score = 0
        return(score)

    print("Summary of Australian Economic Data: ")
    print("-----------------------------")
    AUGDP = AUGDP() 
    AUPMI = AUPMI()
    AUNMPMI = AUNMPMI()
    AUSentiment = AUSentiment()
    AUPermits = AUPermits()
    AUM3 = AUM3()
    AUCashRate = AUCashRate()
    AUCPI = AUCPI()
    AUexCPI = AUexCPI()
    AUEPR = AUEPR()
    tenBond = tenBond()
    
    print("-----------------------------")
    AUDScore = AUPMI + AUSentiment + AUNMPMI + AUPermits + AUM3 + AUCashRate + AUCPI + AUexCPI + AUEPR + tenBond
    AUDScore = (AUDScore + 110) / 11
    print("The current endogenous score for the AUD is {}".format(round(AUDScore, 2)))
    print("")
    print("")

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
##All Exogenous data Goes Here
def USExoScore():
    def USGDP():
        GDP = (quandl.get("FRED/GDP", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2))
        preGDP = GDP.iloc[-1, -2]
        curGDP = GDP.iloc[-1, -1]
        change = (curGDP-preGDP) / preGDP * 100
        if change > 0:
            move = ("grown")
        elif change < 0:
            move = ("shrunk")
        else:
            move = ("not moved, it has changed")
        print("US GDP has {} {}%".format(move, change))
        return (change)

    def USBOP():
        CurrentAccountBalance = quandl.get("FRED/IEABC", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1) #SA
        CapitalAccount = quandl.get("FRED/IEABCP", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        FinancialAccount = quandl.get("FRED/IEANLF", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        WideCapital = CapitalAccount + FinancialAccount
        BalancingItem = CurrentAccountBalance - WideCapital
        ChangeInReserves = -(BalancingItem.iloc[-1,-1])
        print("US gained ${} in reserves".format(ChangeInReserves))
        return(ChangeInReserves)

    def FedFunds():
        rate = quandl.get("FRED/FEDFUNDS", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        currRate = rate.iloc[-1, -1]
        print("Current Fed Funds rate is {}".format(currRate))
        return(currRate)

    def RelativeWealth():
        SP500 = quandl.get("CHRIS/CME_SP1", authtoken="8pyGLCjcAHgwZoTYFnNS")
        SP500 = SP500["Open"]
        high = np.amax(SP500)
        current = SP500.iloc[-1]
        difference = round((current - high) / high * 100, 2)
        if difference <= 5:
            print("The stock market is near all time highs!")
            while True:
                try:
                    high = int(input("What was the previous watermark? "))
                except ValueError:
                    print("That doesnt seem valid, check again (could it be 2171?)")
                    print("If you're not sure, check https://finance.yahoo.com/quote/%5Egspc?ltr=1")
                    continue
                else:
                    difference = round((current - high) / high * 100, 2)
                    print("Relative wealth up {}% from its last peak".format(difference))
                    print("")
                    return(difference)
        else:
            print("Relative wealth is down {}% from its peak".format(difference))
        print("")
        if difference > 25:
            score = 2
        elif difference > 20 and difference <= 25:
            score = 3
        elif differnece > 18 and difference <=20:
            score = 5
        elif difference > 16 and difference <=18:
            score = 7
        elif difference > 14 and difference <= 16:
            score = 9
        elif difference > 12 and difference <=14:
            score = 10
        elif difference > 10 and difference <=12:
            score = 9
        elif difference > 8 and difference <=10:
            score = 7
        elif difference > 6 and difference <=8:
            score = 5
        elif differnece > 4 and difference <=6:
            score = 3
        elif difference > 2 and difference <=4:
            score = 2
        elif difference > 0 and difference <=2:
            score = 0
        elif difference >-2 and difference <=0:
            score = -2
        elif difference >-4 and difference <=-2:
            score = -3
        elif differnece >-6 and difference <=-4:
            score = -5
        elif difference >-8 and diffrence <=-6:
            score = -7
        elif difference >-10 and difference <=-8:
            score = -9
        elif difference >-12 and difference <=-10:
            score = -10
        elif difference > -14 and difference <=-12:
            score = -9
        elif difference >-16 and difference <=-14:
            score = -7
        elif difference >-18 and difference <=-16:
            score = -5
        elif difference >-20 and difference<=-18:
            score = -3
        elif difference >-25 and difference <=-20:
            score = -2
        else:
            score = 0
        return(score)

    USGDP = USGDP()
    USBOP = USBOP()
    FedFunds = FedFunds()
    RelativeWealth = RelativeWealth()
    USEndo = (USGDP, USBOP, FedFunds, RelativeWealth)
    return(USEndo)

###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
def UKExoScore():
    def UKGDP():
        try:
            #quandl.get("UKONS/PGDP_ABMI_Q", authtoken="8pyGLCjcAHgwZoTYFnNS") - not up to date, recheck later
            data = pd.read_csv("UKGDP.csv")
            curGDP = data["GDP"].iloc[-1]
            preGDP = data["GDP"].iloc[-2]
            change = (curGDP-preGDP) / preGDP * 100
            if change > 0:
                move = ("grown")
            elif change < 0:
                move = ("shrunk")
            else:
                move = ("not moved, it has changed")
            print("UK GDP has {} {}%".format(move, change))
            return (change)
        except:
            print("UK GDP Data is not valid")
            return(0)

    def UKBOP():
        # quandl.get("UKONS/PB_HHDH_Q", authtoken="8pyGLCjcAHgwZoTYFnNS") - quarterly not  working, reported to quandl
        BOPErrors = quandl.get("UKONS/UKEA_HHDH_A", authtoken="8pyGLCjcAHgwZoTYFnNS")
        BOPErrors = BOPErrors["Value"].iloc[-1]
        print("Change in UK foreign reserves of £{}m".format(BOPErrors))
        return(BOPErrors)

    def BOEFunds():
        rate = quandl.get("BOE/IUDBEDR", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        currRate = rate.iloc[-1, -1]
        print("BOE Cash Rate is {}".format(currRate))
        return(currRate)

    def RelativeWealth(): #in usd - GBP/USD is a multiplier
        FTSE = quandl.get("CHRIS/LIFFE_Z1", authtoken="8pyGLCjcAHgwZoTYFnNS")
        FTSE = FTSE["Open"]
        exchange = quandl.get("CHRIS/ICE_MP1", authtoken="8pyGLCjcAHgwZoTYFnNS") #GBP/USD
        exchange = exchange["Open"]
        cabsolute = FTSE*exchange
        high = np.amax(cabsolute)
        current = cabsolute.iloc[-1]
        difference = round((high - current) / current * 100, 2)
        if difference <= 5:
            print("The stock market is near all time highs!")
            while True:
                try:
                    high = int(input("What was the previous watermark? "))
                except ValueError:
                    print("That doesnt seem valid, check again")
                    print("If you're not sure, check https://uk.finance.yahoo.com/quote/%5EFTSE?p=%5EFTSE, remembering to adjust against the USD")
                    continue
                else:
                    difference = round((current - high) / high * 100, 2)
                    print("Relative wealth up {}% from its last peak".format(difference))
                    print("")
                    return(difference)
        else:
            print("Relative wealth is down {}% from its peak".format(difference))
        print("")
        if difference > 25:
            score = 2
        elif difference > 20 and difference <= 25:
            score = 3
        elif differnece > 18 and difference <=20:
            score = 5
        elif difference > 16 and difference <=18:
            score = 7
        elif difference > 14 and difference <= 16:
            score = 9
        elif difference > 12 and difference <=14:
            score = 10
        elif difference > 10 and difference <=12:
            score = 9
        elif difference > 8 and difference <=10:
            score = 7
        elif difference > 6 and difference <=8:
            score = 5
        elif differnece > 4 and difference <=6:
            score = 3
        elif difference > 2 and difference <=4:
            score = 2
        elif difference > 0 and difference <=2:
            score = 0
        elif difference >-2 and difference <=0:
            score = -2
        elif difference >-4 and difference <=-2:
            score = -3
        elif differnece >-6 and difference <=-4:
            score = -5
        elif difference >-8 and diffrence <=-6:
            score = -7
        elif difference >-10 and difference <=-8:
            score = -9
        elif difference >-12 and difference <=-10:
            score = -10
        elif difference > -14 and difference <=-12:
            score = -9
        elif difference >-16 and difference <=-14:
            score = -7
        elif difference >-18 and difference <=-16:
            score = -5
        elif difference >-20 and difference<=-18:
            score = -3
        elif difference >-25 and difference <=-20:
            score = -2
        else:
            score = 0
        return(score)
        
    UKGDP = UKGDP()
    UKBOP = UKBOP()
    BOEFunds = BOEFunds()
    RelativeWealth = RelativeWealth()
    UKEndo = (UKGDP, UKBOP, BOEFunds, RelativeWealth)
    return (UKEndo)

######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
def AUDExoScore():
    def AUGDP():
        GDP = (quandl.get("AUSBS/5206001_KEY_AGGREGATES_A2304402X", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=2))
        curGDP = (GDP.iloc[-1, -1])
        preGDP = (GDP.iloc[-2, -1])
        change = round((curGDP-preGDP) / preGDP * 100, 2)
        if change > 0:
            move = ("grown")
        elif change < 0:
            move = ("shrunk")
        else:
            move = ("a move of")
        print("Australian GDP has {} {}%".format(move, change))
        return (change)

    def AUBOP():
        BOP = quandl.get("AUSBS/530201_A3534001K", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1)
        BalancingItem = BOP["Value"]
        BI = BalancingItem.iloc[-1]
        print("Change in Australian reserves of ${}".format(BI))
        return(BI)

    def AUFunds():
        CashRate = (quandl.get("RBA/F01_1", authtoken="8pyGLCjcAHgwZoTYFnNS", rows=1))
        CashRate = CashRate["Interbank Overnight Cash Rate. Units: Per cent; Series ID: FIRMMCRI"]
        CashRate = CashRate[-1]
        print("Australian Cash Rate is {}".format(CashRate))
        return(CashRate)

    def RelativeWealth(): #in usd - AUD/USD is a multiplier
        SPX = quandl.get("CHRIS/ASX_AP1", authtoken="8pyGLCjcAHgwZoTYFnNS")
        SPX = SPX["Previous Settlement"]
        exchange = quandl.get("RBA/FXRUSD", authtoken="8pyGLCjcAHgwZoTYFnNS")
        exchange = exchange["Value"]
        cabsolute = SPX*exchange
        pd.set_option('display.max_rows', 1000)
        high = np.amax(cabsolute)
        if np.isnan(cabsolute.iloc[-1]) == True:
            current = cabsolute.iloc[-2]
        else:
            current = cabsolute.iloc[-1]
        difference = round((high - current) / current * 100, 2)
        if difference <= 5:
            print("The stock market is near all time highs!")
            while True:
                try:
                    high = int(input("What was the previous watermark? "))
                except ValueError:
                    print("That doesnt seem valid, check again")
                    continue
                else:
                    difference = round((current - high) / high * 100, 2)
                    print("Relative wealth up {}% from its last peak".format(difference))
                    print("")
                    return(difference)
        else:
            print("Relative wealth is down {}% from its peak".format(difference))
        print("")
        if difference > 25:
            score = 2
        elif difference > 20 and difference <= 25:
            score = 3
        elif difference > 18 and difference <=20:
            score = 5
        elif difference > 16 and difference <=18:
            score = 7
        elif difference > 14 and difference <= 16:
            score = 9
        elif difference > 12 and difference <=14:
            score = 10
        elif difference > 10 and difference <=12:
            score = 9
        elif difference > 8 and difference <=10:
            score = 7
        elif difference > 6 and difference <=8:
            score = 5
        elif difference > 4 and difference <=6:
            score = 3
        elif difference > 2 and difference <=4:
            score = 2
        elif difference > 0 and difference <=2:
            score = 0
        elif difference >-2 and difference <=0:
            score = -2
        elif difference >-4 and difference <=-2:
            score = -3
        elif difference >-6 and difference <=-4:
            score = -5
        elif difference >-8 and diffrence <=-6:
            score = -7
        elif difference >-10 and difference <=-8:
            score = -9
        elif difference >-12 and difference <=-10:
            score = -10
        elif difference > -14 and difference <=-12:
            score = -9
        elif difference >-16 and difference <=-14:
            score = -7
        elif difference >-18 and difference <=-16:
            score = -5
        elif difference >-20 and difference<=-18:
            score = -3
        elif difference >-25 and difference <=-20:
            score = -2
        else:
            score = 0
        return(score)
        
    AUGDP = AUGDP()
    AUBOP = AUBOP()
    AUFunds = AUFunds()
    RelativeWealth = RelativeWealth()
    return(AUGDP, 2, 3, 4)

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
# Main Exo Loop
def exo(first, second): #inputs as arrays (GDP, BOP, IR, RW)
    def RealGDP(first, second):
        relative = first[0]-second[0]
        print("GDP Differential is {}%".format(relative))
        if relative >=5:
            score = 10
        elif relative >= 4 and relative < 5:
            score = 8
        elif relative >=3 and relative <4:
            score = 6
        elif relative >=2 and relative <3:
            score = 4
        elif relative >=1 and relative <2:
            score = 2
        elif relative >=0 and relative <1:
            score = 0
        elif relative >=-1 and relative <0:
            score = -2
        elif relative >=-2 and relative <-1:
            score = -4
        elif relative >=-3 and relative <-2:
            score = -6
        elif relative >=-4 and relative <-3:
            score = -8
        elif relative <-4:
            score = -10
        else:
            score = 0
        return(score)

        
    def BOP(first, second):
        first = float(first[1])
        second = float(second[1])
        BOP = first/second
        print("Balance of Payments Differential is {}".format(BOP))
        if BOP >=5.5:
            score = 1
        elif BOP >= 5 and BOP < 5.5:
            score = 4
        elif BOP >= 4.5 and BOP < 5:
            score = 7
        elif BOP >= 4 and BOP < 4.5:
            score = 10
        elif BOP >=3.5 and BOP <4:
            score = 9
        elif BOP >=3 and BOP <3.5:
            score = 7
        elif BOP >=2.5 and BOP <3:
            score = 5
        elif BOP>=2 and BOP < 2.5:
            score = 4
        elif BOP >=1.5 and BOP <2:
            score = 3
        elif BOP >=1 and BOP <1.5:
            score = 2
        elif BOP >=0.5 and BOP<1:
            score = 1
        elif BOP >=0 and BOP <0.5:
            score = 0
        elif BOP >=-0.5 and BOP <0:
            score = -1
        elif BOP >=-1 and BOP <0.5:
            score = -2
        elif BOP>=-1.5 and BOP <1:
            score = -3            
        elif BOP >=-2 and BOP <-1.5:
            score = -4
        elif BOP >=-2.5 and BOP <-2:
            score = -5
        elif BOP >=-3 and BOP <-2.5:
            score = -6
        elif BOP >=-3.5 and BOP <-3:
            score = -7
        elif BOP >=-4 and BOP <-3.5:
            score = -9
        elif BOP >=-5.5 and BOP <4:
            score = -10
        elif BOP >=-6 and BOP < -5.5:
            score = -7
        elif BOP >=-6.5 and BOP <-6:
            score = -4
        elif BOP <-6.5:
            score = -1
        else:
            score = 0
        return(score)

    
    def FedFunds(first, second): #will need the synthetic from our broker, synthetic
                                 #is what we pay if long, recieve if short
        differential = (first[2] - second[2])
        print("Fed Funds Differential is {}%".format(differential))
        if differential >= 5.5:
            score = 1
        elif differential >= 5 and differential < 5.5:
            score = 4
        elif differential >= 4.5 and differential < 5:
            score = 7
        elif differential >=4 and differential < 4.5:
            score = 10
        elif differential >=3.5 and differential < 4:
            score = 9
        elif differential >=3 and differential < 3.5:
            score = 7
        elif differential >=2.5 and differential <3:
            score = 5
        elif differential >=2 and differential <2.5:
            score = 4
        elif differential >=1.5 and differential <2:
            score = 3
        elif differential >=1 and differential <1.5:
            score = 2
        elif differential >=-0.5 and differential <1:
            score = 1
        elif differential >=0 and differential <0.5:
            score = 0
        elif differential >=-0.5 and differential <0:
            score = -1
        elif differential >=-1 and differential <-0.5:
            score = -2
        elif differential >=-1.5 and differential <-1:
            score = -3
        elif differential >=-2 and differential <-1.5:
            score = -4
        elif differential >=-2.5 and differential <-2:
            score = -5
        elif differential >=-3 and differential <-2.5:
            score = -7
        elif differntial >=-3.5 and differential <-3:
            score = -9
        elif differential >=-4 and differential <-3.5:
            score = -10
        elif differntial >=-5.5 and differential <-4:
            score = -7
        elif differntial >=-6 and differential <-5.5:
            score = -4
        elif differntial <-6:
            score = -1
        else:
            score = 0
        return(score)

    def RelativeWealth(first, second):
        score = first[3] - second[3]
        return (score)
    
    print("")
    RealGDP = RealGDP(first, second)
    BOP = BOP(first, second)
    FedFunds = FedFunds(first, second)
    RelativeWealth = RelativeWealth(first, second)
    print("Relative Wealth scores {}".format(RelativeWealth))
    total = (int(RealGDP) + int(BOP) + int(FedFunds) + int(RelativeWealth))
    return(total)


#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################

## Main Loop
while True:
    welcome = input("\n"
        "################################################################\n"
                    "Welcome to Panda ChowChow.  What analysis would you like to do? \n"
                    "1.  Full Endogenous Analysis \n"
                    "2.  Exogenous Analysis With Two Currencies \n"
                    "3.  Country Specific Currency Analysis \n"
                    "4.  Quit \n"
                    "################################################################\n\n")
    if welcome == "1":
        USEndoScore()
        UKEndoScore()
        AUDEndoScore()
        
    elif welcome == "2":
        firstc = input("Please select first currency\n")
        secondc = input("Please select second currency\n")
        if firstc == "USD" or firstc == "usd":
            first = USExoScore()
        elif firstc == "GBP" or firstc == "gbp":
            first = UKExoScore()
        elif firstc == "EUR" or firstc == "eur":
            first = EURExoScore()
        elif firstc == "AUD" or firstc == "aud":
            first = AUDExoScore()
        else:
            print("Invalid Option")
            continue
        if secondc == "USD" or secondc == "usd":
            second = USExoScore()
        elif secondc == "GBP" or secondc == "gbp":
            second = UKExoScore()
        elif secondc == "EUR" or secondc == "eur":
            second = EURExoScore()
        elif secondc == "AUD" or secondc == "aud":
            second = AUDExoScore()
        else:
            print("Invalid Option")
            continue
        exo = exo(first, second)
        print("Score for exogenous analysis of {} and {} is {}".format(firstc, secondc, exo))
    
    elif welcome == "3":
        country = input("Which currency would you like to analyse? \n")
        if country == "USD":
            USEndoScore()
        elif country == "GBP":
            UKEndoScore()
        elif country == "EUR":
            EUREndoScore()
        elif country == "AUD":
            AUDEndoScore()
        else:
            print("Invalid Option")
            continue
        
    elif welcome == "4":
        print("See you at the pool, chin-chin \n")
        break

    elif welcome == "9":
        country = input("Right, which exo are we testing? ")
        if country == "USD" or country == "usd":
            USExoScore()
        elif country == "GBP" or country == "gbp":
            UKExoScore()
        elif country == "AUD" or country == "aud":
            AUDExoScore()
        
    else:
        print("Invalid Input")
        continue

