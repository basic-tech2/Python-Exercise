# for loops in python 

my_name = "Astainy"

for characters in my_name:
    print(characters)

# A list of of color iterated by for loop
colors = ["red", "black", "blue", "pink"]

for color in colors:
    print(color)

for letters in "Christain":
    print(letters)


print('===================================================================')
# breaking out of a loop

our_colors = ["red", "black", "blue", "pink", "orange", "maroon"]

for few_colors in our_colors:
    print(few_colors)
    
    if few_colors == "blue":
        break
    else: 
        continue
print(type(few_colors))

print('===================================================================')

for x in range(2, 30):
    print(x * x * "()") # multiplaying each number by itself
    if x == 10:
        break