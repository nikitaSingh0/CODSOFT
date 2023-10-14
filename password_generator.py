import tkinter as tk
import random

def generate_password():
    length = length_entry.get()
    if length.isdigit():
        length = int(length)
        if 6 <= length <= 64:
            password = ""
            for _ in range(length):
                num = random.randint(33, 126)
                password += chr(num)
            password_display.config(text=password, fg="green")
        elif length < 6:
            password_display.config(text="Password length should be at least 6.", fg="red")
        else:
            password_display.config(text="Password length should not exceed 64.", fg="red")
    else:
        password_display.config(text="Invalid input, please enter a number.", fg="red")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")  
root.resizable(0,0)

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18,"underline","bold"))
title_label.pack(pady=10)
length_label = tk.Label(root, text="Enter length of the password (6-64):", font=("Comfortaa", 12,"bold"))
length_label.pack(pady=10)
length_entry = tk.Entry(root, font=("Helvetica", 16))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Georgia", 18), bg="blue", fg="white")
generate_button.pack(pady=10)

password_display = tk.Label(root, text="", font=("Courier New", 20,"bold"), wraplength=300)
password_display.pack(pady=10)

root.mainloop()
