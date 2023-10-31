import random
import sys
from hangman_words import hangman_words_dict
from hangman_art import strikethrough, display_dots, hangman_gallows_sequence, you_won, you_lost

class Hangman():
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.list_of_bad_guesses = []

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
            self.list_of_bad_guesses.append(guess)
            self.display_hangman_art()
            if self.num_lives == 1:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have 1 life left")
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
        print(' '.join(self.word_guessed))
        guess = input("Please enter a single letter: ")
        if guess.lower() == self.word:
            print("Ok Speedy Gonzalez, I did say a single letter, but", end=' ')
            display_dots()
            print(you_won)
            sys.exit()    
        elif guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
            
    def display_hangman_art(self):
        if self.num_lives > 7:
            print(hangman_gallows_sequence[0])
        else:
            print(hangman_gallows_sequence[7 - self.num_lives])
        print(strikethrough(self.list_of_bad_guesses))

        

def main_menu():
        difficulty_settings_dict = {'e': 8,
                                    'm': 6,
                                    'h': 4}
        print("Welcome to Hangman!")
        while True:
            user_difficulty = input("Would you like to play easy, medium, hard or extreme mode? \nPlease type E, M, H or X! ").lower()
            if user_difficulty not in ['e', 'm', 'h', 'x']:
                print("Invalid input, please type E, M, H, or X!")
            elif user_difficulty == 'x': 
                print("You have chosen Extreme! Your word is extremely rarely guessed in Hangman, and you only have 3 lives!")
                word_list = list(hangman_words_dict['x'])
                num_lives = 3
                break
            else:
                num_lives = difficulty_settings_dict[user_difficulty]
                word_list = mode_menu()
                break
        return word_list, num_lives
               

def mode_menu():
    while True:
        user_mode = input("Would you like to guess an animal, vegetable or mineral? \nPlease type A, V or M! ").lower()
        if user_mode not in ['a','v','m']:
            print("Invalid input, please type A, V or M!")
        else:
            word_list = (hangman_words_dict[user_mode])
            break
    return word_list


def play_game():
    word_list, num_lives = main_menu()
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(you_lost)
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(you_won)
            break

play_game()
            