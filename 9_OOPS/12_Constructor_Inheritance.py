class Parent:
    def __init__(self):
        self.parents_balance =50000

    def display_balance(self):
        print(f"Parent Balance is {self.parents_balance}")
        
class Child(Parent):
    def __init__(self):
        #super().__init__() invoking parent class constructor in child class 
        #once the super keyword is used in child class the parent class constructor and methods are invoked
        super().__init__()
        self.child_balance = 10000

    def display_balance(self):
        print(f"Child Balance is {self.child_balance + self.parents_balance}")
    

jo = Child()
jo.display_balance()