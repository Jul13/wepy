"""Yahoo unit test unit test."""
import unittest
from datetime import date

from topyc.io.yahoo import Yahoo


class TestYahoo(unittest.TestCase):
    """A unit test for yahoo data provider."""

    def setUp(self):
        self.yahoo = Yahoo()

    def tearDown(self):
        # this is a useless override here, 
        pass

    def test_batch_snapshot(self):
        df = self.yahoo.batch_snapshot(['F', 'AAPL'])
        symbols = df.ticker.tolist()
        self.assertTrue('F' in symbols)
        self.assertTrue('AAPL' in symbols)
        self.assertTrue('52w_high' in df.columns)

    def test_historic_dividends(self):
        dividends = self.yahoo.historic_dividends('F')
        self.assertTrue({'Date', 'Dividends'}.issubset(dividends.columns))

    def test_historic_close(self):
        test_tickers = ['F', 'GS']
        from_date = date(2013, 1, 3)
        to_date = date(2013, 3, 1)
        dat = self.yahoo.historic_close(test_tickers, from_date=from_date, to_date=to_date)
        self.assertListEqual(test_tickers, dat.columns.tolist())
        self.assertEqual(dat.index.min().date(), from_date)
        self.assertEqual(dat.index.max().date(), to_date)
