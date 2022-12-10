from data.api_request import APIRequest
from data.api_data import RequestData as d


class Pet(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "pet"
        self.path = path
        self.response = APIRequest()

    def post_upload_image(self, path=f"{d.random_id}/uploadImage"):
        response = self.post(self.endpoint, path)
        return self.get_response_data(response)

    def post_add_a_new_pet(self):
        response = self.post(self.endpoint)
        # return self.get_response_data(response)

    def put_update_pet(self):
        response = self.put(self.endpoint)
        # return self.get_response_data(response)

    def get_find_by_status(self, path="/findByStatus"):
        response = self.get(self.endpoint, path)
        # return self.get_response_data(response)

    def get_find_pet_by_id(self, path=f"/{d.random_id}"):
        response = self.get(self.endpoint, path)
        # return self.get_response_data(response)

    def post_update_pet_by_id(self, path=f"/{d.random_id}"):
        response = self.post(self.endpoint, path)
        # return self.get_response_data(response)

    def delete_pet_by_id(self, path=f"/{d.random_id}"):
        response = self.delete(self.endpoint, path)
        # return self.get_response_data(response)


class Store(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "store"
        self.path = path
        self.response = APIRequest()

    def post_place_an_order(self, path=f"/order"):
        response = self.post(self.endpoint, path)

    def get_find_order_by_id(self, path=f"/order/{d.random_order_id}"):
        response = self.get(self.endpoint, path)

    def delete_order_by_id(self, path=f"/order/{d.random_order_id}"):
        response = self.delete(self.endpoint, path)

    def get_return_pet_inventory_by_status(self, path='inventory'):
        response = self.get(self.endpoint, path)


class User(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "user"
        self.path = path
        self.response = APIRequest()

    def post_create_list_users_array(self, path='createWithArray'):
        response = self.get(self.endpoint, path)

    def post_create_list_users_list(self, path='createWithList'):
        response = self.get(self.endpoint, path)

    def get_user_by_username(self, path=f'{d.randome_name}'):
        response = self.get(self.endpoint, path)

    def put_user_by_username(self, path=f'{d.randome_name}'):
        response = self.put(self.endpoint, path)

    def delete_user_by_username(self, path=f'{d.randome_name}'):
        response = self.delete(self.endpoint, path)

    def get_logs_user(self, path='login'):
        response = self.get(self.endpoint, path)

    def get_logs_out_user(self, path='logout'):
        response = self.delete(self.endpoint, path)

    def post_create_user(self):
        response = self.delete(self.endpoint)

