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
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()  # Flush the output buffer to display immediately
        time.sleep(0.8)      # Wait for 0.5 seconds
    print() 

#print(you_won)
#print(you_lost)



