# Errors handling in Python

# sytax error
# print(2*3). 

# zero division error or logical error
# print(1/8)

try:
    user_entry = int(input("Enter number: "))
    x = user_entry + 1
    print(f"The number is {x}")
except ValueError:
    print("Please enter a number.")
