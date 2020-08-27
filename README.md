# StockNews
주식뉴스서비스

## Description
- 증권가 실시간 뉴스 파싱 및 정보 제공 (웹서비스)
- 가장 관심도가 높은 종목 파악
- 종목별 호재,악재 수치화 객관적 지표 제공
- 즐겨찾기한 기업에 해당하는 뉴스만 제공
- 데이터 분석을 통한 정보 제공
- 토론방 및 채팅방 구현

## Predict Result
<img src= "BackEnd/PythonScripts/Resources/ML.JPG" >

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
- [ ]  News Headline 1만개 라벨링 작업
- [ ]  분석된 긍정, 부정 뉴스를 통해 해당 종목에 투자 지수화
- [ ]  시가, 종가, 일일 거래량, 변동추이 메트릭 수치화
- [ ]  메트릭 종합. 투자지표 도출
- [ ]  종목별 해당하는 뉴스 분류기 웹서비스 구현
- [ ]  지표를 바탕으로 모의 투자 진행
- [ ]  KOSPI / KOSDAQ 상장 기업 DB 자동 업로드 모듈 구현
- [ ]  결과 평가

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