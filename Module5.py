#1- Sorry Ilkka, couldn't solve this one

#2- Sorry Ilkka, couldn't solve this one

#3
num = int(input("Enter an integer: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


#4
cities = []

for i in range(5):
    city = input("Enter a city name: ")
    cities.append(city)

print("Cities entered:")

for city in cities:
    print(city)