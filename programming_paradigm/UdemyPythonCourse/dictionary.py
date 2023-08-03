# Python Dictionary
my_dictionary = {"f_name": "John", "l_name": "Doe", "age": 20}

print(my_dictionary)
print(my_dictionary['f_name'])

fruits_prices = {"Apple": 25.50, "Orange": 30.5, "Mango": 50.2}
get_fruits = fruits_prices["Apple"]
print(fruits_prices)
print(get_fruits)
print('\n')

d = {"k1": "Phone", "k2": [123, "something", "in", "this", "list"], "k3":{"Apple": 20, "Plum": 45, "Banana": 50.25}, "k4": [1,2,3,4,5]}
print(d)
print('\n')
get_d = d['k3']['Apple'] #accessing k3 of a list of apple accessing key Apple value
get_numb = d["k4"][3] # indexing
print(get_numb)
print(get_d)
get_value = d['k2'][1].upper()
print(get_value)

d1 = {"k1": 200, "k2": 300}
print(d1)
d1["k3"] = 500
print(d1)
d1["k1"] = 400
print(d1)
print(d1.keys()) # to get all the keys
print(d1.values()) # to get all the values
print(d1.items()) # to get all the item within the dictionary
