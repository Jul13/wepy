# Author: Gheorghe Postelnicu
from datetime import date
import pandas as pd
from io import BytesIO
from urllib.request import urlopen


class Yahoo(object):
    # Taken from http://www.jarloo.com/yahoo_finance/
    yahoo_query_params = {
        'ticker': 's',
        'average_daily_volume': 'a2',
        'dividend_yield': 'y',
        'dividend_per_share': 'd',
        'earnings_per_share': 'e',
        'est_eps_yr': 'e7',
        'est_eps_next_yr': 'e8',
        'ex_dividend_date': 'q',
        'market_cap': 'j1',
        'price_earnings_ratio': 'r',
        'short_ratio': 's7',
        'volume': 'v',
        '52w_low': 'j',
        '52w_high': 'k'
    }

    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size
        self.market_cap_pattern = '(\d+[\.]\d+)([MB])'

    @staticmethod
    def _convert_market_cap(str_value):
        if type(str_value) != str:
            return -1.
        last_char = str_value[-1]
        if last_char in ['B', 'M']:
            base = float(str_value[:-1])
            multiplier = 10. ** 9 if last_char == 'B' else 10. ** 6
            return base * multiplier
        return float(str_value)

    def _fetch_fields(self, symbols, fields):
        def chunker(symbols_):
            i = 0
            while i < len(symbols_):
                count_chunk = min(self.chunk_size, len(symbols_) - i)
                yield symbols_[i:(i + count_chunk)]
                i += count_chunk

        dfs = []
        for chunk in chunker(symbols):
            request = 'http://download.finance.yahoo.com/d/quotes.csv?s={}&f={}'.format(','.join(chunk), fields)
            raw_dat = urlopen(request).read()
            df = pd.read_csv(BytesIO(raw_dat), header=None)
            dfs.append(df)
        ret = pd.concat(dfs)
        return ret

    def batch_snapshot(self, tickers):
        """
        Retrieves financial information for a batch of stock symbols.

        Args:
            tickers (list<str>): list of stock symbols
        Returns:
            pandas.Dataframe: dataframe with one row per symbol.
        """
        ret = self._fetch_fields(tickers, ''.join(Yahoo.yahoo_query_params.values()))
        ret.columns = Yahoo.yahoo_query_params.keys()
        for col in ['ex_dividend_date']:
            ret[col] = pd.to_datetime(ret[col])
        ret['market_cap'] = [self._convert_market_cap(mc) for mc in ret.market_cap]
        return ret

    @staticmethod
    def _history_call(ticker, from_date, to_date, params):
        base_url = 'http://ichart.finance.yahoo.com/table.csv'
        params.update({'s': ticker,
                       'a': from_date.month - 1,
                       'b': from_date.day,
                       'c': from_date.year,
                       'd': to_date.month - 1,
                       'e': to_date.day,
                       'f': to_date.year
                       })
        url = '{}?{}'.format(base_url, '&'.join('{}={}'.format(k, params[k]) for k in params))
        raw_dat = urlopen(url).read()
        df = pd.read_csv(BytesIO(raw_dat), parse_dates=[0])
        return df

    def historic_close(self, tickers, from_date=date(2010, 1, 1), to_date=date.today(), join_type='outer'):
        """
        Extracts the adjusted close for a set of tickers.

        Args:
            tickers (list(str)): stock symbol
            from_date (date): start date
            to_date (date): end date
            join_type (str): type of join
        Returns:
            Dataframe indexed by date with one column by stock ticker.
        """

        def fetch_adj_close(ticker, from_date_, to_date_):
            dat = self._single_historic_ohlc(ticker, from_date_, to_date_)
            dat['Date'] = pd.to_datetime(dat.Date, infer_datetime_format=True)
            dat.set_index('Date', inplace=True)
            dat.sort_index(inplace=True)
            ret = dat[['Adj Close']]
            ret.columns = [ticker]
            return ret

        dats = [fetch_adj_close(ticker, from_date_=from_date, to_date_=to_date) for ticker in tickers]
        return dats[0].join(dats[1:], how=join_type)

    def _single_historic_ohlc(self, ticker, from_date=date(2010, 1, 1), to_date=date.today()):
        return self._history_call(ticker, from_date, to_date, {'g': 'd'})

    def historic_dividends(self, ticker, from_date=date(2010, 1, 1), to_date=date.today()):
        """
        Extracts the dividend payout history for an individual stock.

        Args:
            ticker (str): stock symbol
            from_date (date): start date
            to_date (date): end date
        Returns:
            pandas.DataFrame: dataframe with dates and dividends.
        """
        return self._history_call(ticker, from_date, to_date, {'g': 'v'})
