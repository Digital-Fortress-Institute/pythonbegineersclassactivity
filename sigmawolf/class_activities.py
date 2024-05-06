# word = ["Training", "Mango", "Tech", "Rock", "technicial" "software" "Analysis", "togo" "Tonga" ]

# Question: Bring out the word that start with both capital letter T and small letter t.

# word = [ "Training", "Mango", "Tech", "Rock", "technicial", "software", "Analysis", "togo", "Tonga" ]
# matching_words = [words for words in word if words.startswith('T') or words.startswith('t')]
# print(matching_words)

word = [ "Training", "Mango", "Tech", "Rock", "technicial", "software", "Analysis", "togo", "Tonga" ]
x = word[0]
print(x)

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

# Amswer:
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


# ATM

# Define a dictionary to store card numbers and corresponding PINs
accounts = {
    "1234567890": "1234",
    "0987654321": "4321"
}

# Define a dictionary to store account balances
balances = {
    "1234567890": 1000,
    "0987654321": 2000
}

# Function to authenticate the user
def authenticate():
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    return card_number in accounts and accounts[card_number] == pin

# Function to display the main menu and handle user input
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            withdraw()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle withdrawal
def withdraw():
    # Implement withdrawal logic here
    pass

# Function to check account balance
def check_balance():
    # Implement balance checking logic here
    pass

# Main program
def main():
    print("Welcome to the ATM!")
    if authenticate():
        print("Authentication successful.")
        main_menu()
    else:
        print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()