#adding a product to a position

products = ["Phone","Laptop","Mouse","Keybord","Monitor"]

#display the list of products

print(f"current list of products: {products}")

#asking user to add a product

add_product = input("Enter the product you want to add: ")

add_product = add_product.capitalize()

#asking user to add a position

after_position = input(f"After which product you want to place {add_product}: ")

after_position = after_position.capitalize()

#find the position of the product

position = products.index(after_position)


#adding the product to the list

products.insert(position+1,add_product)

#display the updated list

print(f"updated list of products: {products}")

