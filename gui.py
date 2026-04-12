import json
import os
import tkinter as tk
from tkinter import ttk

from models.clothing import Top, Bottom, Shoes
from models.wardrobe import Wardrobe
from models.outfit import Outfit
import random

# Storage

FILE_NAME = "wardrobe.json"

my_wardrobe = Wardrobe()

saved_outfits = []
current_outfit = None

def save_wardrobe():
    data = []
    for item in my_wardrobe.items:
        extra = getattr(item, "sleeve_length", None) or getattr(item, "style", None) or getattr(item, "shoe_type", None)
        data.append({
            "name": item.name,
            "category": item.category,
            "color": item.color,
            "extra": extra
        })
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

def load_wardrobe():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as f:
        data = json.load(f)

    for item in data:
        if item["category"] == "Top":
            my_wardrobe.add_item(Top(item["name"], item["color"], item["extra"]))
        elif item["category"] == "Bottom":
            my_wardrobe.add_item(Bottom(item["name"], item["color"], item["extra"]))
        elif item["category"] == "Shoes":
            my_wardrobe.add_item(Shoes(item["name"], item["color"], item["extra"]))

load_wardrobe()

if not my_wardrobe.items:
    my_wardrobe.add_item(Top("Red Shirt", "red", "short"))
    my_wardrobe.add_item(Bottom("Blue Jeans", "blue", "jeans"))
    my_wardrobe.add_item(Shoes("Samba", "black", "Sneaker"))


# App setup
BG = "#1e1e2f"
CARD = "#2a2a40"
ACCENT = "#6c63ff"
TEXT = "#ffffff"

root = tk.Tk()
root.title("Wradrobe App")
root.geometry("700x500")
root.configure(bg=BG)

# Frames
frame_generator = tk.Frame(root, bg=BG)
frame_wardrobe = tk.Frame(root, bg=BG)

frame_generator.pack(fill="both", expand=True)

def styled_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=ACCENT,
        fg="white",
        activebackground="#5548c8",
        relief="flat",
        padx=10,
        pady=5
    )


# Navigation
def show_generator():
    frame_wardrobe.pack_forget()
    frame_generator.pack(fill="both", expand=True)

def show_wardrobe():
    frame_wardrobe.pack_forget()
    frame_wardrobe.pack(fill="both", expand=True)
    refresh_list()

# GENERATOR

title = tk.Label(frame_generator, text="Outfit Generator",
                 font=("Helvetica", 20, "bold"),
                 bg=BG, fg=ACCENT)
title.grid(row=0, column=0, columnspan=3, pady=10)

top_label = tk.Label(frame_generator, text="Top: -", bg=BG, fg=TEXT)
bottom_label = tk.Label(frame_generator, text="Bottom: -", bg=BG, fg=TEXT)
shoes_label = tk.Label(frame_generator, text="Shoes: -", bg=BG, fg=TEXT)

top_label.grid(row=1, column=0, columnspan=3)
bottom_label.grid(row=2, column=0, columnspan=3)
shoes_label.grid(row=3, column=0, columnspan=3)

def generate_outfit():
    global current_outfit
    current_outfit = Outfit.generate_random(my_wardrobe)

    if isinstance(current_outfit, Outfit):
        top_label.config(text=f"Top: {current_outfit.top.name}")
        bottom_label.config(text=f"Bottom: {current_outfit.bottom.name}")
        shoes_label.config(text=f"Shoes: {current_outfit.shoes.name}")

    else:
        top_label.config(text=current_outfit)

def new_top():
    tops = my_wardrobe.filter_by_category("Top")
    if current_outfit and tops:
        current_outfit.top = random.choice(tops)
        top_label.config(text=f"Top: {current_outfit.top.name}")

def new_bottom():
    bottoms = my_wardrobe.filter_by_category("Bottom")
    if current_outfit and bottoms:
        current_outfit.bottom = random.choice(bottoms)
        bottom_label.config(text=f"Bottom: {current_outfit.bottom.name}")
 
def new_shoes():
    shoes = my_wardrobe.filter_by_category("Shoes")
    if current_outfit and shoes:
        current_outfit.shoes = random.choice(shoes)
        shoes_label.config(text=f"Shoes: {current_outfit.shoes.name}")

def save_outfit():
    if current_outfit:
        saved_outfits.append(current_outfit)
        update_saved_list()

# Buttons
tk.Button(frame_generator, text="Generate", width=15, command=generate_outfit)\
    .grid(row=4, column=0, pady=10)

tk.Button(frame_generator, text="New Top", command=new_top)\
    .grid(row=5, column=0)

tk.Button(frame_generator, text="New Bottom", command=new_bottom)\
    .grid(row=5, column=1)

tk.Button(frame_generator, text="New Shoes", command=new_shoes)\
    .grid(row=5, column=2)

tk.Button(frame_generator, text="Save Outfit", command=save_outfit)\
    .grid(row=6, column=0, columnspan=3, pady=10)

tk.Button(frame_generator, text="Wardrobe Manager", command=show_wardrobe)\
    .grid(row=7, column=0, columnspan=3)

#saved outfits

saved_label = tk.Label(frame_generator, text="Saved Outfits", bg=BG, fg=ACCENT)
saved_label.grid(row=0, column=3)

saved_listbox = tk.Listbox(frame_generator, bg=CARD, fg=TEXT, selectbackground=ACCENT, width=30)
saved_listbox.grid(row=1, column=3, rowspan=6, padx=20)


def update_saved_list():
    saved_listbox.delete(0, tk.END)
    for outfit in saved_outfits:
        text = f"{outfit.top.name} | {outfit.bottom.name} | {outfit.shoes.name}"
        saved_listbox.insert(tk.END, text)

#WARDROBEPAGE

frame_wardrobe.grid_columnconfigure(0, weight=2)
frame_wardrobe.grid_columnconfigure(1, weight=1)
frame_wardrobe.grid_rowconfigure(1, weight=1)

# Titel
title2 = tk.Label(frame_wardrobe,
                  text="Wardrobe Manager",
                  font=("Helvetica", 20, "bold"),
                  bg=BG, fg=ACCENT)
title2.grid(row=0, column=0, columnspan=2, pady=10)

# -------- LEFT SIDE (LIST) --------
listbox = tk.Listbox(frame_wardrobe,
                     bg=CARD,
                     fg=TEXT,
                     selectbackground=ACCENT)

listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


def refresh_list():
    listbox.delete(0, tk.END)
    for item in my_wardrobe.items:
        listbox.insert(tk.END, str(item))


# -------- RIGHT SIDE (FORM) --------
form_frame = tk.Frame(frame_wardrobe, bg=BG)
form_frame.grid(row=1, column=1, sticky="n", padx=10, pady=10)

tk.Label(form_frame, text="Add Item", bg=BG, fg=ACCENT).pack(pady=5)

name_entry = tk.Entry(form_frame)
color_entry = tk.Entry(form_frame)
extra_entry = tk.Entry(form_frame)

name_entry.pack(pady=5)
color_entry.pack(pady=5)
extra_entry.pack(pady=5)

category_var = tk.StringVar()
category_menu = ttk.Combobox(form_frame, textvariable=category_var)
category_menu['values'] = ("Top", "Bottom", "Shoes")
category_menu.pack(pady=5)


def add_item():
    name = name_entry.get()
    color = color_entry.get()
    extra = extra_entry.get()
    category = category_var.get()

    if category == "Top":
        item = Top(name, color, extra)
    elif category == "Bottom":
        item = Bottom(name, color, extra)
    elif category == "Shoes":
        item = Shoes(name, color, extra)
    else:
        return

    my_wardrobe.add_item(item)
    save_wardrobe()
    refresh_list()


def remove_item():
    selected = listbox.curselection()
    if selected:
        item = my_wardrobe.items[selected[0]]
        my_wardrobe.remove_item(item)
        save_wardrobe()
        refresh_list()


# Buttons im Form
styled_button(form_frame, "Add Item", add_item).pack(pady=5)
styled_button(form_frame, "Remove Selected", remove_item).pack(pady=5)
styled_button(form_frame, "Back", show_generator).pack(pady=10)

# START
root.mainloop()