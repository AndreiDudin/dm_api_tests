import pytest
from hamcrest import assert_that, has_properties, has_entries
from dm_api_account.models.user_envelope_model import UserRole, Rating
from collections import namedtuple


def test_post_v1_account(dm_api_facade, dm_db, prepare_user):
    """
    тест создает нового пользователя,
    активирует его, используя базу данных,
    и потом пробует залогиниться
    :return:
    """
    login = prepare_user.login
    user_password = prepare_user.user_password
    email = prepare_user.email
    # Регистрация нового пользователя
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=user_password
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))

    # Активация нового пользователя
    dm_db.update_activated_status(
        login=login,
        activated_status=True
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': True
            }
        ))

    response = dm_api_facade.login.login_user(
        login=login,
        password=user_password
    )
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
