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

#Inheritance - child class inherits the attributes and methods from the parent class
class Mobile(Product):
    def __init__(self,link):
        self.link = link

    def get_link(self):
        self.link = input("Enter the link of the Mobile product: ")
    
    def put_link(self):
        print(self.link)
    
    def display(self):
        print("Mobile")
    pass

#Inheritance - child class inherits the attributes and methods from the parent class
class Laptop(Product):
    def __init__(self,link):
        self.link = link
    
    def get_link(self):
        self.link = input("Enter the link of the Laptop product: ")
    
    def put_link(self):
        print(self.link)

    def display(self):
        print("Laptop")
    

p2= Mobile("")
p2.get_data()
p2.get_link()
p2.put_data()
p2.put_link()
p2.display()

p3 = Laptop("")
p3.get_data()
p3.get_link()
p3.put_data()
p3.put_link()
p3.display()

