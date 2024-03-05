import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host="http://5.63.153.31:5051")
    login = "adudin97"
    password = "adudin97"
    new_password = "adudin97_new"
    email = "adudin97@mail.ru"
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
    token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(headers=token)
    api.account.reset_user_password(
        login=login,
        email=email,
        status_code=200
    )
    response = api.account.change_user_password(
        login=login,
        old_password=password,
        new_password=new_password
    )
    assert_that(
        response.resource, has_properties(
            {
                "login": "adudin97",
                "roles": [
                    UserRole.guest,
                    UserRole.player
                ],
                "rating": Rating(
                    enabled=True,
                    quality=0,
                    quantity=0
                )
            }
        )
    )
