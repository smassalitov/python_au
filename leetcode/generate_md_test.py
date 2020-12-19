import unittest
from leetcode.generate_md import *


class TestGenerator(unittest.TestCase):
    def test_GetName(self):
        with open("test_in.txt", 'r') as fin:
            all_lines = fin.read().splitlines()
        self.assertEqual(' Reverse String', str(GetName(all_lines)[0]))

    def test_GetUrl(self):
        with open("test_in.txt", 'r') as fin:
            all_lines = fin.read().splitlines()
        self.assertEqual('https://leetcode.com/problems/reverse-string/', str(GetUrl(all_lines)))


if __name__ == '__main__':
    unittest.main()
