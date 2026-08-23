class Student:
    school="BBSUL"
    @classmethod
    def chng(cls):
        cls.school="ABCD"
Student.chng()
print(Student.school)

# Q2-------
class Employee:

    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Zara", 50000)
e2 = Employee("Ali", 60000)

e1.show()
print("----------------")

e2.show()

Employee.change_company("Google")

print("====== After company change ======")

e1.show()
print("----------------")

e2.show()