stud_score = [20,30,45,60,25]

total_score = sum(stud_score)
print(total_score)

s = 0
for score in stud_score :
    s +=score
    
print(s)

print(max(stud_score))
#without builtin function

m = 0
for score in stud_score:
    if score > m:
        m = score
        
print(m)