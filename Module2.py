name = input("enter your name:")
print(f"Hello {name}!")


import math
radius = float((input("Enter radius: ")))
area = math.pi * radius ** 2
print("The area of the circle is", area)


length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is", perimeter)
print ("The area of the rectangles is", area)



a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

sum_value = a + b + c
product = a * b * c
average = sum_value/3

print("The sum of the numbers is", sum_value)
print("The product of the numbers is", product)
print("The average of the numbers is", average)


talents = int(input("talents: "))
pounds = int(input("pounds: "))
lots = float(input("lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
grams = total_lots * 13.3

kg = int(grams // 1000)
g = grams % 1000

print(f"The weight in modern unit {kg} kg and {g:.2af} grams.")