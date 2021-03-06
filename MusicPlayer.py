from tkinter import *
import pygame
import os
Music_Player=Tk()
Music_Player.geometry("1200x600")
Music_Player.title("Music Player By Abhinav Gangrade")
Label(Music_Player,text="Music Player By Abhinav",font="arial 15 bold").place(x=480,y=0)
pygame.init()
pygame.mixer.init()
def play():
    song_name.set(playlist.get(ACTIVE))
    status.set("Playing")
    pygame.mixer.music.load(path+"/"+playlist.get(ACTIVE))
    pygame.mixer.music.play()
def stop():
    song_name.set("----------")
    status.set("Stopped Playing")
    pygame.mixer.music.stop()
def pause():
    status.set("Paused")
    pygame.mixer.music.pause()
def unpause():
    status.set("Playing")
    pygame.mixer.music.unpause()
song_name=StringVar()
status=StringVar()
song_name.set("Hello")
status.set("Playing")
Box1=LabelFrame(Music_Player,text="Song",font="arial 15 bold",bg="navy blue",fg="white",bd=5,relief=GROOVE)
Box1.place(x=0,y=40,height=300,width=850)
Label(Box1,textvariable=song_name,font="arial 12 bold",bg="yellow").place(x=100,y=100,width=400)
Label(Box1,textvariable=status,font="arial 12 bold",bg="red").place(x=550,y=100,width=200)
Box2=LabelFrame(Music_Player,text="Control Panel",font="arial 15 bold",bg="gold",fg="Black",bd=5)
Box2.place(x=0,y=350,width=850,height=250)
Box3=LabelFrame(Music_Player,text="Playlist",font="arial 15 bold",bg="grey",fg="red",bd=5)
Box3.place(x=855,y=40,height=560,width=330)
scroll_bar=Scrollbar(Box3,orient=VERTICAL)
playlist = Listbox(Box3, yscrollcommand=scroll_bar.set, selectbackground="white", selectmode=SINGLE,
                        font=("times new roman", 12, "bold"), bg="grey", fg="gold", bd=5, relief=GROOVE)
# Applying Scrollbar to listbox
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH)
path="/home/abhinav/Videos/music"
song=os.listdir("/home/abhinav/Videos/music")
for i in song:
    playlist.insert(END,i)
Label(Box3,text="Thanks For Using the Service").place(x=50,y=300)
Button(Box2,text="Play",bg="red",fg="black",font="Arial 14 italic",command=play).place(x=20,y=70,width=100)
Button(Box2,text="Pause",bg="red",fg="black",font="Arial 14 italic",command=pause).place(x=210,y=70,width=100)
Button(Box2,text="Stop",bg="red",fg="black",font="Arial 14 italic",command=stop).place(x=430,y=70,width=100)
Button(Box2,text="Unpause",bg="red",fg="black",font="Arial 14 italic",command=unpause).place(x=630,y=70,width=100)
Music_Player.mainloop()
