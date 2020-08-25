import codecs
import matplotlib.pyplot as plt
import plaidml.keras
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, Dense, LSTM
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Okt
import pandas as pd
import os
import numpy as np

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

pos = []
neg = []
posneg = []
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
positive = []
negative = []
posneg = []
pos = codecs.open("Data/positive_words_self.txt", 'rb', encoding='UTF-8')
while True:
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)
    if not line : break
pos.close
neg = codecs.open("Data/negative_words_self.txt", 'rb', encoding='UTF-8')
while True:
    line = neg.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)
    if not line: break
neg.close

train_data = pd.read_csv("Data/train.csv",encoding='CP949')
test_data = pd.read_csv("Data/test.csv",encoding='CP949')
print(train_data.groupby('label').size().reset_index(name='count'))
print(test_data.groupby('label').size().reset_index(name='count'))
# 한글 형태소 분해작업
okt = Okt()
X_train = []
for sentence in train_data['Headline']:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True) #토큰화 작업
    temp_X = [word for word in temp_X if not word in stopwords]
    X_train.append(temp_X)
X_test=[]
for sentence in test_data['Headline']:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True) #토큰화 작업
    temp_X = [word for word in temp_X if not word in stopwords]
    X_train.append(temp_X)

# 토큰화된 단어를 정수인코딩
max_words = 35000
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)


# plt.hist([len(s) for s in X_train], bins=50)
# plt.xlabel('length of Data')
# plt.ylabel('number of Data')
# plt.show()
# y값 (라벨링)인코딩
y_train = []
y_test = []
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

max_len = 35
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen = max_len)

#긍정, 부정, 중립 3가지 분류를 위한 LSTM, softmax, categorical_crossentropy 적용
model = Sequential()
model.add(Embedding(max_words, 100))
model.add(LSTM(128))
model.add(Dense(3,activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train,y_train, epochs=10, batch_size=10, validation_split=0.1)

predict = model.predict(X_test)
predict_labels = np.argmax(predict, axis=1)
original_labels = np.argmax(y_test, axis=1)

for i in range(30): print("기사제목 : ", test_data['Headline'].iloc[i], "/\t 원래 라벨 : ", original_labels[i], "/\t예측한 라벨 : ",predict_labels[i])