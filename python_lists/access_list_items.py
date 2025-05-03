#list items are indexed and you can access them by reffering to the index number
"""thisList = ["apple", "banana", "cherry"]
print(thisList[1])""" #the first list is 0
#Negative indexing
#negative indexing means start from the end
"""thisList = ["apple", "banana", "cherry"]
print(thisList[-1])"""

#Range of Indexes
"""you can specify a range of indexes by specifying where to start and
where to end the range"""
"""when specifying a range , the return value will be a new list with the specified items"""
"""thisList =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[1:4])"""

#Check if item exists-------------------------
thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("yes, \'Apple\' is in the fruits list")