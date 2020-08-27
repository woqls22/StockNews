import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
def get_newses(keyword):
    f = open("navernews.csv", "w")
    # 데이터의 헤더부분을 입력한다.
    f.write("headline, label\n")
    number = 0
    page = 1
    for page in range(1, 1000,10):
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
            number=number+1
            print('['+str(number)+']'+title)

            title = title.replace(",", "")
            source = source.replace(",", "")
            try:
                f.write(title+ '\n')
            except:
                pass
    # navernews.csv 파일 닫음
    f.close()

def shuffle(filename):
    data = pd.read_csv(filename, encoding='CP949')
    x_train = []
    y_train = []
    for sentence in data['headline']:
        x_train.append(sentence)
    for sentence in data['label']:
        y_train.append(sentence)
    tmp = [[x, y] for x, y in zip(x_train, y_train)]
    random.shuffle(tmp)
    x_train = [n[0] for n in tmp]
    y_train = [n[1] for n in tmp]
    data = pd.DataFrame({
        'headline': x_train,
        'label': y_train
    })
    data.to_csv('result.csv', index=False, encoding='cp949')

if __name__ == '__main__':
    #get_newses("수주체결")
    shuffle('Data/train.csv')
    shuffle('Data/test.csv')