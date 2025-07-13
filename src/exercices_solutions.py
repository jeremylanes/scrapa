import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'https://books.toscrape.com/index.html'




def main(threshold=5):
    with requests.Session() as session:

        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # soup.find('ul', class_='nav nav-list').find_all('a')

        # Alternative
        categories = soup.select('ul.nav.nav-list a')

        categories_url = [category.get('href') for category in categories[1:]]

        # print(categories_url)
        for category_url in categories_url:
            absolute_url = urljoin(BASE_URL, category_url)
            # print(absolute_url)

            response = session.get(absolute_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            category_title = soup.select_one('h1').text.strip()

            books = soup.select('article.product_pod')
            print(len(books))

            number_of_books = len(books)
            if number_of_books <= threshold:
                print(f'Category {category_title} has less than {threshold} books -> {number_of_books}')

            else:
                print(f'Category {category_title} has more than {threshold} books -> {number_of_books}')


if __name__ == '__main__':
    main(threshold=5)