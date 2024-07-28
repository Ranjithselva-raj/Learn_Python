import os
import json

def write_data():
    """
    This function writes data to a JSON file. It prompts the user to enter product information, and then appends
      the data to an existing JSON file or creates a new one if the file does not exist.
    """
    create_list = []
    while True:
        product = input("Enter product name or press enter to exit: ")
        if product == "":
            break
        price = int(input("Enter the price of the product: "))
        description = input("Enter the description of the product: ")

        create_list.append({"product": product, "price": price, "description": description})

    if os.path.exists("products.json"):
        with open("products.json", "r") as file:
            old_data = json.load(file)
        create_list.extend(old_data)

    with open("products.json", "w") as file:
        json.dump(create_list, file)

    print("Data written successfully!")

def read_data():
    """
    This function reads data from a JSON file and prints it to the console.
    """
    if not os.path.exists("products.json"):
        print("File does not exist!")
        return
    
    with open("products.json", "r") as file:
        data = json.load(file)
        
    for product in data:
        print(f"Product: {product['product']}, Price: {product['price']}, Description: {product['description']}")


write_data()
read_data()
