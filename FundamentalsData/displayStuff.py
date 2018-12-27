import PySimpleGUI as sg      

import getFunctions as _getFunctions

ticker = "CSCO"

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(_getFunctions.getMarketCap(ticker)), sg.FileBrowse()],      
                 [sg.Submit(), sg.Cancel()]]

tableLayout =[      
          [sg.Text('Fundamentals')],      
          [sg.Text('Market Cap', size=(15, 1)), sg.InputText(_getFunctions.getMarketCap(ticker))],      
          [sg.Text('Net Profit Margin', size=(15, 1)), sg.InputText('Not Complete')],      
          [sg.Text('Cash', size=(15, 1)), sg.InputText('Not Complete')],      
          [sg.Submit(), sg.Cancel()]      
         ]

window = sg.Window('Window Title').Layout(tableLayout)    

event, values = window.Read()    
window.Close()

source_filename = values[0]    