#function that allows for inputs. 
def greet(a):
    print(f"what is your name? {a}")
    print(f"what are you studying {a}")
    print(f"what do you like to do the most? {a}")

# a = geetha and here, a is the parameter and geetha is the argument.here, parameter is the name of the data and argument is the actual value which we are going to store. 
a = input("enter your name: ")
greet(a)

def weeks_inlife(age):
    years = 90-age
    weeks = years*52
    print(f"you have {weeks} weeks left")

a = int(input("enter the age of the person: "))
weeks_inlife(a)

#keyword arguments - instead of just adding the arguments into the function call, 
#we can add each of the parameter names and an equal sign  

def intro(n,l,a):
    print(f"I am {n} and i live in {l}")
    print(f"my age is {a}")
    
name = input("enter your name: ")
location = input("enter the place you live in: ")
age = int(input("my age is: "))
intro(n = name,l = location,a = age)
