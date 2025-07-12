import requests

jeremy_url = 'https://www.jeremy.berlin/'
url = 'https://docstring.fr/api/books_to_scrape/index.html'

response = requests.get(url)
response.raise_for_status()

with open('index.html', 'w') as f:
    f.write(response.text)