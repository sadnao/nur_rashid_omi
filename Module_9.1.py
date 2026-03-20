class Car:
    def __init__(self, registration_number , maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
car = Car("ABC-123",142)

print("Registration_number is:",car.registration_number)
print("Maximum_speed is:", car.maximum_speed, "km/h")
print("Current_speed is:",car.current_speed, "km/h")
print("Travelled_distance is:",car.travelled_distance,"km")
