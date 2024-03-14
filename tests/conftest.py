from collections import namedtuple

import pytest
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.mailhog import MailhogApi

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
    return MailhogApi(host="http://5.63.153.31:5025")


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture()
def dm_db():
    user = 'postgres'
    password = 'admin'
    host = '5.63.153.31'
    database = 'dm3.5'

    orm = OrmDatabase(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return orm


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
