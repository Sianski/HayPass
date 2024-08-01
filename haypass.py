import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    # Get the length from the entry field or generate a random length
    if length_var.get() == 0:  # Check if the user wants a random length
        length = random.randint(16, 20)
    else:
        length = length_var.get()

    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

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

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg='#f0f0f0')

# Variables to hold user selections
length_var = tk.IntVar(value=0)  # Default to 0 for random length
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Create widgets
length_label = tk.Label(root, text="Password Length (0 for random):", bg='#f0f0f0', fg='#333333', font=('Arial', 12))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, textvariable=length_var, bg='#ffffff', fg='#333333', font=('Arial', 12), relief=tk.FLAT)
length_entry.grid(row=0, column=1, padx=10, pady=10)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg='#f0f0f0', fg='#333333', font=('Arial', 12), activebackground='#f0f0f0', activeforeground='#333333')
upper_check.grid(row=1, columnspan=2, padx=10, pady=5, sticky='w')

lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg='#f0f0f0', fg='#333333', font=('Arial', 12), activebackground='#f0f0f0', activeforeground='#333333')
lower_check.grid(row=2, columnspan=2, padx=10, pady=5, sticky='w')

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg='#f0f0f0', fg='#333333', font=('Arial', 12), activebackground='#f0f0f0', activeforeground='#333333')
digits_check.grid(row=3, columnspan=2, padx=10, pady=5, sticky='w')

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg='#f0f0f0', fg='#333333', font=('Arial', 12), activebackground='#f0f0f0', activeforeground='#333333')
special_check.grid(row=4, columnspan=2, padx=10, pady=5, sticky='w')

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#007bff', fg='#ffffff', font=('Arial', 12), relief=tk.FLAT, activebackground='#0056b3')
generate_button.grid(row=5, columnspan=2, padx=10, pady=10)

password_label = tk.Label(root, text="Generated Password:", bg='#f0f0f0', fg='#333333', font=('Arial', 12))
password_label.grid(row=6, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=40, bg='#ffffff', fg='#333333', font=('Arial', 12), relief=tk.FLAT)
password_entry.grid(row=6, column=1, padx=10, pady=10)

# Set default length entry to 0 for random length
length_entry.insert(0, "0")  # User can enter 0 for random length

root.mainloop()
