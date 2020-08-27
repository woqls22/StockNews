from tensorflow.keras.models import load_model
from Interface import MySqlController
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Okt
import numpy as np
import re
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
def classification(newsheadlines,model):
    okt = Okt()
    max_words = 35000
    tokenizer = Tokenizer(num_words=max_words)
    X_test = []
    temp_X = []
    for i in range(len(newsheadlines)):
        newsheadline = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', newsheadlines[i])
        temp_X = okt.morphs(newsheadline, stem=True)  # 토큰화 작업
        temp_X = [word for word in temp_X if not word in stopwords]
        X_test.append(temp_X)
    tokenizer.fit_on_texts(X_test)
    X_test = tokenizer.texts_to_sequences(X_test)
    max_len = 30  # 전체 데이터 길이를 30으로 맞춤
    X_test = pad_sequences(X_test, maxlen=max_len)
    predict = model.predict(X_test)
    predict_labels = np.argmax(predict, axis=1)
    for i in range(len(predict_labels)):
        predict_label = predict_labels[i]
        if (predict_label == 1):
            predict_label = "중립"
        elif (predict_label == 2):
            predict_label = "호재"
        else:
            predict_label = "악재"
        print(newsheadlines[i]+"   ["+predict_label+"]")
        
def run():
    host = 'DB'
    ID = 'ID'
    PW = 'PW'
    DB_name = 'Table Name'
    DBController = MySqlController(host, ID, PW, DB_name)
    SQL = MySqlController(host, ID, PW, DB_name)
    headlines = SQL.GetTop20News()
    model = load_model('./NewsModel.h5')
    classification(headlines, model)
if __name__ == '__main__':
    run()