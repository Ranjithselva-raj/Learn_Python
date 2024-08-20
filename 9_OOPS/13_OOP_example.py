#1)creating a class 

class Vehicle:
    #10)creating class variables
    class_attribute = "This ia a vehicle class variable"

    #2)creating a constructor
    def __init__(self,name,price):
        #3)creating instance variables
        self.name = name
        self.price = price

    #4)creating a method in class are instance methods can access instance variables
    def display_info(self):
        print(f"Name is {self.name} and price is {self.price}")

    #10)creating class methods
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"I can access class variable: {cls.class_attribute}")
    
    #11)creating static methods can't access instance variables or class variables
    @staticmethod
    def static_method():
        print("This is a static method. I can't access instance variables or class variables")

#6)creating a child class that inherits from the parent class
class Bike(Vehicle):

    #7)creating a constructor in child class and invokes parent class constructor using super()
    def __init__(self,name,price,color):
        #8)calling parent class constructor in child class and overrding the parent class constructor with child class constructor
        super().__init__(name,price)
        self.color = color
    
    #9)overriding the parent class method by creating a new method in child class with same name
    def display_info(self):
        print(f"{self.name}, {self.price}, {self.color}")

        
    

#5)creating an object
car = Vehicle("minicooper","100000")
car.display_info()

bike = Bike("pulsar","20000","red")
bike.display_info()

Vehicle.class_method()
Vehicle.static_method()

#1)creating a class 
#2)creating a constructor
 #3)creating instance variables
#4)creating a method in class are instance methods can access instance variables
#5)creating an object
#6)creating a child class that inherits from the parent class
#7)creating a constructor in child class and invokes parent class constructor using super()
#8)calling parent class constructor in child class and overrding the parent class constructor with child class constructor
#9)overriding the parent class method by creating a new method in child class with same name
 #10)creating class methods
#11)creating static methods can't access instance variables or class variables