from faker_marketdata import MarketDataProvider

import unittest


class MarketDataTests(unittest.TestCase):

    def setUp(self):
        self.md = MarketDataProvider()

    def test_figi(self):
        figis = [self.md.figi() for _ in range(10000)]
        self.assertTrue(all(figi for figi in figis))

    def test_isin(self):
        isins = [self.md.isin() for _ in range(10000)]
        self.assertTrue(all(isin for isin in isins))

    def test_lei(self):
        leis = [self.md.lei() for _ in range(10000)]
        self.assertTrue(all(lei for lei in leis))

    def test_market_type(self):
        mt = [self.md.marketType() for _ in range(10000)]
        self.assertTrue(all(marketType for marketType in mt))

    def test_mic(self):
        mics = [self.md.mic() for _ in range(10000)]
        self.assertTrue(all(mic for mic in mics))

    def test_nsin(self):
        nsins = [self.md.nsin() for _ in range(10000)]
        self.assertTrue(all(nsin for nsin in nsins))

    def test_ric(self):
        rics = [self.md.ric() for _ in range(10000)]
        self.assertTrue(all(ric for ric in rics))

    def test_cusip (self):
        cusips = [self.md.cusip() for _ in range(10000)]
        self.assertTrue(all(cusip for cusip in cusips))

    def test_sedol(self):
        sedols = [self.md.sedol() for _ in range(10000)]
        self.assertTrue(all(sedol for sedol in sedols))

    def test_tickers(self):
        tickers = [self.md.ticker() for _ in range(10000)]
        self.assertTrue(all(ticker for ticker in tickers))

    """
    Tests integration with Faker
    """
    def test_faker_provider(self):
        from faker import Faker
        fake = Faker()
        fake.add_provider(MarketDataProvider())
        self.assertTrue(fake.sedol())

    def test_seed_fixes_random (self):
        from faker import Faker
        faker1 = Faker()
        faker2 = Faker()
        faker1.add_provider(MarketDataProvider(seed=23))
        faker2.add_provider(MarketDataProvider(seed=23))
        self.assertEqual(faker1.sedol(), faker2.sedol())


if __name__ == '__main__':
    unittest.main()
