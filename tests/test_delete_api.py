import pytest as pytest

from page_object_pattern.http_methods import Httpmethods

@pytest.mark.delete
class Testdeletetapi(Httpmethods):

    name = {"Delete": "users/2"}

    def test_delete_status_code_204(self, api_key = name["Delete"]):
        API = Httpmethods()
        actual_status = API.delete_record(API.get_properly_url(api_key))
        assert actual_status == 204