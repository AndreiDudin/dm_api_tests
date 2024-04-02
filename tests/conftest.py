import allure
import pytest
import structlog
from vyper import v
from pathlib import Path

from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Facade
from collections import namedtuple

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)


@pytest.fixture
def mailhog():
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
)

connect = None

@pytest.fixture
def dm_db():
    # user = 'postgres'
    # password = 'admin'
    # host = '5.63.153.31'
    # database = 'dm3.5'
    global connect
    if connect is None:
        connect = OrmDatabase(
            user=v.get('database.dm3_5.user'),
            password=v.get('database.dm3_5.password'),
            host=v.get('database.dm3_5.host'),
            database=v.get('database.dm3_5.database')
        )
    yield connect
    #connect.db.db.close()


@pytest.fixture
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)


@allure.step("Подготовка тестового пользователя")
@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    login = "adudin123"
    user_password = "adudin123"
    new_user_password = "adudin123_new"
    email = "adudin123@mail.ru"
    new_email = "adudin123_new@mail.ru"
    user = namedtuple(
        'User', 'login, email, user_password, new_user_password, new_email'
    )
    User = user(
        login=login,
        email=email,
        user_password=user_password,
        new_user_password=new_user_password,
        new_email=new_email
    )
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    return User


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parents[1].joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
