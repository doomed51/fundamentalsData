# Data provided for free by IEX: https://iextrading.com/developer. View IEX’s Terms of Use:https://iextrading.com/api-exhibit-a/

import pandas as pd
import dateutil
import datetime
import re

class api_IEX:
    """A class to work with the IEX API @ api.iextrading.com """
    
    #TODO 
    # need logic to handle tickers that don't exist 

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

    def returnCompanyInformation(self, myTicker):
        """ returns basic company information such as the name, exchange, description, etc: https://iextrading.com/developer/docs/#company """
        apiPath = self.baseURL + myTicker + "/company"
        return pd.read_json(apiPath, typ='series')

    def _normalizeTicker(self, myTicker):
        """ Parses the Symbol to make sure it is only the ticker symbol and not the company name. This is generally needed when scraping from websites as opposed to user input."""
        if '(' and ')' in myTicker:
            # some regex voodoo
            return re.search('\(([^)]+)', myTicker).group(1)
        else:
            return myTicker



        