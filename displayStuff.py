import PySimpleGUIWx as sg      

import ticker
import api_IEX

userInput_ticker = input("what ticker?")

myTicker = ticker.ticker(userInput_ticker)
myTicker.populateTicker()

TableLayoutWx = [
            [sg.Text(myTicker.companyName)],
            [sg.Text('Description', size=(15,5)), sg.Text(myTicker.description,size=(30,5))],
            # ****************************
            #           Basics
            # ****************************
            [sg.Text('Basics', size=(45,2), justification='center')],
            [sg.Text('Market Cap', size=(15, 1)), sg.Text(str(myTicker.marketCap),size=(15,1))],
            [sg.Text('Latest Price', size=(15, 1)), sg.Text(str(myTicker.latestPrice),size=(15,1))],
            [sg.Text('52 Week Low', size=(15, 1)), sg.Text(str(myTicker.week52Low),size=(15,1))],
            [sg.Text('52 Week High', size=(15, 1)), sg.Text(str(myTicker.week52High),size=(15,1))],
            [sg.Text('Total Revenue', size=(15, 1)), sg.Text(str(myTicker.revenue),size=(15,2))],
            # ****************************
            #       Company Health 
            # ****************************
            [sg.Text('Company Health', size=(45,2), justification='center')],
            [sg.Text('Net Profit Margin', size=(15, 1)), sg.Text(str(myTicker.netProfitMargin),size=(15,1))],
            [sg.Text('Total Cash', size=(15, 1)), sg.Text(str(myTicker.cash),size=(15,1))],
            [sg.Text('Total Debt', size=(15, 1)), sg.Text(str(myTicker.debt),size=(15,2))],
            # ****************************
            #           Ratios
            # ****************************
            [sg.Text('Ratios', size=(45,2), justification='center')],
            [sg.Text('Price To Book', size=(15,1)), sg.Text(str(myTicker.priceToBook),size=(15,1))],
            # ****************************
            #           Uncategorized
            # ****************************
            [sg.Text('Uncategorized', size=(45,2), justification='center')],
            [sg.Text('Latest Volume', size=(15, 1)), sg.Text(str(myTicker.latestVolume),size=(15,1))],
            [sg.Text('Dividend Yield', size=(15,1)), sg.Text(str(myTicker.dividendYield),size=(15,1))],
            [sg.Text('ROE', size=(15,1)), sg.Text(str(myTicker.returnOnEquity),size=(15,1))],
            [sg.Quit()]  
]

# ****************************************************************************************
#
#                                       Draw commands 
#
# ****************************************************************************************
window = sg.Window('Company Info',default_element_size=(12,1)).Layout(TableLayoutWx).Finalize()  

event, values = window.Read(timeout=None)    
window.Close()
