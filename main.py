from googleapiclient.discovery import build
import sys
import json
import time
import os, webbrowser
from pprint import pprint

api_key = "AIzaSyAPp5jLDCKocjxQhcAVJFM3X72Se9njAXA"
youtube = build('youtube', 'v3', developerKey=api_key)

quary = input("Search Youtube :")
max_res = 100
def search(youtube, **kwargs):
    return youtube.search().list(
        part="snippet",
        type="video",
        **kwargs
    ).execute()


response = search(youtube, q=quary, maxResults=max_res)

print('''Total results = ''', response['pageInfo']['totalResults'], '\n')
if response['pageInfo']['totalResults'] == 0:
    exit()

items = response.get("items")

dec = {i+1:{'title':items[i]['snippet']['title'],'video_id':items[i]['id']['videoId'], 'channel_name':items[i]['snippet']['channelTitle']} for i in range(len(items))}

for i in dec:
    print(i,dec[i]['title'])


while True:
    index = int(input("\nEnter a index:"))
    vId = dec[index]['video_id']
    print('channel name :',dec[index]['channel_name'],"\ntitle : ",dec[index]['title'])
    stats = youtube.videos().list(
        part="statistics",
        id=vId
    ).execute()
    for i in stats["items"][0]['statistics']:
        print(i,':', stats["items"][0]['statistics'][i])
    acp = input('want to open in web?: ')
    if acp == 'y':

        webbrowser.open_new_tab(f'https://www.youtube.com/watch?v={vId}')
    elif acp == 'n':

        print(f'https://www.youtube.com/watch?v={vId}')
    elif acp =='e':
        break
    else:
        pass