from hamcrest import assert_that, has_properties, has_entries

from dm_api_account.models.user_envelope_model import UserRole, Rating


def test_put_v1_account_token(dm_api_facade, dm_db, prepare_user):
    """
    тест создает и активирует пользователя
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
    response = dm_api_facade.account.activate_registered_user(login=login)
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': True
            }
        ))

    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [
             UserRole.guest,
             UserRole.player
         ],
         "rating": Rating(
             enabled=True,
             quality=0,
             quantity=0)
         }
    ))
