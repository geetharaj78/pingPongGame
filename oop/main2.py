

class User:
    def __init__(self,use_id,username,followers):
        self.use_id = use_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.followers += 1


use = User("23","geetha",0)
use1 = User("43","manny",0)

use1.follow(use1)
print(use.followers)
print(use.following)
print(use1.followers)
print(use1.following)

print(use.use_id)
print(use.username)
print(use1.followers)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
class Intro:
    def __init__(self,name,age):
        self.name = name
        self.age = age

n = Intro(name,age)
print(n.name)
print(n.age)




