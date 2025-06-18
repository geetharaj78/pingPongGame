import random
#todo 1- randomly choose a word from the word list and assign it to a variable called chosen_word, then print it. 
#todo 2 - ask the user to guess a letter and asign their answer to a variable called guess, make guess lowercase. 
#todo 3 - check if the letter, the user guessed is (guess) is one of the the letters in the chosen word. print "Right" if yes, and "wrong" if it is not.
word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(f"the chosen word is:{chosen_word}")

place_holder = ""
word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_"

print(place_holder) 

game_over = False

while not game_over:
    guess_word = input("guess a letter in the word: ").lower()

    display = ""

    for letter in chosen_word:
     if letter == guess_word:
        display += letter
     else:
        display += "_"      

    print(display)
    
    if "_" not in display: 
        game_over = True
        print("you win")