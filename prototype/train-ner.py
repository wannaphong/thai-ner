# -*- coding: utf-8 -*-
"""
NER ภาษาไทย
พัฒนาโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
"""
import argparse
import codecs
from pythainlp.tokenize import word_tokenize
from pythainlp.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
import nltk
import re
pattern = r'\[(.*?)\](.*?)\[\/(.*?)\]'
tokenizer = RegexpTokenizer(pattern)
def text2conll2002(text):
    text=text.replace(' ','<space>')
    text=text.replace("''",'"')
    text=text.replace("’",'"').replace("‘",'"')
    tag=tokenizer.tokenize(text)
    j=0
    conll2002=""
    for tagopen,text,tagclose in tag:
        word_cut=word_tokenize(text)
        i=0
        while i<len(word_cut):
            if word_cut[i]=="''" or word_cut[i]=='"':pass
            elif i==0 and tagopen!='word':
                conll2002+=word_cut[i]
                #conll2002+='\t'+pos_tag2[j][1]
                conll2002+='\t'+'B-'+'NP'#tagopen
            elif tagopen!='word':
                conll2002+=word_cut[i]
                #conll2002+='\t'+pos_tag2[j][1]
                conll2002+='\t'+'I-'+'NP'#tagopen
            else:
                conll2002+=word_cut[i]
                #conll2002+='\t'+pos_tag2[j][1]
                conll2002+='\t'+'O'
            conll2002+='\n'
            #j+=1
            i+=1
    return postag(conll2002)
def postag(text):
    listtxt=[i for i in text.split('\n') if i!='']
    list_word=[]
    for data in listtxt:
        list_word.append(data.split('\t')[0])
    #print(text)
    list_word=pos_tag(list_word,engine='artagger')
    text=""
    i=0
    for data in listtxt:
        text+=data.split('\t')[0]+'\t'+list_word[i][1]+'\t'+data.split('\t')[1]+'\n'
        i+=1
    return text
def get_data(fileopen):
	with codecs.open(fileopen, 'r',encoding='utf8') as f:
		lines = f.read().splitlines()
	return lines
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
        txt=text2conll2002(data).split('\n')
        for d in txt:
            tt=d.split('\t')
            if d!="": data_num.append((tt[0],tt[1],tt[2]))
        #print(data_num)
        data_all.append(data_num)
    #print(data_all)
    return data_all
def write_conll2002(file_name,data):
    with codecs.open(file_name, "w", "utf-8-sig") as temp:
        temp.write(data)
    return True
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in sent] for sent in train_sents]
        #print(train_data)
        self.tagger = nltk.UnigramTagger(train_data)
        self.tagger = nltk.tag.BigramTagger(train_data, backoff=self.tagger)
        self.tagger = nltk.tag.TrigramTagger(train_data, backoff=self.tagger)
        print(self.tagger.evaluate(train_data))
    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag) in zip(sentence, chunktags)]
        #print(conlltags)
        return conlltags
def run(lists):
    data=alldata_list(lists)
    tag=UnigramChunker(data)
    while True:
        texts=input("Text : ")
        toword=word_tokenize(texts)
        pos=pos_tag(toword,engine='artagger')
        ner=tag.parse(pos)
        print(ner)
if __name__ == '__main__':
    listdata=get_data("general.text")
    run(listdata)
