import unittest
from methods import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w',
                         self.convert.generateToken('admin', 'secret', None, True))

    def test_access_data(self):
        self.assertEqual(True, self.validate.access_Data(
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', True))


if __name__ == '__main__':
    unittest.main()
