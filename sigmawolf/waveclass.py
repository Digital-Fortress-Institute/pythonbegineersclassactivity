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

score = {10, 30, 20, 20, 10, 30, 60, 100}
for x in score:
    if x > 10:
        print(x ** 2)
    else:
        print(x)