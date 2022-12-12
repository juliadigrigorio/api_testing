import requests
import json


class Requests:
    
    # def get_pet(self, id):
    #     response = requests.get(f"{url}/pet/{id}")
    #     status = response.status_code
    #     result = response.json()
    #     return status, result

    # def update_pet(self, id, data):
    #     response = requests.post(f"{url}/pet/{id}", data=data)
    #     status = response.status_code
    #     result = response.json()
    #     return status, result

    # def post_add_new_pet(self, data, headers):
    #     response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
    #     status = response.status_code
    #     result = response.json()
    #     return status, result

    @staticmethod
    def get(url, data = None, headers = None, cookies = None):
        return Requests._send(url, data, headers, cookies, "GET")
    def post(url, data = None, headers = None, cookies = None):
        return Requests._send(url, data, headers, cookies, "POST")
    def put(url, data = None, headers = None, cookies = None):
        return Requests._send(url, data, headers, cookies, "PUT")
    def delete(url, data = None, headers = None, cookies = None):
        return Requests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url, data, headers, cookies, method):
        url = f"https://petstore.swagger.io/v2{url}"
        
        if data is None:
            data = {}
        elif headers is None:
            headers = {}
        elif cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url, params = data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data = json.dumps(data), headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data = data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data = data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Very bad method '{method}'")

        return response
