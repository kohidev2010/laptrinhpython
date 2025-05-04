#copy a list
"""you can not copy a list simply by typeing list2 = list1
because list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2"""

#Use copy() method--------------------------
"""you cna use the built-in List method copy() to copy a list"""
"""thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)"""
#another way to copy of a list with the list() method:
"""thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
thisList[0] = "strawberry"
print (thisList)
print(myList)"""