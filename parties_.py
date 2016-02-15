import requests
import bs4
import json

r = requests.get("http://www.bbc.co.uk/news/politics/constituencies")
soup = bs4.BeautifulSoup(r.content, "lxml")
k = soup.findAll("tr", {"class" : "az-table__row"})
kk = [x.find("a") for x in k]
kkk = [x['href'] for x in kk]

print(kkk)
print(len(kkk))

baseUrl = "http://www.bbc.co.uk"

# seatName = soup.find("h1", {"class":"constituency-title__title"})

# ss = '/news/politics/constituencies/W07000049'
# print(ss[len(ss)-9:len(ss)])

# for x in kkk:
# 	r = requests.get(baseUrl + x)
# 	soup = bs4.BeautifulSoup(r.content)
# 	seatName = soup.find("h1", {"class":"constituency-title__title"})
# 	print(seatName)
# 	print(x[len(x)-9:len(x)])

def dropList(x):
	return ''.join(x)


def indivScrap(url):
	r = requests.get(baseUrl + url)
	soup = bs4.BeautifulSoup(r.content, "lxml")

	name = soup.find("h1", {"class":"constituency-title__title"}).contents
	seatName = ''.join(name).replace('&', 'and')

	seatID  = url[len(url)-9:len(url)]

	result = soup.find("span", {"class": "results-turnout__label"}).contents
	seatResult = dropList(result)[0:3]
	majority = soup.find("span", {"class": "results-turnout__value results-turnout__value--right"}).contents
	majority = dropList(majority)[0:len(majority) -1]
	seatMajority = float(majority)
	print(seatName)
	print(seatID)
	print(seatResult)
	print(seatMajority)
	d = {
		seatID: {
			"result": seatResult,
			"name": seatName,
			"majority": seatMajority
		}
	}
	print(d)
	return d


master = {}
counter = 0

for x in kkk:
	part = indivScrap(x)
	master.update(part)
	print(master)
	counter += 1
	print(counter)
	
with open('parties.txt', 'w') as outfile:
    json.dump(master, outfile)
