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
    name.append(str(a.text).strip())

for b in soup.findAll('div',attrs={'class': 'inline-block ratings-imdb-rating'}):
    ratings.append(str(b.text).strip())
df=pd.DataFrame({'Product Name': name, 'Ratings': ratings})
df.to_csv('products.csv',index=True,encoding='utf-8')


