import random
import string

word_list = ["apple", "banana", "passion fruit", "strawberry", "orange"]
word = random.choice(word_list)
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess in string.ascii_lowercase:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.") 

