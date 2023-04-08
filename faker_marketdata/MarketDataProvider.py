from faker.providers import BaseProvider
import pycountry

_alphanumeric_alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_cusip_alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*@#'

class MarketDataProvider(BaseProvider):

    # Validation extracted from https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/isin.py
    def isin(self):
        """
        Generates a random, valid ISIN
        :return: a random ISIN with valid country code and validation digit
        """
        rnd = self.generator.random
        country_codes = map(lambda x: x.alpha_2, list(pycountry.countries))
        code = rnd.choice(list(country_codes)).upper()
        rnd_str = "".join(rnd.choices(_alphanumeric_alph[11:], k=9))
        number = code.upper() + rnd_str.zfill(9)
        number = ''.join(str(_alphanumeric_alph.index(n)) for n in number)
        number = ''.join( str((2, 1)[i % 2] * int(n)) for i, n in enumerate(reversed(number)))
        number = str((10 - sum(int(n) for n in number)) % 10)
        return "{}{}{}".format(code, rnd_str, number)

    def sedol(self):
        """
        Generates a random, valid SEDOL
        :return: SEDOL as a string
        """
        rnd = self.generator.random
        str_part = "".join(rnd.choices(_alphanumeric_alph[11:], k=6))
        weights = (1, 3, 1, 7, 3, 9)
        s = sum(w * _alphanumeric_alph.index(n) for w, n in zip(weights, str_part))
        number =  str((10 - s) % 10)
        return "{}{}".format(str_part, number)

    def mic(self):
        """
        Generates a random MIC
        :return: MIC as a string
        """
        rnd = self.generator.random
        return "".join(rnd.choices(_alphanumeric_alph[10:], k=4))

    def lei(self):
        rnd = self.generator.random
        lou = "".join(rnd.choices(_alphanumeric_alph, k=4))
        reserved = "00"
        org_id = "".join(rnd.choices(_alphanumeric_alph, k=12))
        partial_lei = "{}{}{}".format(lou, reserved, org_id)
        checksum = sum(list(map(lambda x: _alph.index(x) if x in _alph else 0, partial_lei))) % 98
        checksum = 98 - int(checksum)
        return "{}{}".format(partial_lei, checksum)

    def cusip(self):
        rnd = self.generator.random
        base_id = "".join(rnd.choices(_cusip_alph, k=8))
        check_char = ''.join(str((1, 2)[i % 2] * _cusip_alph.index(n)) for i, n in enumerate(base_id))
        check_char = str((10 - sum(int(n) for n in check_char)) % 10)
        return "{}{}".format(base_id, check_char)

    def ric(self):
        """
        Generates a random RIC string
        :return: a RIC with the format {three chars} {dot} {two chars}
        """
        rnd = self.generator.random
        ticker = "".join(rnd.choices(_alph, k=3))
        exchange = "".join(rnd.choices(_alph, k=2))
        return "{}.{}".format(ticker, exchange)

    def ticker (self):
        """
        Generates a random 4-char ticker
        :return: a random ticker ID
        """
        rnd = self.generator.random
        ticker = "".join(rnd.choices(_alph, k=4))
        return "{}".format(ticker)

    def nsin (self):
        rnd = self.generator.random
        code  = "".join(rnd.choices(_alphanumeric_alph, k=9))
        return "{}".format(code)

    def figi (self):
        rnd = self.generator.random
        head = "B" # """.join(rnd.choices(_alph, k=1))
        char2 = rnd.choices(_alph)[0]
        if head == "B":
            char2 = rnd.choice([c for c in _alph if c not in ['S','M']])
        elif head == "G":
            char2 = rnd.choice([c for c in _alph if c not in ['G','B', 'H']])
        elif head == "K":
            char2 = rnd.choice([c for c in _alph if c != 'Y'])
        elif head == "V":
            char2 = rnd.choice([c for c in _alph if c != 'G'])
        char3 = "G"
        tail = "".join(rnd.choices(_alphanumeric_alph, k=7))
        id = "{}{}{}{}".format(head, char2, char3, tail)
        number = ''.join(str(_alphanumeric_alph.index(n) * (1, 2)[i % 2]) for i, n in enumerate(id[:11]))
        number = str((10 - sum(int(n) for n in number)) % 10)
        return "{}{}".format(id, number)

    def marketType (self):
        rnd = self.generator.random
        return rnd.choice(["bond", "commodity", "derivatives", "forex", "otc", "pe", "spot", "stock"])
