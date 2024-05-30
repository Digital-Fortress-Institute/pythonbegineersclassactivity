# GUI

# import tkinter as tk

# window = tk.Tk()
# window.title("test")
# window.geometry("500x300")
# def showmybutton():
#     mybutton = entry.get()
#     print(mybutton)

# def showmytext():
#     mytext = text_box.get("1.0", tk.END)
#     print(mytext)


# frame = tk.Frame()
# greeting = tk.Label(text="name",
#                     foreground = "black",
#                     background = "white",
#                     width = 10,
#                     height = 2
#                     )

# button = tk.Button(text="Enter",
#                    command=showmytext,
#                     fg = "white",
#                     bg = "black",
#                     width = 10,
#                     height = 2
#                     )

# entry = tk.Entry(


#                     fg = "black",
#                     bg = "white",
#                     width = 10,
#                     )

# text_box = tk.Text(

#     width = 20
# )


# frame.pack()
# greeting.pack()
# entry.pack(pady=10)
# button.pack(pady=10)
# text_box.pack()

# window.mainloop()



# import tkinter as tk

# window=tk.Tk()
# window.title("test")

# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text="i am in frame A")
# label_b = tk.Label(master=frame_b,text="i am in frame B")

# frame_a.pack()
# frame_b.pack()
# label_a.pack()
# label_b.pack()
# window.mainloop()



# import tkinter as tk
# window=tk.Tk()
# window.title("whitecake")
# window.geometry("600x400")
# window = tk.Tk()

# label_name = tk.Label(master=window, text= "hello world")
# label_name.pack()

# entry_name = tk.Entry(master=window, show="*")
# entry_name.pack()

# window.mainloop()




# import tkinter as tk
# window=tk.Tk()

# frame1 = tk.Frame(master=window,width=100,height=100,bg="red")
# frame2 = tk.Frame(master=window,width=50,height=50,bg="yellow")
# frame3 = tk.Frame(master=window,width=25,height=25,bg="blue")
# label = tk.Label(master=frame1, width=5, height=5,text="hello", bg="white")
# label1 = tk.Label(master=frame2, width=5, height=5,text="click", bg="white")


# frame1.pack(fill=tk.BOTH, side="right",expand=True)
# label.place(x=0, y=0)
# label.pack(side="right")
# label1.place(x=75, y=75)
# frame2.pack(fill=tk.BOTH, side="right",expand=True)
# frame3.pack(fill=tk.BOTH, side="right",expand=True)

# window.mainloop()



# import tkinter as tk
# window=tk.Tk()
# window.title("user entry")
# window.geometry("600x400")
# def enter():
#     name = entry1.get()
#     pass1 = entry2.get()

#     result = tk.Label(text=name)
#     result.grid(row=8, column=1)
#     result1 = tk.Label(text=pass1)
#     result1.grid(row=10, column=1)

# frame = tk.Frame(master=window, width=300, height=100)
# label1 = tk.Label(master=frame, text="name")
# label2 = tk.Label(master=frame, text="password")
# entry1= tk.Entry(master=frame)
# entry2= tk.Entry(master=frame, show="*")
# button1=tk.Button(master=frame, text="Enter", command=enter)

# frame.grid(row=1,column=1)
# label1.grid(row=1, column=1)
# entry1.grid(row=1, column=5)
# label2.grid(row=5, column=1)
# entry2.grid(row=5, column=5)
# button1.grid(row=10, column=5)


# window.mainloop()


















# number adder




# import tkinter as tk
# window=tk.Tk()
# window.geometry("400x200")
# window.title("try")

# def clickadd():
#     value = int(label["text"])
#     label["text"] = value + 1

# def clicksub():
#     value = int(label["text"])
#     label["text"] = value - 1
    

# button1=tk.Button(master=window, 
#                   text="adder", 
#                   height=2, 
#                   width=4,
#                   padx=4,
#                   pady=4, 
#                   command=clickadd)
# button2=tk.Button(master=window, 
#                   text="subber", 
#                   height=2, 
#                   width=4, 
#                   padx=4, 
#                   pady=4,
#                   command=clicksub)
# # button.bind("<Button-1>", clickme)
# label= tk.Label(master=window, text="0")


# button1.grid(row=0, column=0)
# label.grid(row=0, column=2)
# button2.grid(row=0, column=4)

# window.mainloop()





# temperature



# import tkinter as tk
# window = tk.Tk()
# window.geometry("300x200")
# window.title("Temperature converter")









# def fah():

#     getfah = entry1.get()
#     getfah1 = int(getfah)
#     entry2.delete(0, tk.END)
#     answer1 = getfah1*1.8+32
#     entry2.insert(0, f"Celcius to fahrenheit is: {int(answer1)}")

# def cel():
#     getcel = int(entry1.get())
#     entry2.delete(0,tk.END)
#     answer2 = int((getcel - 32)/1.8)
#     entry2.insert(0, f"Fahrenheit to Celcius is: {answer2}")

# def clear():
#     entry1.delete(0,tk.END)
#     entry2.delete(0,tk.END)
    
# def exit():
#     window.destroy()


# label = tk.Label(window, text="Convert Temperature", relief="sunken", font=("aeriel",16,"bold"), bg="red",fg="white")

# entry1 = tk.Entry(master=window, relief=tk.RAISED, width=15)
# entry2 = tk.Entry(master=window, text="Answer: ", width=45)


# buttonfah = tk.Button(master=window,text="to Fahrenheit", command=fah)
# buttoncel = tk.Button(master=window, text="to Celcius", command=cel)
# buttonclear = tk.Button(master=window,text="Clear", command=clear)
# buttonexit = tk.Button(master=window,text="Exit", command=exit)




# # display
# label.place(x=40,y=1)
# buttonfah.place(x=205,y=80)
# buttoncel.place(x=100,y=80)
# buttonclear.place(x=10,y=80)
# buttonexit.place(x=130,y=150)
# entry1.place(x=100,y=40)
# entry2.place(x=10,y=120)


# window.mainloop()


















# colour changer


# import tkinter as tk
# import random
# smith=tk.Tk()
# smith.geometry("200x100")
# smith.title("colour change")

# colours = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
# colour_index = 0

# def click():
#     global colours
#     button.configure(bg=random.choice(colours))

# button = tk.Button(master=smith, relief=tk.GROOVE,text="Click me", command=click)
# button.pack()

# smith.mainloop()






from tkinter import *
from PIL import Image, ImageTk
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
