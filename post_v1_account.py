import requests


def post_v1_account():
    """
    Register new user
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account"

    payload = {
        "login": "adudin3  ",
        "email": "adudin3@mail.ru ",
        "password": "adudin33"
    }
    headers = {
        'X-Dm-Auth-Token': 'b046f978-b9f9-44a5-844c-90d6f69dedae',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        "POST",
        url, headers=headers,
        json=payload
    )
    return response
