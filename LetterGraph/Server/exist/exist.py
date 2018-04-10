

class Exist:
    def __init__(self):
        pass

    def _autoconfig(self, config=None, mode='development'):
        self.exist_address = config[mode]["address"]
        self.exist_port = config[mode]["port"]
        self.exist_username = config[mode]["username"]
        self.exist_password = config[mode]["password"]


if __name__ == '__main__':
    import sys
    sys.path.append('../LetterGraphV3')
    from config import exist_config

    exist = Exist(config=exist_config)
