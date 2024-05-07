pin = 1234
card_number=8659036754
balance = 0

print('Welcome to Digital Fortress Micro Finance Bank')
card_pin=int(input('Please enter your pin  \n'))
if card_pin == pin:
    print('Welcome')
else:
    print('Invalid')
    exit()
mycard_number=int(input('Please enter your card number  \n'))
if mycard_number == card_number:
    print('Welcome')
else:
    print('Invalid')
    exit()
user =input('Enter your name')
print(f'Welcome Mr/Mrs/Miss {user} you current balance is {balance} ')
newbalance = False
while True:
    mychoice = input('''
            b to check balance
            d to deposit
            w to withdraw
            q to quit
    ''')
    if mychoice == 'b':
        print(balance)

    elif mychoice == 'd':
        amount=float(input('Enter Amount'))
        print(f'Your current balance is: {balance + amount}')
        totalbalance = balance + amount
    elif mychoice == 'w':
        amount=float(input('Enter Amount'))
        if amount > totalbalance:
            print('Insufficient fund')
        else:
            print('transactioin successfull.')
            
        print(f'Your current balance is: {totalbalance - amount}')
    elif mychoice == 'q':
        print('Thanks for banking with us')
        exit()


