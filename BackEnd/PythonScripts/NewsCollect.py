import requests
from bs4 import BeautifulSoup

def get_newses(keyword):
    f = open("navernews.csv", "w")
    # 데이터의 헤더부분을 입력한다.
    f.write("제목, 언론사\n")
    page = 1
    for page in range(1, 4000,10):
        raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start=" + str(page),
                           headers={"User-Agent": "Mozilla/5.0"})
        html = BeautifulSoup(raw.text, 'html.parser')
        # 컨테이너: ul.type01 > li
        # 기사제목: a._sp_each_title
        # 언론사: span._sp_each_source
        articles = html.select("ul.type01 > li")
        for ar in articles:
            title = ar.select_one("a._sp_each_title").text
            source = ar.select_one("span._sp_each_source").text

            print(title)

            title = title.replace(",", "")
            source = source.replace(",", "")
            try:
                f.write(title+ '\n')
            except:
                pass
    # navernews.csv 파일 닫음
    f.close()
if __name__ == '__main__':
    get_newses("실적개선상한가")