from googleapiclient.discovery import build

key = ''
service = 'youtube'
service_ver = 'v3'
# Create a build func

def get_views(url):
    tube = build(service,service_ver,developerKey=key)
    
    r = tube.videos().list(
            part = "statistics",
            id=url
            ).execute()

    return int(r['items'][0]['statistics']['viewCount'])

def find_set(term: str):
    tube = build(service,service_ver,developerKey=key)

    search = tube.search().list(
            q=term,
            part='id,snippet',
            maxResults=10
            ).execute()
    

    views = []
    ids = []
    d = {}
    for result in search.get('items',[]):
        if result['id']['kind'] == 'youtube#video':
            ids.append(result['id']['videoId'])
            views.append(get_views(result['id']['videoId']))
    
    for i in range(len(views)):
        d[views[i]] = ids[i]

    print(d)
    return "https://www.youtube.com/watch?v="+ids[0]

set_1 = find_set('SSBM tournament peach vs fox')
print(set_1)
