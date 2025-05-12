#Change values ------------------------------
"you can change the va;ues of a specific item by referring to its key name"
"""thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["year"] = 2018
print(thisdict)"""


#Update dictionary---------------------------
"""the update() method will update the dictionary with the items from the given argument
the argument must be a dictonary, or an iterable object with key:value pairs"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":2020})
print(thisdict)