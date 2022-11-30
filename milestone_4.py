import random
from random import choice
word_list = ["Guava", "Banana","Apple", "Blueberry", "Mango"]

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess (self, guess):
        guess = guess.lower()
        if  guess in self.word:
            print(f"Good guess! {guess} is in the word.") 
            #self.list_of_guesses.append(guess) 
        else: 
            print(f"Sorry, {guess} is not in the word. Try again.")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter:")
            if guess.isalpha() and len(guess) == 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in [self.list_of_guesses]:
                print("You already tried that letter!")
            else:
                guess = self.check_guess
                
player1 = Hangman(word_list)
player1.ask_for_input()









       



    



 