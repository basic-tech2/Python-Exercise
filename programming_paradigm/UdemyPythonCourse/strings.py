# Slacing of string in Python

myString = "Hello World!"
letter = "abcdefghijklmnopqrstuvwxyz"

print(letter[3:6])
print(len(myString))
print(myString[::-1])

#String immutability

name = "Joe"
# name[0] = 'D' # String is immutable
name = 'Doe'
print(name)

#string concatenation

name = 'John'
half_name = "D" + name[1:]
print(half_name)

text = 'Hello World!'
x = text + " It's beautiful outside. \n"

print(x * 2)

x = 'Hello World!' + ' This is a string'
x = x.upper()
print(x)
x = x.split('I')
print(x)

