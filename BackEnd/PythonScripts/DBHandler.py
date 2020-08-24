# Data/Kosdaq.jpg
# Data/Kospi.jpg
# Data/News ~ .csv
# Data/CompanyNewsList.csv
import pymysql

class MySqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host = host, user = id, password = pw, db = db_name, charset='utf8')
        self.curs = self.conn.cursor()
    def UpdateNews(self, CompanyFromNews, Headline, Text, URL, NewsInfo):
        for index in range(0,len(CompanyFromNews)):
            sql = 'UPDATE News SET Company = %s, Headline = %s, Text = %s, URL = %s, Info = %s where IDX = %s'
            self.curs.execute(sql, (CompanyFromNews[index], Headline[index], Text[index], URL[index], NewsInfo[index], str(index+1)))
            self.conn.commit()
        print("Stock News Updated.")