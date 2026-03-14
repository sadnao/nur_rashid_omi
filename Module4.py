#1
num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#2
inch = float(input("Enter inches (negative number to stop): "))

while inch >= 0:
    cm = inch * 2.54
    print("Centimeters:", cm)
    inch = float(input("Enter inches (negative number to stop): "))

#3- Sorry Ilkka, couldn't solve this one

#4
import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-10): "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")

#5
correct_user = "python"
correct_pass = "rules"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        print("Incorrect credentials")
        attempts += 1

if attempts == 5:
    print("Access denied")

#6- Sorry Ilkka, couldn't solve this one

