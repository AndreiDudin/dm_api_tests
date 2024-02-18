import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_login():
    """
     тест создает, активирует пользователя и логинится
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json_create = {
        "login": "adudin33",
        "email": "adudin33@mail.ru",
        "password": "adudin33"
    }

    json_account_login = {
        "login": "adudin33",
        "password": "adudin33",
        "rememberMe": True
    }

    assert api.account.post_v1_account(json=json_create).status_code == 201
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    assert api.account.put_v1_account_token(token=token).status_code == 200
    assert api.login.post_account_login(json=json_account_login).status_code == 200
