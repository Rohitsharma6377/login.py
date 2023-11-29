from tkinter import *
from tkinter import messagebox
import os
import sys
import getpass

# Define function for login functionality
def login_func():
    # Get the username and password
    username = username_entry.get()
    password = password_entry.get()

    # Define a dictionary with a valid username and password

    users = {"admin": "password123"}

    # Check if the username exists in the dictionary
    if username in users:
        # Check if the password matches the one stored in the dictionary
        if password == users[username]:
            # Show a success message and exit the script
            messagebox.showinfo("Success", "Login Successful!")
            sys.exit()
        else:
            # Show an error message if the password is incorrect
            messagebox.showerror("Error", "Invalid password!")
    else:
        # Show an error message if the username is not found
        messagebox.showerror("Error", "Invalid username!")

# Create a main window
root = Tk()
root.geometry("300x200")
root.title("Login Page")

# Create labels for the username and password
username_label = Label(root, text="Username:")
username_label.pack()
password_label = Label(root, text="Password:")
password_label.pack()

# Create entry fields for the username and password
username_entry = Entry(root)
username_entry.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# Create a login button
login_button = Button(root, text="Login", command=login_func)
login_button.pack(pady=20)

# Run the main loop
root.mainloop()