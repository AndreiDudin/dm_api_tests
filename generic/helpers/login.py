import time

from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, facade):
        self.facade = facade

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
        response = self.facade.login_api.post_account_login(
            json=LoginCredentials(
                login=login,
                password=password,
                rememberMe=remember_me
            ),
            status_code=status_code,
            request_token=request_token
        )
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
        print(response.headers)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return token

    def logout_user(self, status_code: int = 204, **kwargs):
        response = self.facade.login_api.delete_account_login(
            status_code=status_code,
            **kwargs
        )
        return response

    def logout_user_from_all_devices(self, **kwargs):
        response = self.facade.login_api.delete_account_login_all(**kwargs)
        return response
