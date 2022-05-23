import unittest
from unittest import mock
import main

ALL_GOOD_DATA = """100,NEM13,200401101030,MDA1\n
250,NEM13,200401101030,MDA1\n
900,NEM13,200401101030,MDA1
"""

MISSING_100_DATA = """101,NEM13,200401101030,MDA1\n
250,NEM13,200401101030,MDA1\n
900,NEM13,200401101030,MDA1
"""

MISSING_900_DATA = """100,NEM13,200401101030,MDA1\n
250,NEM13,200401101030,MDA1\n
901,NEM13,200401101030,MDA1
"""

class TestFileMethods(unittest.TestCase):
    
    @mock.patch('main.open', new_callable=mock.mock_open, read_data=ALL_GOOD_DATA)
    def test_01_all_ok(self, mock_open):
        res = main.some_func('test.csv')
        self.assertTrue(res['status'])
        self.assertEqual(res['message'], 'all ok')
    
    @mock.patch('main.open', new_callable=mock.mock_open, read_data=MISSING_100_DATA)
    def test_02_first_line_missing(self, mock_open):
        res = main.some_func('test.csv')
        self.assertFalse(res['status'])
        self.assertEqual(res['message'], 'first line error')
    
    @mock.patch('main.open', new_callable=mock.mock_open, read_data=MISSING_900_DATA)
    def test_03_last_line_missing(self, mock_open):
        res = main.some_func('test.csv')
        self.assertFalse(res['status'])
        self.assertEqual(res['message'], 'last line error')