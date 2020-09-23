from scrape import scrape, scrapeToCSV

def example():
    productList = ['haylou gt1', 'dell g5', 'xiaomi redmi note 9']
    for product in productList:
        data = scrape(product)
        scrapeToCSV(data, filename=product+'.csv')

if __name__ == '__main__':
    example()