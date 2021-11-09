class Config:
    domains = [
    'example.com'
    ]
    own_ip_api_url = 'http://api.ipify.org/'
    x_api_key= 'key'
    ionos_api = 'https://api.hosting.ionos.com/dns'

def get_config() -> Config:
    return Config()
