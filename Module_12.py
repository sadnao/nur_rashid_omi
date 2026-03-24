#1
import requests

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])  # only the joke text
    else:
        print("Failed to fetch joke. Try again.")

# Run the program
get_random_joke()


#2
import requests

API_KEY = "d03e7d11c08d99034eb0be90f3562152"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Weather: {description}")
        print(f"Temperature: {temperature:.2f} °C")
    else:
        print("Error:", data)

# Main program
city = input("Enter municipality: ")
get_weather(city)

