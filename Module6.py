#1
import random

# function that returns a dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# main program
result = 0

while result != 6:
    result = roll_dice()
    print("Dice rolled:", result)

#2
import random

# function that rolls a dice with given number of sides
def roll_dice(sides):
    return random.randint(1, sides)

# main program
sides = int(input("Enter the number of sides on the dice: "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print("Dice rolled:", result)

#3
# function to convert gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.785


# main program
gallons = float(input("Enter volume in gallons: "))

while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print("Liters:", liters)

    gallons = float(input("Enter volume in gallons (negative value to stop): "))

#4
# function that returns the sum of numbers in a list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# main program
my_list = [4, 7, 2, 9, 5]

result = sum_list(my_list)

print("The sum of the numbers is:", result)


#5- Couldn't solve

#6
import math

# function to calculate unit price per square meter
def pizza_unit_price(diameter_cm, price_euro):
    radius = diameter_cm / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10000
    unit_price = price_euro / area_m2
    return unit_price


# main program
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (€): "))

d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (€): "))

price1 = pizza_unit_price(d1, p1)
price2 = pizza_unit_price(d2, p2)

print("Pizza 1 unit price:", price1, "€/m²")
print("Pizza 2 unit price:", price2, "€/m²")

if price1 < price2:
    print("Pizza 1 provides better value for money.")
else:
    print("Pizza 2 provides better value for money.")

