import time

import structlog

from dm_api_account.models.registration_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    """
    тест создает и активирует пользователя
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = RegistrationModel(
        login="adudin38",
        email="adudin38@mail.ru",
        password="adudin38"
    )

    assert api.account.post_v1_account(json=json).status_code == 201
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    assert api.account.put_v1_account_token(token=token).status_code == 200
