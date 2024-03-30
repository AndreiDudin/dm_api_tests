import allure
from hamcrest import assert_that, has_properties
from dm_api_account.model.rating import Rating
from dm_api_account.model.user_role import UserRole
from data.post_v1_account import PostV1AccountData as user_data


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
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
        login = user_data.login
        user_password = user_data.password
        email = user_data.email
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
            password=user_password,
            request_token=False
        )
#        print(f"response= {response}")
        assert_that(
            response.resource, has_properties(
                {
                    "login": login,
                    "roles": [
                        UserRole('Guest'),
                        UserRole('Player')
                    ],
                    "rating": Rating(
                        enabled=True,
                        quality=0,
                        quantity=0
                    )
                }
            )
        )
