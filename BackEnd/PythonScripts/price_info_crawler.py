import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlrd
import pandas as pd

def find_price(code): #50일 자료 fetch
    stockItem = code
    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    maxPage = source.find_all("table", align="center")
    mp = maxPage[0].find_all("td", class_="pgRR")
    Date=[]
    price=[]
    volume=[]
    mpNum = 5 #Max Page
    for page in range(1, mpNum + 1):
        url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem + '&page=' + str(page)
        html = urlopen(url)
        source = BeautifulSoup(html.read(), "html.parser")
        srlists = source.find_all("tr")
        isCheckNone = None

        if ((page % 1) == 0):
            time.sleep(1)
        for i in range(1, len(srlists) - 1):
            if (srlists[i].span != isCheckNone):
                srlists[i].td.text
                Date.append(srlists[i].find_all("td", align="center")[0].text)
                price.append(srlists[i].find_all("td", class_="num")[0].text)
                volume.append(srlists[i].find_all("td", class_="num")[5].text)
                print(srlists[i].find_all("td", align="center")[0].text, srlists[i].find_all("td", class_="num")[0].text,srlists[i].find_all("td", class_="num")[5].text)
    return Date,price,volume
def generate_codeInsert_query():
    xlsx = xlrd.open_workbook('Data/stockdata.xls')
    sheet = xlsx.sheet_by_index(0)
    for i in range(1,101):
        code = sheet.cell(i, 0).value
        stock = sheet.cell(i,1).value
        print("INSERT INTO `stock`.`code` (`code`, `company`) VALUES ('"+code+"', '"+stock+"');")
def return_code(company):
    xlsx = xlrd.open_workbook('Data/stockdata.xls')
    sheet = xlsx.sheet_by_index(0)
    for i in range(1, 101):
        code = sheet.cell(i, 0).value
        stock = sheet.cell(i, 1).value
        if(stock == company):
            return code
    return "None"
def write_history(company):
    code = return_code(company)
    if(code=="None"):
        return
    else:
        Date, price, volume = find_price(code)
        data = pd.DataFrame({
            '날짜': Date,
            '가격': price,
            '거래량': volume
        })
        data.to_csv('Data/Histories/'+company+'_Info.csv', index=False, encoding='cp949')
if __name__ == '__main__':
    xlsx = xlrd.open_workbook('Data/stockdata.xls')
    sheet = xlsx.sheet_by_index(0)
    for i in range(1, 101):
        code = sheet.cell(i, 0).value
        stock = sheet.cell(i, 1).value
        write_history(stock)
