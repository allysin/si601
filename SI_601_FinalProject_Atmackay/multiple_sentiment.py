__author__ = 'grizzlemuff'
import unirest
import pandas as pd
from time import sleep
import csv


f=open('sentimentOut.csv', 'rU')
f=pd.read_csv(f)
urls= f['Url']
dates=f['Timestamp']

sentiment_text=[]
sentiment_score=[]



#free natural processing ap from Taewook Kang available via mashape https://www.mashape.com/loudelement/free-natural-language-processing-service#!endpoint-nlp-url

for item in urls:
    response = unirest.get("https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-url/?url=%s" %item,

    headers={
    "X-Mashape-Authorization": "F2yND8dFRqOu3ckw2iMBmVopxGnm9PyH"
    }
    );
    sentiment_text.append(response.body['sentiment-text'])
    sentiment_score.append(response.body['sentiment-score'])
    sleep(5)



fnp=zip(dates,urls, sentiment_score, sentiment_text)
e=open('fnpOut.csv', 'wb')
eWriter=csv.writer(e)
for i in fnp:
    eWriter.writerow(i)
e.close()