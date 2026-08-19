from mimetypes import init


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    def show_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Language:",self.language)
E1=Developer("Alice",50000,"Python")
E1.show_details()












class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
s1=student("Bob",20,"A")
s1.show_details()