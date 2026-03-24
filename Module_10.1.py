class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator created. Current floor: {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Going up... now at floor {self.current_floor}")
        else:
            print("Already at the top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Going down... now at floor {self.current_floor}")
        else:
            print("Already at the bottom floor!")

    def go_to_floor(self, target_floor):
        print(f"Moving to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


# Create an elevator from floor 1 to 10
h = Elevator(1, 10)

# Move to a chosen floor (example: 5)
h.go_to_floor(5)

# Move back to the bottom floor
h.go_to_floor(1)