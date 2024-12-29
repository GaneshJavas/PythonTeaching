import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
    res_url = f"{base_url}pokemon/{name}" 
    response = requests.get(res_url)
    if response.status_code == 200:
        print("Data Existed")
        return (response.json())

    else:
        print("Data not found")

poke_name = "pikachu"
poke_info = get_info(poke_name)

