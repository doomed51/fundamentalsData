import PySimpleGUI as sg      

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
            [sg.Text('Market Cap', size=(15, 1)), sg.Text(myTicker.marketCap,size=(15,1))],
            [sg.Text('Latest Price', size=(15, 1)), sg.Text(myTicker.latestPrice,size=(15,1))],
            [sg.Text('52 Week Low', size=(15, 1)), sg.Text(myTicker.week52Low,size=(15,1))],
            [sg.Text('52 Week High', size=(15, 1)), sg.Text(myTicker.week52High,size=(15,1))],
            [sg.Text('Total Revenue', size=(15, 1)), sg.Text(myTicker.revenue,size=(15,2))],
            # ****************************
            #       Company Health 
            # ****************************
            [sg.Text('Company Health', size=(45,2), justification='center')],
            [sg.Text('Net Profit Margin', size=(15, 1)), sg.Text(myTicker.netProfitMargin,size=(15,1))],
            [sg.Text('Total Cash', size=(15, 1)), sg.Text(myTicker.cash,size=(15,1))],
            [sg.Text('Total Debt', size=(15, 1)), sg.Text(myTicker.debt,size=(15,2))],
            # ****************************
            #           Ratios
            # ****************************
            [sg.Text('Ratios', size=(45,2), justification='center')],
            [sg.Text('Price To Book', size=(15,1)), sg.Text(myTicker.priceToBook,size=(15,2))],
            # ****************************
            #           Stock Health
            # ****************************
            [sg.Text('Stock Health', size=(45,2), justification='center')],
            [sg.Text('EPS', size=(15,1)), sg.Text(myTicker.earningsPerShare,size=(15,2))],
            # ****************************
            #           Uncategorized
            # ****************************
            [sg.Text('Uncategorized', size=(45,2), justification='center')],
            [sg.Text('Latest Volume', size=(15, 1)), sg.Text(myTicker.latestVolume,size=(15,1))],
            [sg.Text('Dividend Yield', size=(15,1)), sg.Text(myTicker.dividendYield,size=(15,1))],
            [sg.Text('ROE', size=(15,1)), sg.Text(myTicker.returnOnEquity,size=(15,1))],
            [sg.Quit()]  
]

# ****************************************************************************************
#
#                                       Draw commands 
#
# ****************************************************************************************
window = sg.Window('Company Info',default_element_size=(12,1)).Layout(TableLayoutWx)  

event, values = window.Read()    
window.Close()
