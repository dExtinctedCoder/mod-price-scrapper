from itertools import count, product
import re
import requests
from bs4 import BeautifulSoup



product = {}

def scrapper(keyword):
  site_url=f"https://www.jumia.com.ng/catalog/?q={keyword}"
  page = requests.get(url=site_url)
  soup=BeautifulSoup(page.content,'lxml')

  for a in soup.findAll('a', href=True, attrs={'class': 'core'}):
    price = a.find('div', attrs={'class': 'prc'})
    name = a.find('h3', attrs={'class': 'name'})
    strip_price = str(price.text)
    strip_name = str(name.text)
    x = strip_price[2:]
    transformed_string = re.sub(",","",x)
    price_num = int(transformed_string)
    product[strip_name] = price_num

  for key in product:
    print(key, '->', product[key])
    print('')

  

def extract(jeyword):
    scrapedword=str(scrapper(jeyword))

    print(scrapedword)

extract('iphone' + '11')
extract('samsung')


