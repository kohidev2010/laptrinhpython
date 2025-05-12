#Accessing Items
"""you can access the items of a dictionary by referring to its key name, inside square brackets"""
"""thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}"""
"""x = thisDict["model"]
print(x)"""

"""there is also a method called get() that will give you the same result"""
"""x = thisDict.get("model")
print(x)"""

#Get keys ------------------------------------
"""the keys() method will return a list of all the keys in the dictionary"""
"""x = thisDict.keys()
print(x)"""



"""the list of the keys is a view of the dictionary, meaning that
any changes done to the dictionary will be reflected in the keys list"""
#EXamples
"""add a new item to the original dictinary, and see that the keys list gets updated as well"""
"""car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"]= "white"
print(car) #after the change"""


#GET Values--------------------------------
#the values() method will return a list of all the values in the dictionary
"""car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)
car['year'] = 2020
print(x)
"""

#Get items-------------------------------------
#the items() method will return each item in a dictionary, as tuples in a list
"""thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = thisDict.items()
print(x)"""

#Check if key exists------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("\"yes\", \"model\" is one of the keys in the thisdict dictionary")
    

