# Create a small basic app that will be a conversation between a user and a person

#Tell the rules to the user - either yes or no
#If yes, ask next question
#If no, abort conversation

def conversation():
    rules = input('Answer yes or no. Do you agree? ')
    if rules != 'yes':
        return print('Try again! ')
    else: print('Next qestion ')
    quest1 = input('Are you hungry? ')
    if quest1 != 'yes':
        return print('Let\'s go for a walk. ')
    else: print('Next question ')
    quest2 = input('Would you like to eat at a resturant? ')
    if quest2 != 'yes':
        return print('Come eat at my place. ')
    else: print('Next question ')
    quest3 = input('Do you want to eat Rice? ')
    if quest3 != 'yes':
        return print('Let\'s go eat a burgar then. ')
    else:
        print("Let's go eat Rice. ")


conversation()