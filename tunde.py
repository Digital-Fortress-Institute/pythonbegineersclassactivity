# pin = 1234
# card_number=8659036754
# balance = 0


# print('Welcome to Digital Fortress Micro Finance Bank')
# card_pin=int(input('Please enter your pin  \n'))
# if card_pin == pin:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# mycard_number=int(input('Please enter your card number  \n'))
# if mycard_number == card_number:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# user =input('Enter your name')
# print(f'Welcome Mr/Mrs/Miss {user} you current balance is {balance}')
# newbalance = False
# while True:
#     mychoice = input('''
#             b to check balance
#             d to deposit
#             w to withdraw
#             q to quit
#     ''')
#     if mychoice == 'b':
#         print(balance)
# =======
# print('Welcome to Digital Fortress Micro Finance Bank')
# card_pin=int(input('Please enter your pin  \n'))
# if card_pin == pin:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# mycard_number=int(input('Please enter your card number  \n'))
# if mycard_number == card_number:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# user =input('Enter your name')
# print(f'Welcome Mr/Mrs/Miss {user} you current balance is {balance} ')
# newbalance = False
# while True:
#     mychoice = input('''
#             b to check balance
#             d to deposit
#             w to withdraw
#             q to quit
#     ''').lower()
#     if mychoice == 'b':
#         print(balance)
# >>>>>>> 166403d2445d57a2aba99ce7e33ba78365dcbe00

#     elif mychoice == 'd':
#         amount=float(input('Enter Amount'))
#         balance += amount
#         print(f'successfull and your new balalce is {amount}')
#         if amount <= 0 :
#             print('Invalid transaction')
     
            
#     elif mychoice == 'w':
#         amount=float(input('Enter Amount'))
#         if amount <= balance:
#             balance -= amount
#             print('successfull')
#         else:
#             print('insufficient')
            
    
#     elif mychoice == 'q':
#         print('Thanks for banking with us')
#         exit()
#     else:
#         print('invalid request')


# employee =  {
#     'name': 'emeka',
#     'state':'Lagos',
#     'lga': 'Eti-osa'
# }
# print(type(employee))
# print(employee["name"])
# print(employee.get('lga'))
# print(employee.keys())
# print(employee.values())
# employee['email']='ameka@gmail.com'
# employee.pop('name')
# employee.popitem()

# employee.update({'city':'Akowonjo'})
# employee.clear()
# # del employee
# print(employee)

# set
# score = { 10, 20, 10, 40, 60, 'banana', 30, 20, True, 1, False, 0}
# mycolor = {'black', 'yellow', 'red', 'purple'}
# colors = ( 'blue', 'purple', 'black', 'yellow')
# x = 10 not in score
# score.add('orange')
# mycolor = score.union(colors)
# mycolor = score |colors
# score.remove('banana')
# x = mycolor ^ colors
# x = mycolor & colors
# print(x)

# x = mycolor.intersection(colors) 
# mycolor.intersection_update(colors)
# colors.difference_update(mycolor)
# print(colors)
# x =  mycolor + colors
# print(x)

# def greetings():
#     print('Welcome to class')


# greetings()
# greetings()
# greetings()
# greetings()


# def tunde(x , y):
#     return x + y

# print(tunde(10, 20))

# def greetings(x, y):
#     print(f'Welcome to python class {x} {y}')
# greetings(input('What is your first name   \n'), input('And your last name'))

# def greetings():
#     name = input('Enter your name: ')
#     name1 = input('Enter your last name: ')
#     print(f'Welcome Mr/Mrs/Miss {name} {name1} to python class')
# greetings()


# def count():
#     x = input('Enter your name >')
#     y = x[0: 3]
#     print(y)
# count()



# myset = {'orange', 'blue' , 'green'}
# newset= {'purple', 'green'}
# set3=myset.intersection(newset)
# print(set3)
# print(myset|newset)
# print(newset^myset)
# print(newset&myset)


# def merge_set(set1, set2):
#     return set1, set2

# set1={1,2,3,4}

# set2 = {1,2,3,4}
# x = set1.issuperset(set2)
# print(x)
# print(len(set2))
# myset=9
# x =myset in set2
# print(x)
# x = set1.isdisjoint(set2)
# print(x)


# x =set1.issubset(set2)
# print(x)
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1^set2) 

# x = [20, 10, 40, 60, 30, 70, 25, 75, 21, 53]
# myx = list(map( lambda y: y % 5 == 0, x))
# # myx = lambda y : y + y
# print(myx)


# handling of errors which is mostly used by try and except


# def mynumber(num1, num2):
#     try:
#         return num1 + num2
#     # except TypeError:
#     #     return ('Value must be an interger')
#     # except NameError:
#     #     return ('parameter does not exixt')
#     except Exception as e:
#         return e


# print(mynumber(10, 30))
# print(mynumber('a', 10))
# print('Success')


# from tkinter import *

# root=Tk()
# root.title('GUI')
# root.geometry('900x300')
# label = Label(root, text="First Name")
# label.grid(row=0, column=0)

# entry = Entry(root, width='60')
# entry.grid(row=0, column=1 )
# mybutton= Button(root, text='Submit')
# mybutton.grid(row=1, column=0, padx='40')

# # label.pack()
# root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
def create_table():
    tunde = sqlite3.connect(
        "class.db"
    )
    myclass= tunde.cursor()
    myclass.execute(
        """CREATE TABLE IF NOT EXISTS prosper (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            
            )
        """
    )
    tunde.commit()
    tunde.close()

root=Tk()
root.title('My GUI INterface')
create_table()
def myclick():
    password = myinput1.get()
    myemail= myinput.get()

    

    result1 = Label(root, text=myemail)
    result1.pack()
    result2= Label(root, text=password)
    result2.pack()
def savedata():
    theemail = myinput.get()
    thepassword = myinput1.get()

    if theemail and thepassword:
        myselect=sqlite3.connect('class.db')
        myconn = myselect.cursor()
        myconn.execute('INSERT INTO prosper (email, password) VALUES (?, ? )', (theemail, thepassword))
        # myconn.commit()
        myconn.close()

        messagebox.showinfo("Email and password save successfully")
    else:
        messagebox.showerror('Credientials not successfully saved')
        
mylabel = Label(root, text='Email')
mylabel.pack() 

myinput = Entry(root, width=30)
myinput.pack()

mypass= Label(root, text='password', show="*")
mypass.pack()

myinput1 = Entry(root, width=30)
myinput1.pack()


mybutton= Button(root, text='submit', command=myclick)
mybutton.pack()
mybutton2 = Button(root, text='Save Data', command=savedata)
mybutton2.pack()


root.mainloop()





