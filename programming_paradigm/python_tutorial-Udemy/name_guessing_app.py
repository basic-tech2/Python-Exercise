# Name guessing app in python

""" Create an app wherein user will be ask 
to guess the developer's name.
In the app, ask user for his/her name. Welcome the user
and tell user what's the game about meanwhile half spelling
the developer's name as a hint for the user to get the name
correctly. Ask user to enter developer's name. 
Allow he/she to try for some number of time. 
If the user gets the name correct, alert an appreciation's 
or congratulations' message indicating user name. 
e.g: 'Congratulations, user_neme! You\'re correct'. 
Else, print a message indicating user's name.
e.g: 'Time\'s out, user_name! Try again?'. """

# First, let's create and assign values to our variables

# declare a function and include the below variables in it
# declare a variable for developer's name
# set variable for user guess name input to an empty string
# declare variable for default try which is 0
# declare variable for the max try in int; could be 3 try
# declare a variable 

# --------- declare variables outside the function --------

# declare a variable to ask the user if he/she wants to play again
# If user input is yes, continue
# Else, print thank you message

def guessing_name():
    notes = """This game is about guessing the developer's name. \nHint: A_t_i_n_"""
    user_name = input("What's your name: ")
    developer_name = "Astainy"
    user_guess_name = " "
    default_try = 0
    max_number_of_try = 3
    try_reached = ""
    incorrect_name = "wrong"
    correct_name = "Yes!"
   
    if len(user_name) < 3:
        return print(f"Please enter your name. \n{user_name}")
    else:
        print(f"\nHello, {user_name}! \n{notes}")
        print("------------------------------------------")
        print("Loading....... ")
        print("------------------------------------------")
    #  # Using Python while loop
    while user_guess_name != developer_name and try_reached != "Has reached max try":
        if default_try < max_number_of_try:
            user_guess_name = input("Guess developer's name: ")
            # increment default try by 1
            default_try += 1
            # print Nope if name is wrong
            if user_guess_name != developer_name:
                print(f'{user_name} you are {incorrect_name}. Check the hint above. \nIt is not {user_guess_name}')
            # print Yes if name is correct
            else:
                print(correct_name)
        else:
            try_reached = "Has reached max try"

    if try_reached == "Has reached max try":
        print("Time's out! Try again.")

    else:
        print(f"Congratulations, {user_name}! You're correct. ")

guessing_name()

# If the game ends by either lose or win, 
# ask the user to press P to continue the game
# or press Q to quit the game. If user presses P, restart
# the game. Elif user presses Q, quit the game with a message.
# Else, ask the user again as to whether he/she want to 
# continue or quit the game by either presssing Q for quit
# or P to continue.

# Continue_the_game = "P"
# quite = "quit"
# ask_user = ""
# continue_playing = 0
# max_number_of_play = 1000

# while ask_user != Continue_the_game and quite != "Q":
    
#     if continue_playing < max_number_of_play:
#         ask_user = input("Press P to continue or Q to quit: ")
#         continue_playing += 1
#         guessing_name()
       

#         # if ask_user == Continue_the_game:
#         #     # ask_user = input("Press P to continue or Q to quit: ")
#         #     guessing_name()
#     # elif ask_user == quite:

#     else:
#         quite = "Q"
#         # print("Thank you for playing!")
#         # quit()
#         # print(ask_user)
# if quite == "Q":
#     print("Thank you for playing!")
#     quit()
# else:
#     print(ask_user)


