import youtube_dl
from tkinter import *
import glob
import os

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("Private Converter")
        self.window.geometry("900x480")
        self.window.minsize(480, 360)
        self.window.config(background='#41B77F')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = inp)

    def create_widgets(self):
        self.create_title()
        self.create_input()
        self.create_output()
        self.create_youtube_button()
        

    def create_title(self):
        label_title = Label(self.frame, text="Paste the url to dowload", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_input(self):
        inputtxt = Text(self.frame,
                   height = 1,
                   width = 50)
        inputtxt.pack()
        self.url = inputtxt
    
    def create_output(self):
        labeltxt = Label(self.frame, text = "Operation = Not lauched yet", font=("Courrier", 15), bg='#41B77F',
                            fg='white')
        labeltxt.pack()
        self.label = labeltxt

    def check_result(self):
        # print if success or not
        if self.info_dict != 'None':
            self.path = self.info_dict['title'] + '-' + self.info_dict['display_id'] + '.mp3'
            self.path1 = self.info_dict['title'] + '-' + self.info_dict['display_id'] + '.webm'
            for root, dirs, files in os.walk(os.getcwd()):
                if self.path in files:
                    result = "download SUCCEED"
                    self.label.config(text = "Operation = " + result, font=("Courrier", 15), bg='#41B77F',
                            fg='green')
                elif self.path1 in files:
                    result = "download SUCCEED"
                    self.label.config(text = "Operation = " + result, font=("Courrier", 15), bg='#41B77F',
                            fg='green')
                else:
                    result = "download FAILED"
                    self.label.config(text = "Operation = " + result, font=("Courrier", 15), bg='#41B77F',
                            fg='red')
        else:
            result = "download FAILED"
            self.label.config(text = "Operation = " + result, font=("Courrier", 15), bg='#41B77F',
                            fg='red')
        self.label.pack()



    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Download and convert", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.converter)
        yt_button.pack(pady=25, fill=X)


    def converter(self):
        self.print_wait()
        url = self.url.get(1.0, "end-1c")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                self.info_dict = ydl.extract_info(url, download=False)
                ydl.download([url])
            except:
                self.info_dict = "None"
        self.check_result()

            
# afficher
app = MyApp()
app.window.mainloop()


