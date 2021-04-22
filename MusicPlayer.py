from tkinter import *
from tkinter import ttk, filedialog, PhotoImage
from PIL import ImageTk, Image
import os
from pygame import mixer

volume_value = 50


def play_song():
    mixer.music.load(play_list.get(ACTIVE))
    mixer.music.play()


def vol_set(val):
    mixer.music.set_volume(float(val)/100)


def open_folder():
    path = filedialog.askdirectory()
    if(path):
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if(song.endswith(".mp3") or song.endswith(".webm")):
                play_list.insert(END, song)


def decrease():
    global volume_value
    if volume_value > 0:
        volume_value -= 10
    vol.set(volume_value)


def increase():
    global volume_value
    if volume_value < 100:
        volume_value += 10
    vol.set(volume_value)


root = Tk()
mixer.init()
root.geometry("550x600")
root.title("Mini Music Player")

icon_play = PhotoImage(file="assets/icons/play.png")
icon_pause = PhotoImage(file="assets/icons/pause.png")
icon_unpause = PhotoImage(file="assets/icons/unpause.png")
icon_open = PhotoImage(file="assets/icons/open.png")
icon_stop = PhotoImage(file="assets/icons/stop.png")
icon_volumeup = PhotoImage(file="assets/icons/volumeup.png")
icon_volumedown = PhotoImage(file="assets/icons/volumedown.png")

s = ttk.Style(root)
s.theme_use('vista')

canv = Canvas(root, width=700, height=700, bg='white')
canv.place(relx=0, rely=0, anchor=NW)
img = Image.open("assets/icons/background.jpg")
img = img.resize((550, 600), Image.ANTIALIAS)
img_save = ImageTk.PhotoImage(img)
canv.create_image(0, 0, anchor=NW, image=img_save)


ttk.Button(root, text="Play", image=icon_play, width=30, command=play_song).place(x=80, y=150)
ttk.Button(root, text="Stop", width=10, image=icon_stop,command=mixer.music.stop).place(x=80, y=192)
ttk.Button(root, text="Pause", width=10, image=icon_pause,command=mixer.music.pause).place(x=80, y=234)
ttk.Button(root, text="UnPause", width=10, image=icon_unpause,command=mixer.music.unpause).place(x=80, y=276)
ttk.Button(root, text="Open", width=10, image=icon_open,command=open_folder).place(x=80, y=318)
ttk.Button(root, image=icon_volumedown, command=decrease).place(x=158, y=392)
ttk.Button(root, image=icon_volumeup, command=increase).place(x=379, y=392)

ttk.Label(root, text="MUSIC PLAYER", font=("Times" ,30), background= "blue4", foreground = "White").place(x=150,y=40)

music_frame = Frame(root)
music_frame.place(x=150, y=150, width=300, height=200)
scroll_y = ttk.Scrollbar(music_frame)
play_list = Listbox(music_frame, width=200,height=200, yscrollcommand=scroll_y.set)
scroll_y.config(command=play_list.yview)
scroll_y.pack(side=RIGHT, fill=Y)
play_list.pack(side=LEFT, fill=BOTH)

vol = ttk.Scale(root, from_=0, to_=100, length=180, command=vol_set)
vol.set(volume_value)
vol.place(x=200, y=400)

root.mainloop()
