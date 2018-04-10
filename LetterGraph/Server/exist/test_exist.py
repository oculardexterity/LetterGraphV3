import unittest

from exist import ExistManager





fake_config = {
    
    'development': {
        'dev_test_field1': 'dev_test_value1',
        'dev_test_field2': 'dev_test_value2'
    },

    'global': {
        'global_test_field': 'global_test_value'
    }

}




class Test_Exist(unittest.TestCase):
    def setUp(self):
        Exist.setup(config=fake_config, mode='development')

        self.exist = Exist()

    def test_setup_imports_config(self):
        exist = Exist()
        assert exist.dev_test_field1 == 'dev_test_value1'
        assert exist.dev_test_field2 == 'dev_test_value2'
        assert exist.global_test_field == 'global_test_value'

