import requests
import pytest

BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = 7232
TRAINER_NAME = "Xanitrol"

def test_get_trainers_status_code():
    response = requests.get(f"{BASE_URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def test_trainer_name_in_response():
    response = requests.get(f"{BASE_URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert TRAINER_NAME in response.text, f"Expected trainer name '{TRAINER_NAME}' in response but it was not found"