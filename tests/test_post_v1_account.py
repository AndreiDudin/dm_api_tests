import time

import structlog
from services.dm_api_account import Facade

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
    api = Facade(host="http://5.63.153.31:5051")
    login = "adudin74"
    email = "adudin74@mail.ru"
    password = "adudin74"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
