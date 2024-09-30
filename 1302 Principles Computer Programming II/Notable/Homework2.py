# Deeper Dive into OOP, using Classes, Class Functions, and Class utilization through Class hierarchy, Based off of given test code (defined at the bottom)

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print('[Make: '+self.make+', Model: '+self.model+', Year: '+str(self.year)+']')

    def __lt__(self, other):
        if self.year < other:
            return True
        else:
            return False


class Car(Vehicle):

    def __init__(self, make, model, year, door):
        Vehicle.__init__(self, make, model, year)
        self.num_door = door

    def honk(self):
        print("Honk! Honk! From Car")

    def get_info(self):
        print('[Make: '+self.make+', Model: '+self.model+', Year: '+str(self.year)+', Doors: '+str(self.num_door)+']')


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, type):
        Vehicle.__init__(self, make, model, year)
        self.type = type

    def honk(self):
        print("Honk! Honk! From Motorcycle")

    def get_info(self):
        print('[Make: '+self.make+', Model: '+self.model+', Year: '+str(self.year)+', Type: '+self.type+']')


class Truck(Vehicle):

    def __init__(self, make, model, year, capacity):
        Vehicle.__init__(self, make, model, year)
        self.capacity = capacity

    def honk(self):
        print("Honk! Honk! From Truck")

    def get_info(self):
        print('[Make: '+self.make+', Model: '+self.model+', Year: '+str(self.year)+', Capacity: '+str(self.capacity)+']')

    def __lt__(self, other):
        if self.capacity < other:
            return True
        else:
            return False


class PickupTruck(Truck, Car):

    def __init__(self, make, model, year, door, capacity, has_cover):
        Truck.__init__(self, make, model, year, capacity)
        Car.__init__(self, make, model, year, door)
        self.has_cover = has_cover

    def get_info(self):
        print('[Make: '+self.make+', Model: '+self.model+', Year: '+str(self.year)+', Capacity: '+str(self.capacity)+', Doors: '+str(self.num_door)+', Cover: '+str(self.has_cover)+']')

# Test Code INP

car = Car('Nissan', 'Altima', 2020, 4)
motorcycle = Motorcycle('Harley-Davidson', 'Sport Glide', 2019, 'Sport Bike')
truck = Truck('Honda', 'Ridgeline ', 2021, 12500)
pickup_truck = PickupTruck('Ford', 'F-150', 2019, 2, 14000, True)

# Test Code

print("-------------------------- Each Class Honk --------------------------")
car.honk()
motorcycle.honk()
truck.honk()
pickup_truck.honk()

print('-------------------------- Each Class get_info() --------------------------')
car.get_info()
motorcycle.get_info()
truck.get_info()
pickup_truck.get_info()

print('-------------------------- Truck VS Pickup Truck --------------------------')
print(truck < pickup_truck.capacity)
