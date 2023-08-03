
#------- Self practice after complating the first section of Udemy 
#Python beginner course ------

# """ Writed a program that will interact with the user. 
# The program should be a game like; writing of the 26 alphabet in English randomly. """

#STEPS

#1. Get user name
#2. Display the rules of the game to the user
#3. Set a condition. If user agrees to the rules  continues. Else, quite the game with a message

def LetterGeme():
    UserName = input('Please enter your name: ')
    rules = input(f'Hi {UserName}! You are to enter the next letter after the displayed letter in the English alphabet. Do you agree? ')

    if rules != 'yes':
        return print('Please try again!')
    else: print('Starting......')
    
    quest1 = input('what\'s the next letter after "A" : ')
    if quest1 != 'B' and quest1 != 'b':
        print('Wrong! ')
        return print('Please try again! ') 
    else: print('Correct! ')
    
    quest2 = input('What\'s the next letter after "E" : ')
    if quest2 != 'F' and quest2 != 'f':
        print('Wrong! ')
        return print('Please try again! ')
    else: print('Awesome! ')

    quest3 = input('What\'s the next letter after "C" : ')
    if quest3 != 'D' and quest3 != 'd':
        print('Opps! ')
        return print('Please try again! ')
    else: print('Excellent! ')

    quest4 = input('What\'s the next letter after "K" : ')
    if quest4 != 'L' and quest4 != 'l':
        print('Nope! ')
        return print('Please try again! ')
    else: print('That\'s good! ')

    quest5 = input('What\'s the next letter after "I" : ')
    if quest5 != 'J' and quest5 != 'j':
        print('Not true! ')
        return print('Please try again! ')
    else: print('Well taken! ')

    quest6 = input('What\'s the next letter after "G" : ')
    if quest6 != 'H' and quest6 != 'h':
        print('Are you serious! ')
        return print('Please try again! ')
    else: print('Passed! ')

    quest7 = input('What\'s the next letter after "Q" : ')
    if quest7 != 'R' and quest7 != 'r':
        print('You must be joking, right? ')
        return print('Please try again! ')
    else: print('Perfect! ')

    quest8 = input('What\'s the next letter after "Y" : ')
    if quest8 != 'Z' and quest8 != 'z':
        print('Who change it? ')
        return print('Please try again! ')
    else: print('You are smart! ')

    quest9 = input('What\'s the next letter after "M" : ')
    if quest9 != 'N'and quest9 != 'n':
        print('It can\'t work here! ')
        return print('Please try again! ')
    else: print('Yeah you are right! ')

    quest10 = input('What\'s the next letter after "S" : ')
    if quest10 != 'T' and quest10 != 't':
        print('You missed it! ')
        return print('Please try again mehn! ')
    else: print('Correct! ')

    quest11 = input('What\'s the next letter after "W" : ')
    if quest11 != 'X' and quest11 != 'x':
        print('plus -0 ')
        return print('Please try again! ')
    else: print('K.O! ')

    quest12 = input('What\'s the next letter after "U" : ')
    if quest12 != 'V' and quest12 != 'v':
        print('Not really! ')
        return print('Please try again! ')
    else: print('Yes! you get it. ')

    quest13 = input('What\'s the next letter after O" : ')
    if quest13 != 'P' and quest13 != 'p':
        print('Not really! ')
        return print('Please try again! ')
    else: print(f'Congraulations, {UserName}! You\'ve made it. ')

LetterGeme()