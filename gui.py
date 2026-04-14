import json
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import random
import shutil


from models.clothing import Top, Bottom, Shoes
from models.wardrobe import Wardrobe
from models.outfit import Outfit

# Storage

FILE_NAME = "wardrobe.json"
IMAGE_FOLDER = "images"

os.makedirs(IMAGE_FOLDER, exist_ok=True)

my_wardrobe = Wardrobe()
saved_outfits = []
current_outfit = None

top_img = None
bottom_img = None
shoes_img = None
preview_img = None

# SAVE /LOAD

def save_wardrobe():
    data = []
    for item in my_wardrobe.items:
        extra = getattr(item, "sleeve_length", None) or getattr(item, "style", None) or getattr(item, "shoe_type", None)
        data.append({
            "name": item.name,
            "category": item.category,
            "color": item.color,
            "extra": extra,
            "image": item.image_path
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
            my_wardrobe.add_item(Top(item["name"], item["color"], item["extra"], item.get("image")))
        elif item["category"] == "Bottom":
            my_wardrobe.add_item(Bottom(item["name"], item["color"], item["extra"], item.get("image")))
        elif item["category"] == "Shoes":
            my_wardrobe.add_item(Shoes(item["name"], item["color"], item["extra"], item.get("image")))

load_wardrobe()

if not my_wardrobe.items:
    my_wardrobe.add_item(Top("Red Shirt", "red", "short", None))
    my_wardrobe.add_item(Bottom("Blue Jeans", "blue", "jeans", None))
    my_wardrobe.add_item(Shoes("Samba", "black", "Sneaker", None))

# IMAGE HANDLING

def copy_image_to_project(path):
    if not path:
        return None

    filename = os.path.basename(path)
    new_path = os.path.join(IMAGE_FOLDER, filename)

    try:
        shutil.copy(path, new_path)
        return new_path
    except:
        return None
    
def load_image(path):
    try:
        img = Image.open(path)
        img = img.resize((100, 100))
        return ImageTk.PhotoImage(img)
    except:
        return None


def choose_image():
    file_path = filedialog.askopenfilename(
        title="select an Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif"),
                   ("All files", "*.*")]
    )
    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_path)
        show_preview(file_path)

def show_preview(path):
    global preview_img
    try:
        img = Image.open(path)
        img = img.resize((80, 80))
        preview_img = ImageTk.PhotoImage(img)
    except:
        preview_label.config(image="")




# App setup
BG = "#1e1e2f"
CARD = "#2a2a40"
ACCENT = "#6c63ff"
TEXT = "#ffffff"

root = tk.Tk()
root.title("Wradrobe App")
root.geometry("900x500")
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

top_image_label = tk.Label(frame_generator, bg=BG)
bottom_image_label = tk.Label(frame_generator, bg=BG)
shoes_image_label = tk.Label(frame_generator, bg=BG)

top_image_label.grid(row=1, column=0)
bottom_image_label.grid(row=1, column=1)
shoes_image_label.grid(row=1, column=2)

def display_outfit():
    global top_img, bottom_img, shoes_img

    if not current_outfit:
        return

    top_img = load_image(current_outfit.top.image_path)
    bottom_img = load_image(current_outfit.bottom.image_path)
    shoes_img = load_image(current_outfit.shoes.image_path)

    if top_img:
        top_image_label.config(image=top_img)
    if bottom_img:
        bottom_image_label.config(image=bottom_img)
    if shoes_img:
        shoes_image_label.config(image=shoes_img)



def generate_outfit():
    global current_outfit
    current_outfit = Outfit.generate_random(my_wardrobe)

    if isinstance(current_outfit, Outfit):
        display_outfit()
    

def new_top():
    tops = my_wardrobe.filter_by_category("Top")
    if current_outfit and tops:
        current_outfit.top = random.choice(tops)
        display_outfit()

def new_bottom():
    bottoms = my_wardrobe.filter_by_category("Bottom")
    if current_outfit and bottoms:
        current_outfit.bottom = random.choice(bottoms)
        display_outfit()
 
def new_shoes():
    shoes = my_wardrobe.filter_by_category("Shoes")
    if current_outfit and shoes:
        current_outfit.shoes = random.choice(shoes)
        display_outfit()

def save_outfit():
    if current_outfit:
        saved_outfits.append(current_outfit)
        update_saved_list()

# Buttons
styled_button(frame_generator, "Generate", generate_outfit).grid(row=2, column=0)
styled_button(frame_generator, "New Top", new_top).grid(row=3, column=0)
styled_button(frame_generator, "New Bottom", new_bottom).grid(row=3, column=1)
styled_button(frame_generator, "New Shoes", new_shoes).grid(row=3, column=2)
styled_button(frame_generator, "Save Outfit", save_outfit).grid(row=4, column=0, columnspan=3)
styled_button(frame_generator, "Wardrobe Manager", show_wardrobe).grid(row=5, column=0, columnspan=3)


#saved outfits

saved_listbox = tk.Listbox(frame_generator, bg=CARD, fg=TEXT)
saved_listbox.grid(row=1, column=3, rowspan=5, padx=20)


def update_saved_list():
    saved_listbox.delete(0, tk.END)
    for o in saved_outfits:
        saved_listbox.insert(tk.END, f"{o.top.name} | {o.bottom.name} | {o.shoes.name}")


#WARDROBEPAGE

frame_wardrobe.grid_columnconfigure(0, weight=2)
frame_wardrobe.grid_columnconfigure(1, weight=1)

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
form_frame.grid(row=1, column=1, sticky="n")

tk.Label(form_frame, text="Add Item", bg=BG, fg=ACCENT).pack(pady=5)

name_entry = tk.Entry(form_frame)
color_entry = tk.Entry(form_frame)
extra_entry = tk.Entry(form_frame)
image_entry = tk.Entry(form_frame)

name_entry.pack()
color_entry.pack()
extra_entry.pack()
image_entry.pack()

styled_button(form_frame, "Choose Image", choose_image).pack()

preview_label = tk.Label(form_frame, bg=BG)
preview_label.pack()


category_var = tk.StringVar()
category_menu = ttk.Combobox(form_frame, textvariable=category_var)
category_menu['values'] = ("Top", "Bottom", "Shoes")
category_menu.pack(pady=5)


def add_item():
    path = image_entry.get()
    new_path = copy_image_to_project(path)
    name = name_entry.get()
    color = color_entry.get()
    extra = extra_entry.get()
    category = category_var.get()

    if category == "Top":
        item = Top(name, color, extra, new_path)
    elif category == "Bottom":
        item = Bottom(name, color, extra, new_path)
    elif category == "Shoes":
        item = Shoes(name, color, extra, new_path)
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