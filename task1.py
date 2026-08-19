class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Money Deposited Successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Money Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")


# Create object
account1 = BankAccount("Zara", 50000)

# Show original details
account1.show_details()

print("--------------------")

# Deposit money
account1.deposit(5000)

# Show updated balance
account1.show_details()

print("--------------------")

# Withdraw money
account1.withdraw(10000)

# Show final balance
account1.show_details()


