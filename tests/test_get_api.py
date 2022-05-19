import pytest as pytest

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

    def test_get_single_user_keys(self, api_key=name["Single user"]):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_dict(Obj.get_response_data(Obj.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_users

    def test_get_list_users_keys(self, api_key=name["List users"]):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_list_of_dicts(Obj.get_response_data(Obj.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_users

    def test_get_single_resource_keys(self, api_key=name["Single <resource>"]):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_dict(Obj.get_response_data(Obj.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_resource

    def test_get_list_resources_keys(self, api_key=name["List <resource>"]):
        Obj = Httpmethods()
        actual_keys = Obj.get_keys_from_list_of_dicts(Obj.get_response_data(Obj.get_properly_url(api_key)))
        assert actual_keys == self.expected_keys_resource

    @pytest.mark.parametrize("api_key", [name["List users"], name["Single user"], name["List <resource>"],
                                         name["Single <resource>"], name["Delayed response"]])
    def test_get_status_code_200(self, api_key):
        Obj = Httpmethods()
        actual_status = Obj.get_status(Obj.get_properly_url(api_key))
        assert actual_status == 200

    @pytest.mark.parametrize("api_key", [name["Single user not found"], name["Single <resource> not found"]])
    def test_get_status_code_404(self, api_key):
        Obj = Httpmethods()
        actual_status = Obj.get_status(Obj.get_properly_url(api_key))
        assert actual_status == 404

