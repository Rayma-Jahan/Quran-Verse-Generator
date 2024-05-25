#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import StringVar, ttk
import random
from PIL import Image, ImageTk

# Verse categories
verse_categories = {
    "Patience": [
        "Indeed Allah is with the patient. (2:135)",
        "So be patient, with a beautiful patience. (70:5)",
        "And seek help through patience and prayer. Indeed, it is a burden except for the humble. (2:45)",
        "And bear with patience, and your patience is only because of the help of Allah – and do not grieve over them, nor feel distressed by their evil plans. (16:127)",
    ],
    "Mercy": [
        "My mercy encompasses all things. (7:156)",
        "My servants, you who have transgressed against yourselves, do not despair of the mercy of Allah. Truly Allah forgives all wrong actions. He is the Ever-Forgiving, the Most Merciful. (39:53)",
        "But those who do evil deeds, then repent and believe, they will find your Lord Forgiving and Merciful. (7:153)",
        "…Truly God is Gentle and Compassionate to mankind. (2:143)",
        "He selects for His mercy whom He wills. And Allah is the possessor of great bounty. (3:74)",
    ],
    "Forgiveness": [
        "Kind speech and forgiveness are better than charity followed by injury. And Allah is Free of need and Forbearing. (2:263)",
        "And to Allah belongs whatever is in the heavens and whatever is on the earth. He forgives whom He wills and punishes whom He wills. And Allah is Forgiving and Merciful. (3:129)",
        "Indeed, Allah does not forgive association with Him, but He forgives what is less than that for whom He wills. And he who associates others with Allah has certainly fabricated a tremendous sin. (4:48)",
        "And whoever does a wrong or wrongs himself but then seeks forgiveness of Allah will find Allah Forgiving and Merciful. (4:110)",
    ],
}

# Function to select and display a verse
def generate_verse():
    category = category_var.get()
    if category in verse_categories:
        verses = verse_categories[category]
        verse = random.choice(verses)
        result_label.config(text=verse)
    else:
        result_label.config(text="Please select a valid category.")
        
# Function to resize GIF frames
def resize_gif(image, size):
    frames = []
    frame_index = 0
    try:
        while True:
            frame = image.copy().convert("RGBA")
            frame = frame.resize(size, Image.ANTIALIAS)
            frames.append(ImageTk.PhotoImage(frame))
            frame_index += 1
            image.seek(frame_index)
    except EOFError:
        pass
    return frames

def update_frame(ind):
    frame = resized_gif_frames[ind]
    ind += 1
    if ind == len(resized_gif_frames):
        ind = 0
    gif_label.config(image=frame)
    root.after(100, update_frame, ind)

# Main application
root = tk.Tk()
root.title("Quran Verse Generator")
root.geometry("600x650")
root.configure(bg="#6B8E23")

# Load and resize the GIF image
gif_path = "C:/Users/rayma/Downloads/plant-plants.gif"
original_gif = Image.open(gif_path)
resized_gif_frames = resize_gif(original_gif, (250, 250))  # Resize to 200x200 pixels

# Display the GIF
gif_label = tk.Label(root, bg="#6B8E23")
gif_label.pack(pady=20)

# Title label
title_label = tk.Label(root, text="Quran Verses for the Soul", font=("Times New Roman", 20, "bold"), bg="#6B8E23", fg="black")
title_label.pack(pady=20)

# Category dropdown menu
category_var = StringVar(root)
category_var.set("Select Category")

category_dropdown = ttk.Combobox(root, textvariable=category_var, values=list(verse_categories.keys()), state="readonly", font=("Times New Roman", 12), width=20)
category_dropdown.pack(pady=10)

# Button to generate verse
verse_button = tk.Button(root, text="Give me a Verse", command=generate_verse, font=("Times New Roman", 14, "bold"), bg="#CD853F", fg="black", padx=10, pady=5, bd=1)
verse_button.pack(pady=20)

# Label that displays the result
result_label = tk.Label(root, text="", font=("Times New Roman", 14), wraplength=500, justify="center", bg="#6B8E23")
result_label.pack(pady=20)


# Runs the application
root.after(0, update_frame, 0)
root.mainloop()



# In[ ]:





# In[ ]:




