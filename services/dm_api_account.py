from apis.dm_api_account.apis.account_api import AccountApi
from apis.dm_api_account.apis.login_api import LoginApi
from generic.helpers.login import Login
from generic.helpers.account import Account


class Facade:
    def __init__(self, host, mailhog=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = mailhog
        self.account = Account(self)
        self.login = Login(self)
