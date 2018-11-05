# Honest CoinMarketCap

[![Build Status](https://travis-ci.org/andr3w321/honest-coinmarketcap.svg?branch=master)](https://travis-ci.org/andr3w321/honest-coinmarketcap) [![Coverage Status](https://coveralls.io/repos/github/andr3w321/honest-coinmarketcap/badge.svg?branch=master)](https://coveralls.io/github/andr3w321/honest-coinmarketcap?branch=master)

## Overview

This script will scrape coinmarket.com and output a csv of the trading volume for USD pairs only. It excludes Bitfinex.com pairs because those are incorrectly listed as USD and are actually USDT.

## Usage

### Output as CSV

```bash
python print_data.py csv > output.csv
```

### Output as HTML

```bash
python print_data.py html > index.html
```

## Notes

BTC Donations: 38hs9PyTbWG4SgyS4yvrR8CQ9PFXErJ5xk

For the time being I'm maintaining an hourly update of this script at https://sportsbettingcalcs.com/honestcoinmarketcap
