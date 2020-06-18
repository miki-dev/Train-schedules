import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

#set webpage you want to search
url = "https://www.jreast-timetable.jp/2006/timetable/tt1341/1341010.html"
response = requests.get(url)

station_name = []
train_line = []
destination = []
timetable = []
hours = []
minutes = []
n_of_trains = []

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
