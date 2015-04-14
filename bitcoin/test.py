__author__ = 'grizzlemuff'

#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json, urllib2



url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-08-08&to-date=2014-02-03&page=1&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page1=urllib2.urlopen(url)
page1=page1.read()
page1=json.loads(page1)

x=0
dates=[]
titles=[]
urls=[]
while x <50:
    day=(page1['response']['results'][x]['webPublicationDate'])
    dates.append(day[:10])
    titles.append(page1['response']['results'][x]['webTitle'])
    urls.append(page1['response']['results'][x]['webUrl'])
    x+=1


x='http://www.theguardian.com/technology/2014/jan/21/ebay-clamps-down-on-bitcoin-sales-in-the-uk'
x=urllib2.urlopen(x)
x=x.read()
body=[]
soup = BeautifulSoup(x)
for p in soup.findAll('div', {"class":"flexible-content-body"}):
    body.append(p.text)


print body