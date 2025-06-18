
capitals = {
        "france" : "paris",
        "germany" : "berlin"
}

travel_log = {
    "france" : ["paris","lill","dijon"],
    "germany": ["sttutegart","berlin"]
}

print(travel_log["france"][1])

nested_list = ["a","b",["c","d"]]
print(nested_list[2][0])

cont = {
    "capitals" : {
        "france" : "paris",
        "germany" : "berlin"
}, 
   "travel_log" : {
    "france" : ["paris","lill","dijon"],
    "germany": ["sttutegart","berlin"]
}     
}

print(cont["capitals"]["germany"])
print(cont["travel_log"]["germany"])