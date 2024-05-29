import tkinter as tk

smith=tk.Tk()
smith.geometry("200x100")
smith.title("colour change")

def createbutton(text, row, column, command=None ):
    return tk.Button(smith, text=text, padx=20,pady=20, command=command).grid(row=row,column=column)

def  click(num):
    currentnumber = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, currentnumber + str(num))

def clear():
    entry.delete(0,tk.END)

def equals():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

entry= tk.Entry(master=smith)
entry.grid(row=1,column=1)

button5= createbutton("5",1,2,command=lambda: click(5))
button3= createbutton("3",2,2,command=lambda: click(3))
buttonplus= createbutton("+",3,2,command=lambda: click("+"))
buttoneq= createbutton("=",4,2,command=lambda: equals())

smith.mainloop()
