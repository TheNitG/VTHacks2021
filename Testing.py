# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = '60397d424a4a8605712843ae'
apiKey = '4f8955b3e4482afb50d7458010308068'

url = f'http://api.reimaginebanking.com/customers/{customerId}/accounts?key={apiKey}'
payload = {
    "type": "Savings",
    "nickname": "test",
    "rewards": 10000,
    "balance": 10000,
}
# Create a Savings Account
response = requests.post(
    url,
    data=json.dumps(payload),
    headers={'content-type': 'application/json'},
)

if response.status_code == 201:
    print('account created')

print(url)
