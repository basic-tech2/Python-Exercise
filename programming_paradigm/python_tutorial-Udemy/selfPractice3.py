# Write a program that will request a user to put three things in his/her bag for lunch
# Write a program that will display the game's rules, request the user name, 
# askes he/she to put three things 
# in his/her bag and later display all three things he/she placed in his/her bag. 

#1. Get user's name
#2. Prompt game's rules to the user
#3. If user agrees to the rules, continues. Else, quite the game
#4. List the available items to the user asking he/she to pick three items
#5. Get user input of the three items
#6. Display all the three things with a message to the user

def collections():

    #Get user's name
    UserName = input('What is your name: ')

    #Prompt game's rules to the user
    rules = input(f'Hi {UserName}, you are to pick three items from our shop. Do you agree? ')
    print('\n')
    #set the condition

    if rules != 'yes':
        return print('Please try again!') 
    else: print('Starting.........')

    #List the available items to the user
    item = input(f'''Hey {UserName}! Here are the available items we have for now. \nPlease pick three items according to the number labelled on each. 
                                    \n1. Executive Pen 
                                    \n2. 32Gb Pen Drive 
                                    \n3. Chrome Book 
                                    \n4. Notepad 
                                    \n5. iPhone 12 Pro Max 
                                    \n........... ''')

    if item != '1' and :
        return print('You lose! Try againy.')
    else: print(f'You have chosen Executive Pen ')
    item2 = input('Please choose again: ')

    if item2 != '2':
        return print('Please again!')
    else: print('You\'ve chosen 32Gb Pen Drive ')
    

collections()


