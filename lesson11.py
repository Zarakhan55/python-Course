class student:
      def __init__(self,name,age):
            self.name=name
            self.age=age
student1=student("zara",21)
student2=student("nasir",22)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)









# ================================
class Car:
    def __init__(self,company,color):
        self.company=company
        self.color=color

car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print(car1.company)
print(car2.color)
print(car2.company)
print(car2.color)



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basic", "Zara")
book2 = Book("OOP Guide", "Ali")

print(book1.author)
print(book1.title)

print(book2.author)
print(book2.title)