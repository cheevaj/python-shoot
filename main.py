import tkinter as tk
def on_click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget to display input and output
entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and position the buttons
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda key=button: on_click(key)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
