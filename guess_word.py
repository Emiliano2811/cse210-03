import csv
import random
guessed_word = []

with open("wordlist.csv") as f:
    chosen_word = random.choice(f.readlines()).strip()
print(chosen_word)
for i in range(len(chosen_word)):
    guessed_word.append("_")
print(*([i for i in guessed_word]))


tries = 5

while(tries):
    tries = tries - 1 
    guessed_letter = input("Guess a letter [a-z]: ")
    if guessed_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guessed_letter:
                guessed_word[i] = chosen_word[i] 
    else:
        """if guessed_letter is not in original_word 
           prompt user for wrong chosen letter"""
        print("You Guessed wrong letter")
        
    guess_word = [i for i in guessed_word]
    guess_word = "".join(guess_word)
    if chosen_word ==guess_word :
        print("You have Got the letter ...")
        exit(0)


    print(*([i for i in guessed_word]))

print(chosen_word)