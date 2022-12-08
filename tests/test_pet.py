import pytest


class TestPet:
    @pytest.mark.parametrize("endpoint", ["pet"])
    def test_same(self, api_client, endpoint):
        status, json_data = api_client.get(endpoint=endpoint, path=10)
        assert status == 200
        print(json_data)

    @pytest.mark.parametrize("endpoint", ["pet"])
    def test_same_two(self, api_client, endpoint):
        status, json_data = api_client.post(endpoint=endpoint)
        print(status)
        print(json_data)

    def test_same_put(self, api_client):
        status, json_data = api_client.post()
        print(status)
        print(json_data)

    # @pytest.mark.parametrize("id", Request.random_id)
    # def test_get_pet_valid_id(self, api_client):
    #     status, result = api_client.post()
    #     assert status == 200

    #
    # def test_post_add_new_pet(self, path):
    #     status, result = pet.post_add_new_pet(Request.data, Request.headers)
    #     assert status == 200
    #     assert result["name"] == Request.data["name"]
    #     print(result["name"])
    #
    # def test_post_update_pet(self, path):
    #     status, result = pet.update_pet(id, data=Request.update_data)
    #     assert status == 200
    #     status, result = pet.get_pet(id)
    #     assert result["name"] == Request.update_data["name"]


class TestStore:
    @pytest.mark.parametrize("endpoint", ["store/order"])
    def test_sam_store(self, api_client, endpoint):
        status, json_data = api_client.get(endpoint=endpoint, path=1)
        assert status == 200
        print(json_data)


#
#
# class TestUser(APIClient):
#     path = "user"
