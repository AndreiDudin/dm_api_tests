from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    activate_account = api.account.put_v1_account_token()
    assert activate_account.status_code == 200



