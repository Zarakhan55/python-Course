# class Student:

#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name


# s1 = Student("Zara")

# print(s1.name)

# s1.name = "Ali"

# print(s1.name)


class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price")


p1 = Product(9090)

print(p1.price)

p1.price = 7000
print(p1.price)

p1.price = -500
print(p1.price)