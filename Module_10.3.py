class Elevator:
    def __init__(self, bottom_floor, top_floor, elevator_id):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor
        self.id = elevator_id

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator {self.id} at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator {self.id} at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom = bottom_floor
        self.top = top_floor
        self.elevators = {}

        for i in range(1, num_elevators + 1):
            self.elevators[i] = Elevator(bottom_floor, top_floor, i)

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number in self.elevators:
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("\033[31mFire Alarm Activated")
        print("All elevators moving to the bottom floor...\033[0m")

        for elevator in self.elevators.values():
            print(f"Elevator {elevator.id} moving to bottom floor ({self.bottom})")
            elevator.go_to_floor(self.bottom)


# -------- Main Program --------
building = Building(1, 10, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 9)
building.run_elevator(3, 3)

# Fire alarm triggered
building.fire_alarm()