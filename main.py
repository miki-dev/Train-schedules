# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# https://opensource.com/article/20/5/web-scraping-python
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# data into CSV;  https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
# look for data;  https://www.edureka.co/blog/web-scraping-with-python/
# programming historian;  https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
# https://realpython.com/beautiful-soup-web-scraper-python/

#import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

#set webpage you want to search
url = "https://www.jreast-timetable.jp/2006/timetable/tt1341/1341010.html"
page = requests.get(url)
#page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

#info from table
info = soup.find_all("div", {"class": "timetable_box"})
print (len(info))

#station name and train line
station_name = info.find_all("h2", {"class": "timetable_h"})
#print(station_name[0].text)
train_line = station_name.br[0].text
#print(train_line)

#weekday/weekend
day = info.find_all("div", {"class": "timetable basicTable02"})
#print(day.h3[0].text)

#timetable
timetable = info.find_all("table", {"class": "result_03"})
hours = timetable.find_all("tr")
minutes = timetable.find_all("span", {"class": "minute"})
#print(len(hours))

for i in hours:
    hour = timetable.tr.td[i].text
    for m in minutes:
        minute = minutes[m].text
        

    
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

station_name = []
train_line = []
destination = []
timetable = []
hours = []
minutes = []
n_of_trains = []

#find time table
timetable= soup.find_all(class_ = "timetable_box")
# find all hours
hours_list = soup.find_all(class_ = "results_03")
for i in hours_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)"""
