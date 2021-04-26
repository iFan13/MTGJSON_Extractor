from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import os
import json
import csv

Tk().withdraw()
file_to_load = askopenfilename(title ="Select MTG set as JSON")

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

dir_to_save = askdirectory(title = "Select where to save file")

name = file_to_load.split("/")
name = name[len(name)-1] .split(".")[0]

file_to_save = dir_to_save+"/"+name+".csv"

if (file_to_load and file_to_save):
    with open(file_to_load, encoding='utf-8') as mtgset:
        try: 
            cards = json.load(mtgset)
            # create list of cards
            cards = cards['data']['cards']

            with open(file_to_save, "w") as textfile:
                for card in cards:
                    textfile.write(f"{card['name']},{card['rarity']}\n")
            messagebox.showinfo("Done", f'Extraction Complete. Please find your csv in {dir_to_save}')
        except json.decoder.JSONDecodeError:
            messagebox.showerror("Error","File Selected not a JSON")
elif (file_to_load and not file_to_save):
    messagebox.showerror("Error","No directory to save selected")
elif (not file_to_load and file_to_save):
    messagebox.showerror("Error","No file selected to open")
            