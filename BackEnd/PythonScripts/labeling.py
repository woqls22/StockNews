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
    if(not is_inPosneg(headline, posneg)):
        return 0
    for i in negative:
        if(i in headline):
            score = score-1
    for i in positive:
        if(i in headline):
            score = score+1
    return score

def Decision(score):
    if(score<0):return '-1'
    elif(score>0):return '1'
    else: return '0'
def make_lable(filename):
    positive, negative, posneg = make_word_list()
    train_data = pd.read_csv(filename, encoding='CP949')
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
    data.to_csv(filename, index = False, encoding='cp949')
if __name__ == '__main__':
    make_lable('navernews.csv')
    print("done")
