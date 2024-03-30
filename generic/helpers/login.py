import time
import allure
from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.login_api.client.session.headers.update(headers)

    def login_user(
            self,
            login: str,
            password: str,
            remember_me: bool = True,
            status_code: int = 200,
            request_token: bool = True
    ):
        response = self.facade.login_api.v1_account_login_post(
            login_credentials=LoginCredentials(
                login=login,
                password=password,
                remember_me=remember_me
            )
        )
        print(response)
        return response

    def get_auth_token(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        response = self.login_user(
            login=login,
            password=password,
            remember_me=remember_me
        )
        time.sleep(5)
        print(response)
 #       token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        token = response[2]['X-Dm-Auth-Token']
        return token

    def logout_user(self, status_code: int = 204, **kwargs):
        response = self.facade.login_api.v1_account_login_delete(
            status_code=status_code,
            **kwargs
        )
        return response

    def logout_user_from_all_devices(self, **kwargs):
        response = self.facade.login_api.v1_account_login_all_delete(**kwargs)
        return response
