# seperate module in python
from functions import square
import functions

for i in range(10):
    print(f'The squre of {i} is {square(i)}')

print('-------------------------------------------------')
for i in range(10):
    print(f'The squre of {i} is {functions.square(i)}')