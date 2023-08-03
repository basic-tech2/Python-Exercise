# Practice 1: Creaiting and blocking password

"""Create a small app where user will enter his/her password.
If he/she does not enter the correct password for a set
number of time, display the message 'Account block!'.
If the user get the correct password, display 
the message 'Access granted!'. """

# 1. We will need two data type: basically, string and numbers 
# 2. We will need five variables 

user_password = "pass1234" # variable 1
user_answer = " " # variable 2
number_of_try = 0 # variable 3
number_of_max_try = 3 # variable 4
max_try = "Not reach" # variable 5

while user_answer != user_password and max_try != "Reached":
    if number_of_try < number_of_max_try:
        user_answer = input("Enter password: ")
        number_of_try += 1
    else:
        max_try = "Reached"
if max_try == "Reached":
    print("Account block!")

else:
    print("Access granted!")
