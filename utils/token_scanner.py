
import requests

API_KEY = "6af53ec9-6f3d-41db-a12f-eb0093ae00a1"
ENDPOINT = f"https://api.helius.xyz/v0/tokens?api-key={API_KEY}"

def get_live_token_data():
    try:
        response = requests.get(ENDPOINT)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print("HATA:", e)
        return []
