import requests
from bs4 import BeautifulSoup

#iphone 7 link
iphone7_link = 'https://www.jumia.com.ng/apple-renewed-iphone-7-plus-32gbram3gb-black-iphone7p-118774089.html'

#iphone 8 link
# iphone8_link='https://www.jumia.com.ng/apple-renewed-iphone-8-64gb3gb-ram-gold-iphone8-102114632.html'

# #Just add the product link here and fetch the price
# iphone13_link = 'https://www.jumia.com.ng/iphone-13-pro-6.1-inch-super-retina-xdr-display-with-promotion-6gb-ram-256gb-rom-ios-15-5g-facetime-sierra-blue-apple-mpg1620490.html'
# samsung_link = 'https://www.jumia.com.ng/samsung-galaxy-a23-6.6-tft-screen-4gb64gb-memory-50mp-quad-camera-5000-mah-battery-android-12-blue-106402124.html'
# techno_link = 'https://www.jumia.com.ng/tecno-pova2-battery-7000mah-color-dazzle-black-132972301.html'
# itel17_link = 'https://www.jumia.com.ng/itel-17-pro-3g-galaxy-blue-128769853.html'
# hot11_link = 'https://www.jumia.com.ng/infinix-hot-11s-6.7-ips-lcd-screen-4gb64gb-memory-50mp-triple-camera-5000-mah-battery-android-11-green-wave-114778541.html'
# note12_link = 'https://www.jumia.com.ng/infinix-note-12i-4gb128gb-memory-force-black-127336449.html'
wrong_link = 'https://abcdef'

def fetch_jumia_product(product_link):
    jumia_product_url= product_link

    try:
        page = requests.get(url=jumia_product_url)
    except:
        return 'Page Not Found'
    # page = requests.get(url=jumia_product_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]




print(fetch_jumia_product(iphone7_link))
print(fetch_jumia_product(wrong_link))
# print(fetch_jumia_product(iphone8_link))
# print(fetch_jumia_product(iphone13_link))
# print(fetch_jumia_product(samsung_link))
# print(fetch_jumia_product(techno_link))
# print(fetch_jumia_product(itel17_link))
# print(fetch_jumia_product(hot11_link))
# print(fetch_jumia_product(note12_link))


