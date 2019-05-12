import requests
import json
# Version: Python3

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
#print(DATA)

#if DATA['query']['search'][0]['title'] == SEARCHPAGE:

 #   print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")

print (DATA['query']['search'][0]['title']) 
print (DATA['query']['search'][1]['title']) 
print (DATA['query']['search'][2]['title'])
print (DATA['query']['search'][3]['title'])
print (DATA['query']['search'][4]['title']) 
print (DATA['query']['search'][5]['title'])
print (DATA['query']['search'][6]['title'])
print (DATA['query']['search'][7]['title']) 
print (DATA['query']['search'][8]['title'])
print (DATA['query']['search'][9]['title'])
