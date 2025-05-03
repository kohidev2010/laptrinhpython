#Sort List Alphanumerically-----------------
"""thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()#this method will print the list  to be sorted
print(thisList)
"""

#Sort the List numerically----------------------
"""thisList =[85, 56, 22, 6, 3]
thisList.sort()
print(thisList)"""

#Sort the list descending. it means to sort from big number to small number
"""thisList = [8, 54, 67, 98, 34, 65]
thisList.sort(reverse=True)
print(thisList)"""

#Case insensitive Sort------------------------
"""by default the sort() method is case sensitive, resulting in all capital letters being sorted befor lower case letters"""

"""thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort()
print(thisList)"""

"""Luckily we can use built-in function as key functions when sorting a list
So if you want a case-insensitive sort function, use str.lower as a key function """

"""thisList = ["banana", "Grapes", "Rambutant", "guava", "Papaya", "Jackfruit"]
thisList.sort(key=str.lower)
print(thisList)"""
#this key function helps the string when printing be sorted from a to z despite capital or lower


#Reverse order------------------------------
"""what if you want to reverse the order of a list, regardless of the alphabet
The Reverse() method reverse the current sorting order of the elements"""
thisList = ["banana", "jackfruit", "grapefruit", "starfruit,"]
thisList.reverse()
print(thisList)