__author__ = 'grizzlemuff'
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json, urllib2
from time import sleep
import csv
import unirest


#the Guardian API will only return a maximum of 50 json strings per page. since we know that there are 246
#articles that containing 'bitcoin' for the period of feb 25, 2013-feb 25, 2014 we make 5 calls, 1 per page
url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-02-25&to-date=2014-02-25&page=1&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page1=urllib2.urlopen(url)
page1=page1.read()
page1=json.loads(page1)

url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-02-25&to-date=2014-02-25&page=2&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page2=urllib2.urlopen(url)
page2=page2.read()
page2=json.loads(page2)

url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-02-25&to-date=2014-02-25&page=3&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page3=urllib2.urlopen(url)
page3=page3.read()
page3=json.loads(page3)

url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-02-25&to-date=2014-02-25&page=4&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page4=urllib2.urlopen(url)
page4=page4.read()
page4=json.loads(page4)

url='http://content.guardianapis.com/search?q=bitcoin&from-date=2013-02-25&to-date=2014-02-25&page=5&page-size=50&api-key=s4x26jtzauepdxkmkjj3rdj3'
page5=urllib2.urlopen(url)
page5=page5.read()
page5=json.loads(page5)




#initialize three lists to contain the date (yyyy-mm-dd), article, and article url
#using a counter (page 1 =50 results, page 2=50 results, etc until all 251 results returned
# write the corresponding values from the json string to the lists
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

x=0
while x<50:
    day=(page2['response']['results'][x]['webPublicationDate'])
    dates.append(day[:10])
    titles.append(page2['response']['results'][x]['webTitle'])
    urls.append(page2['response']['results'][x]['webUrl'])
    x+=1


x=0
while x <50:
    day=(page3['response']['results'][x]['webPublicationDate'])
    dates.append(day[:10])
    titles.append(page3['response']['results'][x]['webTitle'])
    urls.append(page3['response']['results'][x]['webUrl'])
    x+=1

x=0
while x <50:
    day=(page4['response']['results'][x]['webPublicationDate'])
    dates.append(day[:10])
    titles.append(page4['response']['results'][x]['webTitle'])
    urls.append(page4['response']['results'][x]['webUrl'])
    x+=1

x=0
while x <46:
    day=(page5['response']['results'][x]['webPublicationDate'])
    dates.append(day[:10])
    titles.append(page5['response']['results'][x]['webTitle'])
    urls.append(page5['response']['results'][x]['webUrl'])
    x+=1



#initialize a list called body
#iterate through the urls list to open each url and parse the contents of the <p> fields
#<p> tags were chosen as most appropriate because a majority of the pages content the article body in this markup
#if the url html markup does not have any <p> tagged content, then neutral is appended to the list
body=[]

for item in urls:
    x=item
    x=urllib2.urlopen(x)
    x=x.read()
    soup = BeautifulSoup(x)
    inp=''
    for p in soup.findAll('div', {"class":"flexible-content-body"}):
        # print item
        inp=p.text
        body.append(inp)
        # print p.text
    if inp == '':
        for p in soup.findAll('div', {"id":"article-body-blocks"}):
            inp=p.text
            # print p.text
            body.append(inp)
    if inp == '':
        for p in soup.findAll('div', {"class":"block-elements"}):
            inp=p.text
            body.append(inp)
    if inp == '':
        body.append('NONE')


# #zip together all four lists. Will output a list of lists

title_encoded=[]
body_encoded=[]
for item in titles:
    item=item.encode('utf-8')
    title_encoded.append(item)


for item in body:
    item=item.encode('utf-8')
    body_encoded.append(item)

outputFile=zip(dates, title_encoded, urls, body_encoded)

#write to file, date, url, title, and body that was scraped from the HTML
# csvFile=open('articles.csv', 'wb')
# csvW=csv.writer(csvFile)
# for item in outputFile:
#     csvW.writerow(item)
#
# csvFile.close()





#using DatumBox API, passing in each article title and article content from the zipped list for sentiment analysis
#positive, negative or neutral will be returned
#sentiment for title and content is appended to alist

from DatumBox import DatumBox
datum_box = DatumBox('d3ce53ca1cead4e08490df097c890967')
eTitle=[]
eBody=[]
for item in outputFile:
    title=item[1]
    content=item[3]
    eTitle.append(datum_box.sentiment_analysis(title))
    eBody.append(datum_box.sentiment_analysis(content))




#zip together sentiment analyzed titles and body with the date
emoted=zip(dates,urls, eTitle, eBody)
e=open('sentimentOut.csv', 'wb')
eWriter=csv.writer(e)
for i in emoted:
    eWriter.writerow(i)
e.close()
