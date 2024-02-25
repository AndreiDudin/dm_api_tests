import time

import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.registration_model import Registration
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    """
    тест создает и активирует пользователя
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json_registration = Registration(
        login="adudin58",
        email="adudin58@mail.ru",
        password="adudin58"
    )

    api.account.post_v1_account(json=json_registration)
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)
    print(response.resource.rating.enabled) #можно ли таким способом получить значение поля enabled для дальнейшей проверки в строке 39?
    assert_that(response.resource, has_properties(
        {"login": "adudin58",
         "roles": [UserRole.guest, UserRole.player],
         "rating": Rating(enabled=True, quality=0, quantity=0)}
    ))
