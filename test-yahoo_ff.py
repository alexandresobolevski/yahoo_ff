import unittest
import pandas as pd
from yahoo_ff.yahoo_ff import yahoo_ff

aapl = yahoo_ff('aapl')

class Test(unittest.TestCase):

    def setUp(self):
        self.test = aapl

    def test_aapl(self):
        self.assertEqual(self.test.flag, 0)

    def test_ticker(self):
        self.assertEqual(self.test.ticker, 'aapl')

    def test_price(self):
        self.assertGreater(self.test.price.iloc[0][0], 0)

    def test_stats(self):
        self.assertEqual(len(self.test.stats.iloc[0]), 37)

    def test_sec_quarter(self):
        self.assertEqual(len(self.test.sec_quarter.iloc[0]), 70)

    def test_sec_annual(self):
        self.assertEqual(len(self.test.sec_annual.iloc[0]), 70)

if __name__ == '__main__':
    unittest.main()
