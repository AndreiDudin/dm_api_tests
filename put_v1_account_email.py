import requests


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/email"

    payload = {
        "login": "adudin3 ",
        "password": "adudin33",
        "email": "adudin@mail.ru"
    }
    headers = {
        'X-Dm-Auth-Token': 'b046f978-b9f9-44a5-844c-90d6f69dedae',
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
