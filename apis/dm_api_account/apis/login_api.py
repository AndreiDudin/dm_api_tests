import allure
from requests import Response
from apis.dm_api_account.models import *
from common_libs.restclient.restclient import RestClient
from apis.dm_api_account.utilities import validate_request_json, validate_status_code


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
            request_token: bool = True,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json login_credentials_model
        Authentificate via credentials
        :return:
        """
        with allure.step("Authenticate via credentials"):
            response = self.client.post(
                path="/v1/account/login",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        if request_token is True:
            return response
        else:
            return UserEnvelope(**response.json())

    def delete_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response | GeneralError:
        """
        Logout as current user
        :return:
        """
        with allure.step("Logout as current user"):
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
        with allure.step("Logout from every device"):
            response = self.client.delete(
                path="/v1/account/login/all",
                **kwargs
            )
        validate_status_code(response, status_code)
        # if response.status_code == status_code:
        #     return GeneralError(**response.json())
        return response
