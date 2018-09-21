import json
import requests
from datetime import datetime

currency = 'JPY'

global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency

request = requests.get(global_url)

results = request.json()

#print(json.dumps(results, sort_keys=True,indent=4))

active_currencies = int(results['data']['active_cryptocurrencies'])
active_markets = int(results['data']['active_markets'])
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = int(results['data']['last_updated'])
global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
global_volume = int(results['data']['quotes'][currency]['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)
bitcoin_percentage_string = '{:,}'.format(bitcoin_percentage)

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %H%M')

print()
print('There are currently ' + active_currencies_string + ' active cryptocurrencies and ' + active_markets_string + ' active markets.')
print('The global cap of all cryptos is ' + global_cap_string + ' and the 24 hour global volume is ' + global_volume_string + '.')
print('Bitcoin\'s total percentage of the global cap is ' + bitcoin_percentage_string + '%.')
print()
print('This information was last updated on ' + last_updated_string + '.')
