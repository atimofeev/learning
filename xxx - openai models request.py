import requests
import os

# Get API key from OS ENV
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set header for GET request
headers = {
    'Authorization': f'Bearer {openai_api_key}'
}

# Request list of models from openai API with provided header, which contains API key
response = requests.get('https://api.openai.com/v1/models', headers=headers)

## Everything above simplified into one line
#response = requests.get('https://api.openai.com/v1/models', headers={'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'})

# Convert HTTP response into dictionary
json_data = response.json()

# Iterate through dictionary and print IDs
for item in json_data['data']:
    print(item['id'])