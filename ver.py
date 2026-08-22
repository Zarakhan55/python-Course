class Employee:

    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)


e1 = Employee("Zara", 20000)
e2 = Employee("Nasir", 40000)

e1.show_details()
print("----------------")
e2.show_details()


class Student:
    university = "BBSUL"
    def __init__(self,name,semester,CGPA):
        self.name=name
        self.semester=semester
        self.CGPA=CGPA
    def detail(self):
        print("Name of student:",self.name)
        print("Semester:",self.semester)
        print("CGPA:",self.CGPA)
s1=Student("zara khan",7,90)
s1.detail()