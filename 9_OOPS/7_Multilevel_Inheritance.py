class GrandParent:
    def __init__ (self,name,age):
        self.name =name
        self.age = age

    def put_data(self):
        print(self.name, self.age)
#multilevel inhertance parent class inherits the attributes and methods from the grandparent class
class Parent(GrandParent):
    def parent_method(self):
        print("Parent Method")

#multiple inheritance - child class inherits the attributes and methods from the parent class 
class Child(Parent):
    def child_method(self):
        print("Child Method")

c = Child("Ranjith",22)
c.put_data()
c.parent_method() #calling parent method()
c.child_method() #calling child method()