# Creates a pokemon table with columns id, name, height, weight
# Asks the user for 3 pokemon names @
# Fetches each one from the PokeAPI
# Stores them in the database
# Reads them all back and prints them cleanly

import requests
import sqlite3

# SQLite3 things
conn = sqlite3.connect("pokemon.db")

cursor = conn.cursor()

# Deletes table if it already exists
cursor.execute("DROP TABLE IF EXISTS pokemon")

cursor.execute("""CREATE TABLE IF NOT EXISTS Pokemon(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    height INTEGER,
    weight INTEGER
    )""")
conn.commit()


# Input specified data and fetching data from api
for i in range(3):
    name = input(f"Enter pokemon no.{i+1}: ")

    # stores retrieved data
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")


    if response.status_code == 200:
        data = response.json()

        # Name: {data['name']}
        # Height: {data['height']}
        # Weight: {data['weight']}
        # Base Experience: {data['base_experience']}
        # abilities: data["abilities"]

        # adds data for each pokemon to database
        cursor.execute("INSERT INTO pokemon (name, height, weight) VALUES (?, ?, ?)",
                        (data["name"],data["height"],data["weight"]) )
        # saves changes
        conn.commit()
    else:
        print(f"{name} not found")


    # Bulbasaur
    # Charmander
    # Squirtle

cursor.execute("SELECT * FROM pokemon")
rows = cursor.fetchall()

for id, name, height, weight in rows:
    print(f"{id}.{name}\nHeight: {height}\nWeight: {weight}\n")



