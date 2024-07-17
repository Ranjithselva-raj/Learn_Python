

products = {"Phone": 1000, "Laptop": 2000, "Mouse": 500, "Keyboard": 1000, "Monitor": 2000}

# display the list of products

print(f"current list of products: {products}")

#ask user which product price user wants to edit

price_change_product = input("Enter the product you want to edit: ")

price_change_product = price_change_product.capitalize()

price_change = input(f"Enter the New Price of {price_change_product}: ")

products[price_change_product] = price_change

#display the updated list of products

print(f"Price Updated Succesfully. Here is the updated list of products: {products}")



