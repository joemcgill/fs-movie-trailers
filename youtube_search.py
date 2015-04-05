#!/usr/bin/python

from apiclient.discovery import build

import config

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = config.youtube_key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Options():
    def __init__(self, q, maxResults) :
        self.q = q
        self.maxResults = maxResults

def search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.maxResults
  ).execute()

  video_id = ''

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      video_id = search_result["id"]["videoId"]

  return video_id
