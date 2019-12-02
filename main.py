import pandas as pd
import requests
from bs4 import Beautifulsoup


page = requests.get('https://www.transparencia.gob.sv/institutions/capres/documents/otros-documentos-normativos?status=301')

soup = BeautifulSoup(page.content, 'html.parser')
