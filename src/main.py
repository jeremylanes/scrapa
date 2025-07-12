import requests
from bs4 import BeautifulSoup

jeremy_url = 'https://www.jeremy.berlin/'
docstring_url = 'https://docstring.fr/api/books_to_scrape/index.html'
url = 'https://books.toscrape.com/'


# function to browse the DOM tree recursively
def browse_dom(element, level=0):
    # display actual element
    if element.name:
        print(f'{' ' * level}<{element.name}>')

    if hasattr(element, 'children'):
        for child in element.children:
            browse_dom(child, level + 1)

# response = requests.get(url)
# response.raise_for_status()
#
# with open('index.html', 'w') as f:
#     f.write(response.text)

with open('index.html', 'r') as f:
    f = f.read()


soup = BeautifulSoup(f, 'html.parser')
# print(soup.prettify())

browse_dom(soup)