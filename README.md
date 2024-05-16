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