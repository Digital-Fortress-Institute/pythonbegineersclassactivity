# Assignment
# 1. Write a Python program to check if a given number is even and divisible by 3 using if and else statements.
# if the number is even print BUZZ if the number is divisible by three let it print FIZZ.

# def examine_number(num):
#     if num % 2 == 0:
#         print("BUZZ")
#     elif num % 3 == 0:
#         print("FIZZ")
#     else:
#         print("FIZZBUZZ")
# num = int(input("Enter your number: "))
# examine_number(num)


# 2. Create a program that asks the user to input their age and then outputs whether they are eligible to vote or not using if and else.

# age = input("Enter your age: ")
# eligible_age = int(age)
# if eligible_age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")


# 3. Write a Python program that takes a user input for a number and prints "Positive" if it's greater than zero,
# "Negative" if it's less than zero, and "Zero" if it's equal to zero using if, elif, and else.

# print("Hi, you're welcome")
# a = input("Kindly type your desired number: ")
# b = int(a)
# if b > 0:
#     print("Positive")
# elif b < 0:
#     print("Negative")
# else:
#     b == 0
#     print("Zero")


# 4. Create a program that print multiplication table when a user input any number using while loop and for loop.

# While loop:
# def multiplication_table(number):
#     a = 1
#     while a <= 12:
#         result = number * a
#         print(f"{number} x {a} = {result}")
#         a += 1

# print("Hello, you're welcome")
# number = int(input("Enter your preffered number: "))
# multiplication_table(number)

# For loop:
# solution 1:
# def multiplication_tab(number):
#     for i in range(1, 13):
#         result = number * i
#         print(f"{number} x {i} = {result}")
# print("Hello, you're welcome")
# number = int(input("Enter a number: "))
# multiplication_tab(number)

# solution 2:
# def multiplication_tab(number):
#     a = range(1, 13)
#     b = a
#     for b in a:
#         result = number * b
#         print(f"{number} x {b} = {result}")
# print("Hello, you're welcome")
# number = int(input("Enter a number: "))
# multiplication_tab(number)

# class solution
# For loop:
# num = int(input("Enter your number: "))
# for mul in range(1, 12):
#     print(f"{num} x {mul} = {num * mul}")

# while loop:
# i = 1
# while 1 <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 0
# not solved

# 5.⁠ ⁠Write a Python program that compares two numbers provided by the user and prints the larger number using if and else.

# solution 1:
# num1 = input("Enter your first choice of number: ")
# num2 = input("Enter your second choice of number: ")
# a = int(num1)
# b = int(num2)
# if a > b:
#     print(f"{"Your answer is: "} {a}")
# elif b > a:
#     print(f"{"Your answer is: "} {b}")
# else:
#     print('Answer = Void')

# solution 2:
# def compare_num(num1, num2):
#     if num1 > num2:
#         print(f"The larger number is: {num1}")
#     elif num2 > num1:
#         print(f"The larger number is: {num2}")
#     else:
#         print("Both numbers are equal.")

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# compare_num(num1, num2)


# 6.⁠ ⁠Create a program that takes a user input for a grade such that grade between 90 - 100 should print Grade A, grade between 70 - 89 should print Grade B, grade 
# between 50 - 69 should print Grade C, grade between 40 - 49 should print Fail and grade between 0 to 39 should print unknown results. 

# solution a:
# print("Welcome Student!")
# grade_checker = input("Enter your score: ")
# grade_checker = int(grade_checker)
# grade_a = range(90, 100)
# grade_b = range(70, 89)
# grade_c = range(50, 69)
# grade_d = range(40, 49)
# grade_e = range(0, 39)

# if grade_checker in grade_a:
#     print("Grade A")
# elif grade_checker in grade_b:
#     print("Grade B")
# elif grade_checker in grade_c:
#     print("Grade C")
# elif grade_checker in grade_d:
#     print("Fail")
# else:
#     print("Unknown result")

# solution b:
# def grade_classification(grade):
#     if grade >= 90 and grade <= 100:
#         print("Grade A")
#     elif grade >= 70 and grade <= 89:
#         print("Grade B")
#     elif grade >= 50 and grade <= 69:
#         print("Grade C")
#     elif grade >= 40 and grade <= 49:
#         print("Fail")
#     elif grade >= 0 and grade <= 39:
#         print("Unknown Result")
#     else:
#         print("Invalid grade entered.")

# grade = float(input("Enter the grade: "))
# grade_classification(grade)

# Class solution:
# grade = int(input("Enter your grade: "))
# if grade >= 90 and grade <= 100:
#     print("Grade A")
# elif grade >= 70 and grade <= 89:
#     print("Grade B")
# elif grade >= 50 and grade <= 69:
#     print("Grade C")
# elif grade >= 40 and grade <= 49:
#     print("Fail")
# else: 
#     print("Unknown Results")



# 7.⁠ ⁠Write a program that asks the user to input their salary and then calculates their tax based on the following conditions:
# if salary is less than or equal to 5000, tax is 10%; if salary is between 5001 and 10000, tax is 20%; otherwise, tax is 30% using if, elif, and else.

# salary = float(input("Enter your salary: "))
# tax_a = float(salary * 0.10)
# tax_b = float(salary * 0.20)
# tax_c = float(salary * 0.30)

# if salary <= 5000:
#     tax = tax_a
# elif salary <= 10000:
#     tax = tax_b
# else:
#     tax = tax_c

# print(f"Your tax is: {tax}")


# 8. Create a program that asks the user to input two numbers and then checks if their sum is greater than 100.
# If it is, print "Sum is greater than 100", otherwise print "Sum is not greater than 100" using if and else.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# total = int(num1 + num2)
# if total > 100:
#     print("Sum is greater than 100")
# else:
#     print("Sum is not greater than 100")


# 9. Write a Python program that takes three numbers from the user and prints the largest among them using nested if-else statements.

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# if num1 >= num2:
#     if num1 >= num3:
#         largest_number = num1
#     else:
#                 largest_number = num3
# else:
#        if num2 >= num3:
#               largest_number = num2
#        else:
#               largest_number = num3

# print("Largest number is: ", largest_number)


# 10.⁠ ⁠Create a program that takes a user input for their age and then checks if they are eligible for a senior
# citizen discount (age 60 or above). If they are eligible, print "You are eligible for a senior citizen discount",
# otherwise print "You are not eligible for a senior citizen discount" using if and else.

# name = input("Enter your name: ")
# birth_year = input("Enter your birth year: ")
# age = 2024 - int(birth_year)

# if age >= 60:
#     print(f"name, You're eligible for the senior citizen discount.")
# else:
#     print(f"{name}, You're not eligible for the senior citizen discount.")


# 11.⁠ ⁠Create a program for a guessing game when the user guess right it should tell the user that your are right with a congratulation
# message printed and if the user get it wrong the user should be ask to continue trying till the user get the game right.

# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# user_num = int(input("Enter your number: "))
# numbers = (10, 26, 15, 100, 99, 200, 55)
# if user_num in numbers:
#     print("You are right, congratulations 🎉🎉🎉")
# else:
#   print("Try again")


# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# import random

# while True:
# user_num = int(input("Enter your number: "))
# numbers = range(1, 100)
# if user_num in numbers:
#     print("You are right, congratulations 🎉🎉🎉")
# else:
#   print("Try again")


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
data[0::5]