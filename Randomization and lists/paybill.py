import random
friends = ["alice","bob","charlie","david","emanuel"]
#random.choice(seq) = element from the non empty seq. if seq is empty, raises index

#option 1 = random.choice(listname) - to pick a value randomly from a list. 

print(random.choice(friends))

#option 2 - to do from something we already know. 

rando = random.randint(0,4) #ranging for the indexes of the list. 
print(friends[rando])