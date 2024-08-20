
cart =[]
num_items = int(input("Enter the number of items you want to purchase: "))

for i in range(num_items):
    user_purchase = input("Enter item you want to purchase: ")
    cart.append(user_purchase)
    print(cart,len(cart)) 

