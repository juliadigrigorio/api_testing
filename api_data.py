import string
import random


class Request:
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    data = {
        "id": 300,
        "category": {"id": 0, "name": "string"},
        "name": "dog",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }
    data2 = {"id": 650, "name": "Barsik", "status": "available"}
    update_data = {"name": "Bobik", "status": "sold"}
    # def randome_name(self):
    #     self.letters = string.ascii_lowercase
    #     self.name= "".join(random.choice(self.letters) for _ in range(8))
    #     return name
    random_id_avalible = random.randrange(1, 100)
    create_random_id = random.randrange(101, 1000)
    store_data = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2022-12-08T09:10:58.100Z",
        "status": "placed",
        "complete": True,
    }
