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

# pprint(images_urls)


# book's title

books = section.find_all('h3')

books_titles = [book.a.get('title') for book in books if book.name]

# pprint(books_titles)


# from Thibau
# articles = soup.find_all('article', class_='product_pod')
#
# for article in articles:
#     links = article.find_all('a')
#
#     if len(links) >= 2:
#         link = links[1]
#         title = link.get('title')
#         print(title)

titles_tags = soup.find_all('a', title=True)

titles = [title.get('title') for title in titles_tags]
pprint(titles)