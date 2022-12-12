import string
import random


class RequestData:
    random_name = "".join(random.choice(string.ascii_lowercase) for _ in range(5))
    random_id = random.randrange(1, 10)
    random_order_id = random.randrange(1, 10)
    create_random_id = random.randrange(101, 1000)
    data = {
        "id": random_id,
        "category": {"id": 0, "name": "string"},
        "name": random_name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

    def put_data(self):
        return {"id": 650, "name": "Barsik", "status": "available"}

    data2 = {"id": 650, "name": "Barsik", "status": "available"}
    update_data = {"name": "Bobik", "status": "sold"}
    upload_data = {"additionalMetadata": "xml"}
    store_data = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2022-12-08T09:10:58.100Z",
        "status": "placed",
        "complete": True,
    }
