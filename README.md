# Hangman

## Outline
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is a basic implementation of the Hangman game made using Python, where the computer thinks of a word and the user tries to guess it. This version of Hangman includes different difficulty modes and the choice to guess from different types of words - namely **Animal**, **Vegetable** or **Mineral**. The aim of this project was to create a fully functional game while improving my knowledge of fundamental concepts such as object oriented programming, control flow and a wide range of data types.

## Installation and Initialisation
This game was created and tested using Python 3.10.12. It can be played by executing the *hangman_game_main.py* file. The *hangman_words.py* and *hangman_art.py* modules also need to be in the working directory for it to function, while the milestone files were created while carrying out each basic task of the game's creation and can be ignored.

## Usage Instructions
### Initial Options 
After executing the *hangman_game_main.py* file the user is prompted to choose their difficulty setting:
- **Easy** - This mode give you **8** lives to guess the word
- **Medium** - This mode gives you **6** lives to guess the word
- **Hard** - This mode gives you **4** lives to guess the word
- **Extreme** - This mode chooses a word a list of specially selected words that are extremely tricky to guess in Hangman with only **3** lives

If Easy, Medium or Hard is chosen the user can then decide whether they want to guess an **Animal**, **Vegetable** or **Mineral**, with these categories being meant extremely literally (no fruits or non-mineral inorganic objects)!

### Playing the Game
The user is then prompted to guess letters of an unknown word with its length denoted by underscores, with correct guesses revealing the equivalent letters. It is possible to enter the entire word if it has been deciphered early. If the word is guessed before the user runs out of lives, they win the game!

Wrong guesses will result in a basic ASCII gallows artwork being drawn until all lives are up and a full stick figure is hanging from the gallows! At this point, the game has been lost.

## File structure
- *hangman_game_main.py* - This file contains the main script for the game and it should be executed in order to play it
- *hangman_words.py* - This file contains a dictionary with 50 words for each category. These can be freely edited if desired
- *hangman_art.py* - This file contains all of the ASCII artwork used in the game and some functions which slightly embellish the user interface

## License information
This is free and unencumbered software released into the public domain.




