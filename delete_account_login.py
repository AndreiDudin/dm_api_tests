import requests


def delete_account_login():
    """
    Logout as current user
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account/login"

    headers = {
        'X-Dm-Auth-Token': 'b046f978-b9f9-44a5-844c-90d6f69dedae',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        "DELETE",
        url,
        headers=headers)
    return response
