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
# pygame 最初に初期化しておく
pygame.init()
#Title
nowp=tk.Label(text="Stray Music Ver1.0",fg="black",font=("20"))
nowp.place(x=20, y=20)
#Discordのステータス表示
def richpresence():
    global rpc
    rpc=Presence("1085040142634459216")
    rpc.connect()
    rpc.update(details="Playing stray music",large_image="bg",start=time.time())#小アイコンと何の曲を聞いているかみたいなのを表示できるようにしたい
def whatareyouplaying():
    rpc.update(details="Playing stray music",state=presenceyou,large_image="bg",start=time.time())
#何の曲が流れるとか、順番とか（製作中）
sv = tk.StringVar()
nowpte=tk.Entry(textvariable=sv,fg="#000000")
nowpte.configure(state='disabled')#書き込み禁止
nowpte.place(x=200,y=20,width=300,height=30)
#参照ボタン関数
def select():
    global lst
    global filenum
    global file_path
    idir = 'C:\\'
    file_path = tk.filedialog.askdirectory(initialdir = idir)
    lst=glob.glob(file_path+'\\'+'*.mp3')
    filenum=(sum(os.path.isfile(os.path.join(file_path, name)) for name in os.listdir(file_path)))
    for list1 in sorted( lst ):
        list2 = os.path.split( list1 )[1]
        fileviewer.insert('end', list2 )
#順番に流す（継続再生）チェックボタン
boolean_vv = tk.BooleanVar()
playnor = tk.Checkbutton(variable=boolean_vv,text='順番に流す',font=("20"))
playnor.place(x=20, y=70)
#ランダム再生チェックボタン
boolean_v = tk.BooleanVar()
playran=tk.Checkbutton(variable=boolean_v,text="ランダム再生",font=("20"))
playran.place(x=20,y=120)


#######   以降大幅修正      ######
#再生リスト
lst = []

# 曲終了イベントを追加
EVENT_MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(EVENT_MUSIC_END)

def play():
    if pygame.mixer.music.get_busy()==True:
        return

    if len(lst)==0:
        #ここも機能してない____________↓
        try:
            pass
            # print("select")
        except NameError:
            pass
            # print("error")
        #___________________________↑
    else:
        play_music()
 
def get_next_tune():
    if len(lst) > 0:
        return lst.pop()

def play_music():
    if boolean_v.get():
        random.shuffle(lst)
    # 次の曲を取得
    tune = get_next_tune()
    if tune is None: return
    pygame.mixer.music.load(tune)
    tune1=tune.replace(file_path,'')
    global presenceyou
    presenceyou=("Now playing: "+(tune1.replace("\\",'')))
    sv.set("Now playing: "+(tune1.replace("\\",'')))
    try:
        whatareyouplaying()
    except Exception as e:
        pass
    pygame.mixer.music.play(1)

def check_music_end():
    if boolean_vv.get():
        # 曲が自然終了している場合は次の曲を再生。
        if EVENT_MUSIC_END in [event.type for event in pygame.event.get()]:
            play_music()
    else:
        # チェックが入っていない場合は、自然終了のイベントが残っていると次の曲
        # を開始してしまうためイベントを消去。
        clear_events()
    root.after(100, check_music_end)

def clear_events():
    pygame.event.get()

#音楽一時停止関数
def stop():
    if pygame.mixer.music.get_busy() == True:
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
    select()

def playth():
    play()

def stopth():
    stop()
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
vol.place(x=230,y=245)
scale1 = tk.Scale( from_=0, to=100, length=200, orient = 'h', command=set_volume1 )
scale1.place(x=280,y=230,width=150)
scale1.set( 100 )
#ファイルビューワー
fileviewer = tk.Listbox(selectmode = 'single' )
fileviewer.place(x=200,y=85,width=300, height=150 )
#discord起動してない場合の例外処理
scrollbar1 = tk.Scrollbar(orient = 'v', command = fileviewer.yview)
scrollbar1.place( x=500, y=85, height=150 )
#discord起動してない場合の例外処理
try:
    richpresence()
except Exception as e:
    pass
check_music_end()  # イベント監視ループ開始
root.mainloop()
