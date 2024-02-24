from moviepy.editor import *
from tkinter import *
from PIL import ImageTk
import time
import os
import pygame
from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter import colorchooser, messagebox
import tkinter as tk
from tkinter import Entry
import tkinter as tk
from PIL import  ImageTk, Image

root = Tk()
root.geometry('680x530')
root.title("video maker - Vinit")
root.resizable(0, 0)
root.iconbitmap("video-editor-icon.ico")


bg_video = PhotoImage(file="bg video.png")


button_start = PhotoImage(file="button start.png")

button_export_image = PhotoImage(file="button export.png")

button_import_image = PhotoImage(file="button import.png")

button_audio_image = PhotoImage(file="button audio.png")

button_file_1_image = PhotoImage(file="button file.png")

button_file_2_image = PhotoImage(file="button file2.png")

button_ok_image = PhotoImage(file="button ok.png")



label = ttk.Label(image=bg_video)
label.place(x=-3, y=0)



file_box = Listbox(root, bg="gray", fg="white", width=50, selectbackground="blue", selectforeground="black", relief=tk.SOLID)
file_box.place(y=60, x=0)

def starting_video():
    global audio_file
    global c
    global t
    global file
    global file2

    print(audio_file)
    print(c)
    print(t)
    print(int(c)+int(t))

    ##canvas = Canvas(root, width=318, height=173)
    ##canvas.place(x=355, y=70)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(loops=0)
    videoImage = Image.open(file)
    resized = videoImage.resize((318, 173), Image.LANCZOS)
    videoImage = ImageTk.PhotoImage(resized)
    ##canvas.create_image(0, 0, anchor=NW, image=videoImage)
    my_label = Label(root, image=videoImage)
    my_label.place(x=355, y=70)

    root.update()
    for g in range(int(t)):
        root.update()
        time.sleep(1)
    root.update()
    my_label.place_forget()
    videoImage = Image.open(file2)
    resized = videoImage.resize((318, 173), Image.LANCZOS)
    videoImage = ImageTk.PhotoImage(resized)
    ##canvas.create_image(0, 0, anchor=NW, image=videoImage)
    my_label = Label(root, image=videoImage)
    my_label.place(x=355, y=70)
    for g in range(int(c)):
        root.update()
        time.sleep(1)
    my_label.place_forget()
    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    ##canvas.place_forget()

def import_files():
    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    global file_box
    import_file = filedialog.askopenfilename(initialdir='audio/', title="Choose A File", filetypes=(("png Files", "*.png"), ("video files", "*.mp4"), ("music files", "*.mp3")))


    if import_file=="":
        pass
    else:
        file_box.insert(END, import_file)

def import_audio():
    global audio
    global audio_file

    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    ##audio_file = filedialog.askopenfilename(initialdir='audio/', title="Choose A Bg", filetypes=(("mp3 Files", "*.mp3"),))
    audio_file = file_box.get(ACTIVE)

    if audio_file=="":
        pass
    else:
        audio = AudioFileClip(audio_file)


def import_file1():
    global clips_1
    global clips_2
    global t
    global file

    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    t = file2_entry.get()
    ##file = filedialog.askopenfilename(initialdir='audio/', title="Choose A Bg", filetypes=(("png Files", "*.png"), ("video files", "*.mp4")))
    file = file_box.get(ACTIVE)

    if ".mp4" in file:
        clips_1 = VideoFileClip(file)
    if ".png" in file:
        clips_1 = ImageClip(file).set_duration(t)

def import_file2():
    global clips_1
    global clips_2
    global c
    global file2

    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    c = file1_entry.get()
    ##file2 = filedialog.askopenfilename(initialdir='audio/', title="Choose A Bg", filetypes=(("png Files", "*.png"), ("video files", "*.mp4")))
    file2 = file_box.get(ACTIVE)
    if ".mp4" in file2:
        clips_2 = VideoFileClip(file2)
    if ".png" in file2:
        clips_2 = ImageClip(file2).set_duration(c)

def export():
    global clips_1
    global clips_2
    global audio


    pygame.mixer.init()
    pygame.mixer.music.load("click.wav")
    pygame.mixer.music.play(loops=0)

    a = e1_entry.get()
    b = a+".mp4"
    if a=="":
        pygame.mixer.init()
        pygame.mixer.music.load("error.wav")
        pygame.mixer.music.play(loops=0)
        messagebox.showinfo('error', 'dont enter name')
    else:
        print(audio)
        BG = Label(root, text="export", font=("Nokia Standart Light", 30))
        BG.place(x = 100, y = 100)
        root.update()



        final_clip = concatenate_videoclips([clips_1, clips_2], method='compose')



        if audio=="":
            pass
        else:
            final_clip.audio = audio.subclip(0, final_clip.duration)

        final_clip.write_videofile(b, fps=24)
        BG.place_forget()

        pygame.mixer.init()
        pygame.mixer.music.load("error.wav")
        pygame.mixer.music.play(loops=0)

        messagebox.showinfo('info', 'export')


number1 = tk.StringVar()
number2 = tk.StringVar()


e1_entry = Entry(root, highlightthickness=0, bd=0)
e1_entry.place(x = 0, y = 3, height=20, width=650)

enter_btn = Button(root, text='export', command=export, image=button_export_image, highlightthickness=0, bd=0)
enter_btn.place(x = 590, y = 25)

file_btn = Button(root, text='file 1', command=import_file1, image=button_file_1_image, highlightthickness=0, bd=0)
file_btn.place(x = 0, y = 405)

file2_btn = Button(root, text='file 2', command=import_file2, image=button_file_2_image, highlightthickness=0, bd=0)
file2_btn.place(x = 0, y = 435)

audio_btn = Button(root, text='audio', command=import_audio, image=button_audio_image, highlightthickness=0, bd=0)
audio_btn.place(x = 0, y = 25)

import_btn = Button(root, text='import', command=import_files, image=button_import_image, highlightthickness=0, bd=0)
import_btn.place(x = 90, y = 25)

start_btn = Button(root, text='start', image=button_start, highlightthickness=0, bd=0, command=starting_video)
start_btn.place(x = 495, y = 265)

file1_entry = tk.Entry(root, highlightthickness=0, bd=0, textvariable=number1)
file1_entry.place(x = 100, y = 435, height=20, width=100)
file2_entry = tk.Entry(root, highlightthickness=0, bd=0, textvariable=number2)
file2_entry.place(x = 100, y = 405, height=20, width=100)



clips_1 = 0
clips_2 = 0

c = 0

t = 0


audio = ""

media = ""

audio_file = ""

file2 = ""

file = ""

root.mainloop()