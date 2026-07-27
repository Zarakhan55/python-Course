class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)


student1 = Student("Zara", 101)

student1.show()