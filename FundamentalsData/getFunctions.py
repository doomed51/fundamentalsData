import pandas as pd
from api_IEX import api_IEX

dataFeed = api_IEX()

# get Market Cap from IEX
def getMarketCap(myTicker):
    return dataFeed.returnMarketCap("CSCO")
