# Sets in Python
# Unordered collecctions of unique elements. Meaning there can only be one representative of the same object

my_set = set()

my_set.add("Hello")
my_set.add(3)
my_set.add("World")
my_set.remove("World")
my_set.add(4) # it doesn't repeat element in as much it exist
my_set.add(4)
print(my_set)

my_list = [1,1,3,3,1,5,5,5,4,4,4,6,6,2,2]
get_set = set(my_list) # iinserting a list into in a set
print(get_set)