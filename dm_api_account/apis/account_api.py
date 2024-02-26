import requests
from requests import Response

from restclient.restclient import RestClient
from dm_api_account.models import *
from dm_api_account.utilities import validate_request_json, validate_status_code


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:
        """
        :param status_code:
        :param json registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path=f"/v1/account",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 201,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json ResetPasswordModel
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        elif response.status_code == 200:
            return response
        else:
            assert response.status_code == response.status_code, \
                f"Фактический {response.status_code}"

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_password_model
        Change registered use password
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Activate register user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(self, status_code: int = 200, **kwargs) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """
        response = requests.get(
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserDetailsEnvelope(**response.json())
        return response
