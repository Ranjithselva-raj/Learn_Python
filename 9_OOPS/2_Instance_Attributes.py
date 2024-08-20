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

#create an object- pro 1 is an one single instance of the class
pro1 = Product("iphone","1000")

#access the attributes
#print(pro1) #it will print the memory location <__main__.Product object at 0x0000023667A36190>
print(pro1.Quantity)
print(pro1.name,pro1.price)

#creating another object
pro2=Product("samsung","2000")
print(pro2.name,pro2.price)

            