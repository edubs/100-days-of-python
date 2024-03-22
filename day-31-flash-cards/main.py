import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- Read Data ------------------------------- #
df = pandas.read_csv("data/english-german.csv")
data_dict = df.to_dict(orient="records")


# ------------------------- Data Functions ---------------------------- #
def generate_word():
    word_pair = random.choice(data_dict)
    canvas.itemconfigure(german_word, text=word_pair["German"])


# ---------------------------- UI SETUP ------------------------------- #
# Window & Canvas
window = Tk()
window.title("German/English Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
english = canvas.create_text(400, 150, text="German", fill="black", font=("Ariel", 40, "italic"))
german_word = canvas.create_text(400, 263, text="Deutsch", fill="black", font=("Ariel", 80, "bold"))
print(canvas.itemcget(german_word, "text"))

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=1)

window.mainloop()
