# from urllib.request import urlopen
# url = 'http://www.crummy.com/software/BeautifulSoup'
# source = urlopen(url).read()
# print(source)

import requests
import bs4
import json
r = 'http://www.ukpolitical.info/Otherparties.htm#UUP'

######
partydict = {
	"http://www.ukpolitical.info/conservative-mps-elected-2015.htm" : "Conservative",
	"http://www.ukpolitical.info/labour-mps-elected-2015.htm" : "Labour",
	"http://www.ukpolitical.info/liberal-democrat-mps-elected-2015.htm" : "Lib-Dem"
}




# print(r.text)
# print(r.encoding)
# r.encoding = 'utf-8'
# print(r.encoding)
# print('###############')
# soup = bs4.BeautifulSoup(r.content)

	# k = soup.findAll('strong')
	# print(k)

	# kk = [x.contents for x in k]
	# # kk = []
	# # for x in k:
	# # 	kk.append(x.contents)
	# print(kk)
	# # print(len(kk))

	# # lol = json.dumps(kk)
	# # print(lol)
	# # print(type(lol))

	# # kkk = []
	# # for x in kk: 
	# # 	c = ''.join(x)
	# # 	kkk.append(c)
	# kkk = [''.join(x) for x in kk]
	# print(kkk)

# source = r
def find_clean(url, party):
	source = requests.get(url)
	soup = bs4.BeautifulSoup(source.content)
	k = soup.findAll('strong')
	kk = [x.contents for x in k]
	kkk = [''.join(x) for x in kk]
	#####
	gah = {x: party for x in kkk}
	# end = json.dumps(gah)
	print(gah) 
	return gah

master = {}
for key, value in partydict.items():
	x = find_clean(key, value)
	master.update(x)

print(master)
print(len(master))

rr = requests.get('https://petition.parliament.uk/petitions/121152.json')
lol2 = rr.json()['data']['attributes']['signatures_by_constituency']
# lol1 = lol2['attributes']
# lol = lol1['signatures_by_constituency']
print(lol2)
print(type(lol2))

for x in lol2:
	for k, v in x.items():
		print(v)



# gah = {}
# for x in x1:
# 	gah[x] = 'LOL'



# xx = json.dumps(gah)
# print(xx)



