import pytest as pytest

from page_object_pattern.http_methods import Getapi

@pytest.mark.post
class Testpostapi(Getapi):


    def test_post_create_status_code_201(self, api_key='users'):
        post_request_data = {"name": "morpheus", "job": "leader"}
        API = Getapi()
        actual_status = API.post_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 201

    def test_post_create_response_keys(self, api_key='users'):
        post_request_data = {"name": "morpheus", "job": "leader"}
        API = Getapi()
        request = API.post_request(API.get_properly_url(api_key), post_request_data)
        response_keys = API.get_keys_from_dict(request)
        assert response_keys == ["name", "job", "id", "createdAt"]

    def test_post_create_response_values(self, api_key='users'):
        post_request_data = {"name": "morpheus", "job": "leader"}
        API = Getapi()
        request = API.post_request(API.get_properly_url(api_key), post_request_data)
        response_value_list = API.get_value_from_dict(request)
        List1 = ["morpheus", "leader"]
        if (all(elem in response_value_list for elem in List1)):
            assert True
        else: assert False

    def test_post_register_status_code_200(self, api_key='register'):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        API = Getapi()
        actual_status = API.post_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 200

    def test_post_register_response(self, api_key='register'):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        API = Getapi()
        response = API.post_request(API.get_properly_url(api_key), post_request_data)
        expected_response = {"id": 4, "token": "QpwL5tke4Pnpja7X4"}
        assert response == expected_response

    def test_post_register_status_code_400(self, api_key='register'):
        post_request_data = {"email": "sydney@fife"}
        API = Getapi()
        actual_status = API.post_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 400

    def test_post_register_response_unsuccessful(self, api_key='register'):
        post_request_data = {"email": "sydney@fife"}
        API = Getapi()
        response = API.post_request(API.get_properly_url(api_key), post_request_data)
        expected_response = {"error": "Missing password"}
        assert response == expected_response

    def test_post_login_status_code_200(self, api_key='login'):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        API = Getapi()
        actual_status = API.post_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 200

    def test_post_login_response_successful(self, api_key='login'):
        post_request_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        API = Getapi()
        response = API.post_request(API.get_properly_url(api_key), post_request_data)
        expected_response = {"token": "QpwL5tke4Pnpja7X4"}
        assert response == expected_response

    def test_post_login_status_code_400(self, api_key='login'):
        post_request_data = {"email": "peter@klaven"}
        API = Getapi()
        actual_status = API.post_status(API.get_properly_url(api_key), post_request_data)
        assert actual_status == 400

    def test_post_login_response_unsuccessful(self, api_key='login'):
        post_request_data = {"email": "peter@klaven"}
        API = Getapi()
        response = API.post_request(API.get_properly_url(api_key), post_request_data)
        expected_response = {"error": "Missing password"}
        assert response == expected_response