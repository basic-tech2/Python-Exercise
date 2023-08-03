# Tuples in Python
# Tuples are immutable

t = (1, 4, 5, 9, "tuples", "in", "Python")
print(t)
print(type(t))
add_tuple  = ("Added to a tuple", 9)

new_tuple = t + add_tuple

print(new_tuple)
print(t[4])

print("\n")

t2 = ("a", "b", "a", "a", "b", "c")
get_tuple_count = t2.count('a')
print(get_tuple_count)
print("\n")
print(t2.index("b"))

