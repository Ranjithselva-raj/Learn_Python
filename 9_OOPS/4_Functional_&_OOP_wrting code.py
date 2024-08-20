#functional programming

#def product_data():
#    product_name = input("Enter the product name: ")
#    product_price = int(input("Enter the product price: "))
#    print(product_name, product_price)

#product_data()

#***********************************************************
#OOP programming
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    #methods in class  directly operate on the data inside the constructor when called by self and the attributes names
    def get_data(self):
        self.name = input("Enter the product name: ")
        self.price = int(input("Enter the product price: "))
    
    def put_data(self):
        print(self.name, self.price)

p1 = Product("","")
p1.get_data()
p1.put_data()