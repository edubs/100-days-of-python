from tkinter import *
import pyperclip

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("German/English Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="German", fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Deutsch", fill="black", font=("Ariel", 80, "bold"))

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
