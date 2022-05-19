import pytest as pytest

from page_object_pattern.http_methods import Getapi

@pytest.mark.putpatch
class Testputpatchtapi(Getapi):

    def test_patch_response_values(self, api_key='users/2'):
        post_request_data = {"name": "morpheus", "job": "zion resident"}
        API = Getapi()
        request = API.post_request(API.get_properly_url(api_key), post_request_data)
        response_value_list = API.get_value_from_dict(request)
        List1 = ["morpheus", "zion resident"]
        if (all(elem in response_value_list for elem in List1)):
            assert True
        else: assert False

    def test_put_update_status_code_200(self, api_key='users/2'):
        post_request_data = {"name": "morpheus", "job": "zion resident"}
        API = Getapi()
        actual_status = API.put_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 200