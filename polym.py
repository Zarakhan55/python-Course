class Animals:
    def sound(self):
        return "Some generic animal sound"
class Cat:
    def sound(self):
        return "Meow"
c1=Cat()
print(c1.sound())


# ==========================
class Creditcard:
    def pay(self):
        return "Paying with credit card"


class JazzCash:
    def pay(self):
        return "Payment using JazzCash"


class Cash:
    def pay(self):
        return "payment using cash......"


card = Creditcard()
jazz = JazzCash()
cash = Cash()

print(card.pay())
print(jazz.pay())
print(cash.pay())