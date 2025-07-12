from bs4 import BeautifulSoup

# reading html file
with open('SITE_RECETTE/recette.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()


soup = BeautifulSoup(html_content, 'html.parser')

h1 = soup.find('h1')
print(f'Titre de la page : {h1.text}')