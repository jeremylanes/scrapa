from bs4 import BeautifulSoup

# reading html file
with open('SITE_RECETTE/recette.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()


soup = BeautifulSoup(html_content, 'html.parser')

h1 = soup.find('h1')
print(f'Titre de la page : {h1.text}')

# description_paragraph = soup.find('p', class_='description')

# div_centre = soup.find('div', class_='centre')
list_div_centre = soup.find_all('div', class_='centre')
description_paragraph = list_div_centre[1].find('p', class_='description')

print(f'Description : {description_paragraph.text}')


# find image src
print()
print('------ image src ------')
div_info = soup.find('div', class_='info')
img = div_info.find('img')
img_src = img['src']
print(f'Image src: {img_src}')