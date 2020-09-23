# MercadoLibre Scrapper

Usage:
```
python3 scrape.py item1 item2 'item 3'
```

Arguments are the items to scrape information about. There can be multiple items in arguments, they shall be separated by spaces. If you need to search for an item that has more than one word in its name, surround the name by single or double quotes.

Calling scrape.py from the command line will generate a csv file for each item passed to it. 

The csv title includes: 
- Title
- Price (in MXN)
- Url to the item
