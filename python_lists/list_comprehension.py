"""List comprehension offers a shorter syntax when you want to create a
a new list based on the values of an existing list"""

#Examples----------------------------
"""Based on a list of fruits, you want a new list, containing only the fruits
with letters "a" in the same"""

"""fruits = ["apple", "banana", "cherry", "kiwi", ",mango"]
newList = []
for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)"""

#with kist comprehension you can do all that with only one line of code

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [ x for x in fruits if "a" in x ]
print(newList)"""

#the Syntax-----------------------
#newList = [expression for item in iterable if condition == True]


#range() comprehension
"""newList = [x for x in range(10) if x < 5]
print(newList)"""
