
"""
Download Youtube video and convert them into mp3 and delete the dowloaded video
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""


# Library we need
from pytube import YouTube
import os
import time
import moviepy.editor as mp
import glob
from sys import platform

# clear the terminal screen to make process clearer and more readable
def clear_screen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# Find the path to create the music folder
class path_changer:
    def __init__(self):
        clear_screen()
        self.path = os.getcwd()

    def update_path(self):
        print("***")
        print("current path = {}".format(self.path))
        print("create the music folder in the current path (0) or define a path (1)?")
        choice = int(input(""))
        print("***")
        if choice == 0:
            path = "music"
            if not os.path.exists(path):
                os.makedirs(path)
            os.chdir(path)
        else:
            print("define new complete path (e.g., User\\Desktop). An empty folder named music will be created there")
            path = input(">")
            os.chdir("../../../../../../..") # Reset your path
            new_path = os.path.join(path, "music")
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            os.chdir(new_path)
        wd_updated = os.getcwd()
        print("***")
        print("current path updated = {}".format(wd_updated))
        print("***")
        time.sleep(2)

# ask you for all Youtube videos you wanna convert
class list_urls:
    def __init__(self):
        self.list = []

    def add_url(self):
        print("***")
        print("copy paste Youtube url here")
        print(" or type 1 to stop adding URL")
        url = input(">")
        while url != "1":
            self.list.append(url)
            print("*** added ***")
            print("copy paste Youtube url here")
            print(" or type 1 to stop adding URL")
            url = input(">")
        return self.list


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
            YouTube(self.url).streams.first().download(filename=title)
            print("Video Downloaded")
        except:
            print("problem with {} (downloading)".format(title))
            print("URL was: {}".format(self.url))
        time.sleep(2)


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


# Whole procedure including
# taking care of the terminal path
# asking for youtube urls you wanna download
# downloading video, converting into mp3 & deleting remaining video
class YouTube_converter:
    """
    This script will download Youtube videos, convert them into mp3 and delete the
    remaining mp4 video file.
    The title for the mp3 file is the 10 first characters of the Youtube video title.
    Feel free to change it manually in line 72
    => title = self.title[:10]
    """
    def __init__(self):
        clear_screen()
        path_changer().update_path()
        self.urls = list_urls().add_url()
        clear_screen()

    def _process_(self):
        for int, url in enumerate(self.urls):
            Downloader(url).download()
            try:
                video_downloaded = glob.glob("*.mp4")[0]
            except:
                video_downloaded = "No video found"  
            Converter(video_downloaded).convert()
            Eraser(video_downloaded).erase()
            print(" "* 15)
            done = int + 1
            remain = len(self.urls)
            print("...DONE {} / REMAINING {}...".format(done, remain))
            print(" "* 15)

                


# launch the program
YouTube_converter()._process_()

print("Comvert more videos? (type 0 to continue converting)")
input = input(">")
while input == "0":
    print("Alright let's do it again, check out if all urls were converted")
    print("If there is any problem, try closing your terminal and rerunning the program")
    input("press enter to continue")      
    YouTube_converter()._process_()
        
