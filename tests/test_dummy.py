import unittest
import argparse

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    # def test_fun(self):
    #     weekday = calculate(2001, 1, 3)
    #     self.assertEqual(weekday, 2005)

    #     retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
    #     self.assertEqual(retcode, 0)

    def test_calculate_simple(self):
        weekday = calculate(1970, 1, 1)
        self.assertEqual(weekday, 3)     # Unix epoch is thursday
        
        weekday2 = calculate(2017, 5, 10)
        self.assertEqual(weekday, 2)

    def test_wrong_argument(self):
        weekday = calculate(1970, 13, 1)
        self.assertIsNone(weekday)

        weekday2 = calculate(1970, 1, 32)
        self.assertIsNone(weekday2)

        weekday3 = calculate(1970, -1, 1)
        self.assertIsNone(weekday3)

        weekday4 = calculate(1970, 1, -1)
        self.assertIsNone(weekday4)

        weekday5 = calculate(-3, 1, 1)
        self.assertIsNone(weekday5)


    def test_calculate_edge_cases(self):
        weekday = calculate(1, 1, 1)
        self.assertEqual(weekday, 5)     # Apparently it's a saturday

        weekday2 = calculate(2012, 2, 29)
        self.assertEqual(weekday2, 2)    # Leap year check

        weekday3 = calculate(2011, 2, 29)
        self.assertIsNone(weekday3)     # Non-leap year check

    def test_arg_parsing(self):
        self.assertRaises(
            argparse.ArgumentError,
            main(("--year", "201.5", "--month", "1", "--day", "2"))
        )
        self.assertRaises(
            argparse.ArgumentError,
            main(("--year", "asdf", "--month", "1", "--day", "2"))
        )
        self.assertRaises(
            argparse.ArgumentError,
            main(("--year", "2016", "--month", "{}", "--day", "3"))
        )


if __name__ == '__main__':
    unittest.main()
