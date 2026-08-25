# class Product:

#     def __init__(self, price):
#         self.price = price

#     def __add__(self, other):
#         return self.price + other.price
# p1 = Product(1000)
# p2 = Product(2000)

# print(p1 + p2)


# class Book:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#     def __add__(self,other):
#         return self.price+other.price
# b1=Book("chemistry",5000)
# b2=Book("math",800)
# print(b1+b2)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name


s1 = Student("Zara", 22)
s2 = Student("Zara", 20)

print(s1 == s2)