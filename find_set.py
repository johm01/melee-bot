from googleapiclient.discovery import build

key = ''
service = 'youtube'
service_ver = 'v3'
# Create a build func

def find_set(term: str):
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

set_1 = find_set('SSBM tournament peach vs fox')
print(set_1)
