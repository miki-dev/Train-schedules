# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# https://opensource.com/article/20/5/web-scraping-python
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

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
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

station_name = []
train_line = []
destination = []
timetable = []
hours = []
minutes = []
n_of_trains = []

#find time table
timetable= soup.find_all(class_ = "timetable_box")
for i in timetable:
    

# find all hours
hours_list = soup.find_all(class_ = "results_03")
for i in hours_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)
