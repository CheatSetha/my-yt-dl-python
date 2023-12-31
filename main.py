from pytubefix import YouTube
from pytubefix.cli import on_progress
import concurrent.futures
import os

def download_video(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    # copy link to file links_url for loop
    print("Title:", yt.title)
    ys = yt.streams.get_highest_resolution()
    channel_name = yt.channel_name  # Get channel name
    output_path = f"D:\\Video\\yt\\{channel_name}"

    # Create a directory for the channel if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ys.download(output_path)

# List of URLs
urls = []
with open('links_url', 'r') as f:
    for line in f:
        urls.append(line.strip())

# Adjust max_workers to control the number of simultaneous downloads
max_workers = 10  # For example, 5 simultaneous downloads

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(download_video, urls)
