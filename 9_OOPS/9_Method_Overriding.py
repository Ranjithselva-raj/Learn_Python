class Food:
    def type(self):
        print("This is food")
class Fruit(Food):
    def __init__(self,name):
        self.name = name
    #def type(self): # overriding method in Food class 
       # print("This is fruit")
    def welcome(self):
        print("Welcome to Fruit World")

## Function that demonstrates polymorphism
def fruit_type(fruit):
        print(fruit.type())

apple = Fruit("apple")
print(apple.type())
print(apple.name)
print(apple.welcome())
fruit_type(apple)
