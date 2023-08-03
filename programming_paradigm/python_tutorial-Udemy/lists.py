lists = ["banana", "ananana", "orange", "mango", "ananana", "ananana", ]
list2 = [1, 5, 2, 10, 9, 3, 12, 5, 2, 3, 6, 11]

print(lists)
print(lists[0])

lists[0] = "Apple"
print(lists)

lists.append("Bananan")
print(lists)

print('\n')
count_list = lists.count("ananana")
print(count_list)

print(lists)

print('\n')
print(list2)
list2.sort()
print(list2)