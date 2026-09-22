class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
        self.fuel = "gas"

    def inspect(self):
        print(f"This is a {self.make} {self.model} going {self.speed}km/h using {self.fuel}.")

    def refuel(self):
        print(f"The {self.make} {self.model} refuels at a gas station with {self.fuel}.")

    def traffic(self):
        print(f"The {self.make} {self.model} is stuck in traffic.")

class Car(Vehicle):
    def __init__(self, make, model, speed, weight):
        super().__init__(make, model, speed)
        self.weight = weight

    def inspect(self):
        super().inspect()
        print(f"It weighs {self.weight} pounds.")

    def trick(self):
        print(f"The {self.make} {self.model} hits a sick drift.")

    def traffic(self):
        print(f"The {self.make} {self.model} honks their horn in response to traffic. BEEP BEEP!")

class Motorcycle(Vehicle):
    def __init__(self, make, model, speed, weight):
        super().__init__(make, model, speed)
        self.weight = weight

    def inspect(self):
        super().inspect()
        print(f"It weighs {self.weight} pounds.")

    def trick(self):
        print(f"The {self.make} {self.model} pops a wheelie.")

    def traffic(self):
        print(f"The {self.make} {self.model} lane splits to completely avoid traffic.")