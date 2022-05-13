import pytest as pytest

from page_object_pattern.get_api import Getapi


class Testgetapi(Getapi):

    get_api_key_list = ["users?page=2", "users/2", "unknow", "unknow/2", "users?delay=3"]
    expected_keys_users = ['id', 'email', 'first_name', 'last_name', 'avatar']
    expected_keys_resource = ['id', 'name', 'year', 'color', 'pantone_value']


    def test_single_user_keys(self, api_key="users/2"):
        API = Getapi()
        actual_keys = API.get_keys_from_dict(API.get_response_data(API.get_properly_url(api_key)))
        assert  actual_keys == self.expected_keys_users

    def test_get_list_users_keys(self, api_key="users?page=2"):
        API = Getapi()
        actual_keys = API.get_keys_from_list_of_dicts(API.get_response_data(API.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_users

    def test_single_resource_keys(self, api_key="unknow/2"):
        API = Getapi()
        actual_keys = API.get_keys_from_dict(API.get_response_data(API.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_resource

    def test_list_resources_keys(self, api_key="unknow"):
        API = Getapi()
        actual_keys = API.get_keys_from_list_of_dicts(API.get_response_data(API.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_resource

    @pytest.mark.parametrize("api_key", ["users?page=2", "users/2", "unknow", "unknow/2", "users?delay=3"])
    def test_status_code_200(self, api_key):
        API = Getapi()
        actual_status = API.get_status(API.get_properly_url(api_key))
        assert actual_status == 200

    @pytest.mark.parametrize("api_key", ["users/23", "unknow/23"])
    def test_status_code_404(self, api_key):
        API = Getapi()
        actual_status = API.get_status(API.get_properly_url(api_key))
        assert actual_status == 404

    def test_delete_status(self):
        API = Getapi()
        actual_status = API.delete_record(API.get_properly_url("users/2"))
        assert actual_status == 204