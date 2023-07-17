# pip3 install pytube in cmd
from pytube import YouTube
from sys import argv

# argv allows program to be ran from cmd
link = argv[1]
yt = YouTube(link)

# displays YouTube video title + view count
print("Title: ", yt.title)
print("View Count: ", yt.views)

# code to enable downloads in highest res
yd = yt.streams.get_highest_resolution()
yd.download("/Users/onnalinmeakin/Documents/downloaded-yt-vids")

# in cmd type: python3 video-downloader.py "link"