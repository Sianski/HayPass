# Random Password Generator

## Overview

The **Random Password Generator** is a Python application designed to create secure passwords tailored to user preferences. It features a user-friendly graphical interface built with Tkinter and supports multiple languages, making it accessible for a diverse audience.

## Features

- **Password Generation**: Create random passwords based on user-defined criteria.
- **Customizable Options**:
  - Specify password length (leave blank for a random length between 16 and 20 characters).
  - Choose to include or exclude uppercase letters, lowercase letters, digits, and special characters.
- **Multi-Language Support**: Available in:
  - English
  - Polish
  - Spanish
  - German
  - French
- **Clipboard Functionality**: Easily copy the generated password to your clipboard for quick use.

## Installation

To run this application, ensure you have Python installed. You will also need the `pyperclip` library for clipboard functionality. Install it using pip:

```bash
pip install pyperclip
```

## Usage Instructions

1. **Launch the Application**: Run the Python script to open the GUI.
2. **Set Password Length**: Enter a desired length for the password or leave it empty for a random length.
3. **Select Character Types**: Check the boxes to include uppercase letters, lowercase letters, digits, and/or special characters.
4. **Generate Password**: Click the "Generate Password" button to create a password based on your selections.
5. **Copy Password**: Click the "Copy Password" button to copy the generated password to your clipboard.

## Code Structure

The application consists of several key components:

- **Translations**: A dictionary that holds the text for different languages.
- **Functions**:
  - `update_language(new_language)`: Updates the interface text based on the selected language.
  - `generate_password()`: Generates a password according to user preferences.
  - `copy_password()`: Copies the generated password to the clipboard.
  - `show_language_menu(event)`: Displays the language selection menu.
  - `change_language(new_language)`: Changes the application language.

## Example Code Snippet

Here’s a brief example of the password generation function:

```python
def generate_password():
    length = length_var.get()
    if not length:
        length = random.randint(16, 20)
    else:
        length = int(length)

    char_pool = ""
    if upper_var.get():
        char_pool += string.ascii_uppercase
    if lower_var.get():
        char_pool += string.ascii_lowercase
    if digits_var.get():
        char_pool += string.digits
    if special_var.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror(translations[language]["error_title"], translations[language]["error_message"])
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
```

## Conclusion

The **Random Password Generator** is a straightforward yet powerful tool for creating secure passwords. With its intuitive interface and multilingual support, it caters to a wide range of users. Contributions and suggestions for improvements are always welcome!
