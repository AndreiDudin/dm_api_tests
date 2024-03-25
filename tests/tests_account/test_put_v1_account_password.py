from hamcrest import assert_that, has_properties, has_entries
from apis.dm_api_account.models.user_envelope_model import UserRole, Rating



def test_put_v1_account_password(dm_api_facade, dm_db, prepare_user):
    login = prepare_user.login
    user_password = prepare_user.user_password
    new_user_password = prepare_user.new_user_password
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

    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=user_password
    )
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account.reset_user_password(
        login=login,
        email=email,
        status_code=200
    )
    response = dm_api_facade.account.change_user_password(
        login=login,
        old_password=user_password,
        new_password=new_user_password
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
