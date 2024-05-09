# operators
# arithmetical operators - + * / % += >= <= -= ** ==

# num1 = 50
# num2 = 100
# num3 = 150
# print(num1 + num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 % num2)
# print(num1 - num2)
# print(num1 + num2 - num3)
# print(num1 <= num2)
# print(num1 >= num2)
# print(num1 ** 2)

# logical operator and or
# country = "Nigeria"
# age = 18

# if country == "Nigeria" or age < 18:
#     print("You can vote")
# else: 
#     print("You can no vote")

# score = input("Enter your score: \n")
# score = score.upper()
# if score == "A":
#     print("First Position")
# elif score == "B":
#     print("Second Position")
# elif score == "C":
#     print("Third Position")
# elif score == "D" or "d":
#     print("Fourth Position" or "Fail")
# else:
#     print("Unknown Result")

# loops
# x=0
# while x <= 11:
#     print(x)
#     x += 1

# for i in range(0, 20):
#     print(i)
#     i += 1
# import random
# x = random.randint(0, 5)
# print(x)

# score = {10, 30, 20, 20, 10, 30, 60, 100}
# print(score)

# score = {10, 30, 20, 20, 10, 30, 60, 100}
# for x in score:
#     if x > 10:
#         print(x)
#     else:
#         print('')

# score = {10, 30, 20, 20, 10, 30, 60, 100}
# for x in score:
#     if x > 10:
#         print(x ** 2)
#     else:
#         print(x)

# ---------------------------------------------------------------------

# word = ["Training", "Mango", "Tech", "Rock", "technical" "software" "Analysis", "togo" "Tonga" ]

# Question: Bring out the word that start with both capital letter T and small letter t.

# word = [ "Training", "Mango", "Tech", "Rock", "technical", "software", "Analysis", "togo", "Tonga" ]
# matching_words = [words for words in word if words.startswith('T') or words.startswith('t')]
# print(matching_words)

# word = [ "Training", "Mango", "Tech", "Rock", "technical", "software", "Analysis", "togo", "Tonga" ]
# x = word[0]
# print(x)

# 2. 
# person = [
# {
# "name":"Emeka",
# "email":"emeka@gmail.com",
# "country":["United States", "Canada", "Thailand", ["Ghana", "Morocco", "Germany"]]


# },

# {
# "name":"John",
# "email":"emeka@gmail.com",
# "country":["South Africa", "Congo", "", ["Senegal", ["Digital", ["Fortress"], "Software"],"China", "Data"]]
# },

# {
# "name":"Joy",
# "email":"emeka@gmail.com",
# "country":"Nigeria"

# },
# ]

# Question: 
#  From the above data a print out of:
# i. Ghana
# ii. Digital
# iii. Fortress.

# Answer:
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# person = [
# {
# "name":"Emeka",
# "email":"emeka@gmail.com",
# "country":["United States", "Canada", "Thailand", ["Ghana", "Morocco", "Germany"]]


# },

# {
# "name":"John",
# "email":"emeka@gmail.com",
# "country":["South Africa", "Congo", "", ["Senegal", ["Digital", ["Fortress"], "Software"],"China", "Data"]]
# },

# {
# "name":"Joy",
# "email":"emeka@gmail.com",
# "country":"Nigeria"

# },
# ]

# print("i.", person[0]['country'][3][0])
# print("ii.", person[1]["country"][3][1][0])
# print("iii.", person[1]["country"][3][1][1][0])

# print("Altogether = ", person[0]['country'][3][0], person[1]["country"][3][1][0], person[1]["country"][3][1][1][0])

# ----------------------------------------------------------

# ATM

# # Define a dictionary to store card numbers and corresponding PINs
# accounts = {
#     "1234567890": "1234",
#     "0987654321": "4321"
# }
#
# # Define a dictionary to store account balances
# balances = {
#     "1234567890": 1000,
#     "0987654321": 2000
# }
#
# # Function to authenticate the user
# def authenticate():
#     card_number = input("Enter your card number: ")
#     pin = input("Enter your PIN: ")
#     return card_number in accounts and accounts[card_number] == pin
#
# # Function to display the main menu and handle user input
# def main_menu():
#     while True:
#         print("\nMain Menu:")
#         print("1. Withdraw")
#         print("2. Check Balance")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             withdraw()
#         elif choice == "2":
#             check_balance()
#         elif choice == "3":
#             print("Thank you for using the ATM. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# # Function to handle withdrawal
# def withdraw():
#     # Implement withdrawal logic here
#     pass
#
# # Function to check account balance
# def check_balance():
#     # Implement balance checking logic here
#     pass
#
# # Main program
# def main():
#     print("Welcome to the ATM!")
#     if authenticate():
#         print("Authentication successful.")
#         main_menu()
#     else:
#         print("Authentication failed. Please try again.")
#
# if __name__ == "__main__":
#     main()

# -------------------------------------CLASS

pin = 1234
card_number = 333322224444
balance = 1000
cmd = ""
print('Welcome to Digital Fortress MFB')
card_pin = int(input('Enter pin > '))
if card_pin == pin:
    card_no_ver = int(input("Confirm account number > "))
    if card_no_ver == 333322224444:
        name = input('Enter name > ')
        print(f'Hello {name}!\n Choose your option: '
              f'\n C-Check Balance\n D-Deposit\n W-Withdraw\n B-Back\n Q-Quit')
    else:
        print('Invalid')
        exit()

while True:
    cmd = input('> ').upper()
    if cmd == "D":
        new_deposit = float(input('Enter the amount: '))
        balance += new_deposit
        print("Successful!\nYour new balance is: N{:,.2f}".format(new_deposit))
        print("B.Back\nQ.Quit")

    elif cmd == "W":
        withdrawal = float(input('Enter amount: '))
        if withdrawal <= balance:
            balance -= withdrawal
            print("Withdrawal Successful")
            print("B.Back\nQ.Quit")

        else:
            print('Insufficient funds')
            print("B.Back\nQ.Quit")

    elif cmd == "C":
        print("Your current balance is: {:,.2f}".format(balance))
        print("D.Deposit\nW.Withdraw\nB.Back\nQ.Quit")

    elif cmd == "B":
        print(f'Choose your option: '
              f'\n C-Check Balance\n D-Deposit\n W-Withdraw\n B-Back\n Q-Quit')

    elif cmd == "Q":
        print('Thank you for banking with us')
        break

# ------------------------------------

# if card_pin == pin:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# mycard_number = int(input('Please enter your card number  \n'))
# if mycard_number == card_number:
#     print('Welcome')
# else:
#     print('Invalid')
#     exit()
# user =input('Enter your name')
# print(f'Welcome Mr/Mrs/Miss {user} you current balance is {balance} ')
# new_balance = False
# while True:
#     user_choice = input('''
#             b to check balance
#             d to deposit
#             w to withdraw
#             q to quit
#     ''')
#     if mychoice == 'b':
#         print(balance)
#
#     elif mychoice == 'd':
#         amount = float(input('Enter Amount'))
#         print(f'Your current balance is: {balance + amount}')
#         total_balance = balance + amount
#     elif mychoice == 'w':
#         amount = float(input('Enter Amount'))
#         if amount > total_balance:
#             print('Insufficient fund')
#         else:
#             print('transaction successful.')
#
#         print(f'Your current balance is: {total_balance - amount}')
#     elif mychoice == 'q':
#         print('Thanks for banking with us')
#         exit()
