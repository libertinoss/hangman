import random

word_list = ["apple", "banana", "pear", "strawberry", "orange"]
word = random.choice(word_list)
print(word)

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    print(guess)
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()
