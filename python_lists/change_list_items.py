#to change the value of a specific item, refer to the index number
"""thisList =["apple", "banana", "cherry"]
thisList[1]= "blackcurrant"
print(thisList)"""

#change a range of item values---------------
"""to change the value of items within a specific range,
define a list with the new values, and refer to the range of index numbers
where you want to insert the new value """
"""thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)"""

#Insert items-------------------------------
"""to insert a new list item, without replacing any any of the existiing values, we
can use insert() method"""
#the Insert() method inserts an item at the specified index
#for examples
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)
