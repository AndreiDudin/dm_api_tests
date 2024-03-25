from hamcrest import assert_that, has_entries, has_properties
from apis.dm_api_account.models.user_envelope_model import UserRole, Rating


def test_put_v1_account_email(dm_api_facade, dm_db, prepare_user):
    """
    тест создает, активирует пользователя и меняет email
    :return:
    """
    login = prepare_user.login
    user_password = prepare_user.user_password
    email = prepare_user.email
    new_email = prepare_user.new_email

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
    response = dm_api_facade.account.change_registered_user_email(
        login=login,
        password=user_password,
        email=new_email
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Email': new_email
            }
        ))

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
