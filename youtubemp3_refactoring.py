
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
from sys import platform

# clear the terminal screen to make process clearer and more readable
def clear_screen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# make sure that your terminal path is the good one
def path_changer():
    wd = os.getcwd()
    print("***")
    print("current path = {}".format(wd))
    print("***")
    path_ = int(input("path already in Desktop/music? (type 0 if so)"))
    if path_ != 0:
        path = "Desktop/music"
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
    wd_updated = os.getcwd()
    print("***")
    print("current path updated = {}".format(wd_updated))
    print("***")
    time.sleep(2)
    clear_screen()

# ask you for all Youtube videos you wanna convert
def list_urls():
    keep_adding_song = 1
    list_urls = []
    while keep_adding_song == 1:
        print("***")
        print("copy paste Youtube url here")
        url = input(">")
        list_urls.append(url)
        print("***")
        keep_adding_song = int(input("keep adding url? (type 1 to continue, 0 to stop)"))
        print(" " * 15)
    return list_urls


# download a youtube video
class Downloader:
    def __init__(self, url):
        self.url = url
        self.title = YouTube(url).title
        self.length = YouTube(url).length

    def download(self):
        print("***")
        print("Downloading....{}".format(self.title))
        print("***")
        title = self.title[:10]
        try:
            YouTube(url).streams.first().download(filename=title)
            print("Video Downloaded")
        except:
            print("problem with {} (downloading)".format(title))
            stop
        time.sleep(2)
        clear_screen()

# convert a youtube video into mp3
class Converter:
    def __init__(self, video):
        self.video = video
        self.name = video[:-4]

    def convert(self):
        print("***")
        print("Converting....{}".format(self.name))
        print("***")
        try:
            clip = mp.VideoFileClip(self.video)
            mp3 = "{}.mp3".format(self.name)
            clip.audio.write_audiofile(mp3)
            print("Video converted")
            time.sleep(2)
            clip.reader.close()
        except:
            print("problem with {} (converting)".format(self.video))
            stop
        clear_screen()

# erase the downloaded mp4 youtube video
class Eraser:
    def __init__(self, video):
        self.video = video

    def erase(self):
        print("***")
        print("Deleting....{}".format(self.video))
        print("***")
        try:
            os.remove(self.video)
            print("Video deleted")
        except:
            print("problem with {} (erasing)".format(self.video))
            stop
        clear_screen()


# Whole procedure including
# taking care of the terminal path
# listing youtube urls you wanna download
# downloading, converting & deleting all videos
class YouTube_converter:
    """
    This script will download Youtube videos, covert them into mp3 and delte the
    remaining mp4 video file.
    The title for the mp3 file is the 10 first characters of the Youtube video title.
    Feel free to change it manually in line 72
    => title = self.title[:10]
    """
    def __init__(self):
        clear_screen()
        path_changer()
        self.urls = list_urls()

    def _process_(self):
        for url in self.urls:
            Downloader(url).download()
            video_downloaded = glob.glob("*.mp4")[0]
            Converter(video_downloaded).convert()
            Eraser(video_downloaded).erase()
        print("...DONE...")


YouTube_converter()._process_()
