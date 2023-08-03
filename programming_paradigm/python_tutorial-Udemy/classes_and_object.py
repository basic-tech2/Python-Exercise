# Classes and Object in Python
from pizza import pizza1
from pizza import drink

pizzaV = pizza1("Vegetarian", 10.00, "Big")
pizzaP = pizza1("peperonni", 4.00, "Small")


print(pizzaV.size)
print(pizzaP.size)

drink1 = drink("Chocolat", "Brown", "Rubber bottle", "Big")
print(drink1.name)