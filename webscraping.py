from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

driver=webdriver.Chrome()

name=[]
ratings=[]
driver.get('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc')
content=driver.page_source
soup=BeautifulSoup(content,features="html5lib")

for a in soup.findAll('h3',attrs={'class': 'Lister-item-mode-advanced'}):
    name.append(str(h3.text).strip())

for i in name:
    print("\n"+i)


