import ticker 

myTicker = ticker.ticker('CSCO')

myTicker.populateKeyStats()
print(myTicker.netProfitMargin)