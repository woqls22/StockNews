import os
os.environ['KERAS_BACKEND'] = 'tensorflow'
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Okt
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import datetime
pos = []
neg = []
posneg = []
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
# 한글 형태소 분해작업
def run():
    train_data = pd.read_csv("Data/train.csv", encoding='CP949')
    test_data = pd.read_csv("Data/test.csv", encoding='CP949')
    print(train_data.groupby('label').size().reset_index(name='count'))
    print(test_data.groupby('label').size().reset_index(name='count'))
    okt = Okt()
    X_train = []
    for sentence in train_data['headline']:
        temp_X = []
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', str(sentence))
        temp_X = okt.morphs(sentence, stem=True) #토큰화 작업
        temp_X = [word for word in temp_X if not word in stopwords]
        X_train.append(temp_X)
    X_test=[]
    for sentence in test_data['headline']:
        temp_X = []
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', str(sentence))
        temp_X = okt.morphs(sentence, stem=True) #토큰화 작업
        temp_X = [word for word in temp_X if not word in stopwords]
        X_test.append(temp_X)



    # 토큰화된 단어를 정수인코딩
    max_words = 35000
    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(X_train)
    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)
    print("제목의 최대 길이 : ", max(len(l) for l in X_train))
    print("제목의 평균 길이 : ", sum(map(len, X_train))/ len(X_train))
    plt.hist([len(s) for s in X_train], bins=50)
    plt.xlabel('length of Data')
    plt.ylabel('number of Data')
    plt.show()
    # y값 (라벨링)인코딩
    y_train = []
    y_test = []
    # one hot encoding
    for i in range(len(train_data['label'])):
        if train_data['label'].iloc[i] == 1:
            y_train.append([0, 0, 1])
        elif train_data['label'].iloc[i] == 0:
            y_train.append([0, 1, 0])
        elif train_data['label'].iloc[i] == -1:
            y_train.append([1, 0, 0])
    for i in range(len(test_data['label'])):
        if test_data['label'].iloc[i] == 1:
            y_test.append([0, 0, 1])
        elif test_data['label'].iloc[i] == 0:
            y_test.append([0, 1, 0])
        elif test_data['label'].iloc[i] == -1:
            y_test.append([1, 0, 0])

    y_train = np.array(y_train)
    y_test = np.array(y_test)
    # 리스트 셔플
    max_len = 40 #전체 데이터 길이를 30으로 맞춤
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_test = pad_sequences(X_test, maxlen = max_len)

    #긍정, 부정, 중립 3가지 분류를 위한 LSTM, softmax, categorical_crossentropy 적용
    model = Sequential()
    model.add(Embedding(max_words, 100))
    model.add(LSTM(128))
    model.add(Dense(3,activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train,y_train, epochs=5, batch_size=10, validation_split=0.1)

    predict = model.predict(X_test)
    predict_labels = np.argmax(predict, axis=1)
    original_labels = np.argmax(y_test, axis=1)



    for i in range(30):
        origin_label=""
        if(original_labels[i] == 1):
            origin_label="중립"
        elif (original_labels[i] == 2):
            origin_label = "긍정"
        else:
            origin_label="부정"
        predict_label = ""
        if (predict_labels[i] == 1):
            predict_label = "중립"
        elif (predict_labels[i] == 2):
            predict_label = "긍정"
        else:
            predict_label = "부정"
        print("[", test_data['headline'].iloc[i], "]\t[예측한 라벨 : ",predict_label,"]")
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y_%m_%d_%H시%M분%S초')
    model.save('Model'+nowDatetime+'.h5')

if __name__ == '__main__':
    run()