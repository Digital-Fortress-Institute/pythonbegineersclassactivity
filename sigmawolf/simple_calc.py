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


# Function to delete the last character
def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])


# Function to convert current entry to percentage
def percentage():
    try:
        current_text = entry.get()
        result = eval(current_text) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Create the main window
root = tk.Tk()
root.geometry('380x380')
root.title("Simple Calc")

# Create the entry widget to display expressions and results
entry = tk.Entry(root, width=16, font=("Montserrat", 24), borderwidth=0, relief="groove", justify='center')
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'Del', '0', '=', '+',
    '•', 'C', '%', '•'
]

# Create buttons and place them in the grid
row = 1
col = 0
for button in buttons:
    if button == 'C':
        action = clear
    elif button == '=':
        action = evaluate
    elif button == 'Del':
        action = delete
    elif button == '%':
        action = percentage
    else:
        action = lambda x=button: button_click(x)  # To call the button_click function with the button text as an argument when the button is pressed.

    tk.Button(root, text=button, width=5, height=2, command=action, font=("Montserrat", 16)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
root.mainloop()
