import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

def play_music():
    selected_song = song_list.get(tk.ACTIVE)
    song_path = song_dict[selected_song]
    mixer.music.load(song_path)
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def open_file():
    global song_dict
    global song_list
    path = filedialog.askdirectory()
    if path:
        song_list.delete(0, tk.END)
        song_dict = {}
        for song in os.listdir(path):
            if song.endswith('.mp3'):
                song_path = os.path.join(path, song)
                song_dict[song] = song_path
                song_list.insert(tk.END, song)

root = tk.Tk()
root.title("Music Player")
root.configure(bg="#212121")

mixer.init()

song_dict = {}
song_list = tk.Listbox(root, width=50, bg="#333333", fg="#ffffff")
song_list.pack(padx=15, pady=15)

button_frame = tk.Frame(root, bg="#212121")
button_frame.pack(padx=15, pady=15)

play_button = tk.Button(button_frame, text="Play", command=play_music, bg="#4CAF50", fg="#ffffff")
play_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Stop", command=stop_music, bg="#f44336", fg="#ffffff")
stop_button.pack(side=tk.LEFT, padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_music, bg="#2196f3", fg="#ffffff")
pause_button.pack(side=tk.LEFT, padx=5)

unpause_button = tk.Button(button_frame, text="Unpause", command=unpause_music, bg="#9c27b0", fg="#ffffff")
unpause_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(button_frame, text="Open Directory", command=open_file, bg="#03A9F4", fg="#ffffff")
open_button.pack(side=tk.LEFT, padx=5)

root.mainloop()