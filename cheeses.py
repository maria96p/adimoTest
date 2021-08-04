import json
import requests
from bs4 import BeautifulSoup
import re




products={}
response=requests.get(url='https://cdn.adimo.co/clients/Adimo/test/index.html')
data=response.text
soup = BeautifulSoup(data, 'html.parser')

main_div = soup.find_all('div', class_='item')
avgPrice={}
i=1
for item in main_div:
    title=(item.find('h1')).get_text()
    imageurl=str(item.find('img'))[10:-3]
    price=str((item.find('span', class_='price')).get_text())[1:]
    oldprice=item.find('span', class_='oldPrice')
    if oldprice is not None:
        oldprice=str(oldprice.get_text())[1:]
        ## Average price of an item
    
        oldpriceDigit=re.findall(r'\b\d+\b', oldprice)
        priceDigit=re.findall(r'\b\d+\b', price)
        avgPriceitem= (float(oldpriceDigit[0])+(float(oldpriceDigit[1])/100)+float(priceDigit[0])+(float(priceDigit[1])/100))/2
        avgPrice[i]=avgPriceitem
    else:
        priceDigit=re.findall(r'\b\d+\b', price)
        avgPrice[i]=float(priceDigit[0])+(float(priceDigit[1])/100)
        
    products[i]=[title,imageurl,price,oldprice]
    i+=1

print('The list of products with their title,image url,price and discount is')
print(products)
totalNofOfItems=len(products.keys())
print('Total Number if items is: ', totalNofOfItems)
print('The average price of each item is: ',avgPrice)



