"""Requests available AI models from OpenAI"""
import requests

def get_models():
    """Get model list from OpenAI.
    Currently lists ones starting with 'gpt*'"""
    models = []
    with open("openai.key", encoding="utf-8") as f:
        openai_api_key = f.read().strip()

    response = requests.get('https://api.openai.com/v1/models', \
        headers={'Authorization': f'Bearer {openai_api_key}'}, \
        timeout=10)

    json_data = response.json()

    for item in json_data['data']:
        if item['id'].startswith("gpt"):
            models.append(item['id'])
    return models

def _main():
    """Main function for standalone use.
    Prints models list."""
    print(*get_models(), sep='\n', end='')

if __name__ == "__main__":
    _main()
