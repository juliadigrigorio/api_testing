import requests
import json
from api import Requests
from api_data import *


# def test_get_pet_valid_id():
#     status, result = pet.get_pet(id)
#     assert status == 200


# def test_post_add_new_pet():
#     status, result = pet.post_add_new_pet(data, headers)
#     assert status == 200
#     assert result["name"] == data["name"]
#     print(result["name"])


# def test_post_update_pet():
#     status, result = pet.update_pet(id, data=update_data)
#     assert status == 200
#     status, result = pet.get_pet(id)
#     assert result["name"] == update_data["name"]

def test_get_pet_valid_id():
    response = Requests.get(f"/pet/{id}")
    assert response.status_code == 200
    print(response.content)


def test_post_add_new_pet():
    response = Requests.post("/pet", data, headers)
    assert response.status_code == 200
    assert (response.json())["name"] == data["name"]
    print((response.json())["name"])
