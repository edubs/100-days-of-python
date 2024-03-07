import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=700, height=550)
window.config(padx=20, pady=20)

# Label
top_text = tkinter.Label(text="I am top text", font=("Arial", 24, "bold"))
top_text.grid(row=0, column=0)


# bottom_text = tkinter.Label(text="I am bottom text", font=("Arial", 24, "bold"))
# bottom_text.pack(side="bottom")


# change the text value of the label on button click
def button_clicked():
    top_text.config(text=user_input.get())


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(row=1, column=1)

button2 = tkinter.Button(text="New Button")
button2.grid(row=0, column=2)

user_input = tkinter.Entry(width=10)
user_input.grid(row=2, column=3)

window.mainloop()
