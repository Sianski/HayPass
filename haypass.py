import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Dictionary for translations
translations = {
    "en": {  # English
        "error_title": "Error",
        "error_message": "Please select at least one character type.",
        "copy_title": "Copied",
        "copy_message": "Password copied to clipboard!",
        "no_password": "No password to copy.",
        "password_length": "Password Length (leave empty for random):",
        "include_upper": "Include Uppercase Letters",
        "include_lower": "Include Lowercase Letters",
        "include_digits": "Include Digits",
        "include_special": "Include Special Characters",
        "generate_password": "Generate Password",
        "copy_password": "Copy Password",
        "generated_password": "Generated Password:",
        "language_menu": "Change Language"
    },
    "pl": {  # Polish
        "error_title": "Błąd",
        "error_message": "Wybierz co najmniej jeden typ znaku.",
        "copy_title": "Skopiowano",
        "copy_message": "Hasło skopiowane do schowka!",
        "no_password": "Brak hasła do skopiowania.",
        "password_length": "Długość hasła (pozostaw puste dla losowej):",
        "include_upper": "Uwzględnij wielkie litery",
        "include_lower": "Uwzględnij małe litery",
        "include_digits": "Uwzględnij cyfry",
        "include_special": "Uwzględnij znaki specjalne",
        "generate_password": "Generuj hasło",
        "copy_password": "Skopiuj hasło",
        "generated_password": "Wygenerowane hasło:",
        "language_menu": "Zmień język"
    },
    "es": {  # Spanish
        "error_title": "Error",
        "error_message": "Selecciona al menos un tipo de carácter.",
        "copy_title": "Copiado",
        "copy_message": "¡Contraseña copiada al portapapeles!",
        "no_password": "No hay contraseña para copiar.",
        "password_length": "Longitud de la contraseña (dejar vacío para aleatorio):",
        "include_upper": "Incluir letras mayúsculas",
        "include_lower": "Incluir letras minúsculas",
        "include_digits": "Incluir dígitos",
        "include_special": "Incluir caracteres especiales",
        "generate_password": "Generar contraseña",
        "copy_password": "Copiar contraseña",
        "generated_password": "Contraseña generada:",
        "language_menu": "Cambiar idioma"
    },
    "de": {  # German
        "error_title": "Fehler",
        "error_message": "Bitte wählen Sie mindestens einen Zeichentyp aus.",
        "copy_title": "Kopiert",
        "copy_message": "Passwort in die Zwischenablage kopiert!",
        "no_password": "Kein Passwort zum Kopieren vorhanden.",
        "password_length": "Passwortlänge (leer lassen für zufällig):",
        "include_upper": "Großbuchstaben einbeziehen",
        "include_lower": "Kleinbuchstaben einbeziehen",
        "include_digits": "Ziffern einbeziehen",
        "include_special": "Sonderzeichen einbeziehen",
        "generate_password": "Passwort generieren",
        "copy_password": "Passwort kopieren",
        "generated_password": "Generiertes Passwort:",
        "language_menu": "Sprache ändern"
    },
    "fr": {  # French
        "error_title": "Erreur",
        "error_message": "Veuillez sélectionner au moins un type de caractère.",
        "copy_title": "Copié",
        "copy_message": "Mot de passe copié dans le presse-papiers !",
        "no_password": "Aucun mot de passe à copier.",
        "password_length": "Longueur du mot de passe (laisser vide pour aléatoire) :",
        "include_upper": "Inclure les lettres majuscules",
        "include_lower": "Inclure les lettres minuscules",
        "include_digits": "Inclure les chiffres",
        "include_special": "Inclure les caractères spéciaux",
        "generate_password": "Générer un mot de passe",
        "copy_password": "Copier le mot de passe",
        "generated_password": "Mot de passe généré :",
        "language_menu": "Changer de langue"
    }
}

# Variable to store the current language
language = "en"

def update_language(new_language):
    """Update the language in the interface."""
    global language
    language = new_language

    # Update text in the interface
    length_label.config(text=translations[language]["password_length"])
    upper_check.config(text=translations[language]["include_upper"])
    lower_check.config(text=translations[language]["include_lower"])
    digits_check.config(text=translations[language]["include_digits"])
    special_check.config(text=translations[language]["include_special"])
    generate_button.config(text=translations[language]["generate_password"])
    copy_button.config(text=translations[language]["copy_password"])
    password_label.config(text=translations[language]["generated_password"])
    language_menu_button.config(text=translations[language]["language_menu"])
    copy_message_label.config(text="")  # Reset message

def generate_password():
    length = length_var.get()
    if not length:  # Check if the password length field is empty
        length = random.randint(16, 20)
    else:
        length = int(length)  # Convert to integer

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
        messagebox.showerror(translations[language]["error_title"], translations[language]["error_message"])
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    copy_message_label.config(text="")  # Reset message after generating a new password

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)  # Copy password to clipboard
        copy_message_label.config(text=translations[language]["copy_message"])  # Display message
    else:
        copy_message_label.config(text=translations[language]["no_password"])  # Information when there is no password

def show_language_menu(event=None):
    """Display the menu with country names for language selection."""
    if event:
        language_menu.post(event.x_root, event.y_root)
    else:
        language_menu.post(language_menu_button.winfo_rootx(), language_menu_button.winfo_rooty() + language_menu_button.winfo_height())

def change_language(new_language):
    """Change the language when clicking on the country name."""
    update_language(new_language)
    language_menu.unpost()  # Hide the menu after selecting the language

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg='#f0f0f0')

# Language selection menu
language_menu = tk.Menu(root, tearoff=False)
for lang in translations:
    language_menu.add_command(label=translations[lang]["language_menu"], command=lambda l=lang: change_language(l))

# Button for changing language
language_menu_button = tk.Menubutton(root, text=translations[language]["language_menu"], bg='#f0f0f0', fg='#333333', font=('Montserrat', 12), relief=tk.FLAT)
language_menu_button.config(menu=language_menu)  # Set the menu option using config
language_menu_button.grid(row=5, column=0, padx=10, pady=10, sticky='w')
language_menu_button.bind("<Button-1>", show_language_menu)  # Show menu on left mouse click

# Remaining part of the code
length_var = tk.StringVar()  # Change to StringVar to handle empty field
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

length_label = tk.Label(root, text=translations[language]["password_length"], bg='#f0f0f0', fg='#333333', font=('Montserrat', 12))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, textvariable=length_var, bg='#ffffff', fg='#333333', font=('Montserrat', 12), relief=tk.FLAT)
length_entry.grid(row=0, column=1, padx=10, pady=10)

upper_check = tk.Checkbutton(root, text=translations[language]["include_upper"], variable=upper_var, bg='#f0f0f0', fg='#333333', font=('Montserrat', 12), activebackground='#f0f0f0', activeforeground='#333333')
upper_check.grid(row=1, columnspan=2, padx=10, pady=5, sticky='w')

lower_check = tk.Checkbutton(root, text=translations[language]["include_lower"], variable=lower_var, bg='#f0f0f0', fg='#333333', font=('Montserrat', 12), activebackground='#f0f0f0', activeforeground='#333333')
lower_check.grid(row=2, columnspan=2, padx=10, pady=5, sticky='w')

digits_check = tk.Checkbutton(root, text=translations[language]["include_digits"], variable=digits_var, bg='#f0f0f0', fg='#333333', font=('Montserrat', 12), activebackground='#f0f0f0', activeforeground='#333333')
digits_check.grid(row=3, columnspan=2, padx=10, pady=5, sticky='w')

special_check = tk.Checkbutton(root, text=translations[language]["include_special"], variable=special_var, bg='#f0f0f0', fg='#333333', font=('Montserrat', 12), activebackground='#f0f0f0', activeforeground='#333333')
special_check.grid(row=4, columnspan=2, padx=10, pady=5, sticky='w')

generate_button = tk.Button(root, text=translations[language]["generate_password"], command=generate_password, bg='#007bff', fg='#ffffff', font=('Montserrat', 12), relief=tk.FLAT, activebackground='#0056b3')
generate_button.grid(row=5, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text=translations[language]["copy_password"], command=copy_password, bg='#28a745', fg='#ffffff', font=('Montserrat', 12), relief=tk.FLAT, activebackground='#218838')
copy_button.grid(row=5, column=1, padx=10, pady=10, sticky='e')

password_label = tk.Label(root, text=translations[language]["generated_password"], bg='#f0f0f0', fg='#333333', font=('Montserrat', 12))
password_label.grid(row=6, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=40, bg='#ffffff', fg='#333333', font=('Montserrat', 12), relief=tk.FLAT)
password_entry.grid(row=6, column=1, padx=10, pady=10)

# Label to display the copied password message
copy_message_label = tk.Label(root, text="", bg='#f0f0f0', fg='#28a745', font=('Montserrat', 12))
copy_message_label.grid(row=7, columnspan=2, padx=10, pady=10)

root.mainloop()