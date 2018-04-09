"""

Dicts holding config info.


"""

from config_SECRET import exist_secret


exist_config = {
    'development': {
        'address': '127.0.0.1',
        'port': '8080',
        **exist_secret['development']
    }
}


print(exist_config)