import random
from random import choice


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
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    #self.word_guessed = guess * len(self.word)
                #else:
                                #letter = self.word_guessed[letter]
            self.num_letters -= 1
            print(self.word_guessed)
           
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
        

    def ask_for_input(self):
        #while True:
            guess = input("Please enter a single letter:")
            
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                
def play_game (word_list):

    game = Hangman(word_list, 5)
    
    while True:
        if game.num_lives == 0:
            print("You Lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            
        else:
            print("Congratulations. You won the game!")
            break
            #if game.num_lives !=0 or game.num_letters >= 0:
        
word_list = ["Guava", "Banana","Apple", "Blueberry", "Mango"]
word_list = [i.lower() for i in word_list]
play_game(word_list)












       



    



 