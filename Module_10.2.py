class Elevator:
    def __init__(self, bottom_floor, top_floor,elevator_id):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor
        self.id = elevator_id

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

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


# -------- Main Program --------
# Create a building with floors 1–10 and 3 elevators
building = Building(1, 10, 3)

# Run elevators
building.run_elevator(1, 5)
building.run_elevator(2, 9)
building.run_elevator(3, 3)

# Move one elevator back down
building.run_elevator(1, 2)