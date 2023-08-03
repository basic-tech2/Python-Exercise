# It is noted that Python execute its code line by line but while upon reassigning 
# of value to the same variable it ignores the first assignment and execute the 
# second assignment bearing the same variable? like the example below:
    # age = 40, 67, 45 ----- it ignores the first value
    # age = 20 --------- it execute the second value

# age = 69
# age1 = 'Hello'
# print(age)
# print(type(age))
# print(age1)


# # Strings methods
# course = "Python tutorial for beginners by Mosh "
# print(course.replace('for', '4'))
# print(course.find('Python'))
# print("Mosh" in course)

#Arithmatic operator

# x = 20
# print(x * 3)

# x += 5
# print(x)

# a = (10 + 3) * 2
# # a = 10 + 3 * 2

# print(a)

# #Comparison operator

# # >
# # <
# # >=
# # <=
# # ==

# # Local Operator

# price1 = 25
# print(price1 > 10 and price1 < 30) # return True because price1 is in the range of 10 and 30

# price2 = 5
# print(price2 > 10 or price2 < 30) # return True because one of the value true - price is less than 30

# price3 = 15
# print(not price3 > 20) # return True because price3 is not grater than 20
# # and --- (both)
# # or ----- (at least one)
# # is
# # not

# # If Statement

# temperature = float(input('What is the Temperature in your area: '))

# if temperature > 35:
#     print("It's hot day!")
#     print("Drink enough water.")
# else:
#     print('It\'s a nice day!')


# While Loops

    #NOTE: You cannot concatinate a number to a string

# i = 1

# while i < 10:
#     print(i * '*') # You can multiply a number by a string and it will repeat the string based on the value of that number in a loop
#     i = i + 1

# # List in Python
# names = ["John", "Mosh", "Mary", "Peter"]
# names[0] = "Joe"
# print(names[-1])
# print(names[0:3])

# # List methods in python
# names.append("Harris")
# print(names)

# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# numbers.insert(0, -1)
# numbers.remove(4)
# #numbers.clear()
# print(numbers)
# print(len(numbers))
# print(3 in numbers)

# # For loops in python
# number = [1, 2, 3, 4, 5, 6, 7]
# ListOfNames = ["1. Peter", "2. March Bae", "3. Finda", "4. Harris", "\n"]

# for names in ListOfNames:
#     print(names)
# for something in number:
#     print(something)


# # range() function in python 

# print(range(10))
# for items in range(2, 10, 2):
#     print(items)

# Tuples on python

number = (1, 2, 3, 4, 5, 4, 2, 6, 6)
print(number)
print(number.count(4))

