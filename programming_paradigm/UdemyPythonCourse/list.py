# List in Python
my_List = ["One", 123, "Four", 221.2]
x = my_List[::-1]

print(my_List)
print(x)
print(len(x))
print("One" in x)

#Concatenate list
another_list = ["Three", "Five", 332, 3.3]

concate = my_List + another_list
print(concate)

new_list = "one"
new_list = new_list.upper()
concate[0] = new_list
print(concate)

#Add new element to a list
new = ['six', 34.3, "nine", "ten", 44]
new.append('appended new element')
new.append('seven')

#Remove element from a list
new.pop()
popped_item = new.pop()
print(popped_item)
print(new)
new.pop(0)
print(new)

print("\n")

#reversing element in a list
some_list = ['b', 'd', 'a', 'c']
number_list = [2, 4, 1, 3, 5, 6, 8, 7]
some_list.sort()
newlist = some_list
number_list.sort()
new_number_list = number_list
print(newlist)
print(new_number_list)

print('\n')
#get an element from a nested list list in list
get_list = [1,4,5,[1,3]]
print(get_list[3][0])

print(get_list)
print('\n')
#sorting element in a list
reverse_name_list = ["one", "two", "three", "four", "five"]
reverse_number_list = [1,2,3,4,5,6,7,8,9]

reverse_name_list.reverse()
reverse_number_list.reverse()

print(reverse_name_list)
print(reverse_number_list)






######## Simple practice work using list slicing method

# get_word = input("Spell a word backward: ")
# reverse = get_word[::-1]
# print(f'The correct word is: {reverse}')

######## Simple practice work using list sorting method


######## Simple practice work using list reservse method

