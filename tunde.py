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
# print(f'Welcome Mr/Mrs/Miss {user} you current balance is {balance} ')
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

#     elif mychoice == 'd':
#         amount=float(input('Enter Amount'))
#         print(f'Your current balance is: {balance + amount}')
#         totalbalance = balance + amount
#     elif mychoice == 'w':
#         amount=float(input('Enter Amount'))
#         if amount > totalbalance:
#             print('Insufficient fund')
#         else:
#             print('transactioin successfull.')
            
#         print(f'Your current balance is: {totalbalance - amount}')
#     elif mychoice == 'q':
#         print('Thanks for banking with us')
#         exit()


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
# score = { 10, 20, 10, 10, 60, 'banana', 30, 20, True, 1, False, 0}
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

# x = [20, 10, 10, 60, 30, 70, 25, 75, 21, 53]
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
# mybutton.grid(row=1, column=0, padx='10')

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
mylabel.grid(row=0, column=1) 

myinput = Entry(root, width=30)
myinput.grid(row=0, column=2)

mypass= Label(root, text='password')
mypass.grid(row=1, column=1)

myinput1 = Entry(root, width=30,  show='*')
myinput1.grid(row=1, column=2)


mybutton= Button(root, text='submit', command=myclick)
mybutton.grid(row=4, column=1)
mybutton2 = Button(root, text='Save Data', command=savedata)
mybutton2.grid(row=5, column=1) 


root.mainloop()




# from tkinter import *



# root =  Tk()
# root.title('Simple Calculator')
# myentry = Entry(width=20)
# myentry.grid(row=0, column=0, padx=10, pady=10)

# def button_click(x):
#     myclick = myentry.get()
#     myentry.delete(0, END)
#     myentry.insert(0, str(myclick) + str(x))


# def myclear():
#       myentry.delete(0, END)



# def myplus():
#     first_number= myentry.get()
#     global f_number 
#     global tunde
#     tunde = 'x'
#     f_number = int(first_number)
#     myentry.delete(0, END)


# def myequal():
#      second_number=int(myentry.get())
#      myentry.delete(0, END)
#      if tunde == "x":
#         myentry.insert(0, f_number + second_number)
        
        



# # root.geometry('100x200')



# mybutton1 = Button(root, text="1", padx=10, pady=20, command=lambda:button_click(1))
# mybutton2 = Button(root, text="2", padx=10, pady=20, command=lambda:button_click(2))
# mybutton3 = Button(root, text="3", padx=10, pady=20, command=lambda:button_click(3))
# mybutton4 = Button(root, text="4", padx=10, pady=20, command=lambda:button_click(4))

# mybutton5 = Button(root, text="5", padx=10, pady=20, command=lambda:button_click(5))
# mybutton6 = Button(root, text="6", padx=10, pady=20, command=lambda:button_click(6))
# mybutton7 = Button(root, text="7", padx=10, pady=20, command=lambda:button_click(7))
# mybutton8 = Button(root, text="8", padx=10, pady=20, command=lambda:button_click(8))

# mybutton9 = Button(root, text="9", padx=10, pady=20, command=lambda:button_click(9))
# mybutton0 = Button(root, text="0", padx=10, pady=20, command=lambda:button_click(0))
# mybuttonplus = Button(root, text="+", padx=10, pady=20, command=myplus)
# mybuttonminus = Button(root, text="-", padx=10, pady=20)
# mybuttondivide = Button(root, text="/", padx=10, pady=20)
# mybuttonclear = Button(root, text="C", padx=10, pady=20, command=myclear)
# mybuttonmultiply = Button(root, text="x", padx=10, pady=20)
# mybuttonequal = Button(root, text="=", padx=10, pady=20, command=myequal)


# mybutton1.grid(row=3, column=0)
# mybutton2.grid(row=3, column=1)
# mybutton3.grid(row=3, column=2)


# mybutton4.grid(row=4, column=0)
# mybutton5.grid(row=4, column=1)
# mybutton6.grid(row=4, column=2)

# mybutton7.grid(row=5, column=0)
# mybutton8.grid(row=5, column=1)
# mybutton9.grid(row=5, column=2)
# mybutton0.grid(row=6, column=1)
# mybuttonequal.grid(row=6, column=0)

# mybuttonclear.grid(row=1, column=1)


# mybuttonmultiply.grid(row=1, column=0)
# mybuttonplus.grid(row=1, column=2)
# mybuttonminus.grid(row=6, column=2)



# polymorphysm

# class Car:
      








# root.mainloop()

# def tunde(x):
   
#     match x:
#         case _ if x >= 90 and x <= 100:
#             print('Grade A')
#         case _ if x >= 70 and x <= 89:
#             print("grade B ")
#         case _:
#             print('Unknow Result')
# tunde(x=int('Enter your score:'))

        



# class Product:
#     def __init__(self, price, name, version, color):
#         self.name = name
#         self.price = price
#         self.version=version
#         self.color = color

#     def __str__(self):
#         return f"{self.name} {self.price} {self.color}"
#      def tunde(self):
#         return f"The product is {self.name}"
    

# myproduct = Product(1000, 'Headset', 'a.o', 'black')
# print(myproduct.tunde())




# class New_product(Product):
#     def __init__(self, price, name, version, color, size, weight):
#         super().__init__(price, name, version, color)
#         self.size=size
#         self.weight=weight
        
#     def __str__(self):
#         return f'{self.size} {self.weight} {self.name} {self.price} {self.color}'

# ournewproduct = New_product('xxl', '75kg', 'Samsung', 50000, 'red', 'ujj' ) 
# print(ournewproduct)     




