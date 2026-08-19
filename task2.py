class Car:
    def __init__(self,company,color,brand):
        self.company=company
        self.color=color
        self.brand=brand
    def show_details(self):
        print("Company:",self.company)
        print("Color:",self.color)
        print("Brand:",self.brand)
car1=Car("Toyota","White","Corolla")
car2=Car("Honda","Black","Civic")
car1.show_details()
car2.show_details()
# Inheritance---------------------
class Animal:
    
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Animal makes sound")
sound1=Animal("Dog")
sound1.sound()
    