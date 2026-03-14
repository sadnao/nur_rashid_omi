#1
length = float(input("Enter the length of the zander (cm): "))

limit = 42

if length < limit:
    difference = limit - length
    print("Release the fish back into the lake.")
    print(f"The fish is {difference} cm below the size limit.")
else:
    print("The fish meets the size limit.")


#2
cabin = input("Enter cabin class (LUX, A, B, C): ")

if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


#3
gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")


#4
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")