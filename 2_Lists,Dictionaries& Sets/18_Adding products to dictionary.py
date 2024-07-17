#checking the price of a product in dictionary and adding a new product to dicionary as user wnats 

products = {"Phone": 1000, "Laptop": 2000, "Mouse": 500, "Keyboard": 1000, "Monitor": 2000}

#display the list

print(f"current list of products: {products}")

#asking user for which product price user want to check

check_product = input("Enter the product you want to check the price: ")

check_product = check_product.capitalize()

print(f"The price of {check_product} is {products[check_product]}")


new_product =input("Enter the product you want to add: ")

new_product =new_product.capitalize()

price = int(input(f"Enter the price of {new_product}: "))

products[new_product] = price

print(f"updated list of products: {products}")
