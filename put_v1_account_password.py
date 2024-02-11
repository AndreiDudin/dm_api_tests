import requests


def put_v1_account_password():
    """
    Change registered use password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"
    payload = {
        "login": "aduidn3  ",
        "token": "b046f978-b9f9-44a5-844c-90d6f69dedae",
        "oldPassword": "<string>",
        "newPassword": "<string>"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }
    response = requests.request(
        "PUT",
        url,
        headers=headers,
        json=payload
    )
    return response
