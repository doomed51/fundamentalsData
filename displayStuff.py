import PySimpleGUI as sg      

import ticker
import api_IEX

userInput_ticker = input("what ticker?")

myTicker = ticker.ticker(userInput_ticker)
myTicker.populateKeyStats()
myTicker.populateCompanyInformation()

#dataFeed = api_IEX.api_IEX()

#ticker = "CSCO"

#layout = [[sg.Text('My one-shot window.')],      
#                 [sg.InputText(_getFunctions.getMarketCap(ticker)), sg.FileBrowse()],      
#                 [sg.Submit(), sg.Cancel()]]

tableLayout =[      
          [sg.Text(myTicker.companyName)],      
          [sg.Text('Description', size=(15,1)), sg.Text(myTicker.description,size=(40,5))],
          [sg.Text('Market Cap', size=(15, 1)), sg.Text(myTicker.marketCap,size=(15,1))],
          [sg.Text('Dividend Yield', size=(15,1)), sg.Text(myTicker.dividendYield,size=(15,1))],
          [sg.Text('ROE', size=(15,1)), sg.Text(myTicker.returnOnEquity,size=(15,1))],
          [sg.Text('Price To Book', size=(15,1)), sg.Text(myTicker.priceToBook,size=(15,1))],
          [sg.Quit()]      
         ]

window = sg.Window('Window Title').Layout(tableLayout)    

event, values = window.Read()    
window.Close()

#source_filename = values[0]    