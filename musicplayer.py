import tkinter as tk
from pypresence import Presence
import random
from tkinter import filedialog
import glob
import os
import threading
import pygame
import time
from mutagen.mp3 import MP3 as mp3
root = tk.Tk()
root.geometry("700x300")
root.title("Stray Music")
iconfile = 'UI/icon.ico'
root.iconbitmap(default=iconfile)
nowp=tk.Label(text="Stray Music Ver1.0",fg="black",font=("20"))
nowp.place(x=20, y=20)
nowpte=tk.Text()
nowpte.insert(3.0,"Now playing:（調整中")
nowpte.configure(state='disabled')
nowpte.place(x=200,y=20,width=300,height=140)
img=tk.PhotoImage(file="UI/docusign.png")
big_img=img.zoom(2, 2)
imgg=tk.PhotoImage(file="UI/play_icon.png")
small_img = imgg.subsample(1, 1)
def select():
    global lst
    global filenum
    idir = 'C:\\Users\\tamat\\3D Objects\\百人一首'
    file_path = tk.filedialog.askdirectory(initialdir = idir)
    lst=glob.glob(file_path+'\\'+'*.mp3')
    filenum=(sum(os.path.isfile(os.path.join(file_path, name)) for name in os.listdir(file_path)))
    print(filenum)

boolean_vv = tk.BooleanVar()
playnor = tk.Checkbutton(variable=boolean_vv,text='順番に流す',font=("20"))
playnor.place(x=20, y=70)
boolean_v = tk.BooleanVar()
playran=tk.Checkbutton(variable=boolean_v,text="ランダム再生",font=("20"))
playran.place(x=20,y=120)
def play():
    global tune
    global pygame
    if lst==None:
        try:
            print("select")
        except NameError:
            print("error")
    else:
        if boolean_vv.get():
            if boolean_v.get():
                random.shuffle(lst)
            for tune in lst:
                pygame.mixer.init()
                pygame.mixer.music.load(tune)
                mc = mp3(tune).info.length
                pygame.mixer.music.play(1)
                time.sleep(mc + 0.5)
            else:
                for tune in lst:
                    pygame.mixer.init()
                    pygame.mixer.music.load(tune)
                    mc = mp3(tune).info.length
                    pygame.mixer.music.play(1)
                    time.sleep(mc + 0.5)
        else:
            if boolean_v.get():
                random.shuffle(lst)
            for tune in lst:
                pygame.mixer.init()
                pygame.mixer.music.load(tune)
                pygame.mixer.music.play()

def stop():
    if pygame.mixer.music.get_busy()==True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
value=1
def up():
    newvo=value+1
    pygame.mixer.music.set_volume(newvo)
def down():
    newvo=value-1
    pygame.mixer.music.set_volume(newvo)
def set_volume1( str1 ):
    val1 = float( str1 )/100.0
    if val1 < 0.0: val1 = 0.0
    elif val1 > 100.0:
        val1 = 1.0
    pygame.mixer.music.set_volume( val1 )
def selectth():
    thread = threading.Thread(target=select)
    thread.start()
def playth():
    thread=threading.Thread(target=play)
    thread.start()
def stopth():
    thread=threading.Thread(target=stop)
    thread.start()
def upth():
    thread=threading.Thread(target=up)
    thread.start()
def downth():
    thread=threading.Thread(target=down)
    thread.start()
selecmu=tk.Button(image=big_img,command=selectth)
selecmu.place(x=20,y=200)
playbu=tk.Button(image=small_img,command=playth)
playbu.place(x=530 ,y=10)
imggg=tk.PhotoImage(file="UI/stop_icon.png")
small_imgg= imggg.subsample(1, 1)
stopbu=tk.Button(image=small_imgg,command=stopth)
stopbu.place(x=570 ,y=200)

vol=tk.Label(text="Vol",fg="black",font=("20"))
vol.place(x=150, y=215)
scale1 = tk.Scale( from_=0, to=100, length=200, orient = 'h', command=set_volume1 )
scale1.place( x=200, y=200, width=150 )
scale1.set( 100 )
def richpresence():
    rpc=Presence("1085040142634459216")
    rpc.connect()
    rpc.update(details="playing stray music",large_image="bg",start=time.time())

try:
    richpresence()
except Exception as e:
    pass
root.mainloop()
