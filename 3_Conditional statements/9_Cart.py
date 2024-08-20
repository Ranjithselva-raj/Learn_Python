products_list = [{"product":"shoes", "price": 1000,"description": "sneakers"}, 
                 {"product":"t-shirt", "price": 500,"description": "casual"},
                   {"product":"jeans", "price": 2000,"description": "casual"},
                   {"product":"sunglasses", "price": 500,"description": "fashion"},
                   {"product":"Monitor", "price": 1000,"description": "LED"}]

cart= []
while True:
    #asking the user whether they want to continue to add the items
    choice = input("Do you want to add an item to the cart? (y/n): ")
    #if user says yes then display the products
    if choice.lower() == "y":
        print(f"Here is the product list")

        #displaying the products with index using enumerate function
        for index,product in enumerate(products_list):
            print(f"{index} : {product['product']}: £{product['price']} : {product['description']}")

        #asking user to enter the index of the product they want to add
        product_id = int(input("Enter the id you want to add to cart: "))

        #check the product is already in the cart or adding the product to the cart
        if products_list[product_id] in cart:
            products_list[product_id]["quantity"] += 1
        else:
            products_list[product_id]["quantity"] = 1
            cart.append(products_list[product_id])

        #displaying the cart with product and price and quantity and calculate the total cost of the cart
        total = 0
        print(f"Here is your cart")
        for product in cart:
            print(f"{product['product']} :£{product['price']} : {product['quantity']}")
            total += product["price"] * product["quantity"]
        
        print(f"Your total cost is £{total}")

    #if user says no then break the loop
    else:
        break
print(f"Your final cart is {cart} with total items {len(cart)} and the cost is £{total}")

