

class Exist:
    def __init__(self):
        pass

    @classmethod
    def setup(cls, config=None, mode='development'):
        for key, value in {**config[mode], **config['global']}.items():
            setattr(cls, key, value)





if __name__ == '__main__':
    import sys
    sys.path.append('../LetterGraphV3')
    from config import EXIST_CONFIG, MODE

    Exist.setup(config=EXIST_CONFIG, mode=MODE)

    exist = Exist()


    print(exist.exist_app_name)

