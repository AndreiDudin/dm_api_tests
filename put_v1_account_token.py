import requests


def put_v1_account_token():
    """
    Activate register user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/b046f978-b9f9-44a5-844c-90d6f69dedae"

    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }
    response = requests.request(
        "PUT",
        url,
        headers=headers
    )
    return response
