class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

employee1 = Employee("Zara", 20000, "IT")
employee2 = Employee("Sara", 20700, "IT")

employee1.show_details()
print()

employee2.show_details()