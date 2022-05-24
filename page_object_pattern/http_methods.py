import json

import jsonpath as jsonpath
import pytest
import requests


class HTTPBaseMethods:

    def get_properly_url(self, api_key):
        properly_url = "https://reqres.in/api" + f"/{api_key}"
        return properly_url



class Httpmethods(HTTPBaseMethods):

    def get_status(self, api_key):
        properly_url = self.get_properly_url(api_key=api_key)
        resp = requests.get(properly_url)
        status = resp.status_code
        return status

    def get_response_data(self, api_key):
        properly_url = self.get_properly_url(api_key=api_key)
        resp = requests.get(properly_url)
        x = resp.json()
        data = x['data']
        return data

    def get_keys_from_dict(self, api_key):
        data = self.get_response_data(api_key=api_key)
        list_keys = []
        for k, v in data.items():
            list_keys.append(k)
        return list_keys

    def get_value_from_dict(self, api_key):
        data = self.get_response_data(api_key=api_key)
        list_values = []
        for k, v in data.items():
            list_values.append(v)
        return list_values

    def get_keys_from_list_of_dicts(self, api_key):
        data = self.get_response_data(api_key=api_key)
        list_keys = []
        for x in data:
            for z, y in x.items():
                list_keys.append(z)
            return list_keys

    def delete_record(self, api_key):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.delete(properly_url)
        status = r.status_code
        return status

    def post_request(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        post = requests.post(properly_url, data)
        return post.json()

    def post_status(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        post = requests.post(properly_url, data)
        status = post.status_code
        return status

    def put_request(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.put(properly_url, data)
        return r.json

    def put_status(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.put(properly_url, data)
        status = r.status_code
        return status



