import pandas as pd
import dateutil
import datetime
import re

class api_IEX:
    """A class to work with the IEX API @ api.iextrading.com """
    
    def __init__(self):
        self.baseURL = "https://api.iextrading.com/1.0/stock/"

    def testAPI(self, myTicker):
        """ Basic test function to check if the API is working"""
        apiPath = self.baseURL + myTicker + "/delayed-quote"
        self.dfResponse = pd.read_json(apiPath, typ='series')
    
    def returnKeyStats (self, myTicker):
        """ returns the Key Stats set of data as a dataframe: https://iextrading.com/developer/docs/#key-stats """
        apiPath = self.baseURL + myTicker + "/stats"
        return pd.read_json(apiPath, typ='series')

    def returnMarketCap(self, myTicker):
        """ returns marketcap value """
        returnDF = self.returnKeyStats(myTicker)
        return returnDF['marketcap']

    def _normalizeTicker(self, myTicker):
        """ Parses the Symbol to make sure it is only the ticker symbol and not the company name"""
        if '(' and ')' in myTicker:
            # some regex voodoo
            return re.search('\(([^)]+)', myTicker).group(1)
        else:
            return myTicker



        