#adding items-------------------------------
"""adding an item to the dictionary is done by using a new index key and assigning a value to it"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"]="red"
print(thisdict)"""

#Update dictionary------------------------------
"""the update() method will update the dictionary with items from a 
given argument. if the item does not exist, the item will be added
the argument must be a dictionary, or an iterable object with key:value"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color":"red"})
print(thisdict)