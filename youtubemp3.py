
"""
Download Youtube video and convert them into mp3 and delete the dowloaded video
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""


# Library we need
from pytube import YouTube
import os
import subprocess
import time
import moviepy.editor as mp
from IPython import get_ipython
import glob

# select where you want everything to be dowloaded
os.chdir("Desktop\\music")

# paste here the Youtube URL you wanna convert
urls = ["https://www.youtube.com/watch?v=NlUQbrlb2iQ",
        "https://www.youtube.com/watch?v=3V1VwEKFe0g"]


# Download videos
tot = len(urls)
for int, url in enumerate(urls):
    # Display the title of the video
    print("...")
    print(YouTube(url).title)
    print("...")
    # name the file with the 1st 10 characters of the video title
    _filename = YouTube(url).title[:10]# input("Filename: ")
    print("Downloading....")
    try:
        YouTube(url).streams.first().download(filename=_filename)
    except:
        print("problem with {} (downloading)".format(_filename))
    time.sleep(2)
    print("{} videos completed on {} in total".format(int+1, tot))

# Convert into mp3
print("Converting video to mp3....")
videos = glob.glob("*.mp4")
for video in videos:
    try:
        clip = mp.VideoFileClip(video)
        mp3 = "{}.mp3".format(video[:-4])
        clip.audio.write_audiofile(mp3)
    except:
        print("problem with {} (converting)".format(video))
    clip.reader.close()

# Delete videos
print("Deleting video....")
for video in videos:
    try:
        os.remove(video)
    except:
        print("problem with {} (erasing)".format(video))







# ###
# # manually
#
# url = "https://www.youtube.com/watch?v=S1g4Uoqhhc8"
# print(YouTube(url).title)
# _filename = input("Filename: ")
# YouTube(url).streams.first().download(filename=_filename)
