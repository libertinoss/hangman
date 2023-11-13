"""Hangman Art

This module contains:
    * hangman_gallows_sequence - the hangman gallows ASCII art sequence
    * you_won, you_lost - the ASCII artd isplayed at the end of the game for winning 
    or losing the game
    * strikethrough - a function for striking through the incorrect letter guesses
    * dots - a function to display three dots in sequence to build suspense in the  
    special case of the user guessing the entire word directly
"""

import sys
import time

hangman_gallows_sequence = ["""
    +---+
        |
        |
        |
        |
        |
  =========
""",
"""
    +---+
    |   |
        |
        |
        |
        |
  =========
  """,
  """
    +---+
    |   |
    O   |
        |
        |
        |
  =========
  """,
  """
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
  """,
  """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
  """,
  """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========
  """,
  """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========
  """,
  """
    +---+
    |   |     
    O   |
   /|\\  |
   / \\  |
        |
  ========
  """]

# You can now print or use the hangman_art variable in your program.

def strikethrough(text):
    """
    This function takes a string as input and returns it with all characters 
    replaced by their strikethrough equivalent.
    Args:
        text (string): The characters to strikethrough

    Returns:
      result (string): The characters replaced by their strikethrough equivalent
    """
    result = ''
    for c in text:
        result = result + c + '\u0336' + " "
    return result

you_lost = """
 __   __          _        _   _ 
 \\ \\ / /__ _  _  | |___ __| |_| |
  \\ V / _ \\ || | | / _ (_-<  _|_|
   |_|\\___/\\_,_| |_\\___/__/\\__(_)
"""

you_won = """
 __   __                          _ 
 \\ \\ / /__ _  _  __ __ _____ _ _ | |
  \\ V / _ \\ || | \\ V  V / _ \\ ' \\|_|
   |_|\\___/\\_,_|  \\_/\\_/\\___/_||_(_)
                                    
"""

def display_dots():
    """
    This function displays three dots in sequence to build suspense in the  
    special case of the user guessing the entire word directly
    """
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()  # Flush the output buffer to display immediately
        time.sleep(0.8)      # Wait for 0.8 seconds
    print() 




