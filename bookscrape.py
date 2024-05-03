import requests
from bs4 import BeautifulSoup

phaseOneURL = "https://books.toscrape.com/"
phaseOnePage = requests.get(phaseOneURL)
phaseOneSoup = BeautifulSoup(phaseOnePage.content, 'html.parser')

