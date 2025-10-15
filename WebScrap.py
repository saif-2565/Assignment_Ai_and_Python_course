# Web Scraping Program 

import requests as rq
from bs4 import BeautifulSoup as bs

# URL to scrape
url = "https://quotes.toscrape.com"

# Send a GET request to the website
response = rq.get(url)

# Parse HTML using BeautifulSoup
soup = bs(response.text, "html.parser")

# Find all quote elements
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Print each quote with author
for i in range(len(quotes)):
    print("Quote:", quotes[i].text)
    print("Author:", authors[i].text)
    print("------------------------")
