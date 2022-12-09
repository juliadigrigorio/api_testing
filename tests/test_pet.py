import pytest
import allure
from data.api_methods import Pet, Store, User


@allure.epic("US_001.00.00 | Pet > Everything about your Pets")
class TestPet:
    pet = Pet()

    params = [{"status": "sold"}, {"status": "pending"}, {"status": "available"}]

    @allure.feature("TS_001.01.00 |  Uploads an image")
    @allure.story("TC_001.01.01")
    def test_same(self):
        response = self.pet.post_upload_image()

    @allure.feature("TC_001.02.01  | Add a new pet")
    @allure.story("TC_001.02.01.01")
    def test(self):
        response = self.pet.post_add_a_new_pet()

    @allure.feature("TC_001.02.02  | Update an existing pet")
    @allure.story("TC_001.02.01.01")
    def test_1(self):
        response = self.pet.put_update_pet()

    @pytest.mark.parametrize("params", params)
    def test_2(self, params):
        response = self.pet.get_find_by_status(params)


@allure.epic("US_002.00.00 | Store > Access to Petstore orders")
class TestStore:
    store = Store()


@allure.epic("US_003.00.00 | User > Operations about user")
class TestUser:
    user = User()
