#Loop through a dictionary
"""you can loop through a dictionary by using a for loop"""
"""when looping through a dictionary, the return value are the keys of the dictionary, 
but there are methods to return the values as well"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""for x in thisdict:
    print(x)"""
"""for x in thisdict:
    print(thisdict[x])"""
#you can also use the values() method to return values of a dictionary
"""for x in thisdict.values():
    print(x)"""
#you can use the keys() method to return the keys of a dictionary
"""for x in thisdict.keys():
    print(x)"""

#loop through both keys and values, by using the items() method:
for x,y in thisdict.items():
    print(x,y)