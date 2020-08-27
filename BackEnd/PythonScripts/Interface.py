# Data/Kosdaq.jpg
# Data/Kospi.jpg
# Data/News ~ .csv
# Data/CompanyNewsList.csv
import pymysql
class MySqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host = host, user = id, password = pw, db = db_name, charset='utf8')
        self.curs = self.conn.cursor()
    def UpdateNews(self, CompanyFromNews, Headline, Text, URL, NewsInfo): # Top 20 News 업데이트
        try:
            for index in range(0,len(CompanyFromNews)):
                sql = 'UPDATE News SET Company = %s, Headline = %s, Text = %s, URL = %s, Info = %s where IDX = %s'
                self.curs.execute(sql, (CompanyFromNews[index], Headline[index], Text[index], URL[index], NewsInfo[index], str(index+1)))
                self.conn.commit()
            print("Stock News Updated.")
        except:
            print("DB Err] Update Top 20 News ")

    def InsertNewsHistory(self, CompanyFromNews, Headline, Text, URL, NewsInfo,DateTime): # 뉴스 히스토리 기록
        try:
            for index in range(0,len(CompanyFromNews)):
                sql = 'Insert IGNORE  INTO NewsHistory VALUES(%s, %s, %s, %s, %s,%s)'
                self.curs.execute(sql, (CompanyFromNews[index], Headline[index], Text[index], URL[index], NewsInfo[index], DateTime))
                self.conn.commit()
            print("Stock NewsHistory Updated.")
        except:
            print("DB Err] Insert News History")

    def GetTop20News(self): # Top 20 News Fetch
            sql = 'SELECT * FROM News'
            self.curs.execute(sql)
            data = self.curs.fetchall()
            headlines = []
            for i in data:
                headlines.append(i[2])
            return headlines #헤드라인 리턴

    def GetNewsAboutCompany(self, CompanyName): # 원하는 기업 뉴스 Fetch
            sql = "SELECT Headline, NewsInfo, Time, URL FROM NewsHistory where Company = %s"
            self.curs.execute(sql,(CompanyName))
            data = self.curs.fetchall()
            for i in data:
                print(i)

if __name__ == '__main__':
    host = 'HOST'
    ID = 'ID'
    PW = 'PW'
    DB_name = 'DBNAME'
    DBController = MySqlController(host, ID, PW, DB_name)
    print("Stock News App")
    while(True):
        print("Enter the Command [Top20 or CompanyNews] : ", end='')
        command = input()
        if(command =='Top20'):
            DBController.GetTop20News()
        else:
            print("Enter the CompanyName : ", end='')
            CompanyName = input()
            DBController.GetNewsAboutCompany(CompanyName)