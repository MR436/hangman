# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. 

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. The code is written using Python in visual studio editor and github.
# Milestone 2
Building a project on Hangman game, where users will guess a word within certain attempts. The updates are pushed from visual studio to git hub repository.
A list is created that contain name of the fruits. The program displayed a random name from the list. 
The user is asked to provide a string value input. The program will check if the input value is an alphabet or no. The code written through an error message if the input is less than one letter and not an alphabet “Oops! That is not a valid input."
Random.choice method is used that select a letter from the given sequence. It can be a list, tuple, dictionary and more.
If statement is added to check if the input given is valid or not. The code checks the input in two levels: 
1.The length of input should be more than 1 value; and
2.The value should be an alphabet
These functions are used to check the condition in IF statements: len () and ().isalpha. 
If the input is valid, the program print = “Good guess!”
 Otherwise, it print “Oops! That is not a valid input”

Then break command is used to stop the program from asking multiple inputs. 
import random
from random import choice
word_list = ["Guava", "Banana","Apple", "Blueberry", "Mango"]
print(word_list)
word = random.choice(word_list)
print(word)
print("The random word is:", (word))
guess = input("Please enter a single letter:")
print(guess)
while True:
    guess = input("Please enter a single letter:")
    if len(guess)>1 and (guess).isalpha:
        print("Good guess!")
    else: 
        print("Oops! That is not a valid input.")
        break

# Milestone 3
The code has two functions: check_guess and ask_for_input
check-guess function takes the guessed letter convert to lower case and check if the guessed letter is in the word.
Then accordingly it prints the message for the user.
ask_for_input function request for input from user check for two conditions: if input is string value and more than one character.
check_for_guess function is called in ask_for_input function first that if the letter is in the word.




