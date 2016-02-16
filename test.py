import json
import requests
import datetime

with open('parties_ID.txt', 'r') as loadfile:
    partyData = json.load(loadfile)

# petition = requests.get('https://petition.parliament.uk/petitions/121152.json')
# petitionData= petition.json()['data']['attributes']['signatures_by_constituency']

# conval = 0
# labval = 0
# snpval = 0
# othval = 0
# counter = 0

# for x in petitionData:
# 	counter += 1
# 	print(counter)
# 	if partyData[x['ons_code']]['result'] == 'CON':
# 		print(conval)
# 		conval += x['signature_count']
# 	elif partyData[x['ons_code']]['result'] == 'LAB':
# 		labval += x['signature_count']
# 	elif partyData[x['ons_code']]['result'] == 'SNP':
# 		snpval += x['signature_count']
# 	else: 
# 		print('lol2')
# 		othval += x['signature_count']



# print('###')
# print(conval)
# print(labval)
# print(snpval)
# print(othval)


def crunchPetition(url):
	petition = requests.get(url)
	petitionData = petition.json()['data']['attributes']['signatures_by_constituency']

	conval = 0
	labval = 0
	libval = 0
	snpval = 0
	othval = 0
	counter = 0

	for x in petitionData:
		counter += 1
		print(counter)
		if partyData[x['ons_code']]['result'] == 'CON':
			print('lol')
			conval += x['signature_count']
		elif partyData[x['ons_code']]['result'] == 'LAB':
			labval += x['signature_count']
		elif partyData[x['ons_code']]['result'] == 'SNP':
			snpval += x['signature_count']
		else: 
			print('lol2')
			othval += x['signature_count']

	print('###')
	print(conval)
	print(labval)
	print(snpval)
	print(othval)



# crunchPetition('https://petition.parliament.uk/petitions/121152.json')
k = datetime.datetime.now()
print(str(k.year))