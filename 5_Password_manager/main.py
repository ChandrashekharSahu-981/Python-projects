from tkinter import *
from tkinter import messagebox
from pathlib import Path
from Password_generator import generate_password
import json

img_path = Path(__file__).parent / "logo.png"
data_path = Path(__file__).parent / "data.json"

#Saving data
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        "email/username": email,
        "password": password
    }   

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="You can't leave any fields empty!")
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                            f"\nEmail/Username: {email}"
                                                            f"\nPassword: {password} \nDo you want to save?")
        if is_ok:
            account_found = False
            try:
                with open(data_path, "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {
                    website: [new_data]
                }
            except json.JSONDecodeError:
                data = {}
            
            if website in data:
                # Check if this email already exists
                for account in data[website]:
                    if account["email/username"] == email:
                        account["password"] = password
                        account_found = True
                        break
                # If email doesn't exist, add a new account
                if not account_found:
                    data[website].append(new_data)
            else:
                data[website] = [new_data]
            with open(data_path, "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            if account_found:
                messagebox.showinfo(title="Success", message="Your credentials have been updated successfully!")
            else:
                messagebox.showinfo(title="Success", message="Your credentials have been saved successfully!")

#Generate password
def generate_password_button_clicked():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#Search password
def search_password():
    website = website_entry.get()
    try:
        with open(data_path, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            accounts = data[website]
            details = ""
            for account in accounts:
                details += (
                    f"Email/Username : {account['email/username']}\n"
                    f"Password: {account['password']}\n\n"
                )
            messagebox.showinfo(title=website, message=details)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found.")
   
#Creating the interface
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=img_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column= 0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#Buttons 
generate_password_button = Button(text="Generate Password", command=generate_password_button_clicked)
generate_password_button.grid(row=3, column=2, sticky="ew", padx=(5, 0))
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")
search = Button(text="Search", command=search_password)
search.grid(row=1, column=2, sticky="ew", padx=(5, 0))


window.mainloop()