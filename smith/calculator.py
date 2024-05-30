# import tkinter as tk

# smith=tk.Tk()
# smith.geometry("320x500")
# smith.title("colour change")

# def createbutton(text, row, column, command=None ):
#     return tk.Button(smith, text=text, padx=20,pady=20, command=command).grid(row=row,column=column)

# def  click(num):
#     currentnumber = entry.get()
#     entry.delete(0,tk.END)
#     entry.insert(0, currentnumber + str(num))

# def clear():
#     entry.delete(0,tk.END)

# def equals():
#     try:
#         result = eval(entry.get())
#         entry.delete(0,tk.END)
#         entry.insert(0,str(result))
#     except:
#         entry.delete(0,tk.END)
#         entry.insert(0,"Error")
# # frame = tk.Frame(master=smith, height=10, bg="red")
# # frame.pack()
# entry= tk.Entry(master=smith,width=50, )
# entry.grid(row=1,column=1)

# button7= createbutton("7",1,2,command=lambda: click(7))
# button8= createbutton("8",2,2,command=lambda: click(8))
# button7= createbutton("7",1,2,command=lambda: click(7))
# button4= createbutton("4",2,2,command=lambda: click(4))
# button5= createbutton("5",1,2,command=lambda: click(5))
# button6= createbutton("6",2,2,command=lambda: click(6))
# button1= createbutton("1",1,2,command=lambda: click(1))
# button2= createbutton("2",2,2,command=lambda: click(2))
# button3= createbutton("3",2,2,command=lambda: click(3))



# buttonplus= createbutton("+",3,2,command=lambda: click("+"))
# buttoneq= createbutton("=",4,2,command=lambda: equals())

# smith.mainloop()

























import tkinter as tk


def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set(expression)


def button_equal():
    global expression
    try:
        result = str(eval(expression))  
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")

expression = ""


input_text = tk.StringVar()

input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="black", fg="white", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = tk.Button(btns_frame, text="C", fg="white", width=32, height=3, bd=0, bg="orange", cursor="hand2", command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

seven = tk.Button(btns_frame, text="7", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = tk.Button(btns_frame, text="8", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = tk.Button(btns_frame, text="9", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

four = tk.Button(btns_frame, text="4", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = tk.Button(btns_frame, text="5", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = tk.Button(btns_frame, text="6", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

one = tk.Button(btns_frame, text="1", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = tk.Button(btns_frame, text="2", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = tk.Button(btns_frame, text="3", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

zero = tk.Button(btns_frame, text="0", fg="white", width=21, height=3, bd=0, bg="black", cursor="hand2", command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="blue", cursor="hand2", command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()