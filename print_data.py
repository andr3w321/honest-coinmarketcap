import argparse
from coinmarketcap import Market
import json
from bs4 import BeautifulSoup
import requests
import datetime
import time

OUTPUT_FORMAT_HTML = 'html'
OUTPUT_FORMAT_CSV = 'csv'

def ppjson(data):
    """ Pretty print json helper """
    print(json.dumps(data, indent=2, sort_keys=True))

def get_html(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        print("ERROR: Coinmarketcap.com code", res.status_code)

def get_markets(currency):
    """ Get markets table """
    url = "https://coinmarketcap.com/currencies/{}/#markets".format(currency)
    time.sleep(6)
    return scrape_coinmarketcap_markets_html(get_html(url))

def scrape_coinmarketcap_markets_html(html):
    soup = BeautifulSoup(html, "html5lib")
    markets_table = soup.find("table", {"id": "markets-table"})
    tbody = markets_table.find("tbody")
    trs = tbody.find_all("tr")
    markets = []
    for tr in trs:
        market = {}
        tds = tr.find_all("td")
        market["number"] = tds[0].text.strip()
        market["source"] = tds[1].text.strip()
        market["pair"] = tds[2].text.strip()
        market["volume"] = tds[3].text.strip()
        market["price"] = tds[4].text.strip()
        market["volume_per"] = tds[5].text.strip()
        market["updated"] = tds[6].text.strip()
        markets.append(market)
    return markets

def main(args):
    coinmarketcap = Market()
    lim = 100
    coins = coinmarketcap.ticker(limit=lim)["data"]
    if args.output_format == OUTPUT_FORMAT_HTML:
        print("<!DOCTYPE html><head></head><body>")
        print("<div>Last Updated: " + str(datetime.datetime.utcnow()) + " UTC<br/>")
        print("Source Code: <a href='https://github.com/andr3w321/honest-coinmarketcap'>https://github.com/andr3w321/honest-coinmarketcap</a><br/>")
        print("Contact: <a href='https://twitter.com/andr3w321'>@andr3w321</a><br/>")
        print("BTC Donations: 38hs9PyTbWG4SgyS4yvrR8CQ9PFXErJ5xk</div><br/>")
        print("<table border=1>")
    header = "rank,name,market_cap,price,fiat_volume,listed_volume,percent_crypto_to_crypto_volume,listed_volume/market_cap,n_exchanges_fiat_pairs,exchanges"
    if args.output_format == OUTPUT_FORMAT_HTML:
        print("<tr><td>" + "</td><td>".join(header.split(",")) + "</td></tr>")
    else:
        print(header)
    for rank in range(1,lim+1):
        for coin_id in coins:
            coin = coins[coin_id]
            if coin["rank"] == rank:
                markets = get_markets(coin["website_slug"])
                true_volume = 0
                n_exchanges = 0
                exchanges = []
                for market in markets:
                    if (market["pair"].endswith("/USD") or \
                        market["pair"].endswith("/GBP") or \
                        market["pair"].endswith("/EUR") or \
                        market["pair"].endswith("/KRW") or \
                        market["pair"].endswith("/CNY") or \
                        market["pair"].endswith("/JPY")) and \
                        market["volume"].startswith("$") and market["source"] != "Bitfinex" and market["source"] != "Ethfinex":
                        n_exchanges += 1
                        true_volume += float(market["volume"].replace("$","").replace(",",""))
                        exchanges.append(market["source"])
                if args.output_format == OUTPUT_FORMAT_HTML:
                    print("<tr><td>{}</td><td>{}</td><td>${:,.0f}</td><td>${:,.2f}</td><td>${:,.0f}</td><td>${:,.0f}</td><td>{:.2f}%</td><td>{:.2f}%</td><td>{}</td><td>{}</td><td></tr>".format(coin["rank"],coin["name"],coin["quotes"]["USD"]["market_cap"],coin["quotes"]["USD"]["price"],true_volume,coin["quotes"]["USD"]["volume_24h"],100.0 - true_volume / coin["quotes"]["USD"]["volume_24h"] * 100.0,coin["quotes"]["USD"]["volume_24h"] / coin["quotes"]["USD"]["market_cap"] * 100.0,n_exchanges, "/".join(exchanges)))
                else:
                    print("{},{},{},{},{},{},{:.2f}%,{:.2f}%,{},{}".format(coin["rank"],coin["name"],coin["quotes"]["USD"]["market_cap"],coin["quotes"]["USD"]["price"],true_volume,coin["quotes"]["USD"]["volume_24h"],100.0 - true_volume / coin["quotes"]["USD"]["volume_24h"] * 100.0,coin["quotes"]["USD"]["volume_24h"] / coin["quotes"]["USD"]["market_cap"] * 100.0,n_exchanges, "/".join(exchanges)))
    if args.output_format == OUTPUT_FORMAT_HTML:
        print("</table></body></html>")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Honest CoinMarketCap',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('output_format',
                        choices=[OUTPUT_FORMAT_HTML, OUTPUT_FORMAT_CSV],
                        help='Output format')
    main(parser.parse_args())
