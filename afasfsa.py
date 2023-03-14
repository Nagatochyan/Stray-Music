
import os 
import glob 
import tkinter as tk1 
import pygame as pg1 

def play0(): 
    global t0 
    global t1 
    global ply1 
    if ply1 < 0: 
        ply1 = 1 
        frame1.after( 1000, after1 ) 
    pg1.mixer.music.play(start=t1) 

def play1(): 
    global t0 
    global t1 
    global n1 
    global rep1 
    global len1 
    if n1 < 0: 
        n1 = 0 
        set_list1() 
    t0   = 0
    t1   = 0 
    rep1 = -1 
    len1 = -1 
    play0() 

def play2_AB(): 
    global t0 
    global t1 
    global t2 
    global n1 
    global rep1 
    global len1 
    if n1 < 0: 
        n1 = 0 
        set_list1() 
    t1   = int( textbox1.get() ) 
    t2   = int( textbox2.get() ) 
    t0 = t1 
    len1 = t2 - t1 
    rep1 = int( textbox3.get() ) 
    play0() 

def pause1():
    global t1 
    global p1 
    if p1 < 0: 
        pg1.mixer.music.pause() 
    else: 
        pg1.mixer.music.unpause() 
    return 

def stop1(): 
    global t1 
    pg1.mixer.music.stop() 
    t1 = -1 

def set_status1(): 
    return 

def load_file1():
    global n1 
    global t1 
    global list1 
    file1 = list1[n1]
    print( file1 )
    pg1.mixer.music.load( file1 )

def click_list1( event ): 
    global n1 
    n1 = listbox1.curselection()[0] 
    set_list1() 
    play1() 

def set_list1(): 
    global n1 
    label1["text"] = listbox1.get( n1 ) 
    listbox1.select_clear(0, "end") 
    listbox1.select_set( n1 ) 
    listbox1.selection_anchor( n1 ) 
    load_file1() 

def prev1(): 
    global n1 
    global list1 
    n1 = n1 - 1 
    if n1 < 0: 
        n1 = len( list1 )-1 
        set_list1() 
        play1() 
def next1(): 
    global n1 
    global list1 
    n1 = n1 + 1 
    if n1 > len( list1 )-1:
        n1 = 0
    set_list1()
    play1()

def set_volume1( str1 ): 
    val1 = float( str1 )/100.0 
    if val1 < 0.0: val1 = 0.0 
    elif val1 > 100.0:
        val1 = 1.0
    pg1.mixer.music.set_volume( val1 )

def set_text1( str1 ): 
    global t1 
    t1 = int( str1 ) 
    textbox1.delete( 0, tk1.END ) 
    textbox1.insert( tk1.END, str( str1 ) )

def set_text2( str1 ): 
    global t2 
    t2 = int( str1 ) 
    textbox2.delete( 0, tk1.END ) 
    textbox2.insert( tk1.END, str( str1 ) ) 

def set_text3( str1 ): 
    textbox3.delete( 0, tk1.END ) 
    textbox3.insert( tk1.END, str( str1 ) ) 

def after1(): 
    global t0 
    global t1 
    global p1 
    global n1 
    global ply1 
    global len1 
    global rep1 
    global list1 
    label3["text"] = str( t0 ) 
    label4["text"] = str( rep1 ) 
    status1 = "" 
    for event1 in pg1.event.get(): 
        if event1.type == AUDIO_ENDED1: 
            if rep1 > 0: 
                rep1 = rep1 - 1 
                status1 = "next" 
            else: 
                status1 = "end2" 
    if len1 > 0 and t0 > t2-1 and status1 == "": 
        status1 = "end1" 
    if status1 == "end1": 
        if ply1 > 0: 
            pg1.mixer.music.stop() 
            frame1.after( 1000, after1 ) 
        ply1 = -1 
    elif status1 == "end2": 
        t0 = -1 
        rep1 = -1 
        ply1 = -1 
        if chkv1.get() and (n1 < len( list1 )-1):
            next1()
    elif status1 == "next":
        t0 = t1         
        if rep1 > 0: 
            play0() 
    else:
        if t0 > -1: 
            if p1 < 0: 
                t0 = t0 + 1 
                frame1.after( 1000, after1 ) 
def set_A1():
    global t0
    
    if t0 >= 0:
        textbox1.delete( 0, tk1.END )
        textbox1.insert( tk1.END, str(t0) ) 

def set_B1(): 
    global t0 
    if t0 >= 0: 
        textbox2.delete( 0, tk1.END ) 
        textbox2.insert( tk1.END, str(t0) ) 

def minus1(): 
    global t1 
    global t2 
    global len1 
    t1   = int( textbox1.get() ) - 1 
    if t1 < 0: 
        t1 = 0 
    len1 = t2 - t1 
    set_text1( t1 )

def plus1(): 
    global t1 
    global t2 
    global len1 
    t1   = int( textbox1.get() ) + 1 
    if t1 < 0: 
        t1 = 0 
    len1 = t2 - t1 
    set_text1( t1 )

def minus2(): 
    global t1 
    global t2 
    global len1 
    t2   = int( textbox2.get() ) - 1
    len1 = t2 - t1 
    set_text2( t2 )

def plus2(): 
    global t1 
    global t2 
    global len1 
    t2   = int( textbox2.get() ) + 1
    len1 = t2 - t1 
    set_text2( t2 )

def minus3(): 
    global rep1 
    rep1   = int( textbox3.get() ) - 1
    if rep1 < 1: 
        rep1 = 1 
    set_text3( rep1 )

def plus3(): 
    global rep1 
    rep1   = int( textbox3.get() ) + 1
    set_text3( rep1 )

path1 = os.path.dirname(__file__) + "\\audio1\\"    
list1 = glob.glob( path1 + "*.*" )

n1 = -1       # file number 
t0 = -1       # timer 
t1 = -1       # start 
t2 = -1       # stop 
p1 = -1       # pause 
len1 = -1     # length, AB repeat 
rep1 = -1     # repeat 
ply1 = -1     # play or not 

pg1.init() 
pg1.mixer.init() 
AUDIO_ENDED1 = pg1.USEREVENT + 1 
pg1.mixer.music.set_endevent( AUDIO_ENDED1 ) 

frame1 = tk1.Tk()
frame1.title( 'audio player v0.1' ) 
frame1.geometry( "520x300+100+100" ) 

btn1 = tk1.Button( frame1, text="play", command=play1 ) 
btn1.place( x=10, y=10, width=60 ) 

btn2 = tk1.Button( frame1, text="pause", command=pause1 ) 
btn2.place( x=70, y=10, width=60 ) 

btn3 = tk1.Button( frame1, text="stop", command=stop1 ) 
btn3.place( x=130, y=10, width=60 ) 

btn4 = tk1.Button( frame1, text="prev", command=prev1 ) 
btn4.place( x=200, y=10, width=60 ) 

btn5 = tk1.Button( frame1, text="next", command=next1 ) 
btn5.place( x=260, y=10, width=60 ) 

btn6 = tk1.Button( frame1, text="AB repeat", command=play2_AB ) 
btn6.place( x=360, y=80, width=60 ) 

btn7 = tk1.Button( frame1, text="set A", command=set_A1 ) 
btn7.place( x=360, y=130, width=60, height=20 ) 

btn8 = tk1.Button( frame1, text="set B", command=set_B1 ) 
btn8.place( x=360, y=180, width=60, height=20 ) 

btn9 = tk1.Button( frame1, text="-", command=minus1 ) 
btn9.place( x=430, y=130, width=20, height=20 ) 

btn10 = tk1.Button( frame1, text="+", command=plus1 ) 
btn10.place( x=480, y=130, width=20, height=20 ) 

btn11 = tk1.Button( frame1, text="-", command=minus2 ) 
btn11.place( x=430, y=180, width=20, height=20 ) 

btn12 = tk1.Button( frame1, text="+", command=plus2 ) 
btn12.place( x=480, y=180, width=20, height=20 ) 

btn13 = tk1.Button( frame1, text="-", command=minus3 ) 
btn13.place( x=430, y=230, width=20, height=20 ) 

btn14 = tk1.Button( frame1, text="+", command=plus3 ) 
btn14.place( x=480, y=230, width=20, height=20 ) 

scale1 = tk1.Scale(frame1, from_=0, to=100, length=200, orient = 'h', command=set_volume1 )
scale1.place( x=410, y=5, width=100 ) 
scale1.set( 100 ) 

chkv1 = tk1.BooleanVar() 
chk1 = tk1.Checkbutton( frame1, text="continuous", command=set_status1, variable=chkv1 ) 
chk1.place( x=350, y=45, width=90 ) 
chk1.select() 

label2 = tk1.Label( frame1, anchor="w", text="volume" ) 
label2.place( x=350, y=10, width=50 ) 

label3 = tk1.Label( frame1, bg="white", anchor="w" ) 
label3.place( x=430, y=80, width=30 ) 

label4 = tk1.Label( frame1, bg="white", anchor="w" ) 
label4.place( x=470, y=80, width=30 ) 

label5 = tk1.Label( frame1, anchor="w", text="A: start" ) 
label5.place( x=350, y=110, width=60 ) 

label6 = tk1.Label( frame1, anchor="w", text="B: stop" ) 
label6.place( x=350, y=160, width=60 ) 

label7 = tk1.Label( frame1, anchor="w", text="repeat" ) 
label7.place( x=350, y=210, width=60 ) 

textbox1 = tk1.Entry( frame1 ) 
textbox1.place( x=450, y=130, width=30, height=20 ) 
set_text1( 10 ) 

textbox2 = tk1.Entry( frame1 ) 
textbox2.place( x=450, y=180, width=30, height=20 ) 
set_text2( 15 ) 

textbox3 = tk1.Entry( frame1 ) 
textbox3.place( x=450, y=230, width=30, height=20 ) 
set_text3( 10 ) 

label1 = tk1.Label( frame1, bg="white", anchor="w" ) 
label1.place( x=10, y=50, width=310 ) 

listbox1 = tk1.Listbox( frame1, selectmode='single' )
listbox1.place( x=10, y=80, width=305, height=200 ) 

scrollbar1 = tk1.Scrollbar(frame1, orient='v', command=listbox1.yview)
scrollbar1.place( x=305, y=80, height=200 ) 

listbox1.configure( yscrollcommand=scrollbar1.set ) 

for list2 in sorted( list1 ): 
    list3 = os.path.split( list2 )[1] 
    listbox1.insert('end', list3 ) 

listbox1.bind('<<ListboxSelect>>', click_list1 )
frame1.mainloop()