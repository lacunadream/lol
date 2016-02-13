import requests
import bs4
import json

r = requests.get("http://www.bbc.co.uk/news/politics/constituencies")
soup = bs4.BeautifulSoup(r.content)
k = soup.findAll("tr", {"class" : "az-table__row"})
kk = [x.contents for x in k]
print(kk)