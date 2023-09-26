import requests
from bs4 import BeautifulSoup

char = 'fox'
url = f'https://meleeframedata.com/{char}'
r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
table = soup.findAll(class_="move-container")
table2 = soup.findAll("div",attrs={'class':"special-movename"})

keywords = {
        "Jab":['jab','Jab','jab 1','jab1'],
        "U Tilt":['utilt','u-tilt','up-tilt','u tilt'],
        "D Tilt":['d-tilt','dtilt','down tilt','down-tilt'],
        "F Tilt":['f-tilt','forward tilt','ftilt','f tilit'],
        }

def find_move(movename: str):
    can_find_move = None
    string_to_use = None
    for keys in keywords:
        for t in keywords[keys]:
            if movename == t:
                can_find_move = True
                string_to_use = keys
    
    if can_find_move:
        for t in table:
            tags = t.findAll(string=string_to_use)
            if tags:
                print(t.text)

find_move('jab')

