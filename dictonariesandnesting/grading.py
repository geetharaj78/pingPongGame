
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

x = student_scores.values()
for y in x:
    if 91<=y<100:
        print(f"{y} is outstanding")
    elif 81<=y<=90:
        print(f"{y} exceeds expectations")
    elif 71<=y<=80:
        print(f"{y} acceptable")
    else:
        print(f"{y } fail")
         