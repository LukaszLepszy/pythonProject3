import pytest as pytest

import config
from page_object_pattern.http_methods import Httpmethods

@pytest.mark.delete
class Testdeletetapi(Httpmethods):

    name = {"Delete": "users/2"}

    def test_delete_status_code_204(self, api_key = config.delete):
        API = Httpmethods()
        actual_status = API.delete_record(api_key)
        assert actual_status == 204

