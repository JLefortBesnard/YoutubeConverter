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
import youtube_dl

# clear the terminal screen to make process clearer and more readable
def clear_screen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# Select the path to create the music folder
def update_path():
    print("***")
    current_path = os.getcwd()
    print("current path = {}".format(current_path))
    print("create the music folder in the current path (0) or define a path (1)?")
    choice = input(">")
    print("***")
    if choice == "0":
        path = "music"
        # Check if path doesn't already exist
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
    else:
        print("define new complete path (e.g., User\\Desktop). An empty folder named music will be created there")
        path = input(">")
        os.chdir("../../../../../../..") # Reset your path
        new_path = os.path.join(path, "music")
        # Check if path doesn't already exist
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        os.chdir(new_path)
    wd_updated = os.getcwd()
    print("***")
    print("current path updated (where Youtube videos will be converted)= {}".format(wd_updated))
    print("***")


# ask you for all Youtube videos you wanna convert
class list_urls:
    def __init__(self):
        self.list = []

    # Add *one by one* Youtube video urls you wanna convert
    def add_unique_url(self):
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

    # Add *a list* of Youtube video urls you wanna convert (separated by a space)
    def add_urls_list(self):
        print("***")
        print("copy paste Youtube urls separated by (only one) space here")
        print("e.g., url1 url2 url3 url4 etc...")
        urls = input(">")
        for url in urls.split(" "):
            self.list.append(url)
        return self.list


# download a youtube video
def download(url):
    try:
        title = YouTube(url).title
    except:
        title = url[32:]
    print("***")
    print("Downloading....{}".format(title))
    print("***")
    title_short = title[:10]
    try:
        youtube_dl.YoutubeDL().download([url])
    except:
        print("!!!!!!!!!!problem with {} (downloading)!!!!!!!!!!".format(title_short))
        print("URL was: {}".format(url))
    time.sleep(2)

# convert a youtube video into mp3
class video:
    def __init__(self, video):
        self.video = video
        self.name = video[:-4]

    # convert mp4 into mp3
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
            print("!!!!!!!!  problem with {} (converting) !!!!!!!!".format(self.video))

    # erase the downloaded mp4 youtube video
    def erase(self):
        print("***")
        print("Deleting....{}".format(self.video))
        print("***")
        try:
            os.remove(self.video)
            print("Video deleted")
        except:
            print("!!!!!!!!  problem with {} (erasing) !!!!!!!".format(self.video))





# Whole procedure including
# taking care of the terminal path
# asking for youtube urls you wanna download
# downloading video, converting into mp3 & deleting remaining video
class YouTube_converter:
    """
    This script will download Youtube videos, convert them into mp3 and delete the
    remaining mp4 video file.
    The title for the mp3 file is the 10 first characters of the Youtube video title.
    Feel free to change it manually in line 93
    => title_short = title[:10]
    """
    def __init__(self, my_url_list):
        self.urls = my_url_list

    def _process_(self):
        for int, url in enumerate(self.urls):
            download(url)
            try:
                video_downloaded = glob.glob("*.mp4")[0]
                video(video_downloaded).convert()
                video(video_downloaded).erase()
            except:
                video_downloaded = "No video found, check download problem, try closing the terminal and restart the program"
            print(" "* 15)
            done = int + 1
            remain = len(self.urls)
            print("...DONE {} / TOTAL {}...".format(done, remain))
            print(" "* 15)

# launch the program
clear_screen()
choice = input("Add youtube urls one by one (1) or paste a list (2)?")
if choice == "1":
    my_url_list = list_urls().add_unique_url()
else:
    my_url_list = list_urls().add_urls_list()
update_path()
YouTube_converter(my_url_list)._process_()

print("Convert more videos? (type 0 to continue converting)")
print("Remember to check out if all urls were converted")
print("If there is any problem, try closing your terminal and rerunning the program")
go = input(">")

while go == "0":
    choice = input("Add youtube urls one by one (1) or paste a list (2)?")
    if choice == "1":
        my_url_list = list_urls().add_unique_url()
    else:
        my_url_list = list_urls().add_urls_list()

    YouTube_converter(my_url_list)._process_()
    print("Convert more videos (Ctrl + C to stop the program")

