#copy a dictionary-------------------------
"""you cannot copy a dictionary by typing dict2=dict1, because
dict2 will only be a reference to dict1, and changes made in dict1 will aitomatically also
be made in dict2"""
"""there are ways to make a copy, one way is to use the builtin 
dictionary method copy()"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
thisdict["color"] = "red"
print(thisdict)
print(mydict)