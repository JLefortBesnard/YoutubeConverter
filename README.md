# YoutubeConverter
Dowload youtube video, convert video into mp3, delete downloaded video.

Procedures to use the code are written there https://losangebleu.site/English_blogposts/blogposts_html/youtube_conv.php

Remember to upgrade the packages from time to time (pip install youtube_dl --upgrade)

Feel free to clone, pull request or contact me for help


Tip: if you copy-pasted a Youtube URL that contains many videos (Youtube playlist), for example this link including 23 videos https://www.youtube.com/watch?v=3Pii92ft5qg&list=PLPWezF-reU2c_IJ46TS4JzJtA1tlUF-dy, then all the videos from the playlist will be downloaded but not mp3 converted and deleted.
To solve this issue, once all the videos are downloaded in the folder "music", follow these steps:
1. open a new terminal window, activate python
2. cd into the music folder, something like "cd Desktop/music"
3. make sure you are in the "music" folder where all videos are 
(type "pwd" and press Enter: the last part of the path must be "../music")
(type "ls" and press Enter: should display all the video in mp4 to be mp3 converted)
4. copy-paste the playlist_youtube.py script and press Enter, or simply type: run playlist_youtube.py
That's it, enjoy!

    
