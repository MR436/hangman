word = "apple"
guess = input("Please enter a single letter:")
if guess in word:
    print(f"Good guess! {guess} is in the word.") 
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

 