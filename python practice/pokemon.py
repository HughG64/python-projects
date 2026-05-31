import requests

name = input("Enter a Pokemon name: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

if response.status_code == 200:
    data = response.json()
    # print(f"Name: {data['name']}")
    # print(f"Height: {data['height']}")
    # print(f"Weight: {data['weight']}")
    # print(f"Base Experience: {data['base_experience']}")
    abilities = data["abilities"]
else:
    print(f"Pokemon not found. Status code: {response.status_code}")

[
    {'ability':
    {'name': 'blaze','url': 'https://pokeapi.co/api/v2/ability/66/'},
    'is_hidden': False,
    'slot': 1},
    {'ability':
    {'name': 'solar-power','url': 'https://pokeapi.co/api/v2/ability/94/'},
    'is_hidden': True,
    'slot': 3}
 ]

for items in abilities:
    print(items["ability"]["name"], end=" ")
    if items["is_hidden"] == True:
        print("Hidden")
    else:
        print("Not Hidden")


# charizard
