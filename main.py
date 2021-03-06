#Imports
import random
from tkinter import *
import tkinter
import requests
import json

#Variables
ui = tkinter.Tk()
font = "Segoe UI"

#Window Details
ui.title("You are...")
ui.geometry("400x150")
ui.resizable(height=False, width=False)

#Gets List
github_file = requests.get('https://raw.githubusercontent.com/Optimal7/you-are/main/list.json')
print(github_file.text)

#Updates the json file
with open('list.json', 'w+') as file:
    file.write(github_file.text)

#Opens Json
data = json.load(open("list.json"))["Content"]

#Appends everything to list
you_are_list = []
for word in data:
    you_are_list.append(word)

#Startup
print("Started Successfully!")
print("Github Repo: https://github.com/Optimal7/you-are")

#Chooses option
def random_text():
    text = random.choice(you_are_list)
    return text

#Updates the Label
def update_you_are():
    you_are_new = random_text()
    you_are.config(text=you_are_new + ".")

#Title
title = Label(ui, text="You Are...", font=(font, 20, "bold"))
title.pack()

#You Are Text (Random)    
you_are = Label(ui, font=(font, 12))
you_are.pack()

#Button to randomnize
generate = Button(ui, text="Generate", command=update_you_are)
generate.pack(pady=10)

#Credits
credit = Label(ui, text="Inspired by @YouAre_Bot on Twitter", font=(font, 12, "italic"))
credit.pack(pady=7)

#this.
ui.mainloop()