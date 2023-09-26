import requests
from bs4 import BeautifulSoup

url = "https://meleeframedata.com/fox"
r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
#print(soup)
table = soup.findAll(class_="move-container")
table2 = soup.findAll("div",attrs={'class':"special-movename"})

keyword = {
        "Jab":['jab','Jab']
        }

def find_move(movename: str):
    can_find_move = None
    string_to_use = None
    for keys in keyword:
        for t in keyword[keys]:
            if movename == t:
                can_find_move = True
                string_to_use = keys
    
    if can_find_move:
        for t in table:
            tags = t.findAll(string=string_to_use)
            if tags:
                print(t.text)

find_move('jab')

