from bs4 import BeautifulSoup

with open('SITE_RECETTE/recette.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()


soup = BeautifulSoup(html_content, 'html.parser')

print(soup)