import requests

def get_live_token_data():
    try:
        response = requests.get("https://api.helius.xyz/v0/tokens/metadata?api-key=6af53ec9-6f3d-41db-a12f-eb0093ae00a1")
        data = response.json()
        tokens = data.get("tokens", [])  # veya "result", API yapısına göre
        return tokens
    except Exception as e:
        print("Veri çekme hatası:", e)
        return []
