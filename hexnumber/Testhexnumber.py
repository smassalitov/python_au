import unittest
from hexnumber.hex_number import *


class TestGenerator(unittest.TestCase):
    def test_check_nulls(self):
        expect1 = 'ABC'
        expect2 = '0'
        result1 = check_nulls('0ABC')
        result2 = check_nulls('')
        self.assertEqual(expect1, result1)
        self.assertEqual(expect2, result2)

    def test_check_number(self):
        expect1 = '-a'
        expect2 = '-A'
        expect3 = 'f'
        expect4 = 'A'
        self.assertFalse(check_number(expect1))
        self.assertFalse(check_number(expect2))
        self.assertFalse(check_number(expect3))
        self.assertTrue(check_number(expect4))


if __name__ == '__main__':
    unittest.main()