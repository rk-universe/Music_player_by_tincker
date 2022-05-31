import os
import pickle
from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer
window = Tk()



current = 0
paused=True
played=False

img=PhotoImage(file='images\music.gif')
prev=PhotoImage(file='images\previous.gif')
next=PhotoImage(file='images\\next.gif')
play = PhotoImage(file='images\\play.gif')
pause=PhotoImage(file='images\pause.gif')

a=[]

def insert_song(list):

    length = len(list)
    i = 0
    while (i < length):
        playlist.insert(i, list[i])
        i += 1

def load_songs():


    file=filedialog.askopenfilenames()
    insert_song(file)
    a=file
    file = "playsongs.pkl"
    fileobj = open(file, 'wb')
    pickle.dump(a, fileobj)
    fileobj.close()









def clicked(event):

    count=playlist.size()
    for i in range(count):
        playlist.itemconfig(i,bg='white')

    current = playlist.curselection()

    p=playlist.get(current)

    photo2['anchor']='w'
    photo2['text']=os.path.basename(playlist.get(current))
    playlist.activate(current)
    playlist.itemconfig(current,bg='sky blue')

    mixer.init()
    mixer.music.load(p)
    mixer.music.set_volume(0.7)
    played=True
    paused=False
    playbt['image'] = play
    mixer.music.play()
def clicked2(current):
    count=playlist.size()
    for i in range(count):
        playlist.itemconfig(i,bg='white')
    p=playlist.get(current)
    photo2['anchor']='w'
    photo2['text']=os.path.basename(playlist.get(current))
    playlist.activate(current)
    playlist.itemconfig(current,bg='blue')

    mixer.init()
    mixer.music.load(p)
    mixer.music.set_volume(0.7)
    played=True
    paused=False
    playbt['image'] = play
    mixer.music.play()


def playpause():
    global paused
    if(paused):
        paused=False
        playbt['image']=play
        mixer.music.unpause()
    else:

        paused=True
        playbt['image'] = pause
        mixer.music.pause()




def previousbt():
    global current

    if (current > 0):
        current-=1

    else:
        current=0
    clicked2(current)



def nextbt():
    global current
    if (current < playlist.size() ):
        current+=1
    else:
        current=1
    clicked2(current)



def ch_v(event):
    v=volume.get()
    mixer.music.set_volume(v/10)













window.geometry('600x400')



photoframe = LabelFrame(window,
                 text='Song Track',
                 font=("times new roman", 15, "bold"),
                 bg="grey", fg="black", bd=5, relief=GROOVE)
photoframe.config(width=410, height=300)
photoframe.grid(row=0, column=0, padx=10)


playlistframe=LabelFrame(window,
                    text="playlist",
                    font=("times new roman", 15, "bold"),
                    bg="grey", fg="black", bd=5, relief=GROOVE)
playlistframe.config(width=160, height=380)
playlistframe.grid(row=0, column=1, rowspan=3, pady=5)
#
#
controlsframe=LabelFrame(window,

                   font=("times new roman", 15, "bold"),
                   bg="white", fg="black", bd=2, relief=GROOVE)
controlsframe.config(width=410, height=80)
controlsframe.grid(row=2, column=0, pady=5, padx=10)


# .....Inside music frame.......

photo1=Label(photoframe,image=img,
            height=240,
            width=400)
photo1.grid(row=0,column=0)

photo2=Label(photoframe,
             width=30,
             height=1,
             font=("times new roman", 16, "bold"),
             bg="white",fg="dark blue")
photo2.grid(row=1,column=0)

# ____________ iNside fram 2 controls___________________

exist=os.path.exists("playsongs.pkl")
print(exist)

load_songs=Button(controlsframe,text="LOAD SONGS",
                  bg="green",
                  fg="white",
                  command=load_songs)
load_songs.grid(row=2,column=0,padx=10)

prevs=Button(controlsframe,image=prev,command=previousbt)
prevs.grid(row=2,column=1)

playbt=Button(controlsframe,image=pause,command=playpause)
playbt.grid(row=2,column=2)

nextbt=Button(controlsframe,image=next,command=nextbt)
nextbt.grid(row=2,column=3)

volume=DoubleVar()
volbt=Scale(controlsframe,from_=0,to=10, orient=HORIZONTAL,variable=volume,command=ch_v)
volbt.set(5)
mixer.init()
mixer.music.set_volume(0.5)
volbt.grid(row=2,column=4,padx=10)

# -------------inside frame 3------------------

playlist_scrollbar=Scrollbar(playlistframe,orient=VERTICAL)
playlist_scrollbar.grid(row=0,column=1,sticky="ns")




playlist=Listbox(playlistframe,height=20,selectmode=SINGLE,yscrollcommand=playlist_scrollbar.set)

if (exist):
    file="playsongs.pkl"
    fileobj2=open(file,"rb")
    songsls=pickle.load(fileobj2)

    insert_song(songsls)
    fileobj2.close()

playlist.bind('<Double-1>',clicked)
playlist.grid(row=0,column=0)
playlist_scrollbar.config(command=playlist.yview())

























window.title("Music player")

window.mainloop()

