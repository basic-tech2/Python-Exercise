# Write a program that will sell fruit to a user.
# There should be three different kinds of fruits: Cheese, Mourche Biscuit, and Pavini Milk. 
# The price of the cheese is $50.00, the mouche Biscuit cost $100.00 and the Pavini Milk cost $35.

#1. Request the user's name 
#2. Display the list of fruits and their prices.
#3. Ask the user to pick his/her favorite fruit. 
#4. Ask the user how many quantity he/she wants to buy.
#4. Display the total bill the user will pay for the fruit.
#5. Thank the user for purchesing.

def shopping():
    UserName = input('What is your name: ')
    SomeFruite = input(f"Hello {UserName}! Please choose your favorite fruit by the labelled number: \n1. Mouches Biscuit ---- $100.00 \n2. Milk Cheese -------- $50.00 \n3. Pizza -------------- $200.00 \n..........  ")
    quantity = input(f"{UserName} how many quatity do you want to buy? ")
    fruit1 = float(100) * float(quantity)
    fruit2 = float(50) * float(quantity)
    fruit3 = float(200) * float(quantity)

    if SomeFruite != '1' and SomeFruite !='2' and SomeFruite != '3':
        return print('We don\'t have such fruit here.')

    if SomeFruite == '1':
        print(f'Your total bill is: {fruit1}')
        return print('Thank you for purchasing. Enjoy your Sweet Biscuit!')
        
    if SomeFruite == '2':
        print(f'Your total bill is: {fruit2}')
        return print('Thank you for purchasing. Feel yourself with Milk Cheese!')
        
    if SomeFruite == '3':
        print(f'Your total bill is: {fruit3}')
        return print('Thank you for purchasing. Enjoy your Pizza!')
    else: print('You don\'t have much funds to buy.')

shopping()
