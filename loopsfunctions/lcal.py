
count1 = 0
count2 = 0
def cal_l_score(n1,n2):
    names_combined = n1 + n2
    t_count = 0
    for char in "true":
        t_count += names_combined.count(char)
        
    l_count = 0
    for x in "love":
        l_count += names_combined.count(char)
    
    l_score = int(str(t_count) + str(l_count))
    
    print(f"Your love score is {l_score}.")

cal_l_score("kanye west","kim kardashian")
