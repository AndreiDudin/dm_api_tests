import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_token():
    """
    тест создает и активирует пользователя
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "adudin12",
        "email": "adudin12@mail.ru",
        "password": "adudin12"
    }

    assert api.account.post_v1_account(json=json).status_code == 201
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    assert api.account.put_v1_account_token(token=token).status_code == 200



