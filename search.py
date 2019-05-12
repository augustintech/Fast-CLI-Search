# Version: Python 3.7.3
import requests
import json

findme = input("Enter a name to get their DOB: ")
print("Currently searching for",findme)

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

