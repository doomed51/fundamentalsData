import PySimpleGUIWx as sg      

import ticker
import api_IEX

userInput_ticker = input("what ticker?")

myTicker = ticker.ticker(userInput_ticker)
myTicker.populateKeyStats()
myTicker.populateCompanyInformation()
myTicker.populateQuote()
myTicker.populateAnnualFinancials()

TableLayoutWx = [
            [sg.Text(myTicker.companyName)],
            [sg.Text('Description', size=(15,5)), sg.Text(myTicker.description,size=(30,5))],
            [sg.Text('Basics', size=(45,2), justification='center')],
            [sg.Text('Market Cap', size=(15, 1)), sg.Text(str(myTicker.marketCap),size=(15,1))],
            [sg.Text('Latest Price', size=(15, 1)), sg.Text(str(myTicker.latestPrice),size=(15,1))],
            [sg.Text('52 Week Low', size=(15, 1)), sg.Text(str(myTicker.week52High),size=(15,1))],
            [sg.Text('52 Week Low', size=(15, 1)), sg.Text(str(myTicker.week52High),size=(15,1))],
            [sg.Text('Total Revenue', size=(15, 1)), sg.Text(str(myTicker.revenue),size=(15,2))],
            [sg.Text('Uncategorized', size=(45,2), justification='center')],
            [sg.Text('Latest Volume', size=(15, 1)), sg.Text(str(myTicker.latestVolume),size=(15,1))],
            [sg.Text('Dividend Yield', size=(15,1)), sg.Text(str(myTicker.dividendYield),size=(15,1))],
            [sg.Text('ROE', size=(15,1)), sg.Text(str(myTicker.returnOnEquity),size=(15,1))],
            [sg.Text('Price To Book', size=(15,1)), sg.Text(str(myTicker.priceToBook),size=(15,1))],
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

# ========================================================================================
#
#                       Test layouts below from various documentation 
#
# ========================================================================================


# ********************************************************************************
#
#                       from PythonSimpleGUIWx documentation 
#
#*********************************************************************************
buttons =  [sg.Radio('Radio Button 1',1, size=(12,1), default=True, enable_events=True, tooltip='radio buttton', key='_RADIO1_'),
            sg.Radio('Radio Button 2',1, default=False, key='_RADIO2_', enable_events=True, visible=True),
sg.Radio('Radio Button 3',1, enable_events=True, key='_RADIO3_')]

layoutWx =  [ [sg.Text('PySimpleGUIWx ', tooltip='text', font='Arial 18', text_color='red', enable_events=True, key='_Wx_') ,
             sg.Text('', key='_TEXT_', font='Arial 18', text_color='black')],
            [sg.Input('Single Line Input', do_not_clear=True, enable_events=True)],
            [sg.Multiline('Multiline Input', do_not_clear=True, size=(40,4), enable_events=True)],
            [sg.MultilineOutput('Multiline Output', size=(40,5), text_color='blue')],
            [sg.Output(size=(40,5))],
            [sg.Checkbox('Checkbox 1', enable_events=True), sg.Checkbox('Checkbox 2', default=True, enable_events=True)],
           [sg.Column([buttons], visible=True, key='COL')],
            [sg.Combo(values=['Combo 1', 'Combo 2', 'Combo 3'], default_value='Combo 2', enable_events=True, key='_COMBO_', visible=True, readonly=False, tooltip='Combo box', disabled=False, font='Courier 18', size=(12,1))],
            [sg.OK(), sg.Button('Popup')]
          ]

# **********************************************************************************
#
#                               Layout for complicated popup
#
# **********************************************************************************

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layoutComplex = [      
    [sg.Menu(menu_def, tearoff=True)],      
    [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.InputText('This is my text')],      
    [sg.Frame(layout=[      
    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
        sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
        sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
        sg.Frame('Labelled Group',[[      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
        sg.Column(column1, background_color='#F7F3EC')]])],      
    [sg.Text('_'  * 80)],      
    [sg.Text('Choose A Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText('Default Folder'), sg.FolderBrowse()],      
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      
