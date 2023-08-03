"""Create a simple calculator that will apply the following
arithmatic operations: add, substract, divid, multiply. """

# ---------------------------------------------------------------------
#    Create function for each operation
#    Pass two paremeter into each function
#    Create a variable assigning those two parameter to it
# ---------------------------------------------------------------------


def add(a, b):
    answer = a + b
    print("Answer: " + str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b):
    answer = a * b
    print("Answer: " + str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divid(a, b):
    answer = a // b
    print("Answer: " + str(a) + " / " + str(b) + " = " + str(answer) + "\n")

def substract(a, b):
    answer = a - b
    print( "Answer: " + str(a) + " - " + str(b) + " = " + str(answer) + "\n")

# add(int(first_number), int(second_number))

while True:
    choices = input("""Hi! Please choose one of the operation below: \n1. Addition \n2. Multiplication \n3. Divistion \n4. Substraction \nE. Exit \n>>>>> """)
    if choices == "1":
        print("Addtion")
        argument1 = int(input("First number: "))
        argument2 = int(input("Second number: "))
        add(argument1, argument2)
        start =+ 1
        
    elif choices == "2":
        print("Multiplication")
        argument1 = int(input("First number: "))
        argument2 = int(input("Second number: "))
        multiply(argument1, argument2)

    elif choices == "3":
        print("Division")
        argument1 = int(input("First number: "))
        argument2 = int(input("Second number: "))
        divid(argument1, argument2)

    elif choices == "4":
        print("Substraction")
        argument1 = int(input("First number: "))
        argument2 = int(input("Second number: "))
        substract(argument1, argument2)

    elif choices == "e" or choices == "E":
        print("Thank you!")
        exit()
    else:
        print("-------- Please select from the list. --------- ")


