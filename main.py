from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbol = [choice(symbols) for char in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    name = name_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oooops", message="Please dont leave any fields empty!")
    else:


        is_it_ok = messagebox.askokcancel(title=website, message=f"There are details entered \n Email: {name} \n Password: {password}"
                                                      f"\n "f"Is it ok to save?")

        if is_it_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {name} | {password} \n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


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
web_entry.focus()

name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)


name_entry = Entry(width=45)
name_entry.grid(column=1, row=2, columnspan=2)
name_entry.insert(0, "jozef1425@azet.hu")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", width=15, command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command= save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
