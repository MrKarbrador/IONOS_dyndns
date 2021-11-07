import socket
from requests import get, post
import logging
import os
import sys

domains = [
    'example.com'
]
API_URL = 'https://api.hosting.ionos.com/dns/v1/dyndns'
OWN_IP_URL = 'http://api.ipify.org/'
X_API_KEY= 'key'

def get_own_ip() -> str:
    ip = get(OWN_IP_URL).text
    return ip

def test_ip() -> bool:
    own_ip = get_own_ip()
    to_update = []
    for domain in domains:
        temp_ip = socket.gethostbyname(domain)
        if own_ip != temp_ip:
            to_update.append(domain)
    logging.info(f"To update: {str(to_update)}")
    return to_update

def update_ips(list_domains):
    header={'x-api-key': X_API_KEY}
    post_param = {
        'domains': list_domains,
        'description': 'DynamicDNS Script'
    }
    request = post(API_URL, )
    os.system(f'curl -X GET {API_URL}')
    logging.info('update successfull')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    update_list = test_ip()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            update_list = domains
    if len(update_list) > 0:
        update_ips(update_list)
