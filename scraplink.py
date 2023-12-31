from googleapiclient.discovery import build


api_key = "AIzaSyAY4zlBicXjgeBAKNVIVX8W30Tm0Q7F75o"

def get_channel_id(api_key, channel_name):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Searching for channels with the given channel name
    request = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1
    )
    
    response = request.execute()
    if response['items']:
        return response['items'][0]['id']['channelId']
    else:
        return None

def get_total_videos(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Getting total videos count in the channel
    request = youtube.channels().list(
        part="statistics",
        id=channel_id
    )
    
    response = request.execute()
    if response['items']:
        return int(response['items'][0]['statistics']['videoCount'])
    else:
        return 0

def search_shorts_in_channel(api_key, channel_id, total_videos):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Searching for Shorts within the specified channel
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        videoDuration="short",
        maxResults=total_videos  # Fetch all videos in the channel
    )
    
    response = request.execute()
    return response['items']

# Input the channel name
channel_name = input("Enter the channel name: ")

# Get the channel ID from the channel name
channel_id = get_channel_id(api_key, channel_name)

if channel_id:
    total_videos = get_total_videos(api_key, channel_id)
    if total_videos > 0:
        shorts = search_shorts_in_channel(api_key, channel_id, total_videos)
        
        if shorts:
            print(f"Shorts in the channel '{channel_name}':")
           
            for item in shorts:
                video = item['snippet']
                print("Title:", video['title'])
                print("Description:", video['description'])
                print("Video ID:", item['id']['videoId'])
                print("Published At:", video['publishedAt'])
                print("Channel Title:", video['channelTitle'])
                print("Video URL:", f"https://www.youtube.com/shorts/{item['id']['videoId']}")
                print("------------")
            print(f"Total number of Shorts in the channel '{channel_name}': {len(shorts)}")    
        else:
            print("No Shorts found in the channel or unavailable.")
    else:
        print("No videos found in the channel.")
else:
    print("Channel not found or unavailable.")
