import pandas as pd
import codecs
import re
positive = []
negative = []
posneg = []

def make_word_list():
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
        negative.append(line)
        posneg.append(line)
        if not line: break
    neg.close
    return positive,negative,posneg
def is_inPosneg(headline,posneg):
    for word in posneg:
        if(word in headline):
            return True
    return False

def get_score(headline, positive, negative, posneg):
    score = 0
    headline = headline.split(' ')
    if(not is_inPosneg(headline, posneg)):
        return 0
    for i in positive:
        if(i in headline):
            return 1
    for i in negative:
        if(i in headline):
            return -1
    return score

def Decision(score):
    if(score<0):return '-1'
    elif(score==0):return '0'
    else: return '1'
def make_lable():
    positive, negative, posneg = make_word_list()
    train_data = pd.read_csv("Data/train.csv", encoding='CP949')
    test_data = pd.read_csv("Data/test.csv", encoding='CP949')
    score = 0
    label = []
    headlines = train_data['headline']
    for number in range(len(train_data['headline'])):
        headline = train_data.iloc[number][0]
        headline = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》·]', '', headline)
        score = get_score(headline, positive, negative,posneg)
        label.append(Decision(score))
    data = pd.DataFrame({
        'headline': headlines,
        'label' : label
    })
    data.to_csv('Data/Train1.csv', index = False, encoding='cp949')

    label = []
    headlines = test_data['headline']
    for number in range(len(test_data['headline'])):
        headline = test_data.iloc[number][0]
        headline = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》·]', '', headline)
        score = get_score(headline, positive, negative,posneg)
        label.append(Decision(score))
    data = pd.DataFrame({
        'headline': headlines,
        'label' : label
    })
    data.to_csv('Data/Test1.csv', index = False, encoding='cp949')
if __name__ == '__main__':
    make_lable()
