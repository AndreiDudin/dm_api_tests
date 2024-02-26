import time

import structlog

from dm_api_account.models.registration_model import Registration
from dm_api_account.models.change_email_model import ChangeEmail
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    """
    тест создает, активирует пользователя и меняет email
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json_create = Registration(
        login="adudin43",
        email="adudin43@mail.ru",
        password="adudin43"
    )

    json_change_email = ChangeEmail(
        login="adudin43",
        password="adudin43",
        email="adudin43_new@mail.ru"
    )
    api.account.post_v1_account(json=json_create)
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)
    api.account.put_v1_account_email(json=json_change_email)
