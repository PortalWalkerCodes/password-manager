import tkinter.messagebox
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD SEARCH ---------------------------------- #
def password_search():
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(
            title="Data file not found.",
            message="Data file not found.\nIf this is your first time using this please save a password first"
        )
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            tkinter.messagebox.showinfo(
                title="Password not found",
                message=f"The password for {website} does not exist."
            )
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    global email_str


    if len(website_entry.get()) != 0 and len(password_entry.get()) != 0 and len(username_entry.get()):
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details entered: \nEmail: {username_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")

        if is_ok:
            new_data = {website_entry.get():{"email":username_entry.get(), "password":password_entry.get()}}

            try:
                 with open("passwords.json", "r") as passwords:
                    try:
                        data = json.load(passwords)
                    except JSONDecodeError:
                        data = {}
                    data.update(new_data)
            except FileNotFoundError:
                with open("passwords.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                data.update(new_data)

                with open("passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                with open("saved_email.txt", "r+") as saved_email:
                    if email_str.lower() != username_entry.get().lower():
                        choice = messagebox.askokcancel(title="Update saved email?",
                                                        detail="Your typed email is different from the saved one. Do you want to update the saved email?")

                        if choice:
                            saved_email.write(f"{username_entry.get().lower()}")

                username_entry.delete(0, END)
                username_entry.insert(0, f"{email_str}")
                password_entry.delete(0, END)
                website_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

with open("saved_email.txt", "r") as email:
    email_str = email.read()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1, sticky="nsew")
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")
username_entry.insert(0, email_str)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="nsew")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="nsew")
search_password_button = Button(text="Search", command=password_search)
search_password_button.grid(row=1, column = 2, sticky="nsew")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()