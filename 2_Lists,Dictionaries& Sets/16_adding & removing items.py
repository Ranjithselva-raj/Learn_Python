products = ["Phone","Laptop","Mouse","Keybord","Monitor"]

#display the list
print(f"current list of products: {products}")

#asking user to remove a product

remove_product = input("Enter the product you want to remove: ")

remove_product = remove_product.capitalize()

#removing the product from the list

products.remove(remove_product)

#display the updated list

print(f"updated list of products: {products}")

#############################################################################
#code to add a product
# asking user to add a product
add_product = input("Enter the product you want to add: ")

add_product = add_product.capitalize()

#adding the product to the list
products.append(add_product)

#display the updated list after adding a product

print(f"updated list of products: {products}")