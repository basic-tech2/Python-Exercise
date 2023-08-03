# write down a list of number

food = ["pizza", "banana", "pawpaw", "orange", "apple", "orange", "banana",  "pawpaw"]
list_of_numbers = [3, 5, 7, 9, 10, 2, 1, 6]

print(food)

# insert new element in the food list
food.insert(4, "Grib")
print(food)

# delect element from the food list
print('\n')
food.pop(0)
print(f'pizza has been delected {food} ')

# To put two list together
print('\n')
food.extend(list_of_numbers)
print(food)

# Find the index of an element in a list
print(food.index("orange"))

# Find how many times an element appears
food.count("orange")

# Get of your list 

copied_list = food.copy() + list_of_numbers.copy()
food.pop(0)
food.pop(2)
print(copied_list)