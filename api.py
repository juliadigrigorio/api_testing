import requests
import json

url = "https://petstore.swagger.io/v2"


class Pet:
    def __init__(self):
        self.url = url

    def get_pet(self, id):
        response = requests.get(f"{url}/pet/{id}")
        status = response.status_code
        result = response.json()
        return status, result

    def update_pet(self, id, data):
        response = requests.post(f"{url}/pet/{id}", data=data)
        status = response.status_code
        result = response.json()
        return status, result

    def post_add_new_pet(self, data, headers):
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        result = response.json()
        return status, result
