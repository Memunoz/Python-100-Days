from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbol + password_number + password_letter

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Oops, you Cant leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="Empty Storage")
    else:
        web = website_entry.get().title()
        if web in data:
            username = data[web]["username"]
            password = data[web]["password"]
            messagebox.showinfo(
                title=web,
                message=f"For: {web}\nUsername: {username}\nPassword: {password}",
            )
        else:
            messagebox.showinfo(message="File not found")


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.config(padx=50, pady=50, bg="white")
windows.title("Password Manager")
windows.resizable(False, False)
windows.columnconfigure(0, weight=5)
windows.columnconfigure(1, weight=1)
windows.columnconfigure(2, weight=5)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
username_label = Label(text="Email/Username:", bg="white")
password_label = Label(text="Password:", bg="white")
website_label.grid(column=0, row=1, padx=2, sticky="E")
username_label.grid(column=0, row=2, padx=2, sticky="E")
password_label.grid(column=0, row=3, padx=2, sticky="E")

website_entry = Entry(width=31)
website_entry.focus()
username_entry = Entry(width=52)
username_entry.insert(0, "mauricio1994.m@gmail.com")
password_entry = Entry(width=31)
website_entry.grid(column=1, row=1, ipadx=4, padx=0, sticky="E")
username_entry.grid(column=1, row=2, columnspan=2, padx=0, sticky="E")
password_entry.grid(column=1, row=3, ipadx=4, padx=0, sticky="E")

search_button = Button(text="Search", bg="white", width=15, command=search)
password_button = Button(
    text="Generate Password", bg="white", width=15, command=generate_password
)
add_button = Button(text="Add", width=44, bg="white", command=save)
search_button.grid(column=2, row=1, padx=0, sticky="E")
password_button.grid(column=2, row=3, padx=0, sticky="E")
add_button.grid(column=1, row=4, columnspan=2, sticky="W", pady=2)

windows.mainloop()
