# from abc import ABC, abstractmethod

# class Parent(ABC):

#     @abstractmethod
#     def show(self):
#         pass


# class Child(Parent):

#     def show(self):
#         print("Child class ...........")


# c1 = Child()

# c1.show()

from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        print("plz pay your payment")
class Cash(payment):
    def pay(self):
        print("give cash")
p1=Cash()
p1.pay()