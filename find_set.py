from googleapiclient.discovery import build
import json

with open('tokens.json') as d:
    data = json.load(d)

key = str(data['tube-token'])
service = 'youtube'
service_ver = 'v3'
# Create a build func

def get_set(term: str):
    tube = build(service,service_ver,developerKey=key)

    search = tube.search().list(
            q=term,
            part='id,snippet',
            maxResults=10
            ).execute()
    
    ids = []
    for result in search.get('items',[]):
        if result['id']['kind'] == 'youtube#video':
            ids.append(result['id']['videoId'])
    
    return "https://www.youtube.com/watch?v="+ids[0]

print(get_set("SSBM tournament MokyvsJmppop"))
