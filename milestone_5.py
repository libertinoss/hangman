import random
word_list = ["apple", "banana", "pear", "strawberry", "orange"]

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        print(guess)
        #print(self.num_lives)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            index = -1
            for letter in self.word:
                index += 1
                if guess == letter:
                    self.word_guessed[index] = guess  
            self.num_letters -= 1   
        else:
            self.num_lives -= 1
            if self.num_lives == 1:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have 1 life left")
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
       #print(self.word)    
       #print(f"self.num_letters: {self.num_letters}")
        print(' '.join(self.word_guessed))
        guess = input("Please enter a single letter: ")
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
             print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(word_list)
            

        


