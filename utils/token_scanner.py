import requests
import os

def get_live_token_data():
    api_key = os.getenv("HELIUS_API_KEY")

    if not api_key:
        print("API Key YOK!")
        return []

    url = f"https://api.helius.xyz/v0/tokens/metadata?api-key={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        tokens = data.get("tokens", [])[:20]
        print(f"{len(tokens)} token çekildi.")
        return tokens

    except requests.exceptions.RequestException as e:
        print(f"API isteği başarısız: {e}")
        return []

    except Exception as e:
        print(f"Genel hata: {e}")
        return []