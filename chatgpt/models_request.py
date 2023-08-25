import requests

with open("openai.key", encoding="utf-8") as f:
    openai_api_key = f.read().strip()

response = requests.get('https://api.openai.com/v1/models', \
    headers={'Authorization': f'Bearer {openai_api_key}'}, \
    timeout=10)

json_data = response.json()

for item in json_data['data']:
    print(item['id'])
