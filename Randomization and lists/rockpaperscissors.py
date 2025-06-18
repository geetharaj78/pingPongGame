import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input("what do u choose? 0 for rock, 1 for paper, 2 for scissors")

comp = random.randint(0,2)
print(f"computer choice {comp}")

if user==0 and comp == 2:
    print("you win!")
elif comp ==0 and user == 2:
    print("you loose!")
elif comp > user:
    print("you loose!")
elif comp == user:
    print("its a draw!")
elif user>=3 or user<0:
    print("you typed an invalide number, you loose")