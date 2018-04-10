from contextlib import contextmanager
import inspect
import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))


from exist import Exist



test_config = {
    'development': {
        'dev_test_field1': 'dev_test_value1',
        'dev_test_field2': 'dev_test_value2'
    },

    'global': {
        'global_test_field': 'global_test_value',
        'xqueries_path': os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'test_xquery_dir')
    },
}

TEST_PATH = test_config['global']['xqueries_path']

@contextmanager
def build_test_xquery_dir(file_name):
    os.mkdir(TEST_PATH)
    f = open(os.path.join(TEST_PATH, file_name), 'w')
    f.close()
    yield
    os.remove(os.path.join(TEST_PATH, file_name))
    os.rmdir(TEST_PATH)





class Test_Exist(unittest.TestCase):
    def setUp(self):
        try:
            os.remove(os.path.join(TEST_PATH, 'test.xql'))
            os.rmdir(TEST_PATH)
        except FileNotFoundError:
            pass


        os.mkdir(TEST_PATH)
        f = open(os.path.join(TEST_PATH, 'test.xql'), 'w')
        f.close()
        Exist.setup(config=test_config, mode='development', asynchronous=False)
        self.exist = Exist()

    def tearDown(self):
        os.remove(os.path.join(TEST_PATH, 'test.xql'))
        os.rmdir(TEST_PATH)


    def test_setup_imports_config(self):
        exist = Exist()
        assert exist.dev_test_field1 == test_config['development']['dev_test_field1']
        assert exist.dev_test_field2 == test_config['development']['dev_test_field2']
        assert exist.global_test_field == test_config['global']['global_test_field']

    def test_xquery_path(self):
        assert self.exist._xqueries() == ['test.xql']

    def test_xqueries_are_methods(self):
        assert inspect.ismethod(self.exist.test)


