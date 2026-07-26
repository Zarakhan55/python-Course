class students:
    def call(self):
        print("studnet is calling.......")
std1=students()
std1.call()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Zara", 50000)

employee1.show()




class BankAccount:
    
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show_details(self):
        print("Name:",self.name)
        print("balance:",self.balance)

    def deposit(self):
        print("Money Deposited Successfully!")
account1 = BankAccount("Zara", 50000)
account2 = BankAccount("Ali", 30000)
account1.show_details()
account1.deposit()

print("----------------")

account2.show_details()
account2.deposit()