#using while loop asking user to add items to cart without asking total numer of items user want to add

"""cart =[]

while True:
    choice = input("Do you want to add an item to the cart? (y/n): ")
    if choice.lower() == "y":
        user_purchase = input("Enter item you want to purchase: ")
        cart.append(user_purchase)
        print(cart,len(cart))
    else:
        break"""

#Using while loop asking user to add items to cart and stop when user press enter to finish
cart =[]

while True:
    user_purchase = input("Enter item you want to purchase or press enter to finish: ")
    if user_purchase != "":
        cart.append(user_purchase)
        print(cart,len(cart))
    else:
        print(f"Your final cart is {cart} with total items {len(cart)}")
        break
