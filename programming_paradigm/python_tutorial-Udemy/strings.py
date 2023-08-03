# --------- July 8, 2023 ---------

# myString = "Hello word"


# print(myString[0])

# print(myString[-1])

# print(6//8)
# print(6/8)

# print(6%8)

print('The {} {} {} {}' .format('boy', 'ate', 'his', 'food'))
print('The {f} {a} {h} {b}' .format(b='boy', a='ate', h='his', f='food'))

Something = input(f'Say something: ')
print("Awesome! I like the part that say {}" .format(Something))
letter = 'Morris'
ChangeLetter = letter[1:]
text = "L" + ChangeLetter

print(text * 3)

x = 'Hi this is python split string split method.'

print(x.split())

print(x.split('i'))

userName = input(f"Please enter your name: ")
reverse = userName[::-1]
rePrint = userName[::2]
# saySomething = userName[8:11] #abcdefghijkl
print(f'Your name contains {len(userName)} characters.\nIt is spelt backward as: {reverse.upper()} \nSome characters are: {rePrint}')


# Create a program that takes user's input and displays it using the following string methods learned
#Okay here is the algorithm of the program.

# 1. Create a variable that will prompt user for his/her name
# 2. Create another variabel and assign the user's input to it
# 3. Use the all the string methods you learn from he lecture
import random
UserInput = input(f"Enter your name again, please!: ")
# List of string methods: len(not only string thou), upper, indexing, slicing, and spliting

TextAssign1 = UserInput.upper()
print(f'Your name is: {TextAssign1}')
TextAssign2 = len(UserInput)
print(f'Your name has {TextAssign2} characters.')
TextAssign3 = UserInput[-1]
print(f'The last character in your name is: {TextAssign3}')
TextAssign4 = UserInput[::-1]
print(f'Your name is written backward as: {TextAssign4}')
TextAssign5 = UserInput.split(random.choice(UserInput)) 
print(f'Your name is in a list form with double letters missing: {TextAssign5}')

