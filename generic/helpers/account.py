from dm_api_account.models import Registration, ResetPassword, ChangePassword, ChangeEmail

# try:
#     from services.dm_api_account import Facade
# except ImportError:
#     ...


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str,
            **kwargs
    ):
        response = self.facade.account_api.register(
            registration=Registration(
                login=login,
                email=email,
                password=password
            ),
            **kwargs
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.activate(
            token=token
        )
        return response

    def get_user_info(
            self,
            status_code: int = 200,
            **kwargs
    ):
        response = self.facade.account_api.get_v1_account(
            status_code=status_code,
            **kwargs)
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def reset_user_password(
            self,
            login: str,
            email: str,
            status_code: int = 200,
            **kwargs
    ):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            ),
            status_code=status_code,
            **kwargs
        )
        return response

    def change_user_password(
            self,
            login: str,
            old_password: str,
            new_password: str,
            status_code: int = 200,
            **kwargs
    ):
        token = self.facade.mailhog.get_token_by_login_for_reset(login=login)
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                oldPassword=old_password,
                newPassword=new_password
            ),
            status_code=status_code,
            **kwargs
        )
        return response

    def change_registered_user_email(
            self,
            login: str,
            password: str,
            email: str,
            status_code: int = 200,
            **kwargs
    ):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                password=password,
                email=email
            ),
            status_code=status_code,
            **kwargs
        )
        return response
