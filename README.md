#bookscrape

A webscraper designed to extract key data from every book on a bookstore retailer's website for use in a price monitoring system

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install this software, simply download the bookscrape.py file onto your device. Make sure python is installed on your device along with the necessary modules for csv, requests, BeautifulSoup, and Pillow.

## Usage

To use the software, simply navigate to the directory in which the python script is saved in your terminal and run the software using "python bookscrape.py"

## Features

This software is designed to access the website "http://books.toscrape.com/" and navigate through each category of books, then each book within each category. The software then scrapes each book for key data including: 
    - product's URL
    - product's UPC
    - product's title
    - product's price including tax
    - product's price before tax
    - product's quantity available
    - product's description
    - product's category
    - product's number of reviews
    - product's image source
    - product's image as a .jpg file

    URL: http://books.toscrape.com/catalogue/logan-kade-fallen-crest-high-55_384/index.html
UPC: 7093cf549cd2e7de
Title: "Logan Kade (Fallen Crest High #5.5)"
PriceW/Tax: £13.12
PriceW/OTax: £13.12
Quantity: "In stock (5 available)"
Description: "People think that just because they know my name, my reputation, and my family that they know me. They don't.They say I’m a manwhore, but who wouldn’t be with my face and body? They say I’m a partier, and that's not going to change. They say I'm a fighter, and hell yes I am. F*ck with mine, and I’ll f*ck you back ten times worse.So, yes. Maybe what they say is true, but th People think that just because they know my name, my reputation, and my family that they know me. They don't.They say I’m a manwhore, but who wouldn’t be with my face and body? They say I’m a partier, and that's not going to change. They say I'm a fighter, and hell yes I am. F*ck with mine, and I’ll f*ck you back ten times worse.So, yes. Maybe what they say is true, but that’s not all of me.I'm loyal to a damned fault. If you earn it, I'll never leave your side. And when I love, I love hard, but there's another side to me where it's dark and painful. That side's been kept hidden, until her. Taylor saw inside of me, and the second she was there, she owned me.People think they know me……but only she can see me. ...more"
Category: Academic
Reviews: 0
ImageURL: ../../media/cache/2b/44/2b4404e00c242bf1b8263bdd99c07354.jpg