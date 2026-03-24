import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            change_speed = random.randint(-10, 15)
            car.accelerate(change_speed)
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"{'Reg No':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")
        print("-" * 45)
        for car in self.cars_list:
            print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<10} {int(car.travelled_distance):<10}")

    def race_finished(self):
        for car in self.cars_list:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Main program

# Create cars
cars_list = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars_list.append(Car(registration_number, maximum_speed))

# Create race
race = Race("Grand Demolition Derby", 8000, cars_list)

hours = 0

# Simulation loop
while not race.race_finished():
    hours += 1
    race.hour_passes()

    # Print status every 10 hours
    if hours % 10 == 0:
        print(f"Hour {hours} ")
        race.print_status()

# Final result
print(f"Race finished in {hours} hours")
race.print_status()