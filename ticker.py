import pandas as pd
from api_IEX import api_IEX

dataFeed = api_IEX()

class ticker: 
    """ a base class represnting a ticker and associated financial metadata""" 

    def __init__(self, symbol):
        self.symbol = symbol
        self.marketCap = 0
    

    # TODO 
    # key stats: cash, total debt, earnings per share, div yield, ROE, insider buy/own, price/sales, price/book 

    def populateKeyStats(self):
        """ populates the ticker with one call to the API with the following data: market cap, net profit, cash, total debt, earnings per share, div yield, ROE, insider percent, price/sales, price/book """
        pd = dataFeed.returnKeyStats(self.symbol)
        self.marketCap = pd['marketcap']
        self.netProfitMargin = pd['profitMargin']
        self.cash = pd['cash']
        self.totalDebt = pd['debt']
        self.EPS = pd['latestEPS']
        self.dividendYield = pd['dividendYield']
        self.ROE = pd['returnOnEquity']
        self.insiderPercent = pd['insiderPercent']
        self.priceToSales = pd['priceToSales']
        self.priceToBook = pd['priceToBook']


