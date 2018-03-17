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
    
    def writeDatetoFile(self,df,fileName,sheetName):
        import pandas as pd
        writer = pd.ExcelWriter(fileName)
        df.to_excel(writer,sheetName)
        writer.save()
        return "File SuccessFuly Return"
        
    ##Convert HTML to Text 
    def readTextFromHtml(self,htmlData):
        self.htmlData = htmlData
        from bs4 import BeautifulSoup
        soupData = BeautifulSoup(htmlData)
        return soupData


    ##Write to SQLLite DB
    def writeToSQLLiteDb(self,dbName,query):
        self.query = query
        import sqlite3
        conn = sqlite3.connect(dbName)
        conn.execute(query)
        conn.commit()
        conn.close
        return conn


    ##Read from SQLLite DB
    def readFromSQLLiteDb(self,dbName,query):
        self.query = query
        import sqlite3
        import pandas as pd
        conn = sqlite3.connect(dbName)
        df = pd.read_sql_query(query,conn)
        conn.close
        return df

########################---STEP1 - Function to read an excel from a physical location -----##############################
fo = FileOperation()
filePath = "SEO_In_File.xls"
fo.readPath = filePath
data1 = dict(fo.readExcel(filePath))
print(data1) ## Read the data from the file path 
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
insertQuery = 'INSERT into SEO_RESULT Values'
for word in keyWordList:
    pattern = re.compile(word.upper())
    wordCount = len(pattern.findall(urlDataHtml.decode("UTF-8").upper()))   
    wordCountDict[word] = wordCount
    insertQuery =  insertQuery +'(\''+   word.strip() + '\','+str(wordCount) + '),'
    print(wordCount)
    print(wordCountDict)
    print(insertQuery)


## STEP6 - Connect to SQLLite Database and create a table    
## STEP7 - Create a Database for SEO
## STEP8 - Create a table for SEO
queryCreateTable = '''CREATE TABLE SEO_RESULT(KeyWord TEXT NOT NULL, Count INT NOT NULL);'''
createTable = fo.writeToSQLLiteDb("SEO_DB",queryCreateTable)
print(createTable)
##insertQuery =
## STEP9 - Insert the findings from STEP6 into the SEO table.
insetQuery = insertQuery[:len(insertQuery)-1]
insertValues = fo.writeToSQLLiteDb("SEO_DB",insetQuery)
##print(insertValues)erfrom SEO table
readTableQuery = 'Select * from SEO_RESULT'
readResult = fo.readFromSQLLiteDb("SEO_DB",readTableQuery)
print(readResult)
resultWriteToExcel = fo.writeDatetoFile(readResult,"SEO_Count_Result.xls", "SEO_Result1")
