class Student:

    def __init__(self, marks):
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)


student1 = Student(90)

student1.show_marks()

# --------------------------

class Bank:

    def __init__(self, name, account):
        self.name = name
        self.__account = account

    def show(self):
        print("Name:", self.name)
        print("Account number:", self.__account)


p1 = Bank("Zara", 69888888888888888)

p1.show()