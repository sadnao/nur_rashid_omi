import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='passisset',
    database='flight_game'
)

cursor = conn.cursor()

# Ask the user for ICAO code
icao_code = input("Enter the ICAO code of the airport: ").upper().strip()

# Prepare and execute the SQL query
query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao_code,))

# Fetch the result
result = cursor.fetchone()

if result:
    airport_name, town = result
    print(f"Airport Name: {airport_name}")
    print(f"Location (Town): {town}")
else:
    print("No airport found with that ICAO code.")


cursor.close()
conn.close()


#2
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='passisset',
    database='flight_game'
)


cursor = conn.cursor()

# Ask user for country code
country_code = input("Enter the country code: ")


query = """
select type, count(*) 
from airport 
where iso_country = %s 
group BY type
order BY type
"""

cursor.execute(query, (country_code,))
results = cursor.fetchall()

if results:
    print(f"Airports in country {country_code}:")
    for airport_type, count in results:
        print(f"{count} {airport_type} airport(s)")
else:
    print(f"No airports found for country code {country_code}.")


cursor.close()
conn.close()

#3
import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='passisset',
    database='flight_game'
)

cursor = conn.cursor()

# Ask for two ICAO codes
icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")


cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao1,))
coord1 = cursor.fetchone()

cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao2,))
coord2 = cursor.fetchone()

if coord1 and coord2:
    distance = geodesic(coord1, coord2).kilometers
    print(f"Distance between {icao1} and {icao2} is {distance:.2f} km")
else:
    print("One or both ICAO codes not found.")

cursor.close()
conn.close()
