import tkinter as tk

# Function to update the input field when buttons are pressed
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.geometry('370x370')
root.title("Simple Calc")

# Create the entry widget to display expressions and results
entry = tk.Entry(root, width=8, font=("Montserrat", 24), relief="groove", highlightcolor='blue', justify='center')
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    'C', '0', '=', '+'
]

# Create buttons and place them in the grid
row = 1
col = 0
for button in buttons:
    action = lambda x=button: button_click(x) if x not in ('C', '=') else clear() if x == 'C' else evaluate()
    tk.Button(root, text=button, width=5, height=2, command=action, font=("Arial", 18)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
root.mainloop()
