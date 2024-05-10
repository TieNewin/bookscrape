import csv
import requests
from bs4 import BeautifulSoup

phaseOneURL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
phaseOnePage = requests.get(phaseOneURL)
phaseOneSoup = BeautifulSoup(phaseOnePage.content, 'html.parser')

#Scraping data and storing as variables
tableData = phaseOneSoup.find_all("td")
upc = tableData[0]
priceTax = tableData[2]
priceNoTax = tableData[3]
quantity = tableData[5]
reviews = tableData[6]

title = phaseOneSoup.find("h1")

allP = phaseOneSoup.find_all("p")
pList = []
for p in allP:
    pList.append(p.string)

allLi = phaseOneSoup.find_all("a")
liList = []
for l in allLi:
    liList.append(l.string)

image = phaseOneSoup.find("img")

#Lists of column headings and scraped data
headings = ["URL:", "UPC:", "Title:", "PriceW/Tax:", "PriceW/OTax:",
             "Quantity:", "Description:", "Category:", "Reviews:", "ImageURL:"]

phaseOneData = [phaseOneURL, upc.text, title.text, priceTax.text, priceNoTax.text, quantity.text, pList[3],
                 liList[3], reviews.text, image['src']]

#Write data to csv file
with open('bts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')

    for i in range(len(phaseOneData)):
        row = [headings[i], phaseOneData[i]]
        writer.writerow(row)