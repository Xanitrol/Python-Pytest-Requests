import requests
import json

# Базовый URL API
BASE_URL = 'https://api.pokemonbattle.ru/v2'

# Заголовки для авторизации и контента
headers = {
    'trainer_token': 'e6a602c240268c1d2b6d51c7bd635a86',
    'Content-Type': 'application/json'
}

# 1. Создание покемона
create_pokemon_url = f"{BASE_URL}/pokemons"
create_pokemon_data = {
    "name": "generate",
    "photo_id": "-1"
}

response_create = requests.post(create_pokemon_url, headers=headers, data=json.dumps(create_pokemon_data))
print("Создание покемона:")
create_response = response_create.json()
print(create_response)

# Получаем ID созданного покемона
pokemon_id = create_response.get("id")  

# Замените "pokemon_id" на правильное поле из ответа

if not pokemon_id:
    raise ValueError("Не удалось получить ID созданного покемона")

# 2. Смена имени покемона
update_pokemon_url = f"{BASE_URL}/pokemons"
update_pokemon_data = {
    "pokemon_id": str(pokemon_id),
    "name": "QQQQQQ",
    "photo_id": -1
}

response_update = requests.put(update_pokemon_url, headers=headers, data=json.dumps(update_pokemon_data))
print("\Смена имени покемона:")
print(response_update.json())

# 3. Поймать покемона в покебол
add_pokeball_url = f"{BASE_URL}/trainers/add_pokeball"
add_pokeball_data = {
    "pokemon_id": str(pokemon_id)
}

response_add_pokeball = requests.post(add_pokeball_url, headers=headers, data=json.dumps(add_pokeball_data))
print("\Поймать покемона в покебол:")
print(response_add_pokeball.json())