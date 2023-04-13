from faker import Faker

from faker_marketdata import MarketDataProvider

import unittest


class MarketDataTests(unittest.TestCase):

    def setUp(self):
        self.md = Faker()
        self.md.add_provider(MarketDataProvider)

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


class FakerIntegrationTests(unittest.TestCase):
    """
    Tests integration with Faker
    """
    def test_faker_provider(self):
        fake = Faker()
        fake.add_provider(MarketDataProvider)
        self.assertTrue(fake.sedol())

    def test_seed_fixes_random(self):
        faker1 = Faker()
        faker2 = Faker()
        faker1.add_provider(MarketDataProvider)
        faker2.add_provider(MarketDataProvider)

        Faker.seed(123)
        sedol1 = faker1.sedol()
        Faker.seed(123)
        sedol2 = faker2.sedol()
        self.assertEqual(sedol1, sedol2)

    def test_existing_fake_methods_still_work(self):
        fake = Faker()
        fake.add_provider(MarketDataProvider)
        sedol = fake.sedol()
        self.assertTrue(sedol)
        random_str = fake.lexify("???????")
        self.assertTrue(random_str)


if __name__ == '__main__':
    unittest.main()
