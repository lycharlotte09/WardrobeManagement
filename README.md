# Wardrobe Outfit Generator App
Web application for python object-oriented-programming course work

## Overview
The Wardrobe Outfit Generator is a Python-based application that allows users to manage their cothings and generate random outfits. The app applies Object-Oriented Programming principles and provides a graphical user interface built with Tkinter.

Users can:
- Add and manage clothing items
- Upload images for each item
- Generate random outfits
- Save and review outfit combinations

## Features
### Wardrobe Management
- Add clothing items in the categories To, Bottom, Shoes
- Assign attributes such as name, color, category and extra properties
- Upload and preview images using a file picker
- remove items from the wardrobe

### Outfit Generator
- Randomly generates outfits from available items
- Allows re-randomizing individual parts
- Displays outfit visually using images

### Data persitence
- Clothing items are saved in a wardrobe.json file
- Images are copied into a local /images folder
- Data is automatically loaded when the app starts

### GUI
- Built using Tkinter
- Modern dark-themed interface
- Two main views: Outfit Generator, Wradrobe Manager

## OOP Concepts Used
This project demonstrates key OOP principles:
- Encapsulation: Each clothing item stores its own data
- Inheritance: Top, Bottom and Shoes inherit from a base Clothing class
- Polymorphism: different clothing types are handled through a common interface
- Abstraction: Gui interacts with objects without needing to know internal details

## Project Structure
wardrobe-app/ │ ├── main.py ├── wardrobe.json ├── images/ │ ├── models/ │ ├── clothing.py │ ├── wardrobe.py │ └── outfit.py

## Installation
1. Clone the repository
```
git clone https://github.com/lycharlotte09/WardrobeManagement.git
cd wardrobe-app
```
2. Install dependencies
```
pip install pillow
```
3. Run the app
```
python gui.py
```
## Future Improvements
- Improved UI
- Preview of selected image
- preview of image in wardrobe
- saving outfits permamently
- Unit Tests


# To Do after every change:

```
git status        # check
git add .         # add files to commit
git commit -m "Description"
git pull --rebase # optional, if remote changes are there
git push          # upload changes
```

# Author
Lynn Charlotte Ruge