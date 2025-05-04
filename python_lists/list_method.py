#LIST METHODS
"""python has a set of built-in methods that you can use on lists"""

#Append()-------------------------------------
#Adds an element at the end of the list
"""fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)"""
#syntax list.append(elmt)-> elmt:string, number, object
"""fruits = ["apple", "banana", "cherry"]
fruits.append([1,2,3])
print(fruits)"""


#Clear()-------------------------------------
#remove all elements from the fruits list
"""fruits = ["apple", "banana", "cherry", "orange"]
fruits.clear()
print(fruits)"""



#Copy()----------------------------------
#copy the fruits list
"""fruits = ["apple", "banana", "cherry", "orange"]
x = fruits.copy()
print(x)"""



#count()------------------------------------
#return the number of times the value "cherry" appears in the fruits list
"""fruits = ["apple", "banana", "cherry", "orange", "cherry"]
number = fruits.count("cherry")
print(number)"""



#Extend()------------------------------------
#the extend() method adds the specified list elements(or any iterable) to the end of the current list
"""fruits = ["apple", "banana", "cherry"]
cars = ["ford", "bmw", "huyndai"]
fruits.extend(cars)
print(fruits)"""


#index()-----------------------------------
#the index() method returns the position at the first occurenxe of the specified value
#list.index(elmnt, start, end)
"""elmnt: (string, number, list...) the element to search
start: optional, a number representing where to start the search
end: optional. a number representing where to end the search"""

"""fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32, 4)
print(x)"""

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "cherry"]
x = fruits.index("cherry", 4)
print(x)"""


#insert()------------------------------------
#insert the value "orange" as the second element of the fruit list:
"""fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "pineapple")
print(fruits)"""



#pop()------------------------------------
#the pop() method removes the element at the specified piosition
"""fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)"""


#remove()------------------------------------
#the remove() method removes the first occurence of the element with the specified value
"""fruits = ["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)"""

"""fruits = ["apple", "banana", "cherry", "apple", "strawberry", "grapes"]
for x in fruits:
    if x == "apple":
        fruits.remove(x)
print(fruits)
"""

#reverse()-------------------------------------
#the reverse() method reverses the sorting order of the elements
"""fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)"""


#sort()------------------------------------
"""the sort() method sorts the list ascending by default
you can also make a function to decide the sorting criteria"""
cars = ["ford", "bmw", "volvo"]
cars.sort(reverse=True)
print(cars)