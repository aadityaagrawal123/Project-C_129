from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

source_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(source_url)

time.sleep(10)

Star_names = []
Distance =[]
Mass = []
Radius =[]

def scrape():

    page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

    soup = BeautifulSoup(page.text, "html.parser")

    temp_list = []

    star_table = soup.find_all('table', {"class":"wikitable sortable"})

    total_table = len(star_table)

    table_rows = star_table[2].find_all('tr')

    for tr_tag in table_rows:
        td_tags = tr_tag.find_all('td')
        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)

    print(temp_list)

    for i in range(1,len(temp_list)):
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7])
        Radius.append(temp_list[i][8])

scrape()


headers = ['Star_name','Distance','Mass','Radius']
stars_data_file = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=headers)
stars_data_file.to_csv('brown_dwarfs_data.csv', index=False)