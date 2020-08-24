import news_parser as Util
import datetime
def GetNewsInfo():
    headlines, news_info, Text = Util.get_headlines()
    Util.save_headlines(headlines, news_info, Text)
    Util.PrintNews(headlines, news_info, Text)

def GetPriceInfo():
    NameList, PriceInfo, Fluctuation = Util.get_prices() #KTOP 30, KOSPI, KOSPI200, KOSDAQ, KOSDAQ150, KRX300 순
    Util.PrintPrice(NameList, PriceInfo, Fluctuation)

if __name__ == '__main__':
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y_%m_%d_%H시%M분%S초')
    print("[현재 시각] : " + nowDatetime)
    print("========================================")
    GetPriceInfo()
    print("========================================")
    GetNewsInfo()
