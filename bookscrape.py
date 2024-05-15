import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

navbar = soup.find("ul", class_="nav")

categories = navbar.find_all("a")
categoryLinks = []

for c in categories[1:]:
    categoryLinks.append(c['href'])

for c in categoryLinks:

    url = "http://books.toscrape.com/" + c
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    categoryTitle = soup.find("h1")
    csvTitle = categoryTitle.string.replace(" ", "").lower() + ".csv"
    print(csvTitle)

    pods = soup.find_all("article", class_="product_pod")
    links = []

    for p in pods:
        link = p.find("a")
        links.append(link['href'])

    for l in links:
        bookUrl = "http://books.toscrape.com/catalogue/" + l[9:]
        bookPage = requests.get(bookUrl)
        bookSoup = BeautifulSoup(bookPage.content, 'html.parser')

        tableData = bookSoup.find_all("td")
        upc = tableData[0]
        priceTax = tableData[2]
        priceNoTax = tableData[3]
        quantity = tableData[5]
        reviews = tableData[6]

        title = bookSoup.find("h1")

        allP = bookSoup.find_all("p")
        pList = []
        for p in allP:
            pList.append(p.string)

        allLi = bookSoup.find_all("a")
        liList = []
        for l in allLi:
            liList.append(l.string)

        image = bookSoup.find("img")

        headings = ["URL:", "UPC:", "Title:", "PriceW/Tax:", "PriceW/OTax:",
                    "Quantity:", "Description:", "Category:", "Reviews:", "ImageURL:"]

        productData = [bookUrl, upc.text, title.text, priceTax.text, priceNoTax.text, quantity.text, pList[3],
                        liList[3], reviews.text, image['src']]
                        
        with open(csvTitle, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')

            for i in range(len(productData)):
                row = [headings[i], productData[i]]
                writer.writerow(row)