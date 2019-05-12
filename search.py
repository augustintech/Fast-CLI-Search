import requests

# Version: Python3

findme = input("Enter a name to get their DOB: ")
print("Currently searching for",findme)

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHPAGE = findme

PARAMS = {
    'action':"query",
    'list':"search",
    'srsearch': SEARCHPAGE,
    'format':"json",
    
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

if DATA['query']['search'][0]['title'] == SEARCHPAGE:
    print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")
