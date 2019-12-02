import pandas as pd
import requests
from bs4 import Beautifulsoup


page = requests.get('https://www.transparencia.gob.sv/institutions/capres/documents/otros-documentos-normativos?status=301')

soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all(class_='small-order-1')

names = [ item.find('a').get_text() for item in tables]
links = [ item.find('a').get('href') for item in tables]

trans_links = pd.DataFrame({
	'name':names,
	'links':links,
	})

trans_links.to_csv('capres.csv')
