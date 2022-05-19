import json

import jsonpath as jsonpath
import pytest
import requests


class Httpmethods:

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

    def get_value_from_dict(self, data):
        list_values = []
        for k, v in data.items():
            list_values.append(v)
        return list_values

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

    def post_request(self, properly_url, data):
        post = requests.post(properly_url, data)
        return post.json()

    def post_status(self, properly_url, data):
        post = requests.post(properly_url, data)
        status = post.status_code
        return status

    def put_request(self, properly_url, data):
        r = requests.put(properly_url, data)
        return r.json

    def put_status(self, properly_url, data):
        r = requests.put(properly_url, data)
        status = r.status_code
        return status



