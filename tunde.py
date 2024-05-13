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


employee =  {
    'name': 'emeka',
    'state':'Lagos',
    'lga': 'Eti-osa'
}
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