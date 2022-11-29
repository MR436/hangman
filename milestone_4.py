import random
from random import choice
class Hangman():
    def __init__(self, word, word_guessed, num_letters, word_list, list_of_guesses, num_lives = 5, ):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses

        #word_list = ["Guava", "Banana","Apple", "Blueberry", "Mango"]
        #num_lives = 5
        

        word_list =  ['_', '_', '_', '_', '_']
        word = random.choice(word_list)

       




        pass
    


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.") 
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter:")
        if guess.isalpha() and len(guess) == 1:
            print("Good guess!")
            break
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)

ask_for_input()




 