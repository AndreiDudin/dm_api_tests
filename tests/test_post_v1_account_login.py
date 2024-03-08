import time
from hamcrest import assert_that, has_properties
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = Facade(host="http://5.63.153.31:5051")
    api.login.login_user(
        login='adudin74',
        password='adudin74'
    )


def test_put_v1_account_login():
    """
     тест создает, активирует пользователя и логинится
    :return:
    """
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = Facade(host="http://5.63.153.31:5051")
    json_registration = Registration(
        login="adudin95",
        email="adudin95@mail.ru",
        password="adudin95"
    )

    json_account_login = LoginCredentials(
        login="adudin95",
        password="adudin95",
        rememberMe=True)

    api.account_api.post_v1_account(json=json_registration)
    time.sleep(5)
    token = mailhog.get_token_from_last_email()
    api.account_api.put_v1_account_token(token=token)
    response = api.login_api.post_account_login(
        json=json_account_login,
        status_code=200
    )
    assert_that(response.resource, has_properties(
        {"login": "adudin95",
         "roles": [UserRole.guest, UserRole.player],
         "rating": Rating(
             enabled=True,
             quality=0,
             quantity=0)
         }
    ))
