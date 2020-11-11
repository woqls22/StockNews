# StockNews
종목의 주가 상승 및 하락을 예측해주는 웹서비스입니다.

[한국인터넷진흥원 주최 제8회 핀테크 해커톤 우수상 수상]

Contributed by [오승영](https://github.com/seung-00), [김수영](https://github.com/ShiningSu0)

이재빈 - API 모듈, 뉴스예측모델, 데이터 크롤링 모듈 작성, 모듈통합, 클라우드 서버 임포트 작업 진행

김수영 - 기본적 분석 알고리즘 작성, 주가예측 모델 훈련 및 구현

오승영 - 프론트 엔드 작업(UI UX 구현), 애니메이션 효과 적용

## Demo
<img src= "BackEnd/PythonScripts/Resources/Demo.gif" >

## Description
- 증권가 실시간 뉴스 파싱 및 정보 제공 (웹서비스)
- 종목별 호재,악재 분석(ML 모델)과 기본적분석(20년치 데이터 기반 ML 모델)을 진행. 각 결과를 조합하여 투자지표 도출
- 분석된 투자지표를 바탕으로 종목 추천(예측도가 높은순으로 Top 10 종목 추천)

## Predict Result (Train DataSet : 10000, Test DataSet : 1000)
<img src= "BackEnd/PythonScripts/Resources/ML.png" >

## Structure
<img src= "BackEnd/PythonScripts/Resources/structure.jpg" >

## 개발 환경
- Python3.7
- selenium 3.141.0
- urllib3 1.25.10
- pandas 1.15.0 
- numpy 1.19.1
- matplotlib 3.3.1
- pillow 7.2.0
- AWS RDS (mysql)
- Spring boot,  React.js

## Schedule
- [X]  KTOP 30, KOSPI, KOSPI200, KOSDAQ, KOSDAQ150, KRX300 가격 정보 파싱 [08.24]
- [X]  네이버 증권뉴스 속보 TOP 20 파싱 [08.24]
- [X]  뉴스헤드라인으로부터 해당하는 종목 인식[08.24]
- [X]  뉴스에 종목 고유 인덱스 부여[08.24]
- [X]  기업별 뉴스 CSV 파일 저장 구현[08.24]
- [X]  KOSPI / KOSDAQ 현재 시세, 그래프 파싱[08.24]
- [X]  News History Table 작성[08.24]
- [X]  News별 긍정, 중립, 부정 분류를 위한 라벨링 작업 진행[08.25]
- [X]  Top20 News 학습된 모델을 통해 호재/악재 실시간 예측(predict.py)[08.27]
- [X]  분석된 긍정, 중립, 부정 라벨링을 바탕으로 모델 학습 진행[08.27]
- [X]  네이버뉴스 키워드 크롤링 구현[08.27]
- [X]  News Headline 1만개 라벨링 작업[08.27]
- [X]  상위 Top20 뉴스, 회사별 증권 뉴스 조회 API구현[09.04]
- [X]  현재 기준 50일 가격정보, 거래량 정보 파싱, csv저장[09.05]
- [X]  종목별 거래 정보 api 구현[09.07]
- [X]  서비스 구체화작업 진행, 한국거래소 서버 다운으로 인한 크롤링 모듈 수정[09.14]
- [X]  KOSPI, KOSDAQ 가격정보 DB 저장 및 json 리턴 url 구현[09.15]
- [X]  KOSPI TOP 100 기업 다음날 주가 예측결과 DB 저장[09.16]
- [X]  분석된 긍정, 부정 뉴스를 통해 해당 종목에 투자 지수화[09.16]
- [X]  시가, 종가, 일일 거래량, 변동추이 메트릭 수치화[09.16]
- [X]  메트릭 종합. 투자지표 도출[09.16]
- [X]  프론트 엔드 구현[~09.21] Contributed by [seung-00](https://github.com/seung-00)  
- [X]  종목별 해당하는 뉴스 분류기 웹서비스 구현[09.21]
- [X]  KOSPI / KOSDAQ 상장 기업 DB 자동 업로드 모듈 구현[09.21]
- [X]  네이버클라우드 서버 임포팅[09.21]

## Revision History
- [20.08.24] : 가격정보, 증권 뉴스 속보 파싱 [30초 간격, selenium활용] (), DB연동 저장
<img src= "BackEnd/PythonScripts/Resources/get_info.JPG" >

- [20.08.24] : 뉴스 정보 확인 시 회사명이 겹치는 현상 수정
- [20.08.24] : 기업 별 뉴스 분류 모듈 구현
<img src= "BackEnd/PythonScripts/Resources/database.JPG" >

- [20.08.24] : KOSPI/KOSDAQ GRAPH
<img src= "BackEnd/PythonScripts/Resources/Graph.png" >

- [20.08.26] : 주가변동에 따라 css-class변경발생. 크롤링 오류 수정(한국거래소)
- [20.08.26] : 긍정, 부정 단어에 따른 뉴스 가중치 부여 결과
<img src= "BackEnd/PythonScripts/Resources/label.JPG" >

- [20.08.26] : 뉴스 데이터 1200개 학습 결과. 현재 데이터셋 구축중
<img src= "BackEnd/PythonScripts/Resources/NLP.png" >

- [20.08.27] : 훈련데이터 10284개, 테스트데이터 1018개 학습 진행

- [20.08.27] : 히스토그램(뉴스라인 길이)
<img src= "BackEnd/PythonScripts/Resources/histogram.JPG" >

- [20.09.04] : 조회 api json 객체 리턴 구현
<img src= "BackEnd/PythonScripts/Resources/backend.JPG" >

- [20.09.05] : 현재 기준 50일 가격정보, 거래량 정보 파싱, csv저장
<img src= "BackEnd/PythonScripts/Resources/priceinfo.JPG" >
<img src= "BackEnd/PythonScripts/Resources/info.png" >

- [20.09.07] : 종목별 가격 조회 api 구현
<img src= "BackEnd/PythonScripts/Resources/price.png" >

- [20.09.21] : 최종 결과물
<img src= "BackEnd/PythonScripts/Resources/Demo.gif" >