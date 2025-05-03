#append() items------------------------------
#to add an item to the end of the list, use the append() method
"""thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)"""

#Insert() items------------------------------
"""to insert a list item at a specified index, use the insert() method
the insert() method inserts an item at the specified index"""
"""thisList = ["apple", "banana", "cherry"]
thisList.insert(1,"orange")
print(thisList)"""

#Extend List------------------------------------
"""to append elements from another list to the current list, use the extend() method"""
"""thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)"""

#Add any Iterable-------------------------
"""the extend() method doesn't have to append lists, you
can add any iterable object(tuples, sets, dictionaries, etc)"""
"""thisList = ["apple","banana", "cherry"]
thisTuple = ("kiwi", "orange")
thisList.extend(thisTuple)
print(type(thisList))"""