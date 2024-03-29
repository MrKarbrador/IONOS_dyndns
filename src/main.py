import logging
import socket
import sys
from typing import List, Union

from requests import get

from dns_api_client.api.dynamic_dns import activate_dyn_dns
from dns_api_client.models import DynamicDns, DynDnsRequest
from dns_api_client.types import UNSET, Response
from config import get_config
from dns_api_client.client import AuthenticatedClient
from dns_api_client.models.error import Error

config = get_config()

client = AuthenticatedClient(base_url=config.ionos_api, token=config.x_api_key)


def get_own_ip() -> str:
    """return own (external) IP(v4) as retrieved

    Returns:
        str: IP as string
    """
    ip = get(config.own_ip_api_url).text
    return ip


def get_own_ipv6() -> str:
    """return own (external) IP(v4) as retrieved

    Returns:
        str: IP as string
    """
    ip = get(config.own_ipv6_api_url).text
    return ip


def test_ip() -> List[str]:
    """Test if own IP is same as IP in dns-entry for each domain specified

    Returns:
        List[str]: List of domains to update
    """
    own_ip = get_own_ip()
    to_update = []
    for domain in config.domains:
        try:
            temp_ip = socket.gethostbyname(domain)
        except socket.gaierror:
            temp_ip = 'error'
        if own_ip != temp_ip:
            to_update.append(domain)
    logging.info(f"To update: {str(to_update)}")
    return to_update


def test_ipv6() -> List[str]:
    """Test if own IPv6 is same as IPv6 in dns-entry for each domain specified

    Returns:
        List[str]: List of domains to update
    """
    own_ip = get_own_ipv6()
    if not ':' in own_ip:
        logging.error(f'invalid ipv6: {own_ip}')
        return []
    to_update = []
    for domain in config.domains:
        try:
            temp_ip = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
        except socket.gaierror:
            temp_ip = 'error'
        if own_ip != temp_ip:
            to_update.append(domain)
    logging.info(f"To update: {str(to_update)}")
    return to_update


def get_update_url(list_domains: List[str]) -> str:
    """get the update-url for the urls from the API

    Args:
        list_domains (List[str]): list of domains which need to be updated

    Returns:
        str: url to update the dns-entry with or None if the API-call failed
    """
    request_body: DynDnsRequest = DynDnsRequest(
        domains=list_domains,
        description='IONOS_dyndns update-script'
    )
    try:
        response: Response[Union[DynamicDns, List[Error]]] =\
            activate_dyn_dns.sync_detailed(
                client=client,
                json_body=request_body
            )
    except RuntimeError as error:
        logging.error(error)
        return None
    except AttributeError as error:
        logging.error(error)
        return None
    if response.status_code != 200 or\
            type(response.parsed) is not DynamicDns or\
            type(response.parsed.update_url) is UNSET:
        logging.error(
            f'API-call failed: {response.status_code}, {response.parsed}'
        )
        return None
    parsed: DynamicDns = response.parsed
    return parsed.update_url


if __name__ == '__main__':
    logging_file_handler = logging.FileHandler("dyndns_log", 'a')
    logging_stdout_handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging_stdout_handler,
            logging_stdout_handler
        ]
    )
    update_list = list(set(test_ip() + test_ipv6()))
    if len(sys.argv) > 1:
        if sys.argv[1] == 'force':
            update_list = config.domains
    if len(update_list) > 0:
        update_url = get_update_url(update_list)
        if update_url is not None:
            update_url = f'{update_url}&ipv4={get_own_ip()}&ipv6={get_own_ipv6()}'
            logging.info(get(update_url).status_code)
