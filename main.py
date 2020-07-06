# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# https://opensource.com/article/20/5/web-scraping-python
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# data into CSV;  https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
# look for data;  https://www.edureka.co/blog/web-scraping-with-python/
# programming historian;  https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
# https://realpython.com/beautiful-soup-web-scraper-python/

#import libraries
import requests
from bs4 import BeautifulSoup

#set webpage you want to search
url = "https://www.jreast-timetable.jp/2007/timetable/tt1341/1341010.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

#info from table
info = soup.find_all("div", {"class": "timetable_box"})
#print (len(info))

#station name and train line
station_name = soup.find("h2", {"class": "timetable_h"})
print(station_name)
#train_line = station_name.br[0].text
#print(train_line)





#translation
# Convert ShiftJIS to UTF-8
import sys
import codecs

ustdout = codecs.getwriter('utf_8')(sys.stdout)
jstdin = codecs.getreader('shift_jis')(sys.stdin)

for line in jstdin.readlines():
    ustdout.write(line)

#OR
H='Chinese Characters'
print h.decode('utf8')

#OR 
import json
a = "chinese characters here"
print json.dumps(a, ensure_ascii=False)

>>> json_string = json.dumps("ברי צקלה", ensure_ascii=False).encode('utf8')
>>> json_string
b'"\xd7\x91\xd7\xa8\xd7\x99 \xd7\xa6\xd7\xa7\xd7\x9c\xd7\x94"'
>>> print(json_string.decode())
"ברי צקלה"








#weekday/weekend
day = info.find_all("div", {"class": "timetable basicTable02"})
#print(day.h3[0].text)

#timetable
hours = []
minutes = [] 
timetable = info.find_all("table", {"class": "result_03"})
for i in timetable:
    hour = i.find(td[0])
    hours.append(hour.text)
    for m in timetable:
        minute = m.find("span,  {"class": "minute"})
        minutes.append(minute.text)

                        
#new file name
filename = station_name +" Timetable.csv"
f = open(filename, "w")

header = "Hour, Minute\n" 
f.write(header)
"""
for a in soup.findAll('a',href=True, attrs={'class':'timteble_box'}):
name=a.find('div', attrs={'class':''})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 

#find time table
timetable= soup.find_all(class_ = "timetable_box")
# find all hours
hours_list = soup.find_all(class_ = "results_03")
for i in hours_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)"""
