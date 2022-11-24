word = "apple"
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




 