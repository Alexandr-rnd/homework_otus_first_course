import requests


def test_base_url(base_url, expected_statuscode):
    response = requests.get(base_url)
    assert response.status_code == expected_statuscode
