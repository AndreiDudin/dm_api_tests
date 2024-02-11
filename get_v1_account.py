import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

    headers = {
        'X-Dm-Auth-Token': '9f625804-336a-40c6-80dc-dbd326cb76aa',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        "GET",
        url,
        headers=headers
    )
    return response
