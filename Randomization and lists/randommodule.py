import random 
import module
#package which is created by python language to generate random numbers

a = int(input("enter the first number; \n"))
b = int(input("enter the last number\n"))
rando = random.randint(a,b)
print(rando)
rando1 = random.randint(1,25) # this is a function which is used to generate random number withtin the range of the guven numbers
print(rando1)
#a random module is a python module - when we have a large code which is written in scripts, and when the script is very large, we divide them into different modules(functions) which does different operations.
# we can also create our own modules. 
print(module.a)
print(module.b)
