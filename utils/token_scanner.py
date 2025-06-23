
import requests

def get_live_token_data():
    url = "https://quote-api.jup.ag/v6/tokens"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []
