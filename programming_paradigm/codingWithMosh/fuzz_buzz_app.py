# A Fuzz Buzz App in Python
""" Create an app that takes an input,
and depending on the inputs given, you should 
return different results. 

Rule: 
1. If the input given is divisible by 3,
you should return the string 'Fizz'.
2. If the input is divisible by 5, you should
return 'Buzz'.
3. If the input is divisible by both 3 and 5, 
you should return FizzBuzz 
For any other number that are not divisible
by 3 and 5, you should return the 
same input. """

def my_app():

    user_name = input("What's your name: ")

    rules = f"""\nHi {user_name}, Here are the game rules:
    1. If you give an input that is divisible by 3, 
       you will see Fizz.

    2. If you give an input that is divisible by 5, 
       you will see Buzz.

    3. If you give an input that is divisible by both 3 and 5,
       you will see FizzBuzz.

    4. If you give an input that is not divisible by either 3 or 5, 
       you will see the same input.\n"""
    
    if len(user_name) >= 3 and len(user_name) != 0:
         print(rules)
    else:
        print("Please enter your name.")
        exit()
   
    try:
        inputs = int(input("Enter number: "))

        if (inputs % 5 == 0) and (inputs % 3 == 0):
            return "FizzBuzz"
        elif inputs % 5 == 0:
            return "Buzz"
        elif inputs % 3 == 0:
            return "Fizz"
        else:
            return f"The same input is: {inputs} "
    except ValueError:
        return ("Please enter number(s)!")

return_function = my_app()
print(return_function)