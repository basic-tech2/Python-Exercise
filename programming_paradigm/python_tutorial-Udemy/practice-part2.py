# We will have three persons, each of them will have a name. Those three persons will buy a pizza and want to knwo how manay slices each person ate of the pizza and depending on the number of slice each persona ate. We will find out how much each person will pay.
# --- algorithm
#1. Get user name
#. Ask how many slices the pizza has
#2. Get the amount of slices each person ate

#input
first_user = input("First person what is your name? ")
second_user = input("Second person what is your name? ")
third_user = input("Third person what is your name? ")

numberOfSlices = input("How many slices in the Pizza? ")
price_of_pizza = input("What is the price of the Pizza? ")

# Percentage ate by person
#input
percentage_ate_by_person1 = input(f'{first_user} how many percentage have you eaten? ')
percentage_ate_by_person2 = input(f'{second_user} how many percentage have you eaten? ')
percentage_ate_by_person3 = input(f'{third_user} how many percentage have you eaten? ')

#output
number_of_slaces_ate_by_person1 = float(numberOfSlices) * float(percentage_ate_by_person1)
number_of_slaces_ate_by_person2 = float(numberOfSlices) * float(percentage_ate_by_person2)
number_of_slaces_ate_by_person3 = float(numberOfSlices) * float(percentage_ate_by_person3)

# What is the price paid by each person?
#output

price_paid_by_name1 = float(percentage_ate_by_person1) * float(price_of_pizza)
price_paid_by_name2 = float(percentage_ate_by_person2) * float(price_of_pizza)
price_paid_by_name3 = float(percentage_ate_by_person3) * float(price_of_pizza)

#print output

print(f'{first_user} has eaten {numberOfSlices} number of slices, and has paid ${price_paid_by_name1} for his/her meal.')
print(f'{second_user} has eaten {numberOfSlices} number of slices, and has paid ${price_paid_by_name2} for his/her meal.')
print(f'{third_user} has eaten {numberOfSlices} number of slices, and has paid ${price_paid_by_name3} for his/her meal.')





