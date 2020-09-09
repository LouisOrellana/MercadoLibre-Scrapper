import requests
from bs4 import BeautifulSoup as BSoup
import csv

class Item:
    def __init__(self, title=None, price=None, url=None):
        self.title = title
        self.price = price
        self.url = url
    
    def __str__(self):
        return 'Item(title={}, price={})'.format(self.title, self.price)
    
    def __gt__(self, other):
        if type(self) == type(other):
            return self.price > other.price
        elif type(other) == int or type(other) == float:
            return self.price > other
    
    def __lt__(self, other):
        if type(self) == type(other):
            return self.price < other.price
        elif type(other) == int or type(other) == float:
            return self.price < other

    def __eq__(self, other):
        if type(self) == type(other):
            return self.price == other.price
        elif type(other) == int or type(other) == float:
            return self.price == other
          
        
        
def scrape(item):
    product = item.replace(' ', '-')
    
    link       = 'https://listado.mercadolibre.com.mx/' + product
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    page = requests.get(link, headers=headers)
    soup = BSoup(page.content, 'html.parser')
    
    rawItemList = soup.findAll('li', {'class': 'ui-search-layout__item'})
    titles   = [item.find('h2', {'class': 'ui-search-item__title'}).text for item in rawItemList]
    prices   = [item.find('span', {'class': 'price-tag-fraction'}).text.replace(',', '') for item in rawItemList]
    urls     = [item.find('a', {'class': 'ui-search-item__group__element ui-search-link'})['href'] for item in rawItemList]
    
    itemList = []
    for i in range(len(titles)):
        itemList.append(Item(title=titles[i], price=int(prices[i]), url=urls[i]))
    
    return itemList


def scrapeToCSV(scraped, filename='item_data.csv'):
    with open(filename, mode='w') as file:
        fieldnames = ['Title', 'Price', 'Url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in scraped:
            writer.writerow({'Title': item.title, 'Price': item.price, 'Url': item.url})
        
        
def example():
    productList = ['arduino uno', 'arduino nano', 'xiaomi redmi note 9']
    for product in productList:
        data = scrape(product)
        scrapeToCSV(data, filename=product+'.csv')
