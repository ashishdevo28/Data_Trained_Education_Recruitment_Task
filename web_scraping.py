import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

url_cus = 'https://www.flipkart.com/acer-aspire-7-ryzen-5-hexa-core-5500u-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-a715-42g-gaming-laptop/p/itm4385fddc2c72c?pid=COMGYCG8ZBXWPYUU&lid=LSTCOMGYCG8ZBXWPYUUYQDSM8&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=hp_omu_Super%2BSaver%2BDeals%2BOf%2BThe%2BDay_1_3.dealCard.OMU_63GR5Z2DAQL6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Super%2BSaver%2BDeals%2BOf%2BThe%2BDay_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=dc2c7088-7534-4dc3-8824-e17b3552c913.COMGYCG8ZBXWPYUU.SEARCH&ppt=hp&ppn=homepage&ssid=z9ojaa6uqo0000001617258466144'
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []
names = []
ratings = []
prices = []


driver.get(url_cus)

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'aMaAEs'}):
    name = a.find('div', attrs={'class':'B_NuCI'})
    price = a.find('div', attrs={'class':'_30jeq3 _16Jk6d'})
    rating = a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


'''df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')'''
