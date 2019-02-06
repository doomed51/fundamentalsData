import pandas as pd
from api_IEX import api_IEX

dataFeed = api_IEX()

class ticker: 
    """ a base class represnting a ticker and associated financial metadata""" 

    def __init__(self, symbol):
        self.symbol = symbol
        self.marketCap = 0

    def populateKeyStats(self):
        """ populates the ticker with Market Capitalization, dividend yield, TTM Return on Equity, price/book """
        pd = dataFeed.returnKeyStats(self.symbol)
        self.marketCap = pd['marketcap']
        #self.netProfitMargin = pd['profitMargin']
        self.dividendYield = pd['dividendYield']
        
        # ROE is the TTM Value
        self.returnOnEquity = pd['returnOnEquity'] 
        
        # % insider ownership is not as important as TTM net inflow/outflow which is not in IEX
        #self.insiderPercent = pd['insiderPercent']        
        self.priceToBook = pd['priceToBook']


