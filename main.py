import tkinter as tk
from tkinter import font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_enter(e):
    e.widget.configure(bg="#4CAF50", fg="white")

def on_leave(e):
    e.widget.configure(bg="white", fg="#4CAF50")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="white")

entry_font = font.Font(family="Arial", size=20)
button_font = font.Font(family="Arial", size=14, weight="bold")

entry = tk.Entry(root, width=25, borderwidth=5, font=entry_font)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

# Create buttons
for button in buttons:
    text, row, column = button
    btn = tk.Button(root, text=text, padx=20, pady=10, font=button_font, bd=0,
                    command=lambda text=text: button_click(text))
    btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

clear_btn = tk.Button(root, text="C", padx=20, pady=10, font=button_font, bd=0, command=button_clear)
clear_btn.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
clear_btn.bind("<Enter>", on_enter)
clear_btn.bind("<Leave>", on_leave)

equal_btn = tk.Button(root, text="=", padx=20, pady=10, font=button_font, bd=0, command=button_equal)
equal_btn.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
equal_btn.bind("<Enter>", on_enter)
equal_btn.bind("<Leave>", on_leave)

# Configure grid
rows = 6
columns = 4
for row in range(rows):
    root.grid_rowconfigure(row, weight=1)
for column in range(columns):
    root.grid_columnconfigure(column, weight=1)

root.mainloop()
