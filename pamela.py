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

operator = input("enter your operator ( -, +, *,/):")
num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2nd number :"))
if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator" )

    





