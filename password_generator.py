import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length < 1:
        messagebox.showerror("Invalid input", "Password length should be at least 1.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    result.set(password)

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create and place the widgets
tk.Label(root, text="Password Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

result = tk.StringVar()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=result, state='readonly', width=30).pack(pady=5)

# Run the application
root.mainloop()
