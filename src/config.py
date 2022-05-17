class Config:
    domains = [
        'example.com',
        'www.example.com'
    ]
    own_ip_api_url = 'https://api.ipify.org/'
    x_api_key = 'key'
    ionos_api = 'https://api.hosting.ionos.com/dns'

def get_config() -> Config:
    return Config()
