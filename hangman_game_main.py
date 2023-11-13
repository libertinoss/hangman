from hangman_words import hangman_words_dict
from hangman_art import strikethrough, display_dots, hangman_gallows_sequence, you_won, you_lost
import random
import sys

class Hangman():
    """    
    This class is used to represent a game of Hangman

    Attributes:
            word (str): The word to be guessed, chosen at random from a list
            word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed
            num_letters (str): The number of UNIQUE letters in the word that have not been guessed yet
            num_lives (int): The numer of lives the user has
            word_list (string): The list of words that a word is chosen from at random
            list_of_guesses (list): The list of letters the user has already guessed
    """
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.list_of_bad_guesses = []

    def check_guess(self, guess):
        '''
        This function is used to check if the letter guessed is in the word.
        If it is, it replaces the underscore(s) in word_guessed with the letter.
        Otherwise, it takes away a life and displays the hangman gallows artwork at the appropriate stage.

        Args:
                guess (str): the guess made by the user
        '''
        guess = guess.lower()
        print(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            index = 0  
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[index] = guess  
                index += 1
            self.num_letters -= 1   
        else:
            self.num_lives -= 1
            self.list_of_bad_guesses.append(guess)
            self.display_hangman_art()
            if self.num_lives == 1:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have 1 life left") #Added purely to have correct grammar for this unique case
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        '''
        This function is used to check if the user provides a valid input
        (a single alphabetical character which hasn't been guessed).
        It will keep asking until they do so.
        I've included one special case for the user entering the whole
        word exactly as I noticed it was cumbersome typing each individual letter 
        once you have figured out the word. 
        '''
        print(' '.join(self.word_guessed))
        guess = input("Please enter a single letter: ")
        if guess.lower() == self.word:
            print("Ok Speedy Gonzalez, I did say a single letter, but", end=' ')
            display_dots() #three dots printed one after the other for suspense
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
        '''
        This function is used for printing the appropriate stage of the 
        hangman gallows art sequence, which is made up of 8 ASCII art drawings.
        If the difficulty setting is set to more than 7 lives the first 
        drawing (just the gallows frame) is depicted until the number of lives
        falls below that number.
        It also displays all incorrectly guessed letters with a strikethrough.
        '''   
        if self.num_lives > 7:
            print(hangman_gallows_sequence[0])
        else:
            print(hangman_gallows_sequence[7 - self.num_lives])
        print(strikethrough(self.list_of_bad_guesses))

def main_menu():
    """
    This function displays an initial greeting to the user upon running the game 
    and allows them to choose a difficulty setting.
    These difficulty settings correspond to having a different number of lives.
    At this stage they are hard-coded below but in the future a dedicated settings
    menu may be added where the user can define the number of lives for each
    difficulty themselves.
    Following a selection the mode_menu function is executed to choose what kind of 
    word they want to guess.
    A special case is where the user chooses the extreme difficulty setting, in which
    case the mode_menu function is not exectured, and their word to guess is randomly 
    chosen from from a specially selected list of extremely tricky words, with only
    3 lives for them to guess it.

    Returns:
            word_list (list): A list of words corresponding to the user's choice in the mode_menu function
            num_lives (int): The number of lives corresponding to user's difficulty choice in this function
    """      
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
    """
    This function allows the user to choose whether they want to guess an animal, mineral
    or vegetable, with their choice returning the appropriate list of words.

    Returns:
            word_list (list): A list of words corresponding to the user's choice
    """    
    while True:
        user_mode = input("Would you like to guess an animal, vegetable or mineral? \nPlease type A, V or M! ").lower()
        if user_mode not in ['a','v','m']:
            print("Invalid input, please type A, V or M!")
        else:
            word_list = (hangman_words_dict[user_mode])
            break
    return word_list


def play_game():
    """
    This function contains the overarching logic for playing the game.
    When the user runs out of lives the appropriate ASCII art is displayed
    for losing the game and the game stops.
    When the user has guessed all of the letters in the word, the appropriate
    ASCII art is displayed for winning the game and the game stops.
    Otherwise, the user is prompted for their guess and the game runs until 
    one of the aforementioned two conditions is met.
    """   
    word_list, num_lives = main_menu()
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"The word was {game.word}")
            print(you_lost)
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(you_won)
            break

play_game()
            