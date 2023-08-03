# User_input = int(input("Enter 1 for Harris or 0 for Astainy: "))

# for i in range(6):
#     if User_input == 1:
#         print("Harris")
#     elif User_input == 0:
#         print("Astiany")
        



# for i in range(1):
#     get_number = int(input("Enter number(s): "))
#     if get_number % 2 == 0:
#         print(f"{get_number} is an even number. ")
#     elif get_number % 2 != 0:
#         print(f"{get_number} is an odd number. ")


# user_input = input("Search for dalect: ")
# dalects = ["Bassa", "Kpelle", "Kru", "Gio", "Via"]

# for dalect in dalects:
#     if dalect == user_input:
#         print("Dalect found! ")
#     break
# else:
#     print("Dalect not found! ")


# try:
#     number = int(input("Enter a number: "))

#     i = 2
#     while i < number:
#         if number % i == 0:
#             print( number, 'is not a prime number as it ', number //i, 'times', i )
#             break
#         i += 1 
#     else:
#         print(f"{number} is a prime number. ")
# except ValueError:
#     print("Wrong input!")      

# for i in range (3):
#     user_password = input("Enter password: ")
#     if user_password == "Astainy":
#         print(f"Access granted!")
#         break
#     else:
#         print(f"Wrong password!")

# while True:
#     user_password = input("Enter password: ")
#     if user_password == "Astainy":
#         print(f"Access granted!")
#         break
#     else:
#         print(f"Wrong password!")

"""Write a program to display even numbers between 1 to 10. 
When you run the program you should see 2, 4, 6, and 8.
After, print this message 'We have 4 even numbers.' """

# Utilizing the for loop
# || the range function
# condition statement

# for number in range(1, 20):
#     if number % 2 == 0:
#         print(number)
# print(f'We have {number.bit_length()} even numbers.')

increment = 0

for i in range(1, 20):
    if i % 2 == 0:
        print(i)
        increment += 1
    
print(f"You have {increment} nunber of element. ")


