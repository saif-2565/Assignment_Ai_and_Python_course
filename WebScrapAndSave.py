# Program for Web Scraping and save to csv file 

import requests as rq
from bs4 import BeautifulSoup as bs
import csv

# URL to scrape
url = "https://news.ycombinator.com/"

# Send request and parse HTML
response = rq.get(url)
soup = bs(response.text, "html.parser")

# Find all article titles and links
titles = soup.find_all("a", class_="titlelink")

# Creat and save CSV file 
with open("articles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])  # Column headers

    for t in titles:
        title_text = t.text
        link = t["href"]
        writer.writerow([title_text, link])

print("Data saved successfully in 'articles.csv' file.")
