import pytest as pytest

from page_object_pattern.http_methods import Httpmethods

@pytest.mark.delete
class Testdeletetapi(Httpmethods):

    name = {"Delete": "users/2"}

    def test_delete_status_code_204(self, api_key = name["Delete"]):
        API = Httpmethods()
        actual_status = API.delete_record(API.get_properly_url(api_key))
        assert actual_status == 204

    # def test_ggget_single_user_keys(self, api_key=name["Single user"]):
    #     Obj = Httpmethods()
    #     actual_keys = Obj.get_keys_from_dict(Obj.get_response_data(Obj.get_properly_url(api_key)))
    #     assert actual_keys == self.expected_keys_users