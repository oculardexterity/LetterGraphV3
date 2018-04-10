import os

def test_call(thing):
    print(f'Tried to send req to {thing}')
    return f'Called {thing}'


class Exist:
    def __init__(self):
        pass

    @classmethod
    def setup(cls, config=None, mode='development'):
        for key, value in {**config[mode], **config['global']}.items():
            setattr(cls, key, value)
        cls._build_xquery_methods()

    @classmethod
    def _xqueries(cls):
        return os.listdir(cls.xqueries_path)

    @classmethod
    def _build_xquery_methods(cls):
        for xquery in cls._xqueries():
            xq_name = xquery.replace('.xql', '')
            def fn(*args, **kwargs):
                return test_call(xq_name)
            setattr(cls, xq_name, fn)




if __name__ == '__main__':
    import sys
    sys.path.append('../LetterGraphV3')
    from config import EXIST_CONFIG, MODE

    Exist.setup(config=EXIST_CONFIG, mode=MODE)

    exist = Exist()

    print(exist.test())

