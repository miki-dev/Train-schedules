# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#https://opensource.com/article/20/5/web-scraping-python

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
soup = BeautifulSoup(page.text, “html.parser”)

station_name = []
train_line = []
destination = []
timetable = []
hours = []
minutes = []
n_of_trains = []

#find time table
timetable= soup.find_all(class_ = "timetable_box")

