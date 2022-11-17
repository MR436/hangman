while True:
    guess = input("Please enter a single letter:")
    if len(guess)>1 and (guess).isalpha:
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input.")
#word = "apple"
#guess = input("Please enter a single letter:")
#if guess in word:
    #print(f"Good guess! {guess} is in the word.") 
#else:
    #print(f"Sorry, {guess} is not in the word. Try again.")

 