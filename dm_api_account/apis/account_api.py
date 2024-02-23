import requests
from requests import Response

from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from restclient.restclient import RestClient
from dm_api_account.models.change_email_model import ChangeEmailModel
from ..models import change_password_model
from ..models.change_password_model import ChangePasswordModel
from ..models.registration_model import RegistrationModel
from ..models.reset_password_model import ResetPasswordModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        :param json ResetPasswordModel
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered use password
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate register user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """
        response = requests.get(
            path=f"/v1/account",
            **kwargs
        )
        return response
