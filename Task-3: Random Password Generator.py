import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please enable at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# GUI setup
root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

letters_var = tk.BooleanVar()
letters_var.set(True)
letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

numbers_var = tk.BooleanVar()
numbers_var.set(True)
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_var.set(True)
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
