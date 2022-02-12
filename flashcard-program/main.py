# Keanu Aloua
# December 30, 2021
# CAPSTONE PROJECT - Flashcard Program
# Using Tkinter, File I/O with CSV files, pandas, exception handling

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_words.csv")

words_to_learn = data.to_dict(orient="records")
word_index = {}


# -------------------------------- SAVE DATA --------------------------------#
def save_data():
    words_to_learn.remove(word_index)
    new_words = pandas.DataFrame(words_to_learn)
    new_words.to_csv("data/words_to_learn.csv", index=False)

    new_random_word()


# -------------------------------- RANDOM WORD --------------------------------#
def new_random_word():
    global word_index, timer

    window.after_cancel(timer)
    word_index = random.choice(words_to_learn)
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(word, text=word_index["Spanish"], fill="black")
    canvas.itemconfig(card, image=front_card)
    timer = window.after(3000, show_answer, word_index)


# -------------------------------- SHOWS ANSWER --------------------------------#
def show_answer(index):
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=index["English"], fill="white")


# -------------------------------- UI SETUP --------------------------------#
window = Tk()
window.title("Flashy")
window.minsize(width=900, height=600)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, show_answer, word_index)

# Flashcard setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_card)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button setup
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=save_data)
right_button.grid(row=1, column=1)

# Starting the program with a random spanish word
new_random_word()

window.mainloop()
