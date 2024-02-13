import requests
from requests import Response

from ..models.login_credentials_model import login_credentials_model
from requests import session


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers = headers

    def post_account_login(self, json: login_credentials_model, **kwargs) -> Response:
        """
        :param json login_credentials_model
        Authentificate via credentials
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def delete_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """
        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )
        return response

    def delete_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        response = self.session.delete(
            url=f"{self.host}1/v1/account/login/all",
            **kwargs
        )
        return response
