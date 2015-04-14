__author__ = 'grizzlemuff'
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json, urllib2
import time
import csv
import requests

#will merge bitcoin data csv file with the guardian dates, url, title, body csv file on date(aka timestamp)
import pandas as pd

a = pd.read_csv("sentimentOut.csv")
b = pd.read_csv("articles.csv")
c = pd.read_csv("2013-2014_bitcoin.csv")
d = pd.read_csv("fnpOut.csv")

b = b.dropna(axis=1)
merged = a.merge(c)
merged_again=b.merge(c, on='Timestamp')
# merged_again.to_csv('articleContent_with_bitcoinvalue.csv', index=False)
# merged.to_csv("datum_sentiment_bitcoin2.csv", index=False)

e = pd.read_csv("datum_sentiment_bitcoin2.csv")
merged_fnp=d.merge(e)
# merged_fnp.to_csv("datum_fnp_bitcoin.csv", index=False)


e=pd.read_csv('datum_fnp_bitcoin.csv')
#get number articles published by date and write them to file
e1= e.groupby(['Timestamp']).count()
# e1.sort(['Timestamp'],ascending=False).to_csv('yy.csv')

#merge counts file with bitcoin data
f=pd.read_csv('yy.csv')
counts=f.merge(e, on='Timestamp')
# counts.to_csv('with_counts.csv', index=False)





