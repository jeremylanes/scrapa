
import requests
from bs4 import BeautifulSoup

#Retrieve categories with a single book

def retrieve_categories_urls(url: str) -> list:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')

    # --- retrieve categories ---
    categories = side_categories.find('ul').find('li').find('ul')
    categories_url = categories.find_all('a', href=True)
    categories_url_list = [category['href'] for category in categories_url]

    print(categories_url_list)

    # --- retrieve books ---
    books_categories_urls = [f'{url}{book_url}' for book_url in categories_url_list]



    return books_categories_urls

def retrieve_categories_books_number(urls: list) -> dict:
    categories_books_number: dict = {}
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find('section').find_all('li')

        categories_books_number = {
            'category': {
                'name': 'xd',
                'url': url,
                'books_number': len(books)
            }
        }

        print(categories_books_number)

    return categories_books_number


url = 'https://books.toscrape.com/'

urls = retrieve_categories_urls(url)
books_number = retrieve_categories_books_number(urls)

print(books_number)