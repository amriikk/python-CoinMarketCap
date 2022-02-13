import requests
import json

api_key = 'e839c988-6481-4eff-a380-8f898e98a298'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest'

request = requests.get(global_url, headers=headers)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data  = results['data']

btc__dominance = data['btc_dominance']


print(btc__dominance)
