"""

Dicts holding config info.


"""

from config_SECRET import exist_secret


exist_config = {
    'development': {
        'address': '127.0.0.1',
        'port': '8080',


        # And import in and unpack the secret info.
        **exist_secret['development']
    }
}


if __name__ == '__main__':
    print(exist_config)
