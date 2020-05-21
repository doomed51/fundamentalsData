import pandas as pd
import yfinance as yf

yf.pdr_override()

class ticker: 
    """ a base class represnting a ticker and associated financial metadata""" 

    def __init__(self, symbol):
        self.symbol = symbol
        self.marketCap = 0

    def populateTicker(self):
        # consolidate yfinance calls 
        print ('starting INFO lookup')
        self.info = yf.Ticker(self.symbol).info
        print ('INFO retrieved')

        print ('starting FINANCIALS lookup')
        self.financials = yf.Ticker(self.symbol).financials
        print ('FINANCIALS retrieved')
        #print(self.financials[self.financials.columns[0]])

        self.populateKeyStats()
        self.populateCompanyInformation()
        self.populateQuote()
        self.populateAnnualFinancials()

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
        self.marketCap = self.info['marketCap']
        self.dividendYield = self.info['dividendYield']
        
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
        self.exchange = 1000
        
        self.industry = self.info['sector']
        self.description = self.info['longBusinessSummary']
        self.website = self.info['website']
        self.week52High = self.info['fiftyTwoWeekHigh']
        self.week52Low = self.info['fiftyTwoWeekLow']
        self.latestVolume = self.info['averageVolume']
        self.netProfitMargin = self.info['profitMargins']

    def populateQuote(self):
        """ populate ticker with realtime quote info """
        #pd = dataFeed.returnQuote(self.symbol)
        self.latestPrice = 1000


    def populateAnnualFinancials(self):
        """ populate ticker with annual financials """
        #pd = dataFeed.returnFinancials_Annual(self.symbol)
        self.revenue = self.financials[self.financials.columns[0]]['Total Revenue']
        self.cash = 1000
        self.debt = 1000
        self.netIncome = self.financials[self.financials.columns[0]]['Net Income']
        

