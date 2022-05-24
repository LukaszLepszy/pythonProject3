import pytest as pytest
from unittest.mock import patch

import config
from page_object_pattern.http_methods import Httpmethods


@pytest.mark.get
class Testgetapi(Httpmethods):

    name = {"List users": "users?page=2",
            "Single user": "users/2",
            "Single user not found": "users/23",
            "List <resource>": "unknown",
            "Single <resource>": "unknown/2",
            "Single <resource> not found": "unknown/23",
            "Delayed response": "users?delay=3"
            }

    expected_keys_users = ['id', 'email', 'first_name', 'last_name', 'avatar']
    expected_keys_resource = ['id', 'name', 'year', 'color', 'pantone_value']

    def test_get_single_user_keys(self, api_key=config.single_user):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_dict(api_key)
        assert actual_keys == self.expected_keys_users

    # @patch('get_keys_from_dict')
    # def test_get_mocking_keys(self, get_keys_from_dict_mock):
    #     get_keys_from_dict_mock.return_value = ['id', 'email', 'first_name', 'last_name', 'avatar']
    #     assert get_keys_from_dict_mock == ['id', 'email', 'first_name', 'last_name', 'avatar']


    def test_get_list_users_keys(self, api_key=config.list_users):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_list_of_dicts(api_key)
        assert actual_keys == self.expected_keys_users

    def test_get_single_resource_keys(self, api_key=config.single_resource):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_dict(api_key)
        assert actual_keys == self.expected_keys_resource

    def test_get_list_resources_keys(self, api_key=config.list_resource):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_list_of_dicts(api_key)
        assert actual_keys == self.expected_keys_resource

    @pytest.mark.parametrize("api_key", [config.list_users, config.single_user, config.list_resource,
                                         config.single_resource, config.delayed_response])
    def test_get_status_code_200(self, api_key):
        Obj = Httpmethods()
        actual_status = Obj.get_status(api_key)
        assert actual_status == 200

    @pytest.mark.parametrize("api_key", [config.single_user_not_found, config.single_resource_not_found])
    def test_get_status_code_404(self, api_key):
        Obj = Httpmethods()
        actual_status = Obj.get_status(api_key)
        assert actual_status == 404


