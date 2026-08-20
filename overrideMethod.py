class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
d1=Dog()
print(d1.speak())


class Person:
    def work(self):
        return "Person works"
class Employee(Person):
    def work(self):
        return "Employee works"
class Manager(Employee):
    def work(self):
        return "Manager works"
M1=Manager()
print(M1.work())