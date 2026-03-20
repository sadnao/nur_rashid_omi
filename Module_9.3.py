class Car:
    def __init__(self, registration_number , maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        #The speed of the car must stay below the set maximum and cannot be less than zero.
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        #s = v*t
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123",142)

#aacelerates
car.accelerate(60)

#travels for 1.5 hrs
car.drive(1.5)

print("Current speed of the car is:",car.current_speed, "km/h")
print("Travelled distance is:",car.travelled_distance,"km")