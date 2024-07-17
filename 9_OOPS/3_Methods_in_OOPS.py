#create a class and objects

class Product:
    #class attributes
    Quantity = 4000 
    
    #create a constructor
    # constructor is a method that is called when an object is created
    # it is used to initialize the object and perform any necessary setup for the object
    def __init__(self,name,price): #instance attributes - name and price are instance attributes or object attributes
        self.name = name
        self.price = price 
        pass
    
    #methods in class or object - instance methods - they are used to perform operations on the object 
    def summer_discount(self,discount_rate):
        self.price = self.price - (self.price*discount_rate/100)
        return self.price

p1 = Product("iphone",100)
print(p1.name,p1.price)
print(p1.summer_discount(20))

p2= Product("T-shirts",200)
print(p2.name,p2.price)
print(p2.summer_discount(10))