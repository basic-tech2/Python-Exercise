# Dictionaries in python

colors = {
    "b": "Blue",
    "m": "Maroon",
    "p": "Pink",
    "r": "Red"
}

print(colors)
colors.values()
# colors.clear() # clear the entire list
print(colors)

colors.pop("b")
print(colors)

print('\n')

print(colors.get("b",  "not available"))

print('---------------------------------------------------')

employees = {
    233 : "John",
    332 : "Peter",
    443 : "Joe",
    223 : "Moses"
}

get_values = employees.get(232, "Does not exist!")
print(get_values)

print('---------------------------------------------------')

print(employees)


