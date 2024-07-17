class Food:
    def type(self):
        print("This is food")
class Fruit(Food):
    #def type(self): # overriding method in Food class 
       # print("This is fruit")
    def welcome(self):
        print("Welcome to Fruit World")

apple = Fruit()
print(apple.type())
