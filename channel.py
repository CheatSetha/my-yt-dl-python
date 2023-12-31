from pytubefix import Channel
input_cn = 'https://www.youtube.com/@cheatsetha5895'
c = Channel(input_cn)
# print(f'Channel name : {c.channel_name}')
# print(f'total video : {len(c.videos_url)}')

print(f'Download video from channel : {c.channel_name}')
# modify video_url to download video from short video only

print(c.videos_url)


if len(c.videos) == 0:
    print('No video in channel')
else:
    for video in c.videos:
        download = video.streams.get_highest_resolution().download("D:\Video\yt")
        print('Downloaded : ', download)
