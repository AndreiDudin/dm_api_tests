import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_email():
    """
    тест создает, активирует пользователя и меняет email
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json_create = {
        "login": "adudin23",
        "email": "adudin23@mail.ru",
        "password": "adudin23"
    }

    json_change_email = {
        "login": "adudin23",
        "password": "adudin23",
        "email": "adudin23_new@mail.ru"
    }

    assert api.account.post_v1_account(json=json_create).status_code == 201
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    assert api.account.put_v1_account_token(token=token).status_code == 200
    assert api.account.put_v1_account_email(json=json_change_email).status_code == 200
