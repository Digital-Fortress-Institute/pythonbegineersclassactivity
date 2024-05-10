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
    ''').lower()
    if mychoice == 'b':
        print(balance)

    elif mychoice == 'd':
        amount=float(input('Enter Amount'))
        balance += amount
        print(f'successfull and your new balalce is {amount}')
        if amount <= 0 :
            print('Invalid transaction')
     
            
    elif mychoice == 'w':
        amount=float(input('Enter Amount'))
        if amount <= balance:
            balance -= amount
            print('successfull')
        else:
            print('insufficient')
            
    
    elif mychoice == 'q':
        print('Thanks for banking with us')
        exit()
    else:
    print('invalid request')
