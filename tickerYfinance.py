import pandas as pd
from api_IEX import api_IEX

#dataFeed = api_IEX()

class ticker: 
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
        
       # pd = dataFeed.returnKeyStats(self.symbol)
        self.marketCap = 1000
        self.dividendYield = 1000
        
        # ROE is the TTM Value
        self.returnOnEquity = 1000 
        
        # % insider ownership is not as important as TTM net inflow/outflow which is not in IEX
        #self.insiderPercent = pd['insiderPercent']        
        self.priceToBook = 1000
        self.sharesOutstanding = 1000

    def populateCompanyInformation(self): 
        """ populate the ticker with:
        Name 
        Exchange
        Industry
        Description
        Website """
        #pd = dataFeed.returnCompanyInformation(self.symbol)
        self.companyName = 1000
        self.industry = 1000
        self.exchange = 1000
        self.description = 1000
        self.website = 1000

    def populateQuote(self):
        """ populate ticker with realtime quote info """
        #pd = dataFeed.returnQuote(self.symbol)
        self.week52High = 1000
        self.week52Low = 1000
        self.latestPrice = 1000
        self.latestVolume = 1000

    def populateAnnualFinancials(self):
        """ populate ticker with annual financials """
        #pd = dataFeed.returnFinancials_Annual(self.symbol)
        self.revenue = 1000
        self.cash = 1000
        self.debt = 1000
        self.netIncome = 1000
        

