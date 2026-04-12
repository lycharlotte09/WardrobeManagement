import tkinter as tk
from tkinter import ttk

from models.clothing import Top, Bottom, Shoes
from models.wardrobe import Wardrobe
from models.outfit import Outfit
import random

my_wardrobe = Wardrobe()

my_wardrobe.add_item(Top("sexy Red", "red", "short"))
my_wardrobe.add_item(Bottom("baggy grey", "grey", "Jeans"))
my_wardrobe.add_item(Shoes("adidas samba", "black", "Sneaker"))
my_wardrobe.add_item(Top("long Red", "red", "long"))
my_wardrobe.add_item(Bottom("skinny grey", "grey", "Jeans"))
my_wardrobe.add_item(Shoes("adidas samba", "green", "Sneaker"))

saved_outfits = []
current_outfit = None

# App setup

root = tk.Tk()
root.title("Wradrobe App")
root.geometry("600x500")

# Frames
frame_generator = tk.Frame(root)
frame_wardrobe = tk.Frame(root)

frame_generator.pack(fill="both", expand=True)

# Navigation
def show_generator():
    frame_wardrobe.pack_forget()
    frame_generator.pack(fill="both", expand=True)

def show_wardrobe():
    frame_wardrobe.pack_forget()
    frame_wardrobe.pack(fill="both", expand=True)
    refresh_list()

# GENERATOR

title = tk.Label(frame_generator, text = "Outfit Generator", font=("Arial", 18))
title.grid(row=0, column=0, columnspan=3, pady=10)

top_label = tk.Label(frame_generator, text="Top: -", font=("Arial", 12))
bottom_label = tk.Label(frame_generator, text="Bottom: -", font=("Arial", 12))
shoes_label = tk.Label(frame_generator, text="Shoes: -", font=("Arial", 12))

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

saved_label = tk.Label(frame_generator, text="Saved Outfits", font=("Arial", 14))
saved_label.grid(row=0, column=3, padx=20)

saved_listbox = tk.Listbox(frame_generator, width=30)
saved_listbox.grid(row=1, column=3, rowspan=6, padx=20)

def update_saved_list():
    saved_listbox.delete(0, tk.END)
    for outfit in saved_outfits:
        text = f"{outfit.top.name} | {outfit.bottom.name} | {outfit.shoes.name}"
        saved_listbox.insert(tk.END, text)

#WARDROBEPAGE

title2 = tk.Label(frame_wardrobe, text = "Wardrobe Manager", font=("Arial", 18))
title2.pack(pady=10)

listbox = tk.Listbox(frame_wardrobe)
listbox.pack(fill="both", expand=True)

def refresh_list():
    listbox.delete(0, tk.END)
    for item in my_wardrobe.items:
        listbox.insert(tk.END, str(item))

# Add item
name_entry = tk.Entry(frame_wardrobe)
color_entry = tk.Entry(frame_wardrobe)
extra_entry = tk.Entry(frame_wardrobe)

name_entry.pack()
color_entry.pack()
extra_entry.pack()

category_var = tk.StringVar()
category_menu = ttk.Combobox(frame_wardrobe, textvariable=category_var)
category_menu['values'] = ("Top", "Bottom", "Shoes")
category_menu.pack()

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
    refresh_list()

# remove item
def remove_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        item = my_wardrobe.items[index]
        my_wardrobe.remove_item(item)
        refresh_list()

# Buttons
tk.Button(frame_wardrobe, text="Add Item", command=add_item).pack()
tk.Button(frame_wardrobe, text="Remove Selected", command=remove_item).pack()
tk.Button(frame_wardrobe, text="Back to Generator", command=show_generator).pack(pady=10)


# START
root.mainloop()