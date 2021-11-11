import json
import logging
import socket
import sys
from typing import List
from urllib.request import Request, urlopen

from requests import get

from config import get_config

config = get_config()


def get_own_ip() -> str:
    """return own (external) IP(v4) as retrieved

    Returns:
        str: IP as string
    """
    ip = get(config.own_ip_api_url).text
    return ip


def test_ip() -> List[str]:
    """Test if own IP is same as IP in dns-entry for each domain specified

    Returns:
        List[str]: List of domains to update
    """
    own_ip = get_own_ip()
    to_update = []
    for domain in config.domains:
        temp_ip = socket.gethostbyname(domain)
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
    request_body = str(json.dumps({
        'domains': list_domains,
        'description': 'IONOS_dyndns update-script'
    })).encode('utf-8')
    try:
        request = Request(f'{config.ionos_api}/v1/dyndns', data=request_body)
        request.add_header('X-API-Key', config.x_api_key)
        response = urlopen(request)
        status = response.getcode()
        if status != 200:
            logging.error(
                f'API-call failed: {status}, {response.read().decode("utf-8")}'
                )
            return None
    except RuntimeError as error:
        logging.error(error)
        return None
    parsed = response.json()
    return parsed['update_url']


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
    update_list = test_ip()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'force':
            update_list = config.domains
    if len(update_list) > 0:
        update_url = get_update_url(update_list)
        if update_url is not None:
            logging.info(get(update_url).status_code)
