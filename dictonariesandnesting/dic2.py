
intro = {
    "name" : "geetha",
    "age" : 19,
    "year" : 2006
}

intro.pop("age") #removes the specified key name
print(intro)
intro.popitem() #removes the last added item
print(intro)
del intro["name"] #del keyword removed the item with the specified key name
print(intro)
intro.clear()
print(intro) #empties the dic

#adding elements. 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#update - you can update the dic with the items from a given arg, and the item does not exist then it would be added
thisdict.update({"brand" : "suzuki"})
print(thisdict)