import json
import os
import unittest

import print_data

def _read_test_input(filename):
    basepath = os.path.dirname(__file__)
    filepath = os.path.join(basepath, 'testdata', filename)
    with open(filepath) as file_handle:
        return file_handle.read()

class ScrapeTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_scrapes_monacoin_snapshot(self):
        self.assertEqual(
            [
              {
                'number': '1',
                'pair': 'ETN/ETH',
                'price': '$0.018353',
                'source': 'Liquid',
                'updated': 'Spot',
                'volume': '$837,716',
                'volume_per': '54.13%'
              },
              {
                'number': '2',
                'pair': 'ETN/BTC',
                'price': '$0.018202',
                'source': 'Kucoin',
                'updated': 'Spot',
                'volume': '$341,972',
                'volume_per': '22.10%'
              },
              {
                'number': '3',
                'pair': 'ETN/BTC',
                'price': '$0.017944',
                'source': 'Cryptopia',
                'updated': 'Spot',
                'volume': '$260,383',
                'volume_per': '16.83%'
              },
              {
                'number': '4',
                'pair': 'ETN/BTC',
                'price': '$0.018202',
                'source': 'Liquid',
                'updated': 'Spot',
                'volume': '$20,562',
                'volume_per': '1.33%'
              },
              {
                'number': '5',
                'pair': 'ETN/ETH',
                'price': '$0.018208',
                'source': 'Kucoin',
                'updated': 'Spot',
                'volume': '$20,084',
                'volume_per': '1.30%'
              },
              {
                'number': '6',
                'pair': 'ETN/USDT',
                'price': '$0.018405',
                'source': 'Cryptopia',
                'updated': 'Spot',
                'volume': '$18,579',
                'volume_per': '1.20%'
              },
              {
                'number': '7',
                'pair': 'ETN/BTC',
                'price': '$0.018202',
                'source': 'Sistemkoin',
                'updated': 'Spot',
                'volume': '$13,222',
                'volume_per': '0.85%'
              },
              {
                'number': '8',
                'pair': 'ETN/LTC',
                'price': '$0.018235',
                'source': 'Cryptopia',
                'updated': 'Spot',
                'volume': '$13,054',
                'volume_per': '0.84%'
              },
              {
                'number': '9',
                'pair': 'ETN/BTC',
                'price': '$0.018073',
                'source': 'TradeOgre',
                'updated': 'Spot',
                'volume': '$11,820',
                'volume_per': '0.76%'
              },
              {
                'number': '10',
                'pair': 'ETN/INR',
                'price': '$0.018769',
                'source': 'Bitbns',
                'updated': 'Spot',
                'volume': '$7,045',
                'volume_per': '0.46%'
              },
              {
                'number': '11',
                'pair': 'ETN/DOGE',
                'price': '$0.018358',
                'source': 'Cryptopia',
                'updated': 'Spot',
                'volume': '$1,659',
                'volume_per': '0.11%'
              },
              {
                'number': '12',
                'pair': 'ETN/GBP',
                'price': '$0.019515',
                'source': 'Cryptomate',
                'updated': 'Spot',
                'volume': '$612',
                'volume_per': '0.04%'
              },
              {
                'number': '13',
                'pair': 'ETN/BTC',
                'price': '$0.017558',
                'source': 'CoinBene',
                'updated': 'Spot',
                'volume': '$595',
                'volume_per': '0.04%'
              },
              {
                'number': '14',
                'pair': 'ETN/BTC',
                'price': '$0.019809',
                'source': 'Coindeal',
                'updated': 'Spot',
                'volume': '$210',
                'volume_per': '0.01%'
              },
              {
                'number': '15',
                'pair': 'ETN/NZDT',
                'price': '$0.018731',
                'source': 'Cryptopia',
                'updated': 'Spot',
                'volume': '$11',
                'volume_per': '0.00%'
              },
              {
                'number': '16',
                'pair': 'ETN/BTC',
                'price': '*\n\n$0.018009',
                'source': 'OEX',
                'updated': 'Spot',
                'volume': '$0',
                'volume_per': '0.00%'
              }
            ],
            print_data.scrape_coinmarketcap_markets_html(
                _read_test_input('electroneum.html')
                )
            )
