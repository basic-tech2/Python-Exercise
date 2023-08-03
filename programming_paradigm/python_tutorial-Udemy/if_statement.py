#Understanding if statement

var0 = True
var1 = False

if var0:
    print('It\'s true')

numb1 = 5
numb2 = 3

if numb1 == numb2:
    print('They are the same number.')

else:
    print('They are not the samea number.')


color1 = "Red"
color2 = "Blue"
color3 = "White"
color4 = "Orange"

if color1 == color2:
    print("Red and Blue are the same color ")

else:
    print('They are not the same color')

print('\n')
# Build an app to find out who is the richest person between two psersons

#1. Find out the name of each person
#2. Find out how much money does the user have
try:
    personName1 = input("First person what is your name? ")
    wallet1 = float(input('How much money do you have? '))
except:
    print('Invalid input.')

try:
    personName2 = input("Second person what is your name? ")
    wallet2 = float(input('How much money do you have? '))
except:
    print('Invalid input.')

try:
    personName3 = input("Third person what is your name? ")
    wallet3 = float(input('How much money do you have? '))
except:
    print('Invalid input.')


try:
    if wallet1 > wallet2 and wallet1 > wallet3:
        print(f'{personName1} is the richest.')

    elif wallet2 > wallet1 and wallet2 > wallet3:
        print(f'{personName2} is the richest.')

    elif wallet3 > wallet1 and wallet3 > wallet2:
        print(f'{personName3} is the richest.')

    else:
        print('All of them are broke like me.')

    print('\n')

except:
    print(f'Either of you entered an invalid input.')


