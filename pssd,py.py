import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password based on random characters
def generate_password():
    input_chars = length_entry.get()
    
    if len(input_chars) < 4:
        messagebox.showerror("Error", "Input length should be at least 4 characters.")
        return
    
    # Generate password using the input characters (instead of numbers)
    password = ''.join(random.choice(input_chars) for _ in range(len(input_chars)))
    
    password_display.config(text=f"Generated Password: {password}")

# User Interface
root = tk.Tk()
root.title("Corporate Password Generator")
root.geometry("400x300")
root.config(bg="#f0f4f8")

# Labels
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#1a73e8", fg="white", pady=10)
title_label.pack(fill="x")

instruction_label = tk.Label(root, text="Enter any characters (min. 4) to create a password:", font=("Arial", 14), bg="#f0f4f8")
instruction_label.pack(pady=10)

# Entry for input characters
length_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid")
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#1a73e8", fg="white", relief="raised", command=generate_password)
generate_button.pack(pady=20)

# Display generated password
password_display = tk.Label(root, text="", font=("Courier", 14), fg="#333333", bg="#f0f4f8", pady=10)
password_display.pack()

# Corporate branding footer
footer_label = tk.Label(root, text="Your Secure Password Solution", font=("Arial", 10, "italic"), bg="#f0f4f8", fg="#666666")
footer_label.pack(side="bottom", pady=5)

# Start the Tkinter loop
root.mainloop()
