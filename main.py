from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_entry = Entry(width=45)
web_entry.grid(column=1, row=1, columnspan=2)

name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)

name_entry = Entry(width=45)
name_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", width=15)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
