import requests
import pytest
from data.api_data import Request


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint="", path='', params=None):
        url = f'{self.base_url}/{endpoint}/{path}'
        print(url)
        response = requests.get(url, params=params)
        status = response.status_code
        json_data = response.json()
        return status, json_data

    def post(self, endpoint="", path='', params=None, json=None, headers=None):
        url = f'{self.base_url}/{endpoint}/{path}'
        response = requests.post(url, params=params, json=Request.data, headers=Request.headers)
        status = response.status_code
        json_data = response.json()
        return status, json_data

    def put(self, endpoint="", params=None, json=None, headers=None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.post(url, params=params, json=Request.data2, headers=Request.headers)
        status = response.status_code
        json_data = response.json()
        return status, json_data

    def delete(self):
        pass

    # def get_pet(self, id):
    #     response = requests.get(f"{url}/pet/{id}")
    #     status = response.status_code
    #     result = response.json()
    #     return status, result
    #
    # def update_pet(self, id, data):
    #     response = requests.post(f"{url}/pet/{id}", data=data)
    #     status = response.status_code
    #     result = response.json()
    #     return status, result
    #
    # def post_add_new_pet(self, data, headers):
    #     response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
    #     status = response.status_code
    #     result = response.json()
    #     return status, result


@pytest.fixture
def api_client():
    pet_store_url = "https://petstore.swagger.io/v2"
    return APIClient(base_url=pet_store_url)


# @pytest.mark.parametrize('endpoint', ['pet'])
# @pytest.fixture()
# def endpoint():
#     return "pet"

