#List---------------------
#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets:
"""thisList = ["apple", "banana", "cherry"]
print(thisList)"""
#List items ---------------------------
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered ---------------------------------------
"""When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list."""

#changeable------------------------------
"""the list is changeable, meaning that we can  change, add, and remove
items in a list after it has been created"""

#allow duplicates------------------------
"""Since lists are indexed, lists can have items with the same value:"""
"""thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)"""

#List Length-------------------------------
#to determine how many items a list has, use the len() function
"""thisList = ["apple", "banana", "cherry"]
print(len(thisList))"""

#List Items - Data Types
"""list1 = ["apple", "banana", "cherry"]
list2 = [1,5,7,9,3]
list3 = [True, False, False]
print(type(list1))
print(type(list2))
print(type(list3))"""

# A list can contain diffirent data types
'''list = ["abc", 34, True, 40, "male"]
print(list)'''

# type()-------------------------------
#from python's perspective, lists are defined as objects with data type "list"
"""myList = ["apple", "banana", "cherry"]
print(type(myList))"""

#the list() constructor-------------------------
#it is possible to use the list() constructor when creating a new list
thisList = list(("apple", "banana", "cherry"))
#note the double round-brackets
print(thisList)

#Python Collection(Arrays)
#Collections (Bộ sưu tập) là các kiểu dữ liệu dùng để lưu trữ nhiều mục (items) trong một biến duy nhất.
#List is a collection which is ordered and changeable. Allows duplicate members
#Tuple is a collecion which is ordered and unchangeable. allows duplicate members
#Set is a collection which is unordered and unchangeable, and unindexed. no duplicate members
#Dictinary is a collection which is ordered and changeable. no duplicate memebers