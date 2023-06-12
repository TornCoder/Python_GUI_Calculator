import tkinter as tk
# Function to perform the calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# Function to add a digit or operator to the entry field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
# Create the main window
window = tk.Tk()
window.title("Calculator")
# Create the entry field
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)
# Create the number buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = tk.Button(window, text=buttons[i][j], width=5, command=lambda value=buttons[i][j]: button_click(value))
        button.grid(row=i+1, column=j)
# Create the equal button
equal_button = tk.Button(window, text='=', width=5, command=calculate)
equal_button.grid(row=len(buttons)+1, column=0, columnspan=4)
# Run the main loop
window.mainloop()
