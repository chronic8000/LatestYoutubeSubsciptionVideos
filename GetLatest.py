import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# Set up the API credentials
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
client_secret_file = "path/to/client_secret.json"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
creds, _ = google.auth.default(scopes=scopes)

# Set up the YouTube Data API client
youtube = build("youtube", "v3", credentials=creds)

# Get a list of the user's subscriptions
subscriptions = []
next_page_token = None
while True:
    response = youtube.subscriptions().list(
        part="snippet",
        mine=True,
        maxResults=50,
        pageToken=next_page_token
    ).execute()
    subscriptions.extend(response["items"])
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

# Get the latest video from each subscription
latest_videos = []
for subscription in subscriptions:
    channel_id = subscription["snippet"]["resourceId"]["channelId"]
    response = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        order="date",
        maxResults=1
    ).execute()
    video = response["items"][0]
    latest_videos.append({
        "title": video["snippet"]["title"],
        "url": f"https://www.youtube.com/watch?v={video['id']['videoId']}",
        "publishedAt": datetime.fromisoformat(video["snippet"]["publishedAt"])
    })

# Sort the videos by publish time
latest_videos.sort(key=lambda x: x["publishedAt"], reverse=True)

# Write the list of videos to a file
with open("latest_videos.txt", "w") as f:
    for video in latest_videos:
        f.write(f"{video['title']} - {video['url']} - {video['publishedAt']}\n")

# Print a message to the user
print("Latest videos from your subscriptions have been saved to latest_videos.txt.")
