import pyperclip
from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '=', '?']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    random_characters = [choice(letters) for _ in range(randint(8, 10))]
    random_characters += [choice(symbols) for _ in range(randint(2, 4))]
    random_characters += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(random_characters)
    password = ''.join(random_characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------ SEARCH PASSWORD -------------------------------- #
def find_password():
    website = website_var.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    # The best practice here is to use exception handling only when it's hard to manage with
    #   regular code, an if/else block is preferred here in this case.
    # except KeyError:
    #     messagebox.showinfo(title="No Matches", message="No details for the website exists")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="No Matches", message=f"No details for {website} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_var.get()
    email = email_var.get()
    password = password_var.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 00:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            print("File not found, creating...")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Writing updated data
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Entries
website_var = StringVar()
website_entry = Entry(width=21, textvariable=website_var)
website_entry.grid(row=1, column=1, columnspan=1, sticky="EW")
website_entry.focus()

email_var = StringVar()
email_entry = Entry(width=35, textvariable=email_var)
email_entry.insert(0, "williams.erik@protonmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_var = StringVar()
password_entry = Entry(width=21, textvariable=password_var)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
