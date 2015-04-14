__author__ = 'grizzlemuff'


from bs4 import BeautifulSoup
import json, urllib2
import time
import csv
import pandas as pd

f=open('articles.csv','ru')
f=pd.read_csv(f)

aa= f['Article Content'][240]



from DatumBox import DatumBox
datum_box = DatumBox('d3ce53ca1cead4e08490df097c890967')
print aa
print datum_box.sentiment_analysis(aa)

# eTitle=[]
# eBody=[]
# for item in outputFile:
#     title=item[1]
#     content=item[3]
#     eTitle.append(datum_box.sentiment_analysis(title))
#     eBody.append(datum_box.sentiment_analysis(content))
#
# emoted=zip(dates, urls, eTitle, eBody)
# e=open('sentimentOut.csv', 'wb')
# eWriter=csv.writer(e)
# for i in emoted:
#     eWriter.writerow(i)
# e.close()