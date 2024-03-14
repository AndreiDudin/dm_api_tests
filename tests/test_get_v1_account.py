import structlog
from hamcrest import assert_that, has_properties, has_entries

from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade
from generic.helpers.orm_db import OrmDatabase


def test_get_v1_account(dm_api_facade, dm_db, prepare_user):
    login = prepare_user.login
    user_password = prepare_user.user_password
    email = prepare_user.email
    # Регистрация нового пользователя
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=user_password
    )
    dm_db.update_activated_status(
        login=login,
        activated_status=True
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Activated': True
            }
        ))

    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=user_password
    )

    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)
    response = dm_api_facade.account.get_current_user_info()
    assert_that(
        response.resource, has_properties(
            {
                "login": login,
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
