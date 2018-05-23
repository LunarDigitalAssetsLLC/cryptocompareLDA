python_cryptocompare
#############

Python3 Wrapper to query cryptocurrency prices (and more) using the CryptoCompare_ API.

Installation
************

Installation instructions coming soon.

Usage
*****

Import
======

.. code:: python

   from python_cryptocompare import price as p

Methods
=======

Following API requests are supported:
- CoinList
- Price
- PriceMulti
- PriceMultiFull
- PriceHistorical
- generateAvg
- dayAvg
- CoinSnapshot
- CoinSnapshotFullById
- HistoMinute
- HistoHour
- HistoDay
- topPairs
- socialStats
- miningEquipment


Coin List
---------

.. code:: python

   from python_cryptocompare import price as p
   print(p.coinSnapshot('btc', 'usd'))

   # ...
   # },
   # 'BTC': {
   #  'Id': '1182'
   #  'Url': '/coins/btc/overview'
   #  'ImageUrl': '/media/19633/btc.png'
   #  'Name': 'BTC'
   #  'CoinName': 'Bitcoin'
   #  'FullName': 'Bitcoin (BTC)'
   #  'Algorithm': 'SHA256'
   #  'ProofType': 'PoW'
   #  'FullyPremined': '0'
   #  'TotalCoinSupply': '21000000'
   #  'PreMinedValue': 'N/A'
   #  'TotalCoinsFreeFloat': 'N/A'
   #  'SortOrder': '1'
   # },
   # ...

Price
-----
.. code:: python

   cc.get_price('BTC')
   # or
   cc.get_price('BTC',curr='USD',full=True)
   # or
   cc.get_price(['BTC','ETH'],['EUR','GBP'])

   # {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
   #  'ETH': {'EUR': 258.1, 'GBP': 241.25}}

Historical Price
----------------
.. code:: python

   # pass either datetime or time instance
   cc.get_historical_price('XMR', timestamp=datetime.datetime(2017,6,6), exchange='CCCAGG')
   # or
   cc.get_historical_price('XMR', 'EUR', datetime.datetime(2017,6,6))

   # {'XMR': {'EUR': 43.05}}

Day
---
.. code:: python

   cc.get_historical_price_day('BTC', curr='EUR')

Hour
----
.. code:: python

   cc.get_historical_price_hour('BTC', curr='EUR')

Average
-------

.. code:: python

   cc.get_avg('BTC', curr='EUR', exchange='Kraken')

   # {
   # 'MARKET': 'CUSTOMAGG',
   # 'FROMSYMBOL': 'BTC',
   # 'TOSYMBOL': 'EUR',
   # 'FLAGS': 0,
   # 'PRICE': 3610,
   # 'LASTUPDATE': 1503066719,
   # 'LASTVOLUME': 0.5,
   # 'LASTVOLUMETO': 1805,
   # 'LASTTRADEID': 1503066719.7584,
   # 'VOLUME24HOUR': 12614.509997469995,
   # 'VOLUME24HOURTO': 46397723.00499387,
   # 'OPEN24HOUR': 3847.9,
   # 'HIGH24HOUR': 3848.96,
   # 'LOW24HOUR': 3555,
   # 'LASTMARKET': 'Kraken',
   # 'CHANGE24HOUR': -237.9000000000001,
   # 'CHANGEPCT24HOUR': -6.182593102731363
   # }


Exchanges
---------

.. code:: python

   cc.get_exchanges()


Credit
******

Thanks to CryptoCompare_ for providing this service and building a community around everything crypto related.

.. _Cryptocompare: https://min-api.c.com/

Thanks to lagerfeuer for getting the project started.

Disclaimer
**********
If you want additional features, open an issue or create a pull request.
