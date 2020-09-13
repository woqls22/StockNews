import news_parser as Util
import datetime
import time
import DBHandler
from tensorflow.keras.models import load_model
import predict
CompanyList=[]
Headless = True # False : 창띄움, True : 창없음
MakeCompanyList = False # 회사 리스트 갱신
host = '데이터베이스 주소'
ID= '계정명'
PW='비밀번호'
DB_name='DB이름'


def GetNewsInfo(driver):
    headlines, news_info, Text,NewsUrl = Util.GetNews(driver) # 헤드라인, 신문사 정보 및 게시 시간, 본문, 기사링크 파싱.
    CompanyFromNews = Util.GetCompanyFromNews(headlines, CompanyList)
    #Util.save_headlines(headlines, news_info, Text,CompanyFromNews,NewsUrl)
    #Util.PrintNews(headlines, news_info, Text, CompanyFromNews)
    return headlines, news_info, Text, NewsUrl,CompanyFromNews

def GetPriceInfo(driver):
    NameList, PriceInfo, Fluctuation = Util.get_prices(driver) #KTOP 30, KOSPI, KOSPI200, KOSDAQ, KOSDAQ150, KRX300 순
    Util.PrintPrice(NameList, PriceInfo, Fluctuation)
    return NameList, PriceInfo, Fluctuation

def MakeCompanyFile(MakeCompanyList):
    #Company CSV파일 생성
    Util.MakeCompanyCSV()

if __name__ == '__main__':
    print("Setting Interface...")
    CompanyList = Util.GetCompanyList() # 코스피 상장 기업 업로드
    try: #네이버 증권
        NewsDriver = Util.News_get_driver(Headless)
    except Exception as ex:
        print("News Driver Err")
        print('에러가 발생 했습니다', ex)
    try : #한국거래소
         PriceDriver = Util.NowPriceDriver(Headless)
    except Exception as ex:
         print("Price Driver Err")
         print('에러가 발생 했습니다', ex)
    try: # 다음 증권
        KospiImageDriver = Util.Get_KospiGraphDriver(Headless)
    except Exception as ex:
        print("KospiImage Driver Err")
        print('에러가 발생 했습니다', ex)
    MakeCompanyFile(MakeCompanyList) #기업 리스트 갱신
    DBController = DBHandler.MySqlController(host, ID, PW, DB_name)

    label=[]
    while(True):
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y_%m_%d_%H시%M분%S초'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
            nowDatehour = now.strftime('%Y_%m_%d_%H시%M분'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
            try:
                NameList, PriceInfo, Fluctuation = Util.get_prices(PriceDriver)
                Util.PrintPrice(NameList,PriceInfo,Fluctuation)
            except Exception as ex:
                print("Price Info Err")
                print('에러가 발생 했습니다', ex)
                PriceDriver.quit()
                PriceDriver = Util.NowPriceDriver(Headless)
                NameList, PriceInfo, Fluctuation = Util.get_prices(PriceDriver)
            # print("========================================")
            try:
                headlines, news_info, Text,NewsUrl,CompanyFromNews = GetNewsInfo(NewsDriver) #뉴스에서 기업 추출
                print("News Updated...")
            except Exception as ex:
                print("News Update Err")
                NewsDriver.quit()
                NewsDriver = Util.News_get_driver(Headless)
                print('에러가 발생 했습니다', ex)
            try:
                Util.Write_News(headlines, CompanyFromNews, nowDatehour)  # 기업별 뉴스 자료 Writing
            except Exception as ex:
                print("News Write Err")
                CompanyList = Util.GetCompanyList()  # 코스피 상장 기업 업로드
            try:
                Util.GetKospiGraph(KospiImageDriver, PriceInfo, Fluctuation) # Kospi, Kosdaq 그래프 이미지 저장
                print("Get Kospi Graph")
            except Exception as ex:
                KospiImageDriver.quit()
                KospiImageDriver = Util.Get_KospiGraphDriver(Headless)
                print("Graph Err")
                print('에러가 발생 했습니다', ex)
            try:
                label = predict.classification(headlines, model)
                print("Get labels")
                DBController.UpdateNews(CompanyFromNews, headlines, Text, NewsUrl, news_info, label)  # 최신 20개 기사 DB저장
                DBController.InsertNewsHistory(CompanyFromNews, headlines, Text, NewsUrl, news_info, nowDatehour)
                print("DB Commit : News Updated, News History Inserted")
            except Exception as ex:
                print("Label Err")
                MakeCompanyFile(MakeCompanyList)  # 기업 리스트 갱신
                DBController = DBHandler.MySqlController(host, ID, PW, DB_name)
                print('에러가 발생 했습니다', ex)
            time.sleep(30)
            NewsDriver.refresh()
            PriceDriver.refresh()
            KospiImageDriver.refresh()
            print("DONE")