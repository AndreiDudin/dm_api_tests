import structlog
from dm_api_account.model.rating import Rating
from dm_api_account.model.user_role import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login(dm_api_facade, dm_db, prepare_user, assertions):
    """
     тест создает, активирует пользователя и логинится
    :return:
    """
    login = prepare_user.login
    user_password = prepare_user.user_password
    email = prepare_user.email
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=user_password
    )
    assertions.check_user_was_created(login=login)
    dm_db.update_activated_status(
        login=login,
        activated_status=True
    )
    assertions.check_user_was_activated(login=login)
    response = dm_api_facade.login.login_user(
        login=login,
        password=user_password
    )
    assert_that(
        response.resource, has_properties(
            {
                "login": login,
                "roles": [UserRole("Guest"), UserRole("Player")],
                "rating": Rating(enabled=True, quality=0, quantity=0)
            }
        )
    )
