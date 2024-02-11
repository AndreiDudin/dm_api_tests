import requests


def post_account_login():
    """
    Authentificate via credentials
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {
        "login": "adudin3",
        "password": "adudin33",
        "rememberMe": "true"
    }
    headers = {
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        json=payload
    )
    return response
