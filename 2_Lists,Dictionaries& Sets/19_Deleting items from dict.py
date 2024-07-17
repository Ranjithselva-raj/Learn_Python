# asking the user to delete a product from the dictionary

products = {"Phone": 1000, "Laptop": 2000, "Mouse": 500, "Keyboard": 1000, "Monitor": 2000}

#display the list of products

print(f"current list of products: {products}")

#asking user which product user wants to delete

delete_product =input("Enter the name of product you want to delete: ")

delete_product = delete_product.capitalize()

products.pop(delete_product) # del products[delete_product] also works

#display the updated list of products

print(f"Product {delete_product} deleted. Here is the updated list of products: {products}")


