import PySimpleGUI as sg      

import ticker
import api_IEX

userInput_ticker = input("what ticker?")

myTicker = ticker.ticker(userInput_ticker)
myTicker.populateTicker()

TableLayoutWx = [
            # ****************************
            #           Input 
            # ****************************
            [sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],  
            [sg.Input(do_not_clear=True, key='_IN_'), sg.Button('Show')],
            # ****************************
            #           Meta Data
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('Description', size=(15,5)), sg.Multiline(myTicker.description,disabled=True, size=(30,8))]],
            title = myTicker.companyName, title_color='red',relief=sg.RELIEF_SUNKEN)],
            # ****************************
            #           Basics
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('Market Cap', size=(15, 1)), sg.Text(myTicker.marketCap,size=(15,1))],
            [sg.Text('Latest Price', size=(15, 1)), sg.Text(myTicker.latestPrice,size=(15,1))],
            [sg.Text('52 Week Low', size=(15, 1)), sg.Text(myTicker.week52Low,size=(15,1))],
            [sg.Text('52 Week High', size=(15, 1)), sg.Text(myTicker.week52High,size=(15,1))],
            [sg.Text('Total Revenue', size=(15, 1)), sg.Text(myTicker.revenue,size=(15,1))]],
            title = 'Basics', title_color='red',relief=sg.RELIEF_SUNKEN)],
            # ****************************
            #       Company Health 
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('Net Profit Margin', size=(15, 1)), sg.Text(myTicker.netProfitMargin,size=(15,1))],
            [sg.Text('Total Cash', size=(15, 1)), sg.Text(myTicker.cash,size=(15,1))],
            [sg.Text('Total Debt', size=(15, 1)), sg.Text(myTicker.debt,size=(15,1))]],
            title = 'Company Health', title_color='red',relief=sg.RELIEF_SUNKEN)],
            # ****************************
            #           Ratios
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('Price To Book', size=(15,1)), sg.Text(myTicker.priceToBook,size=(15,1))]],
            title = 'Ratios', title_color='red',relief=sg.RELIEF_SUNKEN)],
            # ****************************
            #           Stock Health
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('EPS', size=(15,1)), sg.Text(myTicker.earningsPerShare,size=(15,1))]],
            title = 'Stock Health', title_color='red',relief=sg.RELIEF_SUNKEN)],
            # ****************************
            #           Uncategorized
            # ****************************
            [sg.Frame(layout=[
            [sg.Text('Latest Volume', size=(15, 1)), sg.Text(myTicker.latestVolume,size=(15,1))],
            [sg.Text('Dividend Yield', size=(15,1)), sg.Text(myTicker.dividendYield,size=(15,1))],
            [sg.Text('ROE', size=(15,1)), sg.Text(myTicker.returnOnEquity,size=(15,1))]],
            title = 'Miscellaneous', title_color='red',relief=sg.RELIEF_SUNKEN)],

            [sg.Button('Exit')]
]

# ****************************************************************************************
#
#                                       Draw commands 
#
# ****************************************************************************************
window = sg.Window('Company Info',default_element_size=(12,1)).Layout(TableLayoutWx)  

while True:
    event, values = window.Read()
    print(event,values)
    if event is None or event =='Exit':
        break
    if event == 'Show':
        window.FindElement('_OUTPUT_').Update(values['_IN_'])    
window.Close()
