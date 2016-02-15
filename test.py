import json
import requests
import pprint

with open('data_fix.json', 'r') as loadfile:
    partyData = json.load(loadfile)

print(partyData['Edinburgh North and Leith']['majority'])

petition = requests.get('https://petition.parliament.uk/petitions/121152.json')
petitionData= petition.json()['data']['attributes']['signatures_by_constituency']

conval = 0
labval = 0
libval = 0
snpval = 0
othval = 0
counter = 0

for x in petitionData:
	counter += 1
	print(counter)
	if partyData[x['name']]['result'] == 'CON':
		print('lol')
		conval += x['signature_count']
	# elif partyData[x]['result'] == 'LAB':
	# 	labval += x['signature_count']
	# elif partyData[x]['result'] == 'SNP':
	# 	snpval += x['signature_count']
	else: 
		print('lol2')
		othval += x['signature_count']

# for x in petitionData:
# 	print(x['signature_count'])

# Linlithgow and Falkirk East

# West Aberdeenshire and Kincardine