import json

import jsonpath as jsonpath
import pytest
import requests


class Getapi():

    # def __init__(self, api_key):
    #     self.api_key = api_key
    #     self.base_url = "https://reqres.in/api"
    #     self.new_data = {"name": "morpheus", "job": "leader"}

    def api_test(self, api_key):
        BASE_URL = "https://reqres.in/api"
        API = BASE_URL + f"/{api_key}"
        url = API
        resp = requests.get(url)
        status = resp.status_code
        x = resp.json()
        data = x['data']
        return data

    def get_keys_form_dict(self, api_key):
        list_keys = []
        for key, value in self.api_test(api_key).items():
            list_keys.append(key)
        return list_keys



    def get_properly_url(self, api_key):
        properly_url = "https://reqres.in/api" + f"/{api_key}"
        return properly_url

    def get_status(self, properly_url):
        resp = requests.get(properly_url)
        status = resp.status_code
        return status

    def get_response_data(self, properly_url):
        resp = requests.get(properly_url)
        x = resp.json()
        data = x['data']
        return data

    def get_keys_from_dict(self, data):
        list_keys = []
        for k, v in data.items():
            list_keys.append(k)
        return list_keys

    def get_keys_from_list_of_dicts(self, data):
        list_keys = []
        for x in data:
            for z, y in x.items():
                list_keys.append(z)
            return list_keys

    def delete_record(self, properly_url):
        r = requests.delete(properly_url)
        status = r.status_code
        return status

    def post_data(self, properly_url):
        self.new_data = {"name": "morpheus", "job": "leader"}
        post = requests.post(properly_url, self.new_data)
        return post.text

    def post_register(self, properly_url):
        self.register_data = { "email": "eve.holt@reqres.in", "password": "pistol"}
        post = requests.post(properly_url, self.register_data)
        return post.text

    def loads(self):
        url = "https://reqres.in/api/users/2"
        r = requests.get(url)
        y = r.json()
        z = y["data"]["id"]
        x = json.loads(r.text)
        return z

    def loadss(self):
        url = "https://reqres.in/api/users/2"
        r = requests.get(url)
        x = json.loads(r.text)
        pages = jsonpath.jsonpath(x, "data")
        return pages


API = Getapi()
print(API.post_register(API.get_properly_url("register")))
# print(type(API.loadss()))


# print(API.get_keys(API.get_response_data(API.get_properly_url('users/2'))))

