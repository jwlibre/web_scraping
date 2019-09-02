import requests
from bs4 import BeautifulSoup
import pdb

page = requests.get("https://www.bbc.co.uk/news")

# create an instance of the BeautifulSoup class, which will parse the html (content) from the requests response
soup = BeautifulSoup(page.content, 'html.parser')

# puts the html content into a nicer format with indentation - write to file
f = open("webscrape.txt", "w")
f.write(soup.prettify())
f.close()

# extract the top-ten most-read headlines plus their surrounding contextual html (to be separated out later)
topTen_full = soup.find(class_="nw-c-most-read__items gel-layout gel-layout--no-flex")
topTen = topTen_full.find_all(class_="gs-c-promo-heading__title gel-pica-bold")

# extract just the headlines and print to console
for line in topTen:
    line = str(line)
    headline = line[line.index(">") + 1:line.index("</span>")]
    print(headline)
