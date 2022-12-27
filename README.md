# faker_marketdata
Generates random, valid market data for testing purposes.

## Installation

``` bash
pip install faker_marketdata
```

## Usage

Add as a provider to your Faker instance:
``` python
>>> from faker import Faker
>>> from faker_marketdata import MarketDataProvider
>>> fake = Faker()
>>> fake.add_provider(MarketDataProvider())
```
Optionally you can use a seed value to have repeatable output: 
``` python
>> fake.add_provider(MarketDataProvider(see=1220))
```

Now you can start to generate market data, some examples:
``` python
>> fake.isin()   # "GTYMQXUIYPB6"
>> fake.sedol()  # "NKDEKC8"
>> fake.cusip()  # "Z57XGDJW7"
>> fake.ticker() # "GRTT"
```

## Documentation
Supported market data identifiers:
* ISIN
* SEDOL
* MIC
* LEI
* CUSIP
* RIC
* TICKER
* NSIN
* FIGI
* Market type (e.g. "bond", "commodity", "otc")