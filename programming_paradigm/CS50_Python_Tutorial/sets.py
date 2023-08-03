# Sets in python

my_set = set()
my_set.add(1)
my_set.add(3)
my_set.add(2)
print(my_set)

def something():
    lists = [3, 2, 1, 4, 5, 9, 5, 8, 7, 4, 2, 10]
    s = set(lists)
    s.add("string")
    s.remove(3)
    print(s)

    print(f'This set has {len(s)} elements. ')

something()