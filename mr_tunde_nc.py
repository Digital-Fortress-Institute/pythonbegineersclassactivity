from tkinter import *

root = Tk()
root.title("Simple Calculator")

v = Entry(root, width=35, borderwidth=5)
v.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

numbers = []
operations = []


def button_click(number):
    current = v.get()
    v.delete(0, END)
    v.insert(0, str(current) + str(number))


def button_clear():
    v.delete(0, END)
    numbers.clear()
    operations.clear()


def button_add():
    first_number = v.get()
    numbers.append(int(first_number))
    operations.append("addition")
    v.delete(0, END)


def button_subtract():
    first_number = v.get()
    numbers.append(int(first_number))
    operations.append("subtraction")
    v.delete(0, END)


def button_multiply():
    first_number = v.get()
    numbers.append(int(first_number))
    operations.append("multiplication")
    v.delete(0, END)


def button_divide():
    first_number = v.get()
    numbers.append(int(first_number))
    operations.append("division")
    v.delete(0, END)


def button_equal():
    second_number = v.get()
    numbers.append(int(second_number))
    v.delete(0, END)

    result = numbers[0]
    for i in range(1, len(numbers)):
        if operations[i - 1] == "addition":
            result += numbers[i]
        elif operations[i - 1] == "subtraction":
            result -= numbers[i]
        elif operations[i - 1] == "multiplication":
            result *= numbers[i]
        elif operations[i - 1] == "division":
            result /= numbers[i]

    v.insert(0, result)
    numbers.clear()
    operations.clear()


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()