"""Bagels, by Astainy
A deductive logic game where you must guess a number based on clues.
View this code at https://mostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own 
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 4 #(!) Try setting this to 1 or 10.
MAX_GUESSES = 6 # (!) Try setting this to 1 or 100.


def main():
    print(f'''Bagels, a deductive logic game.
    By Astainy
    
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:         That means:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.

    For example, if the secret number was 2478 and your guess was 2843, the
    clues would be Fermi Pico. ''')

    while True: # Main game loop.
    #This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looping until they enter a avalid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

            # Ask player it they want to play again.
            print('Do you want to play again? (yes or no)')
            if not input('>').lower().startswith('y'):
                break
        print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) #Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the corrct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
                # A correct digit is in the incorrect place.
                clues.append('Pico')
    if len(clues) == 0:
            return "Bagels" # There are no correct digits at all.
    else: 
            # Sort the clues into alphabetical order so their original order
            # doesn't give information away.
            clues.sort()
            # Make a single string from the list of string clues.
            return ''.join(clues)

        
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

# Programming is a skill that you improve by programming.

# --------------------------------------------------------------

# In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.

#-------------------------------------------------------------------