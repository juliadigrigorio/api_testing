import pytest
import allure
from data.api_methods import Pet, Store, User
from data.api_request import Response


@allure.epic("US_001.00.00 | Pet > Everything about your Pets")
class TestPet:
    pet = Pet()

    payload = [{"status": "sold"}, {"status": "pending"}, {"status": "available"}]

    @allure.feature("TS_001.01.00 |  Uploads an image")
    @allure.story("TC_001.01.01")
    def test_same(self):
        response = self.pet.post_upload_image()
        print(response.status_code)
        print(response.json_data)

    @allure.feature("TC_001.02.01  | Add a new pet")
    @allure.story("TC_001.02.01.01")
    def test(self):
        response = self.pet.post_add_a_new_pet()
        print(response.status_code)
        assert 'id' in response.json_data.keys()
        print(response.json_data['id'])
        print(response.json_data['name'])
        print(response.headers)

    @allure.feature("TC_001.02.02  | Update an existing pet")
    @allure.story("TC_001.02.01.01")
    def test_1(self):
        response = self.pet.put_update_pet()

    @pytest.mark.parametrize("params", payload)
    def test_2(self, params):
        response = self.pet.get_find_by_status(params)
        print(response.status_code)
        print(response.json_data)


@allure.epic("US_002.00.00 | Store > Access to Petstore orders")
class TestStore:
    store = Store()

    @allure.feature("TS_002.03.00   | Returns pet inventories by status")
    @allure.story("TC_001.02.01.01")
    def test_return(self):
        response = self.store.get_return_pet_inventory_by_status()


@allure.epic("US_003.00.00 | User > Operations about user")
class TestUser:
    user = User()

    @allure.feature("TS_003.03.00   | ")
    @allure.story("TC_001.02.01.01")
    def test_return(self):
        response = self.user.post_create_list_users_array()
