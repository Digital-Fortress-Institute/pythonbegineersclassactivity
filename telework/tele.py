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

# def calculator(x, y, v):
#         if v == "A":
#             print(f"The addition of {x} and {y} is: {x + y}")
#         elif v == "S":
#             print(f"The Subtraction of {x} and {y} is: {x - y}")
#         elif v == "D":
#             if y == 0:
#                 print("Error: Division by zero is not allowed.")
#             else:
#                 print(f"The Division of {x} and {y} is: {x / y}")
#         elif v == "M":
#             print(f"The Multiply of {x} and {y} is: {x * y}")
#         else:
#             print(f'"{v}" is not an option for an Operator')

# while True:
#     print('''Use this calculator to Add, Subtract, Divide and Multiply:
#         Choose "A" to Add,
#                 "S" to Subtract,
#                 "D" to Divide,
#                 "M" to Multiply,
#         your two values''')

#     calculator(int(input("Enter your first value:\n")), int(input("Enter your second value:\n")), input("Enter your operator to calculate:\n").upper())


mycolor = {'black', 'yellow', 'red', 'purple'}
colors = { 'blue', 'purple', 'black', 'yellow'}
#1
# Write a Python program to find the common elements between two sets.
x = mycolor & colors
print(x)

# 2.Write a Python program to merge two sets without duplicates.
merged_set = mycolor.union(colors)
print("Merged set without duplicates:", merged_set)

# 3.Write a Python program to find the elements that are present in the first set but not in the second set.
elements_only_in_mycolor = mycolor.difference(colors)
print("Elements present in mycolor but not in colors:", elements_only_in_mycolor)


# 4.Write a Python program to find the elements that are present in either set but not in both.
symmetric_difference = mycolor.symmetric_difference(colors)
print("Elements present in either set but not in both:", symmetric_difference)

# 5. Write a Python program to check if one set is a subset of another.
is_subset = mycolor.issubset(colors)
print("Is mycolor a subset of colors?", is_subset)

# 6. Write a Python program to check if one set is a superset of another.
is_superset = mycolor.issuperset(colors)
print("Is mycolor a superset of colors?", is_superset)

# 7.Write a Python program to find the length of a set.
set_length = len(mycolor)
print("Length of the set:", set_length)

# 8.Write a Python program to check if an element is present in a set.
element = "black"
is_present = element in mycolor
print(f"Is {element} present in the set?", is_present)

# 9.Write a Python program to check if two sets have no common elements.

no_common_elements = mycolor.isdisjoint(colors)
print("Do mycolor and colors have no common elements?", no_common_elements)
