import json 
import requests
import bs4
import psycopg2

try:
	conn = psycopg2.connect("dbname='petitionUK' user='lacunadream' host='localhost' password='mayyie?hmm'")
	print("I established a connection to the database")
except:
    raise Exception("I am unable to connect to the database")

cur = conn.cursor()
# cur.execute("CREATE TABLE webcam (id serial PRIMARY KEY, index integer, value float);")

r = requests.get("https://petition.parliament.uk/petitions/")
k = r.text
k = k.encode('utf-8', 'ignore')
# print(k)
soup = bs4.BeautifulSoup(k)
g = soup.findAll("li", {"class":"petition-item"})
gg = [x.find("a") for x in g]
ggg = [x['href'] for x in gg]

print(ggg)

def scrapLink(url):
	baseURL = "https://petition.parliament.uk/"
	json = ".json"
	r = requests.get(baseURL + url + '.json')	
	jsondata = r.json()
	petitdata = url[len(url)-6:len(url)]
	petitdata = int(petitdata)
	cur.execute("INSERT INTO petitionsdata (petid, data) VALUES (%s, %s)", (petitdata, jsondata))
	conn.commit()

counter = 0
for x in ggg: 
	scrapLink(x)
	counter += 1
	print(counter)


cur.close()
conn.close()

# for x in g: 
# 	# x = x.encode('utf-8', 'ignore')
# 	print(x)

