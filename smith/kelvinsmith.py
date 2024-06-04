# 1.Write a Python program to find the common elements between two sets.
# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {1,2,3,4,50,60,70,8,9,10}

# print(set1 & set2)


# 2.Write a Python program to merge two sets without duplicates.
# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 | set2)


# 3.Write a Python program to find the elements that are present in the first set but not in the second set.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 - set2)



# 4.Write a Python program to find the elements that are present in either set but not in both.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 ^ set2)




# 5. Write a Python program to check if one set is a subset of another.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# sub_set = set2.issubset(set1)
# print(sub_set)



# 6. Write a Python program to check if one set is a superset of another.

# set1 = {1,2,3,4,5,6,8,9,10}
# set2 = {1,2,3,4,5,6,7,8,9,50,60,"mirror",8,9,10}
# super_set = set2.issuperset(set1)
# print(super_set)




# 7.Write a Python program to find the length of a set.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(len(set1))
# print(len(set2))






# 8.Write a Python program to check if an element is present in a set.


# set1 = {1,2,3,4,5,6,8,9,10}
# set2 = {1,2,3,4,5,6,7,8,9,50,60,"mirror",8,9,10}
# if "mirror" in set2:
#     print("true")
# else:
#     print("not there")





# 9.Write a Python program to check if two sets have no common elements.


# set1 = {3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror"}
# common = set1 & set2
# if common:
#     print("both sets have something in common")
# else:
#     print("both sets have nofacething in common")






# from tkinter import *
# import sqlite3
# def create_table():
#     tunde=sqlite3.connect(
#         "class.db"
#     )
#     myclass= tunde.cursor()
#     myclass.execute(
#         """CREATE TABLE IF NOT EXISTS prosper (
#         id INTERGER PRIMARY KEY AUTOINCREMENT,
#         email TEXT NOT NULL
#         pass TEXT NOT NULL
#         )
#         """
#     )
#     tunde.commit()
#     tunde.close()

# root =Tk()
# root.title("my GUI INterface")
# create_table()
# def myclick():
#     password = myinput1.get()
#     myemail = myinput.get()

#     result1 = Label(root, text=myemail)
#     result1.pack()
#     result2 = Label(root, text=password)
#     result2.pack()

# def savedata():
#     theemail = myinput.get()
#     thepassword = myinput1.get()

#     if theemail and thepassword:
#         myselect=sqlite3.connect("class.db")
#         myconn = myselect.cursor()
#         myconn.execute("SELECT * FROM prosper (email, password)")
# mylabel = Label(root, text = "Email")
# mylabel.pack()


# myinput = Entry(root, width=30)
# myinput.pack()

# mypass = Label(root, text="password")
# mypass.pack()

# myinput1 = Entry(root, width=30)
# # myinput1.grid(row=1, column=1)
# myinput1.pack()

# mybutton = Button(root, text= "submit", command=myclick)
# mybutton.pack()

# root.mainloop()







#GUI

# import tkinter as tk
# window = tk.Tk()
# window.title("Address Entry Form")
# window.geometry("800x600")
# # window.geometry("400x220")



# frame=tk.Frame(master=window,height=160,width=400,relief="groove",borderwidth=5)
# frame1=tk.Frame(master=window, width=380, height=50,background="red")

# label1=tk.Label(text="First Name: ", master=frame)
# label2=tk.Label(text="Last Name: ", master=frame)
# label3=tk.Label(text="Address Line 1: ", master=frame)
# label4=tk.Label(text="Address Line 2: ", master=frame)
# label5=tk.Label(text="City: ", master=frame)
# label6=tk.Label(text="State/Province: ", master=frame)
# label7=tk.Label(text="Postal Code: ", master=frame)
# label8=tk.Label(text="Country: ", master=frame)


# entry1=tk.Entry(master=frame, width=50)
# entry2=tk.Entry(master=frame, width=50)
# entry3=tk.Entry(master=frame, width=50)
# entry4=tk.Entry(master=frame, width=50)
# entry5=tk.Entry(master=frame, width=50)
# entry6=tk.Entry(master=frame, width=50)
# entry7=tk.Entry(master=frame, width=50)
# entry8=tk.Entry(master=frame, width=50)

# button=tk.Button(master=frame1, text="Clear", height=1, width=6)
# button1=tk.Button(master=frame1, text="Clear", height=1, width=6)

# # Entry
# label1.grid(row=0,column=0)
# label2.grid(row=5, column=0)
# label3.grid(row=10, column=0)
# label4.grid(row=15, column=0)
# label5.grid(row=20, column=0)
# label6.grid(row=25, column=0)
# label7.grid(row=30, column=0)
# label8.grid(row=35, column=0)
# # Entry
# entry1.grid(row=0, column=5)
# entry2.grid(row=5, column=5)
# entry3.grid(row=10, column=5)
# entry4.grid(row=15, column=5)
# entry5.grid(row=20, column=5)
# entry6.grid(row=25, column=5)
# entry7.grid(row=30, column=5)
# entry8.grid(row=35, column=5)
# frame.grid()
# frame1.grid(sticky="se")
# button.grid()
# button1.grid()


# window.mainloop()

















# import tkinter as tk

# # Create the main application window
# root = tk.Tk()
# root.title("Simple Calculator")

# # Create an entry widget
# entry = tk.Entry(root, width=35, borderwidth=5)
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # Define button click function
# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, current + str(number))

# # Define clear function
# def button_clear():
#     entry.delete(0, tk.END)

# # Define equal function
# def button_equal():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")

# # Define button creation function
# def create_button(text, row, col, command=None):
#     return tk.Button(root, text=text, padx=20, pady=20, command=command).grid(row=row, column=col)

# # Create number buttons
# button_1 = create_button('1', 3, 0, command=lambda: button_click(1))
# button_2 = create_button('2', 3, 1, command=lambda: button_click(2))
# button_3 = create_button('3', 3, 2, command=lambda: button_click(3))

# button_4 = create_button('4', 2, 0, command=lambda: button_click(4))
# button_5 = create_button('5', 2, 1, command=lambda: button_click(5))
# button_6 = create_button('6', 2, 2, command=lambda: button_click(6))

# button_7 = create_button('7', 1, 0, command=lambda: button_click(7))
# button_8 = create_button('8', 1, 1, command=lambda: button_click(8))
# button_9 = create_button('9', 1, 2, command=lambda: button_click(9))

# button_0 = create_button('0', 4, 0, command=lambda: button_click(0))

# # Create operator buttons
# button_add = create_button('+', 4, 1, command=lambda: button_click('+'))
# button_equal = create_button('=', 4, 2, command=button_equal)
# button_clear = create_button('C', 4, 3, command=button_clear)

# button_subtract = create_button('-', 3, 3, command=lambda: button_click('-'))
# button_multiply = create_button('', 2, 3, command=lambda: button_click(''))
# button_divide = create_button('/', 1, 3, command=lambda: button_click('/'))

# # Run the application
# root.mainloop()







import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox



root = tk.Tk()
root.title("Simple Form")
root.geometry("500x500")


image = Image.open("C:/Users/SMITH/Desktop/dcmi/spanels.png")
photo=ImageTk.PhotoImage(image)

lab = tk.Label(master=root, height=80, width=100,image=photo)
lab.pack()


fn = tk.StringVar()
ln = tk.StringVar()
dob = tk.StringVar()
var = tk.StringVar()
var_cb=tk.StringVar()



def exit():
    root.destroy()

def printt():
    fname = fn.get()
    lname = ln.get()
    dobirth = dob.get()
    dmenu = var.get()
    print(f"your name is: {fname} {lname}")
    print(f"your date of birth is: {dobirth}")
    print(f"and your country is: {dmenu}")


label1 = tk.Label(master=root, text="Registration Form", relief=tk.SOLID, width=20, font=("arial",19,"bold"))
label1.place(x=90, y=100)

label2 = tk.Label(master=root, text="First Name: ",width=15, font=("arial",10,"bold"))
label2.place(x=40, y=170)
label3 = tk.Label(master=root, text="Last Name: ",width=15, font=("arial",10,"bold"))
label3.place(x=40, y=220)
label4 = tk.Label(master=root, text="DOB: ",width=15, font=("arial",10,"bold"))
label4.place(x=40, y=260)
label5 = tk.Label(master=root, text="Country: ",width=15, font=("arial",10,"bold"))
label5.place(x=50, y=360)
label6 = tk.Label(master=root, text="Prog Lang :",width=15, font=("arial",10,"bold"))
label6.place(x=40, y=290)
label7 = tk.Label(master=root, text="Gender: ",width=15, font=("arial",10,"bold"))
label7.place(x=40, y=325)



cb = tk.Checkbutton(master=root, text="Java", variable=var_cb)
cb.place(x=165, y=290)


entry1 = tk.Entry(master=root, width=24,relief="groove", borderwidth=2, cursor="xterm", textvariable=fn)
entry1.place(x=170, y=170)
entry2 = tk.Entry(master=root, width=24, borderwidth=2,relief="groove", cursor="xterm", textvariable=ln)
entry2.place(x=170, y=220)
entry3 = tk.Entry(master=root, textvar=dob, width=24, borderwidth=2,relief="groove", cursor="xterm")
entry3.place(x=170, y=265)

list1 = ["Nepal","" "Nigeria", "Cameroon", "Ghana"]
droplist = tk.OptionMenu(root,var,*list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=180, y=360)



button1 = tk.Button(master=root, text="Login", width=12, background="brown", foreground="white", command=printt)
button1.place(x=150,y=400)
button2 = tk.Button(master=root, text="Quit", width=12, background="brown", foreground="white", command=exit)
button2.place(x=280,y=400)


root.mainloop()
