#1
# tuple containing seasons
seasons = ("winter", "spring", "summer", "autumn")

# ask user for month number
month = int(input("Enter a month number (1-12): "))

# determine season
if month == 12 or month == 1 or month == 2:
    print("Season: winter")
elif month >= 3 and month <= 5:
    print("Season: spring")
elif month >= 6 and month <= 8:
    print("Season: summer")
elif month >= 9 and month <= 11:
    print("Season: autumn")


#2- Couldn't solve

#3
# Dictionary to store airport data
airports = {}

while True:
    # Ask user for the action
    print("Choose an option:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Add a new airport
        icao = input("Enter ICAO code of the airport: ")
        if icao in airports:
            print(f"Airport with ICAO code {icao} already exists: {airports[icao]}")
        else:
            name = input("Enter name of the airport: ").strip()
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} added successfully.")

    elif choice == "2":
        # Fetch airport information
        icao = input("Enter ICAO code of the airport to fetch: ")
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    elif choice == "3":
        # Quit the program
        print("Exiting program. !")
        break





