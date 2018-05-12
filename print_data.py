from coinmarketcap import Market
import json
from bs4 import BeautifulSoup
import requests

def ppjson(data):
    """ Pretty print json helper """
    print(json.dumps(data, indent=2, sort_keys=True))

def get_soup(res):
    return BeautifulSoup(res.text, "html5lib")

def get_html_soup(url):
    res = requests.get(url)
    if res.status_code == 200:
        return get_soup(res)
    else:
        print("ERROR: Coinmarketcap.com", res.status_code)

def get_markets(currency):
    """ Get markets table """
    url = "https://coinmarketcap.com/currencies/{}/#markets".format(currency)
    soup = get_html_soup(url)
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
        
coinmarketcap = Market()
lim = 100
coins = coinmarketcap.ticker(limit=lim)["data"]
print("rank,name,market_cap,price,true_volume,listed_volume,percent_fake_volume,n_exchanges_USD_pairs,exchanges")
for rank in range(1,lim+1):
    for coin_id in coins:
        coin = coins[coin_id]
        if coin["rank"] == rank:
            markets = get_markets(coin["website_slug"])
            true_volume = 0
            n_exchanges = 0
            exchanges = []
            for market in markets:
                if market["pair"].endswith("/USD") and market["volume"].startswith("$") and market["source"] != "Bitfinex":
                    n_exchanges += 1
                    true_volume += float(market["volume"].replace("$","").replace(",",""))
                    exchanges.append(market["source"])
            print("{},{},{},{},{},{},{:.2f}%,{},{}".format(coin["rank"],coin["name"],coin["quotes"]["USD"]["market_cap"],coin["quotes"]["USD"]["price"],true_volume,coin["quotes"]["USD"]["volume_24h"],100.0 - true_volume / coin["quotes"]["USD"]["volume_24h"] * 100.0,n_exchanges, "/".join(exchanges)))

