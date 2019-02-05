import PySimpleGUI as sg      

import getFunctions as _getFunctions
import api_IEX

dataFeed = api_IEX.api_IEX()

ticker = "CSCO"

#layout = [[sg.Text('My one-shot window.')],      
#                 [sg.InputText(_getFunctions.getMarketCap(ticker)), sg.FileBrowse()],      
#                 [sg.Submit(), sg.Cancel()]]

tableLayout =[      
          [sg.Text('Fundamentals')],      
          [sg.Text('Market Cap', size=(15, 1)), sg.Text(dataFeed.returnMarketCap(ticker),size=(15,1))],      
          [sg.Quit()]      
         ]

window = sg.Window('Window Title').Layout(tableLayout)    

event, values = window.Read()    
window.Close()

source_filename = values[0]    