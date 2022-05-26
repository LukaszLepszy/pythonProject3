import pytest as pytest

import config
from page_object_pattern.http_methods import Httpmethods

@pytest.mark.putpatch
class Testputpatchtapi(Httpmethods):

    name = {"Update": "users/2",
            "Patch": "users/2"
            }

    def test_patch_response_keys(self, api_key=config.patch):
        patch_request_data = {"name": "morpheus", "job": "zion resident"}
        API = Httpmethods()
        response_value_list = API.patch_responses_key_from_dict(api_key, patch_request_data)
        List1 = ["name", "job", "updatedAt"]
        if (all(elem in response_value_list for elem in List1)):
            assert True
        else: assert False

    def test_patch_response_values(self, api_key=config.patch):
        patch_request_data = {"name": "morpheus", "job": "zion resident"}
        API = Httpmethods()
        response_value_list = API.patch_respones_values_from_dict(api_key, patch_request_data)
        List1 = ["morpheus", "zion resident"]
        if (all(elem in response_value_list for elem in List1)):
            assert True
        else:
            assert False

    def test_put_update_status_code_200(self, api_key=config.update):
        post_request_data = {"name": "morpheus", "job": "zion resident"}
        API = Httpmethods()
        actual_status = API.put_status(api_key, post_request_data)
        assert actual_status == 200