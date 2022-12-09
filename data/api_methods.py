from data.apirequest import APIRequest
from data.api_data import RequestData as d


class Pet(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "pet"
        self.path = path
        self.response = APIRequest

    def post_upload_image(self, path=f"{d.random_id}/uploadImage"):
        response = self.post(self.endpoint, path)
        # return self.get_response_data(response)

    def post_add_a_new_pet(self):
        response = self.post(self.endpoint)
        # return self.get_response_data(response)

    def put_update_pet(self):
        response = self.put(self.endpoint)
        # return self.get_response_data(response)

    def get_find_by_status(self, path=f"/findByStatus"):
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
        self.response = APIRequest

    def post_place_an_order(self, path=f"/order"):
        response = self.post(self.endpoint, path)

    def get_find_order_by_id(self, path=f"/order/{d.random_order_id}"):
        response = self.get(self.endpoint, path)

    def delete_order_by_id(self, path=f"/order/{d.random_order_id}"):
        response = self.delete(self.endpoint, path)

    def get_return_pet_by_status(self, path=f"/inventory"):
        response = self.get(self.endpoint, path)


class User(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "store"
        self.path = path
        self.response = APIRequest
