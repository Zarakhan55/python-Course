class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"Name: {self.name}")

    def show_age(self):
        print(f"Age: {self.age}")


class Student(Person):

    def study(self):
        print(f"{self.name} is studying")


# Person object
person1 = Person("Alice", 25)

person1.show_name()
person1.show_age()

print("----------------")

# Student object
student1 = Student("Zara", 22)

student1.show_name()   # inherited method
student1.show_age()    # inherited method
student1.study()       # Student's own method






# __________Q!!______________
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show_details(self):
        print("Account Holder:",self.name)
        print("Balance:",self.balance)
class SavingsAccount(BankAccount):
    def add_interest(self,interest_rate):
        interest=self.balance*interest_rate/100
        self.balance+=interest
class CurrentAccount(BankAccount):
    def deduct_fees(self,fees):
     if self.balance>=fees:
        self.balance-=fees
s1=SavingsAccount("John",1000)
s1.add_interest(5)
s1.show_details()