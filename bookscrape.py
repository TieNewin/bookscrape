import csv
import requests
from bs4 import BeautifulSoup
from PIL import Image

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

navbar = soup.find("ul", class_="nav")

categories = navbar.find_all("a")
categoryLinks = []
imageNumber = 1

for c in categories[1:]:
    categoryLinks.append(c['href'])

#Loop through each category of entire site
for c in categoryLinks:

    url = "http://books.toscrape.com/" + c
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    categoryTitle = soup.find("h1")
    csvTitle = categoryTitle.string.replace(" ", "").lower() + ".csv"
    print("Writing " + csvTitle)

    pods = soup.find_all("article", class_="product_pod")
    links = []

    #Loop through book pods in each category to get to individual book
    for p in pods:
        link = p.find("a")
        links.append(link['href'])

    #Loop through individual books to scrape data
    for l in links:
        bookUrl = "http://books.toscrape.com/catalogue/" + l[9:]
        bookPage = requests.get(bookUrl)
        bookSoup = BeautifulSoup(bookPage.content, 'html.parser')

        #Extract
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
        imgURL = "http://books.toscrape.com/" + image['src'][6:]
        imageName = "image" + str(imageNumber) + ".jpg"

        img = Image.open(requests.get(imgURL, stream = True).raw)
        img.save("image_files/" + imageName)
        imageNumber += 1

        headings = ["URL:", "UPC:", "Title:", "PriceW/Tax:", "PriceW/OTax:",
                    "Quantity:", "Description:", "Category:", "Reviews:", "ImageURL:"]
        
        #Transform
        productData = [bookUrl, upc.text, title.text, priceTax.text, priceNoTax.text, quantity.text, pList[3],
                        liList[3], reviews.text, image['src']]

        #Load
        #Write data to csv file             
        with open("csv_files/" + csvTitle, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')

            for i in range(len(productData)):
                row = [headings[i], productData[i]]
                writer.writerow(row)