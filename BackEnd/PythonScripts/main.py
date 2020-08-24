import news_parser as Util
import datetime
import time
CompanyList=[]
def GetNewsInfo():
    headlines, news_info, Text,NewsUrl = Util.GetNews()
    CompanyFromNews = Util.GetCompanyFromNews(headlines, CompanyList)
    Util.save_headlines(headlines, news_info, Text,CompanyFromNews,NewsUrl)
    Util.PrintNews(headlines, news_info, Text, CompanyFromNews)

def GetPriceInfo():
    NameList, PriceInfo, Fluctuation = Util.get_prices() #KTOP 30, KOSPI, KOSPI200, KOSDAQ, KOSDAQ150, KRX300 순
    Util.PrintPrice(NameList, PriceInfo, Fluctuation)

if __name__ == '__main__':
    CompanyList = Util.GetCompanyList() # 코스피 상장 기업 업로드
    while(True):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y_%m_%d_%H시%M분%S초')
        print("#########################################")
        print("||  [현재 시각] : " + nowDatetime+"  ||")
        print("========================================")
        GetPriceInfo()
        print("========================================")
        GetNewsInfo()
        time.sleep(60)
