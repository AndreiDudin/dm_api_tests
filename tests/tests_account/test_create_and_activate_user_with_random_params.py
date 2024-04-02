import allure
import pytest
from hamcrest import assert_that, has_entries
from generic.assertions.response_checker import check_status_code_http
from utilities import random_string


@allure.suite("Параметрический тест на проверку метода POST{host}/v1/account")
@allure.title("Параметрический тест: cоздание и активация пользователей с рандомными параметрами")
class TestsPostV1AccountParametrize:
    @pytest.mark.parametrize(
        'login, email, password, status_code, check', [
            ('12', '12@12.ru', '123456', 201, ''),  # валидные значения
            ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),  # пароль менее или равен 5 символам
            ('1', '12@12.ru', '123456', 400, {"Login": ["Short"]}),  # логин менее 2 символов
            ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),  # Email не содержит доменную часть
            ('12', '12', '123456', 400, {"Email": ["Invalid"]})  # Email не содержит @
        ]
    )
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            status_code,
            check
    ):
        login = login
        password = password
        email = email
        dm_db.delete_user_by_login(login=login)
        with check_status_code_http(expected_status_code=status_code, expected_result=check):
            dm_api_facade.account.register_new_user(
                login=login,
                email=email,
                password=password
            )
        if status_code == 201:
            dm_api_facade.account.activate_registered_user(login=login)
            dm_api_facade.login.login_user(login=login, password=password)

