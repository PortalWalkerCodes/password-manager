from tkinter import *
from tkinter import messagebox
import pandas

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    global email_str

    with open("passwords.txt", "a") as passwords:
        passwords.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")

    with open("saved_email.txt", "r+") as saved_email:
        if email_str.lower() != username_entry.get().lower():
            choice = messagebox.askokcancel(title="Update saved email?", detail="The email you typed does not match autofilled email. Would you like to update the autofilled email?")

            if choice:
                saved_email.write(f"{username_entry.get().lower()}")





# ---------------------------- UI SETUP ------------------------------- #

with open("saved_email.txt", "r") as email:
    email_str = email.read()

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", pady=5)
website_entry.focus()

# Email/Username
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky="e")
username_entry = Entry(width=35)
username_entry.insert(0, email_str)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w", pady=5)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w", pady=5, padx=(5, 0))

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()