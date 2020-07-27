#intoduction:  https://realpython.com/python-web-scraping-practical-introduction/
#cheatsheet:   https://blog.hartleybrody.com/web-scraping-cheat-sheet/#making-simple-requests
#clean-up data: https://opensource.com/article/20/5/web-scraping-python
#data into CSV:  https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
# https://realpython.com/beautiful-soup-web-scraper-python/
#pandas table tutorial:  https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
#pandas table rearrange:  https://medium.com/swlh/how-to-scrape-a-website-with-a-single-line-of-python-code-5efe124275bb
#tr -> td: https://stackoverflow.com/questions/46242664/python-web-scraping-html-table-and-printing-to-csv

#import libraries
import requests
from bs4 import BeautifulSoup
from ftfy import fix_encoding

#set webpage you want to search
url = "https://www.jreast-timetable.jp/2007/timetable/tt1341/1341011.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

#station name and train line
title = soup.find("h2", {"class": "timetable_h"})
title = title.get_text()
title = fix_encoding(title)
title = str.split(title)
station_name = title[0]
#print(station_name)
train_line = ' '.join(title[1:])
#print(train_line)

#weekday or weekend
for p in soup.select('p'):
    if p['class'] == "tit_holiday"
        day = p.text.strip()
        print(p.text)
        elif p['class'] == "tit_weekday":
            day = p.text.strip()
            print(p.text)
            else:
                break

#timetable
timetable = soup.find("table", {"class": "result_03"})
timetable = timetable.find_all("tr")
print(len(timetable)) #should be 21
for td in timetable.select('td')):
    time = td.chilren[0]
    time = time.text.strip()
    for s in td.select('span', {"class": "minute"}):
        time.append(s)
    print(time.text)
    
#another way for timetable
list_of_rows = []
for row in timetable.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

for item in list_of_rows:
    print(' '.join(item))

    
#new file name
filename = station_name +" Timetable.csv"
f = open(filename, "w")

header = "Hour, Minute\n" 
f.write(header)

import pandas as pd
info = pd.DataFrame({
    "station_name": station_name,
    "train_line": train_line,
    "week": day,
    "times": hours
})
info
                        
#can put lines together
for product in soup.find_all("div", "products"):
    product_title = product.find("h3").text
    product_price = product.find("span", "price").text
    product_url = product.find("a")["href"]
    print "{} is selling for {} at {}".format(product_title, product_price, product_url)

