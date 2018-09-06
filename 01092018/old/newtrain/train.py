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
thaicut="newmm"
#จัดการประโยคซ้ำ
data_not=[]
def Unique(p):
 text=re.sub("<[^>]*>","",p)
 text=re.sub("\[(.*?)\]","",text)
 text=re.sub("\[\/(.*?)\]","",text)
 if text not in data_not:
  data_not.append(text)
  return True
 else:
  return False
# เตรียมตัวตัด tag ด้วย re
pattern = r'\[(.*?)\](.*?)\[\/(.*?)\]'
tokenizer = RegexpTokenizer(pattern) # ใช้ nltk.tokenize.RegexpTokenizer เพื่อตัด [TIME]8.00[/TIME] ให้เป็น ('TIME','ไง','TIME')
# จัดการกับ tag ที่ไม่ได้ tag
def toolner_to_tag(text):
 text=text.strip().replace("FACILITY","LOCATION").replace("[AGO]","").replace("[/AGO]","")
 text=re.sub("<[^>]*>","",text)
 text=re.sub("(\[\/(.*?)\])","\\1***",text)#.replace('(\[(.*?)\])','***\\1')# text.replace('>','>***') # ตัดการกับพวกไม่มี tag word
 text=re.sub("(\[\w+\])","***\\1",text)
 text2=[]
 for i in text.split('***'):
  if "[" in i:
   text2.append(i)
  else:
   text2.append("[word]"+i+"[/word]")
 text="".join(text2)#re.sub("[word][/word]","","".join(text2))
 return text.replace("[word][/word]","")
# แปลง text ให้เป็น conll2002
def text2conll2002(text,pos=True):
    """
    ใช้แปลงข้อความให้กลายเป็น conll2002
    """
    text=toolner_to_tag(text)
    text=text.replace("''",'"')
    text=text.replace("’",'"').replace("‘",'"')#.replace('"',"")
    tag=tokenizer.tokenize(text)
    j=0
    conll2002=""
    for tagopen,text,tagclose in tag:
        word_cut=word_tokenize(text,engine=thaicut) # ใช้ตัวตัดคำ newmm
        i=0
        txt5=""
        while i<len(word_cut):
            if word_cut[i]=="''" or word_cut[i]=='"':pass
            elif i==0 and tagopen!='word':
                txt5+=word_cut[i]
                txt5+='\t'+'B-'+tagopen
            elif tagopen!='word':
                txt5+=word_cut[i]
                txt5+='\t'+'I-'+tagopen
            else:
                txt5+=word_cut[i]
                txt5+='\t'+'O'
            txt5+='\n'
            #j+=1
            i+=1
        conll2002+=txt5
    if pos==False:
        return conll2002
    return postag(conll2002)
# ใช้สำหรับกำกับ pos tag เพื่อใช้กับ NER
# print(text2conll2002(t,pos=False))
def postag(text):
    listtxt=[i for i in text.split('\n') if i!='']
    list_word=[]
    for data in listtxt:
        list_word.append(data.split('\t')[0])
    #print(text)
    list_word=pos_tag(list_word,engine='perceptron')
    text=""
    i=0
    for data in listtxt:
        text+=data.split('\t')[0]+'\t'+list_word[i][1]+'\t'+data.split('\t')[1]+'\n'
        i+=1
    return text
# เขียนไฟล์ข้อมูล conll2002
def write_conll2002(file_name,data):
    """
    ใช้สำหรับเขียนไฟล์
    """
    with codecs.open(file_name, "w", "utf-8-sig") as temp:
        temp.write(data)
    return True
# อ่านข้อมูลจากไฟล์
def get_data(fileopen):
	"""
    สำหรับใช้อ่านทั้งหมดทั้งในไฟล์ทีละรรทัดออกมาเป็น list
    """
	with codecs.open(fileopen, 'r',encoding='utf-8-sig') as f:
		lines = f.read().splitlines()
	return [a for a in lines if Unique(a)] # เอาไม่ซ้ำกัน

def alldata(lists):
    text=""
    for data in lists:
        text+=text2conll2002(data)
        text+='\n'
    return text

def alldata_list(lists):
    data_all=[]
    for data in lists:
        data_num=[]
        try:
            txt=text2conll2002(data,pos=True).split('\n')
            for d in txt:
                tt=d.split('\t')
                if d!="":
                    if len(tt)==3:
                        data_num.append((tt[0],tt[1],tt[2]))
                    else:
                        data_num.append((tt[0],tt[1]))
            #print(data_num)
            data_all.append(data_num)
        except:
            print(data)
    #print(data_all)
    return data_all

def alldata_list_str(lists):
	string=""
	for data in lists:
		string1=""
		for j in data:
			string1+=j[0]+"	"+j[1]+"	"+j[2]+"\n"
		string1+="\n"
		string+=string1
	return string

def get_data_tag(listd):
	list_all=[]
	c=[]
	for i in listd:
		if i !='':
			c.append((i.split("\t")[0],i.split("\t")[1],i.split("\t")[2]))
		else:
			list_all.append(c)
			c=[]
	return list_all
def getall(lista):
    ll=[]
    for i in lista:
        o=True
        for j in ll:
            if re.sub("\[(.*?)\]","",i)==re.sub("\[(.*?)\]","",j):
                o=False
                break
        if o==True:
            ll.append(i)
    return ll

data1=getall(get_data(file_name+".txt"))
print(len(data1))
'''import dill
with open('datatrain.data', 'rb') as file:
 datatofile = dill.load(file)'''
datatofile=alldata_list(data1)
tt=[]
#datatofile.reverse()
import random
#random.shuffle(datatofile)
print(len(datatofile))
#training_samples = datatofile[:int(len(datatofile) * 0.8)]
#test_samples = datatofile[int(len(datatofile) * 0.8):]
'''training_samples = datatofile[:2822]
test_samples = datatofile[2822:]'''
#print(test_samples[0])
#tag=TrainChunker(training_samples,test_samples) # Train

#run(training_samples,test_samples)


from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
import sklearn_crfsuite
from pythainlp.corpus import stopwords
stopwords = stopwords.words('thai')

def isThai(chr):
 cVal = ord(chr)
 if(cVal >= 3584 and cVal <= 3711):
  return True
 return False
def isThaiWord(word):
 t=True
 for i in word:
  l=isThai(i)
  if l!=True and i!='.':
   t=False
   break
 return t

def is_stopword(word):
    return word in stopwords
def is_s(word):
    if word == " " or word =="\t" or word=="":
        return True
    else:
        return False

def lennum(word,num):
    if len(word)==num:
        return True
    return False
def doc2features0(doc, i):
    word = doc[i][0]
    postag = doc[i][1]
    # Features from current word
    features={
        'word.word': word,
        'word.stopword': is_stopword(word),
        'word.isthai':isThaiWord(word),
        'word.isspace':word.isspace(),
        'postag':postag,
        'postag[:2]': postag[:2],
        'word.isdigit()': word.isdigit(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:]
    }
    if word.isdigit() and len(word)==5:
        features['word.islen5']=True
    #if postag=='NCNM':
    #    features['word.islenten']=len(word)==10
    # Features from previous word
    if i > 0:
        prevword = doc[i-1][0]
        postag1 = doc[i-1][1]
        features['word.prevword'] = prevword
        features['word.previsspace']=prevword.isspace()
        features['word.previsthai']=isThaiWord(prevword)
        features['word.prevstopword']=is_stopword(prevword)
        features['word.prepostag'] = postag1
        features['-1:postag[:2]']: postag1[:2]
        features['word.prevwordisdigit'] = prevword.isdigit()
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1][0]
        postag1 = doc[i+1][1]
        features['word.nextword'] = nextword
        features['word.nextisspace']=nextword.isspace()
        features['word.nextpostag'] = postag1
        features['word.nextisthai']=isThaiWord(nextword)
        features['word.nextstopword']=is_stopword(nextword)
        features['word.nextwordisdigit'] = nextword.isdigit()
        features['+1:postag[:2]']: postag1[:2]
    else:
        features['EOS'] = True # Special "End of Sequence" tag
    return features

def extract_features0(doc):
    return [doc2features0(doc, i) for i in range(len(doc))]

def get_labels(doc):
    return [tag for (token,postag,tag) in doc]

from sklearn.model_selection import train_test_split
X_data = [extract_features0(doc) for doc in datatofile]
y_data = [get_labels(doc) for doc in datatofile]

X, X_test, y, y_test = train_test_split(X_data, y_data, test_size=0.2)

def is_stopword(word):
    return word in stopwords
def doc2features2(doc, i):
    word = doc[i]
    postag = doc[i][1]
    # Features from current word
    features={
        'word.word': word,
        'word.stopword': is_stopword(word),
        'postag':postag,
        'postag[:2]': postag[:2],
        'word.isdigit()': word.isdigit(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:]
    }
    # Features from previous word
    if i > 0:
        prevword = doc[i-1]
        postag1 = doc[i-1][1]
        features['word.prevword'] = prevword
        features['word.prepostag'] = doc[i-1][1]
        features['-1:postag[:2]']: postag1[:2]
        features['word.prevwordisdigit'] = prevword.isdigit()
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1]
        postag1 = doc[i+1][1]
        features['word.nextword'] = nextword
        features['+1:postag[:2]']: postag1[:2]
        features['-1:postag[:2]']: postag1[:2]
        features['word.nextwordisdigit'] = nextword.isdigit()
    else:
        features['EOS'] = True # Special "End of Sequence" tag
    return features

def extract_features2(tag):
    i=0
    l=[]
    while i<len(tag):
        l.append(doc2features2(tag,i))
        i+=1
    return l

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=500,
    all_possible_transitions=True,
    model_filename=file_name+"-pos-new.model2"
)
crf.fit(X, y);

labels = list(crf.classes_)
labels.remove('O')
y_pred = crf.predict(X_test)
e=metrics.flat_f1_score(y_test, y_pred,
                      average='weighted', labels=labels)
print(e)
sorted_labels = sorted(
    labels,
    key=lambda name: (name[1:], name[0])
)
print(metrics.flat_classification_report(
    y_test, y_pred, labels=sorted_labels, digits=3
))
import dill
with open("datatrain.data", "wb") as dill_file:
 dill.dump(datatofile, dill_file)

