import allure
import pytest
from hamcrest import assert_that, has_properties, has_entries
from dm_api_account.models.user_envelope_model import UserRole, Rating
from collections import namedtuple

from generic import assertions


@allure.suite("Тесты на проверку метода POST{host}/v1/account/password")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    @allure.title("Проверка регистрации и активации пользователя")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertions):
        """
        тест проверяет создание и активацию пользователя в базе данных
        :param dm_api_facade:
        :param dm_db:
        :param prepare_user:
        :param assertions:
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
