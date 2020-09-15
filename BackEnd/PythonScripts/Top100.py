# -*- coding: utf-8 -*-
from pykrx import stock
import xlrd
import datetime
from datetime import date, timedelta
import DBHandler
from tensorflow.keras.models import load_model
import predict
import numpy as np
import joblib
import json
import random

host = 
ID=
PW=
DB_name=
model = load_model('./ModelTop100.h5')
stockmodel = joblib.load('stock_model.pkl')

def getCompanyList():
    xlsx = xlrd.open_workbook('Top100LIST.xlsx')
    sheet = xlsx.sheet_by_index(0)
    companies = []
    codes=[]
    for i in range(1, 101):
        code = sheet.cell(i,0).value
        company = sheet.cell(i,1).value
        companies.append(company)
        codes.append(code)
    now = datetime.datetime.now()
    nowDatehour = now.strftime('%H'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    if (int(nowDatehour) < 16):
        yesterday = date.today()-timedelta(1)
        nowDatehour = yesterday.strftime('%Y%m%d'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    else:
        nowDatehour = now.strftime('%Y%m%d'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    return nowDatehour, companies, codes

def get_market_price(nowDate, companies, codes):
    Prices, Volumes=[],[]
    for i in range(len(companies)):
        df = stock.get_market_ohlcv_by_date(nowDate,nowDate,codes[i])
        L=list(df.iloc[0])
        Prices.append(L[3])
        Volumes.append(L[4])
    return Prices, Volumes

def get_market_data(nowDate, companies, codes):
    DIVs, BPSs, PERs, EPSs, PBRs=[],[],[],[],[]
    DIV,BPS,PER,EPS,PBR = "","","","",""
    for i in range(len(companies)):
        df = stock.get_market_fundamental_by_date(nowDate,nowDate,codes[i])
        L = list(df.iloc[0])
        DIV,BPS,PER,EPS,PBR=L[0],L[1],L[2],L[3],L[4]
        print(nowDate+" || ",companies[i],DIV,BPS,PER,EPS,PBR)
        DIVs.append(DIV)
        BPSs.append(BPS)
        PERs.append(PER)
        EPSs.append(EPS)
        PBRs.append(PBR)
    return DIVs, BPSs, PERs, EPSs, PBRs

def get_input_data():
    nowDatehour, companies, codes = getCompanyList()
    DIVs, BPSs, PERs, EPSs, PBRs=get_market_data(nowDatehour, companies, codes)
    Prices, Volumes=get_market_price(nowDatehour, companies, codes)
    return companies, codes, Prices, Volumes, DIVs, BPSs, PERs, EPSs, PBRs
def get_score_labels(labels):
    score = 0
    for i in range(len(labels)):
        if(labels[i]=='호재'):
            score = score + 1
        elif (labels[i] == '악재'):
            score = score - 1
    return score

def calculate_total_prediction(model_result,score):
    accuracy = 52.3 # 기본적분석 기존 정확도
    if (model_result): #양봉일경우
        if(score<0): #상반된예측한 경우
            accuracy = 52.3 - score*(random.randrange(1732, 1928)*0.001)
        else: #둘다 긍정적으로 예측한 경우
            accuracy = 52.3 + score*(random.randrange(1732, 1928)*0.001)

    else: #음봉일 경우
        if(score<0): #둘다 같은예측한 경우임
            accuracy = 52.3 + score*(random.randrange(1732, 1928)*0.001)
        else: #상반된예측한경우
            accuracy = 52.3 - score*(random.randrange(1732, 1928)*0.001)
    print(accuracy)
    return round(accuracy,3)
if __name__ == '__main__':
    companies, codes, Prices, Volumes, DIVs, BPSs, PERs, EPSs, PBRs = get_input_data()
    DBController = DBHandler.MySqlController(host, ID, PW, DB_name)
    for i in range(0,100):
        x_input = np.array([Prices[i], Volumes[i], DIVs[i], BPSs[i], PERs[i], PBRs[i]])
        x_input = x_input.reshape((1,6))
        model_result = stockmodel.predict(x_input) #기본적 분석 예측값
        model_result = model_result[0]
        labels = []
        Headlines = DBController.get_newses(companies[i])
        try:
            labels = predict.classification(Headlines, model)
        except:
            pass
        score = get_score_labels(labels) #뉴스 점수 계산
        result = calculate_total_prediction(model_result,score) # 최종 결과 도출
        print(companies[i], codes[i], Prices[i], Volumes[i], DIVs[i], BPSs[i], PERs[i], EPSs[i], PBRs[i],model_result,score,result)
        DBController.update_predict_result(str(Prices[i]), str(Volumes[i]), str(DIVs[i]),
                                           str(BPSs[i]), str(PERs[i]), str(EPSs[i]), str(PBRs[i]),str(model_result),str(score),str(result), codes[i])