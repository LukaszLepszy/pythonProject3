import json

import jsonpath as jsonpath
import pytest
import requests


class HTTPBaseMethods:

    def get_properly_url(self, api_key):
        properly_url = "https://reqres.in/api" + f"/{api_key}"
        return properly_url



class Httpmethods(HTTPBaseMethods):

    """GET METHODS"""
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

    """DELETE METHODS"""
    def delete_record(self, api_key):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.delete(properly_url)
        status = r.status_code
        return status

    """POST METHODS"""
    def post_response(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        post = requests.post(properly_url, data)
        return post.json()

    def post_status(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        post = requests.post(properly_url, data)
        status = post.status_code
        return status

    def post_respones_keys_from_dict(self, api_key, post_data):
        data = self.post_response(api_key=api_key, data=post_data)
        list_keys = []
        for k, v in data.items():
            list_keys.append(k)
        return list_keys

    def post_respones_values_from_dict(self, api_key, post_data):
        data = self.post_response(api_key=api_key, data=post_data)
        list_values = []
        for k, v in data.items():
            list_values.append(v)
        return list_values

    """PUT METHODS"""
    def put_response(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.put(properly_url, data)
        return r.json()

    def put_status(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.put(properly_url, data)
        status = r.status_code
        return status

    """PATCH METHODS"""
    def patch_response(self, api_key, data):
        properly_url = self.get_properly_url(api_key=api_key)
        r = requests.patch(properly_url, data)
        return r.json()

    def patch_responses_key_from_dict(self, api_key, patch_data):
        data = self.patch_response(api_key=api_key, data=patch_data)
        list_keys = []
        for k, v in data.items():
            list_keys.append(k)
        return list_keys

    def patch_respones_values_from_dict(self, api_key, patch_data):
        data = self.post_response(api_key=api_key, data=patch_data)
        list_values = []
        for k, v in data.items():
            list_values.append(v)
        return list_values

#     def example(self):
#         data = {"name": "morpheus", "job": "zion resident"}
#         properly_url = "https://reqres.in/api/users/2"
#         patch = requests.patch(properly_url, data)
#         return patch.json()
#
# HTTP = Httpmethods()
# print(HTTP.xx())