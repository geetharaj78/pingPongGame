print("welcome to pizza delivery")
size = print(input("enter the size of the pizza?S,m or L:\n"))
pepper = print(input("do u want pepperoni or not: y or n\n"))
extra_chesse = print(input("do u want extra cheese or not:y or n\n"))
bill = 0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("inappropriate size given")

if pepper == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_chesse == "Y":
    bill+=1
    
print(f"your final bill is: {bill}")
