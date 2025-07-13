
import requests
from bs4 import BeautifulSoup

#Retrieve categories with a single book

def retrieve_categories_headers(url: str) -> list:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')

    # --- retrieve categories ---
    categories = side_categories.find('ul').find('li').find('ul')
    categories = categories.find_all('a', href=True)
    # print(categories)
    categories_headers = [
        {
            'name': category.text.strip(),
            'url': f'{url}{category.get('href')}'
        }
        for category in categories if category.name
    ]
    return categories_headers

def retrieve_categories_books_number(categories_headers: list) -> dict:
    categories_books_number: list[dict] = []
    for header in categories_headers:
        print(f'Processing category {header.get("name")}')

        response = requests.get(header.get('url'))
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find('section').find_all('li')

        categories_books_number += [
            {
                'name': header.get('name'),
                'url': header.get('url'),
                'books_number': len(books)
            }
        ]

    return categories_books_number


url = 'https://books.toscrape.com/'

urls = retrieve_categories_headers(url)
print(urls)
books_number = retrieve_categories_books_number(urls)

books = [x for x in books_number if x.get('books_number') <= 5]
print(books)