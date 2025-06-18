#dictionries are useful because they allow us to group together and tag related pieces of information
#every dic has two parts to it. on the left hand side is the key, and that is equivalent of the actual definition. and it also has a n associated value which is actually equivalent of the actual definition
#bascially key - value pairs

programing_dic = {
    "bug" : "a flaw, error, or defect in the code that causes a program to behave unexpectedly or incorrectly",
    "function":  "a reusable block of code that performs a specific task",
    123 : "a number"
}

print(programing_dic["bug"]) # we print it by accesing the key. 
print(programing_dic[123])

empty_dictionary = {} #used to wipe an existing dictionary. 

#editing an item in the dictionary. 
programing_dic["bug"] = "i changed the def of the bug"
print(programing_dic) #if there was no key in the dictinoary with this name, then it will create a key value pair with this sort of thing

#looping through a dictionary : 
for x in programing_dic:
    print(x) 
    print(programing_dic[x]) #if i wanted to print the values instead of the key - value pairs
    
#for accessing both key and value pairs

for x,y in programing_dic.items():
    print(x,y)
    
#for printing the values/for accessing the values, we use dic_name.values()
#for keys, we use dic_name.keys()
    
