import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.vagalume.com.br/linkin-park/numb.html')
soup = BeautifulSoup(page.content, 'html.parser')

print(str(soup.find('div', {'itemprop': 'description'})).replace('<br/>', '\n'))
