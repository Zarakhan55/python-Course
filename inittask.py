class Vehicle:

    def __init__(self, brand, rent_per_day):
        self.brand = brand
        self.rent_per_day = rent_per_day

    def show_details(self):
        print("Brand:", self.brand)
        print("Rent per day:", self.rent_per_day)


class Car(Vehicle):

    def __init__(self, brand, rent_per_day, seats):
        super().__init__(brand, rent_per_day)
        self.seats = seats

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Bike(Vehicle):

    def __init__(self, brand, rent_per_day, speed):
        super().__init__(brand, rent_per_day)
        self.speed = speed

    def calculate_rent(self, days):
        return self.rent_per_day * days


c1 = Car("Toyota", 100, 5)

c1.show_details()
print("Seats:", c1.seats)
print("Car Rent for 3 days:", c1.calculate_rent(3))

print("----------------")

b1 = Bike("Honda", 50, 120)

b1.show_details()
print("Speed:", b1.speed)
print("Bike Rent for 3 days:", b1.calculate_rent(3))