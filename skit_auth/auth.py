from urllib.parse import urljoin

import requests
from loguru import logger

from skit_auth import constants as const
from skit_auth import utils


def check_network_error(response: requests.Response) -> None:
    """
    Raise a network error if the response is not successful.

    :param response: The response from the API Gateway.
    :type response: requests.Response
    :return: None
    :rtype: None
    """
    if response.status_code != const.HTTP_SUCCESS:
        raise ValueError(
            f"{response.status_code}: Unable to get "
            f"token from API Gateway, error: {response.text}."
        )


def get_default_token(url: str, email: str, password: str) -> str:
    """
    Get a token from the API Gateway.

    :param url: The URL of the API Gateway.
    :type url: str
    :param email: The email address of the user or IAM.
    :type email: str
    :param password: The password of the user or IAM.
    :type password: str
    :return: JSON Web Token
    :rtype: str
    """
    payload = {const.EMAIL: email, const.PASSWORD: password}
    response = requests.post(urljoin(url, const.ROUTE_OAUTH), json=payload)
    check_network_error(response)
    token = response.json().get(const.ACCESS_TOKEN)
    utils.set_session(token)
    return token


def get_org_token(url: str, email: str, password: str, org_id: int) -> str:
    """
    Get a token from the API Gateway for an organization with id = `org_id`.

    :param url: The URL of the API Gateway.
    :type url: str
    :param org_id: The ID of the organization.
    :type org_id: int
    :param token: The token provided for skit's organization.
    :type token: str
    :return: JSON Web Token
    :rtype: str
    """

    payload = {const.ORG_ID: org_id}
    token = get_default_token(url, email, password)
    headers = {const.AUTHORIZATION: f"Bearer {token}"}
    response = requests.post(
        urljoin(url, const.ROUTE_CHANGE_ORG), json=payload, headers=headers
    )
    check_network_error(response)
    logger.debug(f"Acquired organization token for {org_id=}.")
    logger.debug(f"{response.json()}")
    token = response.json().get(const.ACCESS_TOKEN)
    utils.set_session(token)
    return token
