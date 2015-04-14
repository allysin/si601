__author__ = 'grizzlemuff'
import csv
feelings=open('gDatum.txt','rU')
date=[]
title=[]
article=[]
d=0
t=1
b=2


for item in feelings:
    item =item.split('\t')
    while d<148:
        # item=item[:10]
        date.append(item[d][:10])
        d+=3
    while t < 296:
        title.append(item[t])
        t+=3
    while b < 446:
        article.append(item[b])
        b+=3

datumed=zip(date, title, article)
# csvFile=open('datumList.csv', 'wb')
# c=csv.writer(csvFile)
# for item in datumed:
#     c.writerow(item)
# csvFile.close()
print datumed
import pandas as pd
print datumed.groupby(date)