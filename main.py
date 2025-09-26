from tkinter import *
from tkinter import messagebox
import random

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


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    global email_str

    if len(website_entry.get()) != 0 and len(password_entry.get()) != 0 and len(username_entry.get()):
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details entered: \nEmail: {username_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as passwords:
                passwords.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")

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

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w", pady=5, padx=(5, 0))

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()