class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
        self.fuel = "gas"

class Car(Vehicle):
    def __init__(self, make, model, speed, weight):
        super().__init__(make, model, speed)
        self.weight = weight

class Motorcycle(Vehicle):
    def __init__(self, make, model, speed, weight):
        super().__init__(make, model, speed)
        self.weight = weight