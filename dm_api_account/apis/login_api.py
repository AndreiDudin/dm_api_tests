import requests
from requests import Response

from restclient.restclient import RestClient
from ..models import *
from dm_api_account.utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_account_login(
            self,
            json: LoginCredentials,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json login_credentials_model
        Authentificate via credentials
        :return:
        """
        response = self.client.post(
            path="/v1/account/login",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def delete_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response | GeneralError:
        """
        Logout as current user
        :return:
        """
        response = self.client.delete(
            path="/v1/account/login",
            **kwargs
        )
        validate_status_code(response, status_code)
#         if response.status_code == status_code:
#             assert response.status_code == status_code
# #            return GeneralError(**response.json())
        return response

    def delete_account_login_all(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response | GeneralError:
        """
        Logout from every device
        :return:
        """
        response = self.client.delete(
            path="/v1/account/login/all",
            **kwargs
        )
        validate_status_code(response, status_code)
        # if response.status_code == status_code:
        #     return GeneralError(**response.json())
        return response
