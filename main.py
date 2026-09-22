from vehicles import Vehicle
from vehicles import Car
from vehicles import Motorcycle

vehicle = Vehicle("NA", "NA", "NA")
car = Car("Honda", "Civic", 100, 2700)
motorcycle = Motorcycle("Yamaha", "YZF-R1", 80, 448)

select = """Choose your type of vehicle:
1 for Car | 2 for Motorcycle | 3 for Vehicle | 4 for exit\n"""

message = """Enter an input: 
| Inspect | Refuel | Traffic | Trick | Exit |\n"""

message2 = """Enter an input: 
| Inspect | Refuel | Traffic | Exit |\n"""

recover = "How much health should be recovered"

commands = [
    "inspect",
    "refuel",
    "traffic",
    "trick",
]

actions1 = [
    car.inspect,
    car.refuel,
    car.traffic,
    car.trick,
]

actions2 = [
    motorcycle.inspect,
    motorcycle.refuel,
    motorcycle.traffic,
    motorcycle.trick,
]

actions3 = [
    vehicle.inspect,
    vehicle.refuel,
    vehicle.traffic,
]

while True:
    try:
        type = int(input(select))
        if type == 1:
            user_input = input(message).strip().lower()
            for command, action in zip(commands, actions1):
                if user_input == command:
                    action()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif type == 2:
            user_input = input(message).strip().lower()
            for command, action2 in zip(commands, actions2):
                if user_input == command:
                    action2()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif type == 3:
            user_input = input(message2).strip().lower()
            for command, action3 in zip(commands, actions3):
                if user_input == command:
                    action3()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif type == 4:
            break
    except ValueError:
        print("Invalid input")

