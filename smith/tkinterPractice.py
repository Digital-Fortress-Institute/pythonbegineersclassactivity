# from tkinter import *
# root = Tk()
# root.title("Simple Calculator")

# # define function

# def click(num):
#     current_text = e.get()
#     e.delete(0,END)
#     e.insert(0, str(current_text) + num)

# def equals():
#     displays=e.get()
#     e.delete(0,END)
#     mathss=int(eval(displays))
#     e.insert(0,str(mathss))

# def clear():
#     e.delete(0,END)

# # widget

# e = Entry(root, width=35,borderwidth=5)

# button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: click("1"))
# button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: click("2"))
# button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: click("3"))

# button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: click("4"))
# button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: click("5"))
# button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: click("6"))

# button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: click("7"))
# button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: click("8"))
# button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: click("9"))

# button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: click("0"))

# button_clear =  Button(root, text="C", padx=40, pady=20, command=lambda: clear())
# button_plus =  Button(root, text="+", padx=40, pady=85, command=lambda: click("+"))
# button_minus = Button(root, text="-", padx=40, pady=20, command=lambda: click("-"))
# button_divide =Button(root, text="/", padx=40, pady=20, command=lambda: click("/"))
# button_times = Button(root, text="x", padx=40, pady=20, command=lambda: click("*"))
# button_dot =   Button(root, text=".", padx=40, pady=20, command=lambda: click("."))

# button_equals =Button(root, text="=", padx=70, pady=20, command=lambda: equals())


# # grid

# e.grid(row=0, column=0, columnspan=3,rowspan=1,padx=10, pady=10)

# button_1.grid(row=2,column=0,rowspan=1,columnspan=1)
# button_2.grid(row=2,column=1,rowspan=1,columnspan=1)
# button_3.grid(row=2,column=2,rowspan=1,columnspan=1)

# button_4.grid(row=3,column=0,rowspan=1,columnspan=1)
# button_5.grid(row=3,column=1,rowspan=1,columnspan=1)
# button_6.grid(row=3,column=2,rowspan=1,columnspan=1)

# button_7.grid(row=4,column=0,rowspan=1,columnspan=1)
# button_8.grid(row=4,column=1,rowspan=1,columnspan=1)
# button_9.grid(row=4,column=2,rowspan=1,columnspan=1)

# button_0.grid(row=5,column=1,rowspan=1,columnspan=1)

# button_dot.grid(row=5,column=0,rowspan=1,columnspan=1)
# button_plus.grid(row=2,column=3,rowspan=3,columnspan=1)
# button_minus.grid(row=1,column=3,rowspan=1,columnspan=1)
# button_divide.grid(row=1,column=2,rowspan=1,columnspan=1)
# button_times.grid(row=1,column=1,rowspan=1,columnspan=1)
# button_clear.grid(row=1,column=0,rowspan=1,columnspan=1)

# button_equals.grid(row=5,column=2,columnspan=1,rowspan=1)



# root.mainloop() 























from tkinter import *
from PIL import ImageTk,Image


kel=Tk()
kel.geometry("200x200")
kel.title("gui class")
kel.iconbitmap("C:/Users/SMITH/Desktop/gitpython/WhatsApp Image 2024-02-27 at 20.12.41_7a838314.jpg")

my_img = ImageTk.PhotoImage(Image.open("C:/Users/SMITH/Desktop/gitpython/WhatsApp Image 2024-02-27 at 20.12.41_7a838314.jpg"))
my_lab = Label(kel,image=my_img, height=100,width=100).grid(row=1, column=1)

but1 = Button(kel, text="Exit", command=kel.quit).grid(row=0,column=0)


kel.mainloop()