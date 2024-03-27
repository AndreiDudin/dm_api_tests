from hamcrest import assert_that, has_properties
from data.post_v1_account import PostV1AccountData as user_data
from dm_api_account.models.user_envelope_model import UserRole, Rating


def test_get_v1_account(dm_api_facade, dm_db, prepare_user, assertions):
    login = user_data.login
    user_password = user_data.password
    email = user_data.email
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
    assertions.check_user_was_activated(login=login)
    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=user_password
    )
    #
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
