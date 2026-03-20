import random
import math
import story
from geopy import distance
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='skybound',
    user='root',
    password='passisset',
    autocommit=True
)

# FUNCTIONS

# select 21 airports for the game
def get_airports():
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
FROM airport
WHERE continent = 'EU' 
AND type='large_airport'
ORDER by RAND()
LIMIT 21;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#get all events
def get_events():
    sql = "SELECT * FROM event;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# create new game
def create_game(start_money, fuel_range, cur_airport, p_name, a_ports):
    sql = "INSERT INTO game (money, fuel, location, player_name) VALUES (%s, %s, %s, %s);"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (start_money, fuel_range, cur_airport, p_name))
    game_id = cursor.lastrowid

#add_events
    events = get_events()
    event_list = []
    for event in events:
        for i in range(0, event['probability'], 1):
         event_list.append(event['id'])

# exclude starting airport
    event_ports = a_ports[1:].copy()
    random.shuffle(event_ports)

    for i, event_id in enumerate(event_list):
      sql = "INSERT INTO ports (game, airport, event) VALUES (%s, %s, %s);"
      cursor = conn.cursor(dictionary=True)
      cursor.execute(sql, (game_id, event_ports[i]['ident'],event_id))

    return game_id

# get airport info
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# check if airport has an event
def check_event(game_id, cur_airport):
    sql = f'''SELECT ports.id, event.id as event_id, type, description, money, fuel
    FROM ports 
    JOIN event ON event.id = ports.event 
    WHERE game = %s 
    AND airport = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (game_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result

# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


# get airports in range
def airports_in_range(icao, a_ports, fuel):
    in_range = []
    max_distance = fuel* 3   # convert fuel to km

    for a_port in a_ports:
        dist = calculate_distance(icao, a_port['ident'])

        if dist <= max_distance and dist != 0:
            in_range.append(a_port)

    return in_range
# set event happened

# update location
def update_location(icao, fuel_range, u_money, game_id):
    sql = f'''UPDATE game SET location = %s, fuel = %s, money = %s WHERE id = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao, fuel_range, u_money, game_id))

# game starts
# ask to show the story
storyDialog = input('\033[34mWelcome to SKYBOUND EXPRESS. Do you want to read the background story? (Y/N):\033[0m ')
if storyDialog == 'Y':
    # print wrapped string line by line
    for line in story.getStory():
        print(line)

# GAME SETTINGS
print('When you are ready to start, ')
player = input('What should we call you? ')
# boolean for game over and win
game_over = False
win = False

# start money = 300
money = 300
# start range = 600
fuel= 600
#mission completed
missions_completed = 0

# all airports
all_airports = get_airports()
# start_airport ident
start_airport = all_airports[0]['ident']

# current airport
current_airport = start_airport

# game id
game_id = create_game(money, fuel, start_airport, player, all_airports)


while not game_over:

    #Show current airport status
    airport = get_airport_info(current_airport)
    print(f"\nYou are at \033[35"
          f"m{airport['name']}.\033[0m")
    print(f"You have \033[35m{money:.0f}$ and {fuel:.0f}fuel.\033[0m")
    input("Press Enter to continue...")

    #Buy fuel
    buy = input("Do you want to buy fuel? 1$ = 2 fuel. Enter amount or press enter: ")
    if buy != "":
        cost = int(buy)
        if cost <= money:
            money -= cost
            fuel += cost * 2
            print(f"\033[34mBought {cost*2} fuel. New fuel: {fuel:.0f}fuel\033[0m")
        else:
            print("Not enough money!")

    #List airports in range
    airports = airports_in_range(current_airport, all_airports, fuel)
    if len(airports) == 0:
        print("You are out of range! Game over.")
        break

    print(f"\nThere are \033[36m{len(airports)}\033[0m airports in range:")
    print("Airports:")
    for airport in airports:
        dist = calculate_distance(current_airport, airport['ident'])
        fuel_needed = math.ceil(dist / 3)
        print(f"{airport['name']}, icao: {airport['ident']}, \033[33m distance: {dist:.0f} km\033[0m, \033[32m fuel needed: {fuel_needed}\033[0m ")

    #Choose destination
    dest = input("\nEnter destination ICAO: ").upper()
    selected_distance = calculate_distance(current_airport, dest)
    fuel_needed = math.ceil(selected_distance / 3)

    if fuel_needed > fuel:
        print("Not enough fuel to reach this airport! Choose another.")
        continue

    #Move to destination
    fuel -= fuel_needed
    update_location(dest,fuel, money, game_id)
    current_airport = dest

    #Give fixed delivery money
    money += 200
    print(f"\033[34m\nDelivery completed! +200$\033[0m")

    #Show airport status before event
    airport = get_airport_info(current_airport)
    print(f"You are at \033[35m{airport['name']}.\033[0m")
    print(f"You have \033[35m{money:.0f}$ and {fuel:.0f}fuel.\033[0m")
    input("Press Enter to continue...")

    #Check if this airport has an event
    event = check_event(game_id, current_airport)

    if event:

        if event['type'] == "Pirates":
                print("\033[34m\nEvent triggered: Pirates attacked! All money lost! But you found some fuel.\033[0m")
                money = 0
                fuel += 50
                print("Fuel: +50")
                print(f"You have 0$ and {fuel:.0f}fuel.")

        else:
            # for other events
            money += event['money']
            fuel += event['fuel']
            print(f"\033[34m\nEvent triggered: {event['description']}\033[0m")
            if event['money']:
                print(f"Money: {event['money']:+}$")
            if event['fuel']:
                print(f"Fuel: {event['fuel']:+}")

        update_location(current_airport, fuel, money, game_id)

        input("Press Enter to continue...")

    #Check losing conditions after updating fuel
    if  fuel <= 0:
        print("You lost! You have no fuel left.")
        game_over = True

    #Update missions
    missions_completed += 1

    #Display every 3 missions
    if missions_completed % 3 == 0:
        print(f"You have completed {missions_completed} missions!"
              f"Let's carry on champ!")

    if missions_completed >= 15 and fuel > 0 and money >= 0:
        print("Congratulations! You are one of  the most trusted pilot in Skybound Express.")
        game_over = True

# if game is over loop stops
# show game result
print(f'''You have {money:.0f}$''')
print(f'''You have {fuel:.0f}fuel''')











