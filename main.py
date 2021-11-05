#Imports
import random
from tkinter import *
import tkinter

#Variables
ui = tkinter.Tk()
font = "Segoe UI"

#Window Details
ui.title("You are...")
ui.geometry("400x150")
ui.resizable(height=False, width=False)

#Startup
print("Started Successfully!")
print("Github Repo: https://github.com/Optimal7/you-are")

#Chooses option
def random_text():
    you_are_list = ['a clone', 'doing great', 'everything', 'washing', 'artistic', 'you', 'me', 'a liquid', 'tasty',
                    'a cool person', 'Squidward', 'dating', 'an axolot', 'a fish', 'an uncle', 'a dad', 'going to be okay',
                    'not the chosen one', 'not funny', 'a goat', 'a bunny', 'a cat', 'destroying', 'a crab', 'a gnome',
                    'not human', 'a fox', 'a weeb', 'a magician', 'rich', 'Jesus Christ', 'in the World', 'dead', 'breathing',
                    'alive', 'pogchamp', 'a mouse']
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