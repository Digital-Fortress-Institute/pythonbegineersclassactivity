# 1.Write a Python program to find the common elements between two sets.
# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {1,2,3,4,50,60,70,8,9,10}

# print(set1 & set2)


# 2.Write a Python program to merge two sets without duplicates.
# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 | set2)


# 3.Write a Python program to find the elements that are present in the first set but not in the second set.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 - set2)



# 4.Write a Python program to find the elements that are present in either set but not in both.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(set1 ^ set2)




# 5. Write a Python program to check if one set is a subset of another.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# sub_set = set2.issubset(set1)
# print(sub_set)



# 6. Write a Python program to check if one set is a superset of another.

# set1 = {1,2,3,4,5,6,8,9,10}
# set2 = {1,2,3,4,5,6,7,8,9,50,60,"mirror",8,9,10}
# super_set = set2.issuperset(set1)
# print(super_set)




# 7.Write a Python program to find the length of a set.

# set1 = {1,2,3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror",8,9,10}
# print(len(set1))
# print(len(set2))






# 8.Write a Python program to check if an element is present in a set.


# set1 = {1,2,3,4,5,6,8,9,10}
# set2 = {1,2,3,4,5,6,7,8,9,50,60,"mirror",8,9,10}
# if "mirror" in set2:
#     print("true")
# else:
#     print("not there")





# 9.Write a Python program to check if two sets have no common elements.


# set1 = {3,4,5,6,"water",8,9,10}
# set2 = {1,2,"house",50,60,"mirror"}
# common = set1 & set2
# if common:
#     print("both sets have something in common")
# else:
#     print("both sets have nothing in common")


