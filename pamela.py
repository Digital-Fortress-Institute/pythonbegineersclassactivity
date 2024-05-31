# my_list = []
# print(my_list)

# my_list = [20,40,60,80,10]
#print(my_list[2])

# fruits=["oranges","grape","banana","pear"]
# fruits.append("apple")
# print(fruits)

# number=["veggies","carrots","lettuce","cucumber"]
# number.pop(2)
# print(number)

# append method is use to add a single element at the end of the list
# my_data = [5,4,8,9]
# my_data.append(10)
# print(my_data)

# extend method is use to add all the element of the eterabes to the end of the list, 
# by selecting each character as an element.
#my_data = ["honey"]
# my_data.extend("honey")
# print(my_data)

# check if an element exist in a list
# my_list =["bay","soap","lotion","shawl"]
# print(my_list)
# if "shawl" in my_list:
    # print("found")

# what will be an output of len(["a","b","c"])
#my_list = ["a","b","c"]
#print("found")

# what will be the output of len["a","b","c"]
#my_list = ["a","b","c"]
# print(len(my_list))

# how do you reverse the order of an element in a list called my_list
#my_list = [10,30,50,80,100,120]
# print(my_list)
#my_list.reverse()
# print(my_list)

# explain the purpose of sort method in python
#num_list = [5,3,8,2,10,3#
#num_list.sort()
#print(num_list

#create a program to find out the common elements between two set
#set1 = {10, 20, 30, 5, 50, 7}
#set2 = { 50, 30, 20, 6, 9}
#common_elem = set1.intersection(set2)
#print(common_elem)

#write a program to merge two elements without duplicate

#my_elem1 = {5, 4, 9, 60}
#my_elem2 = {80,70,2,4}
#sets = my_elem1.union(my_elem2)
#print(sets)

#merge_set= (my_elem1, my_elem2)
#x =my_elem1| my_elem2
#print(x)



#write a program to find out elements that are present in the first set but not in the second set

#my_elem1 = {5, 4, 9, 60}
#my_elem2 = {80,70,2, 9,5}
#sets = my_elem1.difference(my_elem2)
#print(sets)
#or
#print(my_elem1.difference(my_elem2))

#n0 4, write a program a to find out the element that are present in either set but not in both.

#set1 = {5, 4, 2, 9, 60}
#set2 = {80,70, 5, 2}
#print(set1.symmetric_difference(set2))

#set1 = {5, 4, 2, 9, 60}
#set2 = {80,70, 5, 2}
#print(set1^set2)



#n0 5, write a program to check if one set is subset of another.

#def is_subset(set1, set2):
# return set1.issubset(set2)
#set1 = {5, 4, 9, 60}
#set2 = {80,70,2}
#if is_subset (set1, set2):
 #print("set1 is a subset to set2") 
#else:
# print("set1 is not a subset of set2")

#set1 = {5, 4, 9, 60}
#set2 = {80,70,2}
#x = set1  .issubset(set2)
#print(x)


#create a calculator program

#operator = input("enter your operator ( -, +, *,/):")
#num1 = float(input("enter the 1st number: "))
#num2 = float(input("enter the 2nd number :"))
#if operator == "+":
   # result = num1 + num2
   # print(round(result))
#elif operator == "-":
  #  result = num1 - num2
 #   print(round(result))
#elif operator == "*":
 #   result = num1 * num2
  #  print(round(result))
#elif operator == "/":
   # result = num1 / num2
  #  print(round(result))
#else:
 #   print(f"{operator} is not a valid operator" )

    
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    if math == "division":
        entry.insert(0, f_num / float(second_number))

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = tk.Button(root, text="C", padx=40, pady=20, command=button_clear)
button_equal = tk.Button(root, text="=", padx=90, pady=20, command=button_equal)
button_add = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()


