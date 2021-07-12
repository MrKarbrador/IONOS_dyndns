import socket
from requests import get
import logging
import os

domains = [
    'example.com'
]
update_url = 'update_url',

def get_own_ip() -> str:
    ip = get('http://api.ipify.org/').text
    return ip

def test_ip() -> bool:
    own_ip = get_own_ip()
    to_update = []
    for domain in domains:
        temp_ip = socket.gethostbyname(domain)
        logging.info(f'testing own ip: {own_ip} against gotten ip: {temp_ip}')
        if own_ip != temp_ip:
            to_update.append(domain)
    logging.info(f"To update: {str(to_update)}")
    return len(to_update) > 0

def update_ips():
    os.system(f'curl -X GET {update_url}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    update_list = test_ip()
    if update_list:
        update_ips()
