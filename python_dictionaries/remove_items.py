#Remove items---------------------------------
"""the pop() method removes  the item with the specified key name"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)"""



#the popitem() method removes the last inserted item(in versions before 3.7, a random item is removed instead))
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
"""

#del 
"""The del keyword removes the item with the specified key name:"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict)"""
#"""The del keyword can also delete the dictionary completely:"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print (thisdict)"""


#clear () method emties the dictionary-----------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)