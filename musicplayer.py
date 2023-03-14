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
#Title
nowp=tk.Label(text="Stray Music Ver1.0",fg="black",font=("20"))
nowp.place(x=20, y=20)
#何の曲が流れるとか、順番とか（製作中）
nowpte=tk.Text()
nowpte.insert(3.0,"Now playing:（調整中")
nowpte.configure(state='disabled')#書き込み禁止
nowpte.place(x=200,y=20,width=300,height=140)
#参照ボタン関数
def select():
    global lst
    global filenum
    idir = 'C:\\Users\\tamat\\3D Objects\\百人一首'
    file_path = tk.filedialog.askdirectory(initialdir = idir)
    lst=glob.glob(file_path+'\\'+'*.mp3')
    filenum=(sum(os.path.isfile(os.path.join(file_path, name)) for name in os.listdir(file_path)))
    print(filenum)
#順番に流す（継続再生）チェックボタン
boolean_vv = tk.BooleanVar()
playnor = tk.Checkbutton(variable=boolean_vv,text='順番に流す',font=("20"))
playnor.place(x=20, y=70)
#ランダム再生チェックボタン
boolean_v = tk.BooleanVar()
playran=tk.Checkbutton(variable=boolean_v,text="ランダム再生",font=("20"))
playran.place(x=20,y=120)
#再生開始ボタン関数
def play():
    global tune
    global pygame #多分これ不要
    if lst==None:
        #ここも機能してない____________↓
        try:
            print("select")
        except NameError:
            print("error")
        #___________________________↑
    else:
        #継続◯+ランダム◯
        if boolean_vv.get():
            if boolean_v.get():
                random.shuffle(lst)
            for tune in lst:
                pygame.mixer.init()
                pygame.mixer.music.load(tune)
                mc = mp3(tune).info.length
                pygame.mixer.music.play(1)
                time.sleep(mc+0.5)
            else:
                #継続◯だけ
                for tune in lst:
                    pygame.mixer.init()
                    pygame.mixer.music.load(tune)
                    mc = mp3(tune).info.length
                    pygame.mixer.music.play(1)
                    time.sleep(mc + 0.5)
        else:
            #ランダム◯だけ
            if boolean_v.get():
                random.shuffle(lst)
            for tune in lst:
                pygame.mixer.init()
                pygame.mixer.music.load(tune)
                pygame.mixer.music.play()
#音楽一時停止関数
def stop():
    if pygame.mixer.music.get_busy()==True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
#音量調節関数
def set_volume1(str1):
    val1=float(str1)/100.0
    if val1 < 0.0: val1 = 0.0
    elif val1 > 100.0:
        val1 =1.0
    pygame.mixer.music.set_volume(val1)
def selectth():
    thread = threading.Thread(target=select)
    thread.start()
def playth():
    thread=threading.Thread(target=play)
    thread.start()
def stopth():
    thread=threading.Thread(target=stop)
    thread.start()

#ファイル参照ボタン
img=tk.PhotoImage(file="UI/docusign.png")
big_img=img.zoom(2,2)
selecmu=tk.Button(image=big_img,command=selectth)
selecmu.place(x=20,y=200)
#再生開始ボタン
imgg=tk.PhotoImage(file="UI/play_icon.png")
small_img = imgg.subsample(1,1)
playbu=tk.Button(image=small_img,command=playth)
playbu.place(x=530,y=10)
#一時停止ボタン
imggg=tk.PhotoImage(file="UI/stop_icon.png")
small_imgg= imggg.subsample(1,1)
stopbu=tk.Button(image=small_imgg,command=stopth)
stopbu.place(x=570,y=200)
#音量調節バー         #左右の端に音量のアイコン付けたい
vol=tk.Label(text="Vol",fg="black",font=("20"))
vol.place(x=150,y=215)
scale1 = tk.Scale( from_=0, to=100, length=200, orient = 'h', command=set_volume1 )
scale1.place(x=200,y=200,width=150)
scale1.set( 100 )
#Discordのステータス表示
def richpresence():
    rpc=Presence("1085040142634459216")
    rpc.connect()
    rpc.update(details="playing stray music",large_image="bg",start=time.time())#小アイコンと何の曲を聞いているかみたいなのを表示できるようにしたい
#discord起動してない場合の例外処理
try:
    richpresence()
except Exception as e:
    pass
root.mainloop()
