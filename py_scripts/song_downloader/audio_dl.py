from __future__ import unicode_literals
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import youtube_dl
import json

DEVELOPER_KEY = "AIzaSyCXBfzVo_3ZAirO_wa7Sy8nvL4pk_rAAOA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)


def youtube_search(q, max_results=1,order="relevance", token=None, location=None, location_radius=None):

  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id",
    fields = "items/id",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius

  ).execute()
  videos = []
  for search_result in search_response.get("items", []):
      videos.append(search_result["id"]["videoId"])

  return videos

def download(song_list):
    for song in song_list:
        search_data = youtube_search(song)
        video_id = (search_data[0])
        url = "http://www.youtube.com/watch?v=" + video_id
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def text_import(text_file = 'input.txt'):
    with open(text_file, 'r') as f:
        song_list = f.read().splitlines()
        return song_list

#format for download
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}











download_list = text_import('input.txt')
download(download_list)




