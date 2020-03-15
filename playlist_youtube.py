"""
Special script to deal with Youtube playlist
2020
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""


# Library we need
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


for int, mp4_file in enumerate(glob.glob("*.mp4")):
     try:
        video(mp4_file).convert()
        video(mp4_file).erase()
     except:
        print("Problem converting/erasing file, try rerunning the program"
              
