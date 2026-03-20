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

#main program

#create list of cars
cars_list =[]
for i in range(1, 11):
 registration_number = f"ABC-{i}"
 maximum_speed = random.randint(100,200)
 car = Car(registration_number,maximum_speed)
 cars_list.append(car)

race_finished = False

#loop
while not race_finished:
    for car in cars_list:
        change_speed = random.randint(-10,15)
        car.accelerate(change_speed)

        #travels for 1.5 hrs
        car.drive(1)

        if car.travelled_distance >= 10000:
         race_finished = True

# Print results in table format
print(f"{'Reg No':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")
print("-" * 45)

for car in cars_list:
    print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<10} {int(car.travelled_distance):<10}")