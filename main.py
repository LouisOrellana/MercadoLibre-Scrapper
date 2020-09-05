import requests
from bs4 import BeautifulSoup as BSoup


product = 'xiaomi redmi note 9'

product = product.replace(' ', '-')

link       = 'https://listado.mercadolibre.com.mx/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
page = requests.get(link + product, headers=headers)
soup = BSoup(page.content, 'html.parser')



#print(soup.prettify())