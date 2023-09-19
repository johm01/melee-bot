from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests

key = 'AIzaSyDXq73Ca4uGdkP4z9SqkCJZHGMi60qFRlo'
service = 'youtube'
service_ver = 'v3'
# Create a build func

def sort_views(views: list):
    pass


def get_views(url):
    tube = build(service,service_ver,developerKey=key)
    
    r = tube.videos().list(
            part = "statistics",
            id=url
            ).execute()

    return r['items'][0]['statistics']['viewCount']

def find_set(term: str):
    tube = build(service,service_ver,developerKey=key)

    search = tube.search().list(
            q=term,
            part='id,snippet',
            maxResults=10
            ).execute()
    
    ids = []
    views = []
    for result in search.get('items',[]):
        if result['id']['kind'] == 'youtube#video':
            ids.append(result['id']['videoId']
            views.append(get_views(result['id']['videoId']))
    
    # Sort views for most views
    v_sorted = sort

    return ids[0]

set_1 = find_set('ssbm yoshi vs fox')
print(set_1)
