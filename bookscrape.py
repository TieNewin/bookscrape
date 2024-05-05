import requests
from bs4 import BeautifulSoup

phaseOneURL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
phaseOnePage = requests.get(phaseOneURL)
phaseOneSoup = BeautifulSoup(phaseOnePage.content, 'html.parser')

tableData = phaseOneSoup.find_all("td")
upc = tableData[0]
priceTax = tableData[2]
priceNoTax = tableData[3]
quantity = tableData[5]

title = phaseOneSoup.find("h1")

print(tableData)

print(phaseOneURL)
print(upc.text)
print(title.text)
print(priceTax.text)
print(priceNoTax.text)
print(quantity.text)