import pandas as pd
from api_IEX import api_IEX

dataFeed = api_IEX()

class tickerOld: 
    """ a base class represnting a ticker and associated financial metadata""" 

    def __init__(self, symbol):
        self.symbol = symbol
        self.marketCap = 0

    def populateTicker(self):
        self.populateKeyStats()
        self.populateCompanyInformation()
        self.populateQuote()
        self.populateAnnualFinancials()

        # Calculated data
        # Dependencies -> populateAnnualFinancials()
        self.netProfitMargin = self.netIncome / self.revenue * 100
        # Dependencies -> populateAnnualFinancials() &&  populateKeyStats
        self.earningsPerShare = self.netIncome / self.sharesOutstanding
        
        #this P/E is invalid since the EPS is from fiscal 2017 and the price is the latest market price! 
        #self.priceToEarnings = self.latestPrice / self.earningsPerShare
            
    def populateKeyStats(self):
        """ populates the ticker with: 
        Market Capitalization, 
        dividend yield, 
        TTM Return on Equity, 
        price/book """
        
        pd = dataFeed.returnKeyStats(self.symbol)
        self.marketCap = pd['marketcap']
        self.dividendYield = pd['dividendYield']
        
        # ROE is the TTM Value
        self.returnOnEquity = pd['returnOnEquity'] 
        
        # % insider ownership is not as important as TTM net inflow/outflow which is not in IEX
        #self.insiderPercent = pd['insiderPercent']        
        self.priceToBook = pd['priceToBook']
        self.sharesOutstanding = pd['sharesOutstanding']

    def populateCompanyInformation(self): 
        """ populate the ticker with:
        Name 
        Exchange
        Industry
        Description
        Website """
        pd = dataFeed.returnCompanyInformation(self.symbol)
        self.companyName = pd['companyName']
        self.industry = pd['industry']
        self.exchange = pd['exchange']
        self.description = pd['description']
        self.website = pd ['website']

    def populateQuote(self):
        """ populate ticker with realtime quote info """
        pd = dataFeed.returnQuote(self.symbol)
        self.week52High = pd['week52High']
        self.week52Low = pd['week52Low']
        self.latestPrice = pd['latestPrice']
        self.latestVolume = pd['latestVolume']

    def populateAnnualFinancials(self):
        """ populate ticker with annual financials """
        pd = dataFeed.returnFinancials_Annual(self.symbol)
        self.revenue = pd[1][0]['totalRevenue']
        self.cash = pd[1][0]['totalCash']
        self.debt = pd[1][0]['totalDebt']
        self.netIncome = pd[1][0]['netIncome']
        

