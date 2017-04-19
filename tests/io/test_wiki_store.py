import unittest
import os
import tempfile

import datetime

from topyc.io.wiki_store import WikiStore


class TestWikiStore(unittest.TestCase):
    """
    A class to test the data available in Quandl WIKI dataset (see main class for details)
    """
    def test_wiki_store(self):
        """The test for the MVO class."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        input_csv = os.path.join(test_dir, '../resources/WIKI_test.csv')
        test_dir = tempfile.mkdtemp()

        WikiStore.store_snapshot(test_dir, input_csv)

        w_store = WikiStore(test_dir)

        self.assertEqual(len(w_store.keys()), 2, "# Wrong dimension !")
        df = w_store['A']
        self.assertEqual(df.index.min(), datetime.datetime(1999, 11, 18), "# Wrong start date !")

        ac = w_store.tickers_column(w_store.keys())
        self.assertListEqual(ac.columns.tolist(), ['A', 'ZUMZ'], "# Problem with tickers !")

        ac_filter = w_store.tickers_column(w_store.keys(), fun_filter=lambda x: x[x.index.year == 2000])
        self.assertListEqual(ac_filter.columns.tolist(), ['A', 'ZUMZ'])
        self.assertEqual(ac_filter.index.year.max(), 2000)
        self.assertEqual(ac_filter.index.year.min(), 2000)

        # to increase coverage, test degenerate cases
        ac = w_store.tickers_column([])
        self.assertEqual(ac, None)
        ac = w_store.tickers_column(w_store.keys()[0])
        self.assertAlmostEqual(ac['A']['1999-11-18'], 41.9362590963, delta=1e-5)

        w_store.close()
