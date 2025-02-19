import requests

API_KEY = 'your_api_key_here'
URL = 'https://api.abuseipdb.com/api/v2/blacklist'
HEADERS = {
    'Accept': 'application/json',
    'Key': API_KEY
}
PARAMS = {
    'confidenceMinimum': 90
}

response = requests.get(URL, headers=HEADERS, params=PARAMS)
blacklist = response.json()

with open('/etc/nginx/blocklist.conf', 'w') as file:
    for ip in blacklist['data']:
        file.write(f"deny {ip['ipAddress']};\n")
