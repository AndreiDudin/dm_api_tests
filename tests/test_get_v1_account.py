import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade
from generic.helpers.orm_db import OrmDatabase

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    login = "adudin123"
    user_password = "adudin123"
    email = "adudin123@mail.ru"
    user = 'postgres'
    password = 'admin'
    host = '5.63.153.31'
    database = 'dm3.5'
    api = Facade(host='http://5.63.153.31:5051')
    orm = OrmDatabase(
        user=user,
        password=password,
        host=host,
        database=database
    )
    orm.delete_user_by_login(login=login)
    dataset = orm.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.account.register_new_user(
        login=login,
        email=email,
        password=user_password
    )

    orm.update_activated_status(
        login=login,
        activated_status=True
    )
    dataset = orm.get_user_by_login(login=login)
    for row in dataset:
        assert row.Activated is True, f'User {login} is not activated'

    token = api.login.get_auth_token(
        login=login,
        password=user_password
    )

    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    response = api.account.get_current_user_info()
    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [UserRole.guest, UserRole.player],
         "rating": Rating(
             enabled=True,
             quality=0,
             quantity=0)
         }
    ))
