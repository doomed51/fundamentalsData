import pandas as pd
import yfinance as yf
import xlsxwriter
import openpyxl

from openpyxl import load_workbook

yf.pdr_override()

class ticker: 
    """ a base class represnting a ticker and associated financial metadata""" 

    def __init__(self, symbol):
        self.symbol = symbol
        self.marketCap = 0

    def populateTicker(self):
        # consolidate yfinance calls 
        
        print ('starting INFO lookup...')
        self.info = yf.Ticker(self.symbol).info
        print ('DONE!')

        print ('starting FINANCIALS lookup...')
        self.financials = yf.Ticker(self.symbol).financials
        print ('DONE!')
        
        print ('starting BALANCE SHEET lookup...')
        self.balanceSheet = yf.Ticker(self.symbol).balance_sheet
        print ('DONE!')

        print ('getting 1d quote...')
        self.history1d = yf.Ticker(self.symbol).history(period="1d")
        print ('DONE!')

        self.populateKeyStats()
        self.populateCompanyInformation()
        self.populateQuote()
        self.populateAnnualFinancials()

        # TODO implement below calls with actual data
        self.companyName = "companyName"
        self.exchange = "exchange"
        self.salesPerShare = "salesPerShare"
        self.cashflowPerShare = "cashflowPerShare"
        self.insiderOwnership = "insiderOwnership"
        self.stockBuyBack = "stockBuyBack"
        self.EPSRank = "EPSRank"
        self.RPSRank = "RPSRank"
        self.earningsPerShare5y = "earningsPerShare5y"
        self.revenue5y = "revenue5y"
        self.projectedSales = "projectedSales"
        self.projectedHigh = "projectedHigh"
        self.projectedLow = "projectedLow"
        self.starsFairVal = "starsFairVal"
        self.currentPE = "currentPE"
        self.averagePE = "averagePE"
        self.priceToSales = "priceToSales"
        self.currentRatio = "currentRatio"
        self.quickRatio = "quickRatio"
        self.returnOnEquity = "returnOnEquity"        
        self.priceToBook = "priceToBook"
        self.sharesOutstanding = "sharesOutstanding"
        
        # Dependencies -> populateAnnualFinancials() &&  populateKeyStats
        self.earningsPerShare = "earningsPerShare"
        
        print ('Printing to Excel...')
        self.printExcel()
        print ('DONE! ')

        #this P/E is invalid since the EPS is from fiscal 2017 and the price is the latest market price! 
        #self.priceToEarnings = self.latestPrice / self.earningsPerShare
            
    def populateKeyStats(self):
        """ populates the ticker with: 
        Market Capitalization, 
        dividend yield, 
        TTM Return on Equity, 
        price/book """
        
       # pd = dataFeed.returnKeyStats(self.symbol)
        self.marketCap = self.info['marketCap']
        self.dividendYield = self.info['dividendYield']

    def populateCompanyInformation(self): 
        """ populate the ticker with:
        Name 
        Exchange
        Industry
        Description
        Website """
        #pd = dataFeed.returnCompanyInformation(self.symbol)

        
        self.sector = self.info['sector']
        self.description = self.info['longBusinessSummary']
        self.website = self.info['website']
        self.week52High = self.info['fiftyTwoWeekHigh']
        self.week52Low = self.info['fiftyTwoWeekLow']
        self.latestVolume = self.info['averageVolume']
        self.netProfitMargin = self.info['profitMargins']

    def populateQuote(self):
        """ populate ticker with realtime quote info """
        #pd = dataFeed.returnQuote(self.symbol)
        self.latestPrice = self.history1d['Close'][0]


    def populateAnnualFinancials(self):
        """ populate ticker with annual financials """
        #pd = dataFeed.returnFinancials_Annual(self.symbol)
        self.revenue = self.financials[self.financials.columns[0]]['Total Revenue']
        self.netIncome = self.financials[self.financials.columns[0]]['Net Income']
        
        self.cash = self.balanceSheet[self.balanceSheet.columns[0]]['Cash']
        self.currentLiabilities = self.balanceSheet[self.balanceSheet.columns[0]]['Total Current Liabilities']
        self.shareholderEquity = self.balanceSheet[self.balanceSheet.columns[0]]['Total Stockholder Equity']
        self.commonStock = self.balanceSheet[self.balanceSheet.columns[0]]['Common Stock']

    # Convert ticker object into a dataframe for simplified data manipulation 
    # TODO is this the simplest way? 
    def tickerToDataframe(self):

        
        return pd.DataFrame({'Data' : [self.symbol, self.sector, self.latestPrice, self.week52High, self.week52Low, self.marketCap, self.latestVolume, self.revenue, self.netProfitMargin, self.cash, self.currentLiabilities, self.salesPerShare, self.cashflowPerShare, self.earningsPerShare, self.dividendYield, self.returnOnEquity, self.insiderOwnership, self.stockBuyBack, self.EPSRank, self.RPSRank, self.earningsPerShare5y, self.revenue5y, self.projectedSales, self.projectedHigh, self.projectedLow, self.starsFairVal, self.currentPE, self.averagePE, self.priceToSales, self.priceToBook, self.currentRatio, self.quickRatio]})
    
    def printExcel(self):
       # self.tickerToDataframe()
       # covert the tickercalss into a dataframe to simplify writing to Excel 
        testdf = self.tickerToDataframe()

        # load up the file 
        # TODO catch file not found error
        # TODO filename from config 
        myFilename = 'Valuations.xlsx'
        mySheetName = 'Valuations'
        myExcelFile = load_workbook(filename = myFilename)
        myWorksheet = myExcelFile[mySheetName]

        nextRow = 2
        nextCol = myWorksheet.max_column

        writer = pd.ExcelWriter(myFilename, engine = 'openpyxl')
        writer.book = myExcelFile
        writer.sheets = {ws.title: ws for ws in myExcelFile.worksheets}


        testdf.to_excel(writer, sheet_name=mySheetName, startrow = nextRow, startcol = nextCol, header=False, index=False, )

        writer.save()