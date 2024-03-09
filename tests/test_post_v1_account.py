import time
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_post_v1_account():
    """
    тест создает нового пользователя,
    активирует его, используя базу данных,
    и потом пробует залогиниться
    :return:
    """
    api = Facade(host="http://5.63.153.31:5051")
    login = "adudin117"
    email = "adudin117@mail.ru"
    password = "adudin117"
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(
        login=login
    )
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} is activated'

    #api.account.activate_registered_user(login=login)
    db.update_user_activated_status(
        login=login,
        activation_status='True'
    )
    time.sleep(10)
    dataset = db.get_user_by_login(
        login=login
    )
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    dataset = db.get_user_by_login(
        login=login
    )
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    response = api.login.login_user(
        login=login,
        password=password
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

