height = int(input("enter the height of the person:\n"))
bill =0
if height >=120:
    print("You can ride the rollercoster")
    age = int(input("what is your age:\n"))
    if age <=12:
        print("please pay 5")
    elif age<=18:
        print("please pay 7")
    else:
        print("please pay 12")
        
        want_photo = input("do you want to have a photo taken? press y for yes and n for no")
        if want_photo == "y":
            bill+=3
            
            print(f"your final bill is{bill}")
else:
        print("you cant ride the roller coster")