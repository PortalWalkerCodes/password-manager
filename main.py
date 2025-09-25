from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=40, pady=40)

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
username_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w", pady=5)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w", pady=5, padx=(5, 0))

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()