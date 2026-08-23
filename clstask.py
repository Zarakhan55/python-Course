class Book:

    library_name = "City Library"

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Library Name:", self.library_name)

    def discount(self, amount):
        self.price = self.price - amount

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


b1 = Book("Python Basics", "Ali", 2000)
b2 = Book("JavaScript Basics", "Sara", 2500)

b1.show()
print("-----------------")
b2.show()

b1.discount(500)

print("-----------------")

Book.change_library_name("NewYork Library")

b1.show()
print("-----------------")
b2.show()











# Q2==============
class Doctor:

    hospital = "City Hospital"
    doctor_count = 0

    def __init__(self, name, specialization, fee, available):
        self.name = name
        self.specialization = specialization
        self.fee = fee
        self.available = available

        Doctor.doctor_count += 1

    def show(self):
        print("Name:", self.name)
        print("Specialization:", self.specialization)
        print("Fee:", self.fee)
        print("Available:", self.available)
        print("Hospital Name:", self.hospital)

    def increase_amount(self, amount):
        self.fee = self.fee + amount

    @classmethod
    def change_hospital(cls, new_hospital):
        cls.hospital = new_hospital


# Create doctors
d1 = Doctor("Dr. Ali", "Cardiologist", 3000, True)
d2 = Doctor("Dr. Sara", "Dermatologist", 2500, False)
d3 = Doctor("Dr. Ahmed", "Dentist", 2000, True)


# Show doctors
d1.show()

print("---------------------------")

d2.show()

print("---------------------------")

d3.show()


# Increase fee
d1.increase_amount(500)

print("---------------------------")
print("After fee increase:")

d1.show()


# Change hospital
Doctor.change_hospital("Civil Hospital")

print("---------------------------")
print("After hospital change:")

d1.show()
d2.show()
d3.show()


# Total doctors
print("---------------------------")
print("Total Doctors:", Doctor.doctor_count)