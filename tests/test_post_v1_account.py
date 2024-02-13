from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "adudin9",
        "email": "adudin9@mail.ru",
        "password": "adudin99"}

    create_account = api.account.post_v1_account(json=json)
    assert create_account.status_code == 201
    activate_account = api.account.put_v1_account_token()
    assert activate_account.status_code == 200
