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
            for letter in range(len(self.word)):
                if guess == self.word[letter]:
                    self.word_guessed = guess
                    #self.word_guessed = guess * len(self.word)
                else:
                    letter = self.word_guessed[letter]
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
        #self.num_letters - 1

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter:")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break
                
player1 = Hangman(word_list)
player1.ask_for_input()










       



    



 