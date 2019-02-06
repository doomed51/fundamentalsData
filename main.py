import ticker 

userInput_ticker = input("what ticker?")

myTicker = ticker.ticker(userInput_ticker)

myTicker.populateKeyStats()
attrs = vars(myTicker)

# debug print
#print(', '.join("%s: %s" % item for item in attrs.items()))
