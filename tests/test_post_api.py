import pytest as pytest

from page_object_pattern.http_methods import Httpmethods

@pytest.mark.post
class Testpostapi(Httpmethods):

    name = {"Create": "users",
            "Register successful": "register",
            "Register unsuccessful": "register",
            "Login successful": "login",
            "Login unsuccessful": "login"
            }

    def test_post_create_status_code_201(self, api_key=name['Create']):
        post_request_data = {"name": "morpheus", "job": "leader"}
        Obj = Httpmethods()
        actual_status = Obj.post_status(Obj.get_properly_url(api_key), post_request_data)
        assert actual_status == 201

    def test_post_create_response_keys(self, api_key=name['Create']):
        post_request_data = {"name": "morpheus", "job": "leader"}
        Obj = Httpmethods()
        request = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        response_keys = Obj.get_keys_from_dict(request)
        assert response_keys == ["name", "job", "id", "createdAt"]

    def test_post_create_response_values(self, api_key=name['Create']):
        post_request_data = {"name": "morpheus", "job": "leader"}
        Obj = Httpmethods()
        request = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        response_value_list = Obj.get_value_from_dict(request)
        List1 = ["morpheus", "leader"]
        if (all(elem in response_value_list for elem in List1)):
            assert True
        else: assert False

    def test_post_register_status_code_200(self, api_key=name['Register successful']):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        Obj = Httpmethods()
        actual_status = Obj.post_status(Obj.get_properly_url(api_key), post_request_data)
        assert actual_status == 200

    def test_post_register_response(self, api_key=name['Register successful']):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        Obj = Httpmethods()
        response = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        expected_response = {"id": 4, "token": "QpwL5tke4Pnpja7X4"}
        assert response == expected_response

    def test_post_register_status_code_400(self, api_key=name["Register unsuccessful"]):
        post_request_data = {"email": "sydney@fife"}
        Obj = Httpmethods()
        actual_status = Obj.post_status(Obj.get_properly_url(api_key), post_request_data)
        assert actual_status == 400

    def test_post_register_response_unsuccessful(self, api_key=name["Register unsuccessful"]):
        post_request_data = {"email": "sydney@fife"}
        Obj = Httpmethods()
        response = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        expected_response = {"error": "Missing password"}
        assert response == expected_response

    def test_post_login_status_code_200(self, api_key=name["Login successful"]):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        Obj = Httpmethods()
        actual_status = Obj.post_status(Obj.get_properly_url(api_key), post_request_data)
        assert actual_status == 200

    def test_post_login_response_successful(self, api_key=name["Login successful"]):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        Obj = Httpmethods()
        response = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        expected_response = {"token": "QpwL5tke4Pnpja7X4"}
        assert response == expected_response

    def test_post_login_status_code_400(self, api_key=name["Login unsuccessful"]):
        post_request_data = {"email": "peter@klaven"}
        Obj = Httpmethods()
        actual_status = Obj.post_status(Obj.get_properly_url(api_key), post_request_data)
        assert actual_status == 400

    def test_post_login_response_unsuccessful(self, api_key=name["Login unsuccessful"]):
        post_request_data = {"email": "peter@klaven"}
        Obj = Httpmethods()
        response = Obj.post_request(Obj.get_properly_url(api_key), post_request_data)
        expected_response = {"error": "Missing password"}
        assert response == expected_response