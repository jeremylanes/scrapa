from pprint import pprint

import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'

# response = requests.get(url)

with open('index.html', 'r') as f:
    html = f.read()


soup = BeautifulSoup(html, 'html.parser')

side_categories = soup.find('div', class_='side_categories')

categories = side_categories.find('ul').find('li').find('ul')

# for category in categories.children:
#     print(category.name)

   # print(category.text.strip())

names = [category.text.strip() for category in categories.children if category.name]

# pprint(names)
section = soup.find('section')

images = section.find_all('img')

images_urls = [image.get('src') for image in images if image.get('src')]

pprint(images_urls)