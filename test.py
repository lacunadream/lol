import json
import requests
import pprint

with open('parties.txt', 'r') as loadfile:
    partyData = json.load(loadfile)

xx = json.dumps(partyData)

print(xx)

k = xx.replace('&', 'and')
print(k)

with open('parties_new.txt', 'w') as outfile: 
	outfile.write(k)

# for v in partyData.items():
# 	v.replace('&', 'and')

# print(partyData['Edinburgh North and Leith']['majority'])

# petition = requests.get('https://petition.parliament.uk/petitions/121152.json')
# petitionData= petition.json()['data']['attributes']['signatures_by_constituency']

# conval = 0
# labval = 0
# libval = 0
# snpval = 0
# othval = 0
# counter = 0

# for x in petitionData:
# 	counter += 1
# 	if partyData[x['name']]['result'] == 'CON':
# 		print('lol')
# 		conval += x['signature_count']
# 	# elif partyData[x]['result'] == 'LAB':
# 	# 	labval += x['signature_count']
# 	# elif partyData[x]['result'] == 'SNP':
# 	# 	snpval += x['signature_count']
# 	else: 
# 		print('lol2')
# 		othval += x['signature_count']

# for x in petitionData:
# 	print(x['signature_count'])

