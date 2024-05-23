# mySet = {"Blue", "Red", "Pink"}
# set2 = {"Red", "white", "purple"}

# set1= {1, 2, 3, 4}
# set2={2,3,6,8}
# print(set1)

     

# set1= {"green", "blue", "red"}
# set2= {"purple", "blue", "red"}

# difference= (set1|set2)
# print(difference)

# my_set = {1, 2, 3, 4}
# print(element_in_set(my_set, 2)) # prints True
# print(element_in_set(my_set, 5)) # prints False


# LAMBDA, ANONYMOUS FUNCTION
# X = 12
# myx = lambda y : y * y 
# print(myx(X))


# FILTER FUNCTION
# x = [10, 20, 30, 40, 75, 25, 53]
# myx = list(filter(lambda y: y % 5 == 0, x))
# print(myx)


# # MAP FUNCTION
# x = [10, 20, 30, 40, 75, 25, 53]
# myx = list(map(lambda y: y % 5 == 0, x))
# print(myx)



# DATABASE MANAGEMENT

import sqlite3
from tkinter import *

prosper = sqlite3.connect("class.db") 

myclass=prosper.cursor()
myclass1 ="""
    CREATE TABLE IF NOT EXISTS 
    classTable(
    firstName TEXT, 
    secondname TEXT, 
    date TEXT,
    gender TEXT,
    address TEXT,
    status TEXT
)
"""

myclass.execute(myclass1)
prosper.commit()
# prosper.close()

# def myclick():
#     result = []
#     firstName= entry1.get()
#     secondName= entry2.get()
#     Date= entry3.get()
#     address=addrressEntry.get()
#     if var1.get() or var2.get():
#         gender = result.append(" ")
#     if var3.get() or var4.get():
#         status = result.append(" ")


#     # result1= Label(root, text=firstName)
#     # result1.pack()
#     # result2= Label(root, text=secondName)
#     # result2.pack()
#     # result3=Label(root, Date)
#     # result3.pack()
#     # result4= Label(root, text=gender)
#     # result4.pack()
#     # result5= Label(root, text=address)
#     # result5.pack()
#     # result6= Label(root, text=status)
#     # result6.pack()
    
#     c1=(firstName, secondName, Date, gender, address, status)
#     myclassinsert = """INSERT INTO classTable(firstName, secondname, date, gender, status)
#     VALUES(?,?,?,?,?) """
    
#     myclass.execute(myclassinsert, c1)
#     prosper.commit()

def saveData():
    result = []
    result_label.config(text="Selected options: "+", ".join(result))
    firstName= entry1.get()
    secondName= entry2.get()
    Date= entry3.get()
    address=addrressEntry.get()
    if var1.get() or var2.get():
        gender = result.append(var1 or var2)
    if var3.get() or var4.get():
        status = result.append(var3 or var4)

    c1=(firstName, secondName, Date, gender, address, status)
    myclassinsert = """INSERT INTO classTable(firstName, secondname, date, gender, address, status)
    VALUES(?,?,?,?,?,?) """
    
    myclass.execute(myclassinsert, c1)
    prosper.commit()


root= Tk()
root.geometry('600x400')

root.title('DECISION CARD FORM')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

label = Label(root, text="FIRST NAME: ")
label.grid(row=0, column=0)
entry1 = Entry ( root, width='20')
entry1.grid(row=0, column=1 )

label = Label(root, text="SECOND NAME: ")
label.grid(row=0, column=2)
entry2 = Entry ( root, width='20')
entry2.grid(row=0, column=3)


date = Label(root, text='Date: ')
date.grid(row= 2, column=0, pady='10' )
entry3 = Entry ( root, width='30')
entry3.grid(row=2, column=1 )

gender = Label(root, text='Gender:')
gender.grid(row=3, column=0)
gender = Checkbutton(text='MALE', variable=var1)
gender.grid(row=3, column=1, )
gender = Checkbutton(text='FEMALE', variable=var2)
gender.grid(row=3, column=2, )

address = Label(root, text="HOME ADDRESS: ")
address.grid(row=4, column=0, pady='10')
addrressEntry = Entry ( root, width='40')
addrressEntry.grid(row=4, column=1)

maritalStatus = Label(root, text='Marital Status:')
maritalStatus.grid(row=5, column=0)
maritalStatus = Checkbutton(text='Married', variable=var3)
maritalStatus.grid(row=5, column=1, )
maritalStatus = Checkbutton(text='Single', variable=var4)
maritalStatus.grid(row=5, column=2, )

myButton= Button(root, text='submit', command=saveData)
myButton.grid(row=6, column=0, padx=20, )
result_label=Label(root, text="")
result_label.grid(row=6, column=0)

# label.pack()
root.mainloop()


    
