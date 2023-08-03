# An app to block user password after several attempt

""" Create an app that will request a user to enter 
his/her email and password. Let the user password be our 
default password which is hidden in the code. 
Allow the user to enter his/her password with three 
attempts. If user password is wrong after several try, 
display the message 'Account is blocked!. If user enters 
the correct password, display the message 'Access granted!'. 
"""

# Before we begin, let's define a function
# After, let's declare and initialize five variables
# I'm gonna use two datatype: string and integer

# define function

def password_app(email):

    # declaring of variables

    default_password = "pass231"
    user_old_password = " "
    default_max_try = 0
    user_max_try = 3
    max_try_reach = "not reach"

    # email_valid_character1 = "@gmail.com"
    # empty_email = " "
    # user_email = empty_email
   
    # Utilizing python while loop

    if len(email) < 5 and email != "@gmail.com":
        print("Invalid email address.")
        
    else:
        while user_old_password != default_password and max_try_reach != "Has reached!":
            if default_max_try < user_max_try:
                user_old_password = input("Password: ")
                default_max_try += 1
            else:
                max_try_reach = "Has reached!"
        if max_try_reach == "Has reached!":
            print("Sorry, account blocked!")
        else:
            print("Access granted!")
    

password_app(input("Email: "))

  