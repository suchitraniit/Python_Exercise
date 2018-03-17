### SEO Project Python for Data Science ###
## STEP1 - Read an excel file from a physical location
## STEP2 - Read the URL mentioned in the 1st Sheet of the Excel
## STEP3 - Read the Keywords mentioned in the Excel Sheet
## STEP4 - Read the HTML mentioned in the URL on the Excel Sheet.
## STEP5 - Count the number of times the keyword in the excel sheet is used in the HTML page
           ## for each keyword traverse throw the HTML content and check if the word exists. If yes increase the counter. 
## STEP6 - Connect to SQLLite Database
## STEP7 - Create a Database for SEO
## STEP8 - Create a table for SEO
## STEP9 - Insert the findings from STEP6 into the SEO table.
## STEP10 - Read the table from SEO table 
## STEP11 - Print the data from STEP 10 onto a new excel.
## STEP12 - Draw a graph for data writen into the excel.
## STEP13 - Repeat the step 1 to 12 for the number of sheets present in the excel.


########################---STEP1 - Function to read an excel from a physical location -----##############################
class FileOperation:
    ##Using Pyexcel Library     
    def readExcel(self,filepath):
        self.filePath = filepath
        from pyexcel_xls import read_data
        data = read_data(filePath)
        return data

    ##Read excel using Pandas library.
    def readExcelUsingPandas(self,filepath):
        self.filePath = filePath
        ##self.sheetName = sheetName
        import pandas as pd
        data = pd.read_excel(filePath)
        return data
    ##Read URL using urllib
    def readURLData(self,urlRef):
        self.urlRef = urlRef
        from urllib.request import urlopen
        file_handle=urlopen(urlRef)
        data = file_handle.read()
        return data
    
    def writeDatetoFile(self,fileName):
        self.fileName = fileName
        filewrite = open(filename,'w')
        
    ##Convert HTML to Text 
    def readTextFromHtml(self,htmlData):
        self.htmlData = htmlData
        from bs4 import BeautifulSoup
        soupData = BeautifulSoup(htmlData)
        return soupData


    ##Connect to SQLLite DB
    def connectToSQLLiteDb(self,dbName):
        self.dbName = dbName
        import sqlite3
        conn = sqlite3.connect(dbName)
        return conn

    ##Write to SQLLite DB
    def writeToSQLLiteDb(self,conn,query):
        self.query = query
        import sqlite3
        self.conn = conn
        conn.execute(query)
        return "Success"


########################---STEP1 - Function to read an excel from a physical location -----##############################
fo = FileOperation()
filePath = "SEO_In.xls"
fo.readPath = filePath
data1 = dict(fo.readExcel(filePath))
print(data1) ## Read teh data from the file path 
data2 = fo.readExcelUsingPandas(filePath)

## STEP2 - Read the URL mentioned in the 1st Sheet of the Excel
urlToRead = data2.URL[0] 
print("URL :" + urlToRead)

## STEP3 - Read the Keywords mentioned in the Excel Sheet
keyWordList = data2.to_dict()["Keywords"].values()
print(keyWordList)

## STEP4 - Read the HTML mentioned in the URL on the Excel Sheet.
urlDataHtml = fo.readURLData(urlToRead)
print("------1----")
import re

## STEP5 - Count the number of times the keyword in the excel sheet is used in the HTML page
           ## for each keyword traverse throw the HTML content and check if the word exists. If yes increase the counter. 
wordCountDict = dict()
for word in keyWordList:
    pattern = re.compile(word.upper())
    wordCount = len(pattern.findall(urlDataHtml.decode("UTF-8").upper()))   
    wordCountDict[word] = wordCount
    print(wordCount)
    print(wordCountDict)

## STEP6 - Connect to SQLLite Database and create a table
queryCreateTable = '''CREATE TABLE SEO_RESULT(KeyWord TEXT NOT NULL, Count INT NOT NULL);'''
queryInsertTable = '''INSERT INTO SEO_RESULT VALUES (?, ?)')''', wordCountDict
conn = fo.connectToSQLLiteDb("SEO_DB")
createTable = fo.writeToSQLLiteDb(conn,queryCreateTable)
print(createTable)
insertValues = fo.writeToSQLLiteDb(conn,queryInsertTable)
print(insertValues)
