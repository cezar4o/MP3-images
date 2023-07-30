# Author     : Fedya Serafiev
# Version    : 1.1
# License    : MIT
# Copyright  : Fedya Serafiev (2023)
# Github     : https://github.com/cezar4o/fedya
# Description: This is a simple Python script that embeds images into an MP3 file.
# Contact    : https://urocibg.eu/

import tkinter as tk
from tkinter import filedialog
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3

def choose_mp3_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    mp3_entry.delete(0, tk.END)
    mp3_entry.insert(0, file_path)

def choose_image_file():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)

def embed_cover_art():
    mp3_file = mp3_entry.get()
    cover_image = image_entry.get()

    try:
        audio = MP3(mp3_file, ID3=ID3)
        audio.tags = ID3()

        with open(cover_image, 'rb') as f:
            cover_data = f.read()

        audio.tags.add(APIC(3, 'image/jpeg', 3, 'Front cover', cover_data))
        audio.save()

        result_label.config(text="Картинката е успешно вградена в MP3 файла.")

    except Exception as e:
        result_label.config(text=f"Възникна грешка: {e}")

# Създаване на графичното потребителско средство (GUI)
root = tk.Tk()
root.title("Вграждане на картинка в MP3")
root.geometry("400x200")

mp3_label = tk.Label(root, text="Изберете MP3 файл:")
mp3_label.pack()

mp3_entry = tk.Entry(root, width=40)
mp3_entry.pack()

mp3_button = tk.Button(root, text="Изберете файл", command=choose_mp3_file)
mp3_button.pack()

image_label = tk.Label(root, text="Изберете картинка (JPEG):")
image_label.pack()

image_entry = tk.Entry(root, width=40)
image_entry.pack()

image_button = tk.Button(root, text="Изберете файл", command=choose_image_file)
image_button.pack()

embed_button = tk.Button(root, text="Вграждане на картинката", command=embed_cover_art)
embed_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
