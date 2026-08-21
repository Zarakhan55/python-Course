from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Payment of", amount, "using Credit Card")


class Cash(Payment):

    def pay(self, amount):
        print("Payment of", amount, "using Cash")


pay1 = Cash()

pay1.pay(500000)