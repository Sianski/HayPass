import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    # Create the character pool based on user selections
    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Set default length
default_length = 15

# Variables to hold user selections
length_var = tk.IntVar(value=default_length)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Create widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.grid(row=1, columnspan=2, sticky='w')

lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.grid(row=2, columnspan=2, sticky='w')

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.grid(row=3, columnspan=2, sticky='w')

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.grid(row=4, columnspan=2, sticky='w')

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=6, column=0)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=6, column=1)

# Set default password length in the entry
length_entry.insert(0, default_length)

# Run the application
root.mainloop()
