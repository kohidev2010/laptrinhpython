#Nested Dictionaries----------------------------
"""A dictionary can contain dictionaries, this is called nested dictionaries."""
"""myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
"""

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myFamily = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}
currentYear = 2025
for child in myFamily.values():
    name = child["name"]
    age = currentYear - child["year"]
    print("my name is {} and my age is {}".format(name, age))