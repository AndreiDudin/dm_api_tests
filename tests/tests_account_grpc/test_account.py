import pprint

import grpc
import pytest
import pytest_asyncio.plugin
from google.protobuf.json_format import MessageToDict

from apis.dm_api_account_grpc.account_pb2 import RegisterAccountRequest
from apis.dm_api_account_grpc.account_pb2_grpc import AccountServiceStub


def test_account(grpc_account):
    # channel = grpc.insecure_channel(target='5.63.153.31:5055')
    # client = AccountServiceStub(channel=channel)
    response = grpc_account.register_account(
        login="adudin1035",
        password="adudin1035",
        email="adudin1035@mail.ru"
    )
    pprint.pprint(MessageToDict(response))


@pytest.mark.asyncio
async def test_account_async(grpc_account_async):
    response = await grpc_account_async.register_account(
        register_account_request=RegisterAccountRequest(
            login="adudin1036",
            password="adudin1036",
            email="adudin1036@mail.ru"
        )
    )
    print(response)
