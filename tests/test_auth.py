from urllib.parse import urljoin

import pytest
import requests

from skit_auth import constants as const
from skit_auth.auth import check_network_error, get_default_token, get_org_token


def test_get_default_token(requests_mock):
    fake_token = "fake_access_token"
    requests_mock.post(
        urljoin(const.DEFAULT_API_GATEWAY_URL, const.ROUTE_OAUTH),
        json={const.ACCESS_TOKEN: fake_token},
        status_code=const.HTTP_SUCCESS,
    )
    assert fake_token == get_default_token(
        const.DEFAULT_API_GATEWAY_URL, "fake_email", "fake_password"
    )


def test_get_org_token(requests_mock):
    fake_token = "fake_access_token"
    fake_headers = {const.AUTHORIZATION: f"Bearer {fake_token}"}
    requests_mock.post(
        urljoin(const.DEFAULT_API_GATEWAY_URL, const.ROUTE_OAUTH),
        json={const.ACCESS_TOKEN: fake_token},
        status_code=const.HTTP_SUCCESS,
    )
    requests_mock.post(
        urljoin(const.DEFAULT_API_GATEWAY_URL, const.ROUTE_CHANGE_ORG),
        json={const.ACCESS_TOKEN: fake_token},
        status_code=const.HTTP_SUCCESS,
        headers=fake_headers,
    )
    assert fake_token == get_org_token(
        const.DEFAULT_API_GATEWAY_URL, "fake_email", "fake_password", 9999
    )


def test_check_network_error(requests_mock):
    correct_url = "https://correct-url"
    wrong_url = "https://wrong-url"
    failure_status_code = 401
    fake_payload = {const.EMAIL: "fake_email", const.PASSWORD: "fake_password"}

    requests_mock.post(
        correct_url, status_code=const.HTTP_SUCCESS, text="this will show passed"
    )
    requests_mock.post(
        wrong_url, status_code=failure_status_code, text="this will show failed"
    )

    resp_pass = requests.post(correct_url, json=fake_payload)
    resp_fail = requests.post(wrong_url, json=fake_payload)

    assert check_network_error(resp_pass) is None
    with pytest.raises(ValueError):
        check_network_error(resp_fail)
