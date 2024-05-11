# Assignment:
# 1. Write a Python program to find the common elements between two sets.
# 2. Write a Python program to merge two sets without duplicates.
# 3. Write a Python program to find the elements present in the first but not in the second set.
# 4. Write a Python program to find the elements in either set but not in both.
# 5. Write a Python program to check if one set is a subset of another.
# 6. Write a Python program to check if one set is a superset of another.
# 7. Write a Python program to find the length of a set.
# 8. Write a Python program to check if an element is present in a set.
# 9. Write a Python program to check if two sets have no common elements.
# 10. Write a Python program to check if an element is present in a set.


# •---------------------Solution---------------------•

# 1.
print('\n---•1•---')
print('Hi, we are here to find the common elements between two sets')

home = {'Table', 'Chair', 'Dining', 'Utensils', 'Refrigerator', 'TV', 'Decoder'}
hotel = {'Table', 'Chair', 'TV', 'Decoder', 'Free WiFi', 'Utensils', 'Free Electricity'}
x = home & hotel
print('The common elements between home and hotel are', x)
print('\n---•2•---')

# 2.
print("Now let's merge two sets without duplicates.")
home = {'Table', 'Chair', 'Dining', 'Utensils', 'Refrigerator', 'TV', 'Decoder'}
hotel = {'Table', 'Chair', 'TV', 'Decoder', 'Free WiFi', 'Utensils', 'Free Electricity'}
y = home | hotel
print(y)
print('\n---•3•---')

# 3.
print("Let's find the element present in our home and not in hotel\nHere we go 👇🏾")
home = {'Table', 'Chair', 'Dining', 'Utensils', 'Refrigerator', 'TV', 'Decoder'}
hotel = {'Table', 'Chair', 'TV', 'Decoder', 'Free WiFi', 'Utensils', 'Free Electricity'}
z = home.difference(hotel)
print(z)
print('\n---•4•---')

# 4.
print("Now it's time to find the elements we have in home and hotel but not in both.")
home = {'Table', 'Chair', 'Dining', 'Utensils', 'Refrigerator', 'TV', 'Decoder'}
hotel = {'Table', 'Chair', 'TV', 'Decoder', 'Free WiFi', 'Utensils', 'Free Electricity'}
a = home ^ hotel
print("We have", a)
print('\n---•5•---')

# 5.
print("Checking if 'Set A' is subset of 'Set B'.....")

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {2, 4, 6, 8, 10}
if set_a.issubset(set_b):  # Set A is a subset of a set B if each element of the set A belongs to set B as well.
    print("Set A is a subset of Set B")
else:
    print('Set A is not a subset of Set B.')
print('\n---•6•---')

# 6.
print("Checking if 'Set A' is superset of 'Set B'.....")

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {2, 4, 6, 8, 10}

if set_a.issuperset(set_b):  # Set A is a superset of a set B if set A contains all elements of set B (but it may also contain other elements).
    print("Set A is a superset of Set B")
else:
    print("Set A is a not a superset of Set B")
print('\n---•7•---')

# 7.
print("Let's find the length of the set below...")

# set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set = range(5, 20000)
b = len(set)
print(b)
print('\n---•8•---')

# 8.
print("Let's check if an element is present in a particular set.")

my_set = {2, 4, 6, 8, 10}
i = 5 in my_set
print("Is it True or False?")
print(f'{i}, 5 is not present in my_set.')
print('\n---•9•---')

# 9.
print("Let's check if two sets have no common elements.")

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {2, 4, 6, 8, 10}

if set_a.intersection(set_b):
    print(f"They both have common elements which are, {set_a & set_b}.")
else:
    print("They don't have common elements")