# -*- coding: utf-8 -*-
# เรียกใช้งานโมดูล
file_name="data"
import codecs
from pythainlp.tokenize import word_tokenize
#import deepcut
from pythainlp.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
import glob
import nltk
import re
# thai cut


from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
import sklearn_crfsuite
from pythainlp.corpus import stopwords
stopwords = stopwords.words('thai')
def is_stopword(word):
    return word in stopwords
def is_s(word):
    if word == " " or word =="\t" or word=="":
        return True
    else:
        return False
def doc2features_notpost(doc, i):
    word = doc[i][0]
    # Features from current word
    features={
        'bias': 1.0,
        'word.word': word,
        'word.stopword': is_stopword(word),
        'word.isdigit()': word.isdigit(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:]
    }
    # Features from previous word
    if i > 0:
        prevword = doc[i-1][0]
        features['word.prevword'] = prevword
        features['word.prevwordisdigit'] = prevword.isdigit()
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1][0]
        features['word.nextword'] = nextword
        features['word.nextwordisdigit'] = nextword.isdigit()
    else:
        features['EOS'] = True # Special "End of Sequence" tag
    return features

def extract_features_notpost(doc):
    return [doc2features_notpost(doc, i) for i in range(len(doc))]

def get_labels(doc):
    return [tag for (token,tag) in doc]

def is_stopword(word):
    return word in stopwords
def doc2features2_notpost(doc, i):
    word = doc[i]
    # Features from current word
    features={
        'bias': 1.0,
        'word.word': word,
        'word.stopword': is_stopword(word),
        'word.isdigit()': word.isdigit(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:]
    }
    # Features from previous word
    if i > 0:
        prevword = doc[i-1]
        features['word.prevword'] = prevword
        features['word.prevwordisdigit'] = prevword.isdigit()
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1]
        features['word.nextword'] = nextword
        features['word.nextwordisdigit'] = nextword.isdigit()
    else:
        features['EOS'] = True # Special "End of Sequence" tag
    return features

def extract_features2_notpost(tag):
    i=0
    l=[]
    while i<len(tag):
        l.append(doc2features2_notpost(tag,i))
        i+=1
    return l

crf2 = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=600,
    all_possible_transitions=True,
    model_filename=file_name+".model2"
)
X_test = extract_features2_notpost(["พวกเรา","จะ","ไป","เที่ยว","หนองคาย"])
print(crf2.predict_single(X_test))
def get_ner(text):
    word_cut=word_tokenize(text)
    #print(list_word)
    X_test = extract_features_notpost([(data) for i,data in enumerate(word_cut)])
    y_=crf2.predict_single(X_test)
    return [(word_cut[i],data) for i,data in enumerate(y_)]

while True:
    t=input("Text : ")
    print(get_ner(t))