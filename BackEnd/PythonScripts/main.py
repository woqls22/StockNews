import news_parser as Util
import datetime
import time
CompanyList=[]
Headless = True # False : 창띄움, True : 창없음
MakeCompanyList = False # 회사 리스트 갱신

def GetNewsInfo(driver):
    headlines, news_info, Text,NewsUrl = Util.GetNews(driver) # 헤드라인, 신문사 정보 및 게시 시간, 본문, 기사링크 파싱.
    CompanyFromNews = Util.GetCompanyFromNews(headlines, CompanyList)
    Util.save_headlines(headlines, news_info, Text,CompanyFromNews,NewsUrl)
    Util.PrintNews(headlines, news_info, Text, CompanyFromNews)
    return headlines, news_info, Text, NewsUrl,CompanyFromNews
def GetPriceInfo(driver):
    NameList, PriceInfo, Fluctuation = Util.get_prices(driver) #KTOP 30, KOSPI, KOSPI200, KOSDAQ, KOSDAQ150, KRX300 순
    Util.PrintPrice(NameList, PriceInfo, Fluctuation)
    return NameList, PriceInfo, Fluctuation
def MakeCompanyFile(MakeCompanyList):
    #Company CSV파일 생성
    Util.MakeCompanyCSV()

if __name__ == '__main__':
    CompanyList = Util.GetCompanyList() # 코스피 상장 기업 업로드
    NewsDriver = Util.News_get_driver(Headless)
    PriceDriver = Util.NowPriceDriver(Headless)
    MakeCompanyFile(MakeCompanyList) #기업 리스트 갱신
    while(True):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y_%m_%d_%H시%M분%S초')
        nowDatehour = now.strftime('%Y_%m_%d_%H시%M분') #뉴스 기록 TimeStamp
        print("\n\n#########################################")
        print("||  [현재 시각] : " + nowDatetime+"  ||")
        print("========================================")
        NameList, PriceInfo, Fluctuation = GetPriceInfo(PriceDriver)
        print("========================================")

        headlines, news_info, Text,NewsUrl,CompanyFromNews = GetNewsInfo(NewsDriver) #뉴스에서 기업 추출
        Util.Write_News(headlines, CompanyFromNews,nowDatehour)
        time.sleep(60)
        NewsDriver.refresh()
        PriceDriver.refresh()
