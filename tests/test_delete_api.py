import pytest as pytest

from page_object_pattern.http_methods import Getapi

@pytest.mark.delete
class Testdeletetapi(Getapi):

    def test_delete_status_code_204(self):
        API = Getapi()
        actual_status = API.delete_record(API.get_properly_url("users/2"))
        assert actual_status == 204