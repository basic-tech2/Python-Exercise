# ------------ Create an app that will calculate the price of each product and its quantity. -------
# Get user input of the price of each product and the quantity.
# The price of each product will be twenty dollars and the quantity in this case will be five.
# There are three products in this case:
# --------------------------------------------------------------------------
# 1. The price of product 1
# 2. The quantity of product 1
# 3. The price of product 2
# 4. The quantity of product 2
# 5. The price of product 3
# 6. The quantity of product 3

# Hard coding

price_of_product_1 = input("What is the price of product 1 ?: ")
quantity_of_product_1 = input("What is the quantity of product 1 ?: ")
price_of_product_2 = input("What is the price of product 2 ?: ")
quantity_of_product_2 = input("What is the quantity of product 2 ?: ")
price_of_product_3 = input("What is the price of product 3 ?: ")
quantity_of_product_3 = input("What is the quantity of product 3 ?: ")

print('\n')

result_of_product_1 = float(price_of_product_1) * float(quantity_of_product_1)
# print(f"The cost lof product 1 is: {result_of_product_1} ")

result_of_product_2 = float(price_of_product_2) * float(quantity_of_product_2)
# print(f"The cost of product 2 is: {result_of_product_2} ")

result_of_product_3 = float(price_of_product_3) * float(quantity_of_product_3)
# print(f"The cost of product 3 is: {result_of_product_3} ")

result_product = result_of_product_1 + result_of_product_2 + result_of_product_3

print(f"The total bill of all the products is: {result_product} ")



