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