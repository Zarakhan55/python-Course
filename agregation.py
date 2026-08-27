# class Teacher:
#     def teach(self):
#         print("Teacher is teaching")


# class Department:
#     def __init__(self, teacher):
#         self.teacher = teacher

#     def start_class(self):
#         self.teacher.teach()
#         print("Class started")


# t1 = Teacher()

# d1 = Department(t1)

# d1.start_class()
class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Company:

    def __init__(self, employee):
        self.employee = employee

    def start(self):
        self.employee.work()
        print("Company started")


e1 = Employee("Zara")

c1 = Company(e1)

c1.start()
c1.employee.work()