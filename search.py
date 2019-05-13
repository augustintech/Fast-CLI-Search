# Version: Python 3.7.3
import requests
import json
import re

findme = input("Enter a name to get their DOB: ")
print("Currently searching for",findme,"...")

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHPAGE = findme

PARAMS = {
    'action':"query",
    'list':"search",
    'srsearch': SEARCHPAGE,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

for i in range(10):
    print(DATA['query']['search'][i]['title'])

# Prompts user to choose for the correct article. 

findme = input("Choose the correct article: ")
print("Currently fetching article for",findme,"...")

TITLE = findme

PARAMS = {
    'action': "parse",
    'page': TITLE,
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)

print(type(R))

DATA = R.json()

#print(DATA)

print(type(DATA))






#r1 = re.findall(r'.*([1-3][0-9]{3})',DATA)
#print(r1) 