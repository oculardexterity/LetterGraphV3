import os



async def async_test_call(thing):
    print(f'Tried to send async req to {thing}')
    #fetch('http://motherfuckingwebsite.com/')

def sync_test_call(thing):
    print(f'Tried to send sync req to {thing}')



class Exist:
    def __init__(self):
        pass

    @classmethod
    def setup(cls, config=None, mode='development', asynchronous=True):
        for key, value in {**config[mode], **config['global']}.items():
            setattr(cls, key, value)
        cls._build_xquery_methods(asynchronous)

    @classmethod
    def _xqueries(cls):
        return os.listdir(cls.xqueries_path)

    @classmethod
    def _build_xquery_methods(cls, asynchronous):
        for xquery in cls._xqueries():
            xq_name = xquery.replace('.xql', '')

            if asynchronous:
                async def fn(*args, **kwargs):
                    await async_test_call(xq_name)
            else:
                def fn(*args, **kwargs):
                    return sync_test_call(xq_name)
            setattr(cls, xq_name, fn)




if __name__ == '__main__':
    import sys
    sys.path.append('../LetterGraphV3')
    from config import EXIST_CONFIG, MODE

    Exist.setup(config=EXIST_CONFIG, mode=MODE)

    exist = Exist()

    exist.test()

