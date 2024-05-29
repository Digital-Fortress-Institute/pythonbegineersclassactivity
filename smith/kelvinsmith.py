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

import tkinter as tk
window = tk.Tk()
window.title("Address Entry Form")
window.geometry("800x600")
# window.geometry("400x220")



frame=tk.Frame(master=window,height=160,width=400,relief="groove",borderwidth=5)
frame1=tk.Frame(master=window, width=380, height=50,background="red")

label1=tk.Label(text="First Name: ", master=frame)
label2=tk.Label(text="Last Name: ", master=frame)
label3=tk.Label(text="Address Line 1: ", master=frame)
label4=tk.Label(text="Address Line 2: ", master=frame)
label5=tk.Label(text="City: ", master=frame)
label6=tk.Label(text="State/Province: ", master=frame)
label7=tk.Label(text="Postal Code: ", master=frame)
label8=tk.Label(text="Country: ", master=frame)


entry1=tk.Entry(master=frame, width=50)
entry2=tk.Entry(master=frame, width=50)
entry3=tk.Entry(master=frame, width=50)
entry4=tk.Entry(master=frame, width=50)
entry5=tk.Entry(master=frame, width=50)
entry6=tk.Entry(master=frame, width=50)
entry7=tk.Entry(master=frame, width=50)
entry8=tk.Entry(master=frame, width=50)

button=tk.Button(master=frame1, text="Clear", height=1, width=6)
button1=tk.Button(master=frame1, text="Clear", height=1, width=6)

# Entry
label1.grid(row=0,column=0)
label2.grid(row=5, column=0)
label3.grid(row=10, column=0)
label4.grid(row=15, column=0)
label5.grid(row=20, column=0)
label6.grid(row=25, column=0)
label7.grid(row=30, column=0)
label8.grid(row=35, column=0)
# Entry
entry1.grid(row=0, column=5)
entry2.grid(row=5, column=5)
entry3.grid(row=10, column=5)
entry4.grid(row=15, column=5)
entry5.grid(row=20, column=5)
entry6.grid(row=25, column=5)
entry7.grid(row=30, column=5)
entry8.grid(row=35, column=5)
frame.grid()
frame1.grid(sticky="se")
button.grid()
button1.grid()


window.mainloop()