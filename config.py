"""

Dicts holding config info.


"""

from config_SECRET import EXIST_SECRET



MODE = 'development'

EXIST_CONFIG = {

    'global': {
        'app_name': 'testapp'
    },
    'development': {
        'address': '127.0.0.1',
        'port': '8080',


        # And import in and unpack the secret info.
        **EXIST_SECRET['development']
    }
}


if __name__ == '__main__':
    print(exist_config)
