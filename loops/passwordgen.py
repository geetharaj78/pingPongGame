import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B''C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers  = ['0','1','2','3','4','5','6','7''8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the pyPassowrd Generator!")
nr_let = int(input("how many letters would you like in your password\n"))
nr_num = int(input("how many numbers would u like in your passwaord\n"))
nr_sym = int(input("how many symbols would u like in your passwaord\n"))

passwordList = []

for char in range(0, nr_let):
     #random.choice() - is used to randomly select single element from a given seq(list, tuple or string)
    passwordList.append(random.choice(letters))
    

for char in range(0, nr_sym):
    passwordList.append(random.choice(symbols))
    

for char in range(0, nr_num):
    passwordList.append(random.choice(numbers))
    
print(passwordList)
random.shuffle(passwordList)
print(passwordList)

password = ""
for char in passwordList:
    password += char
    
print(f"your password is : {password}")