import requests
import os

API_KEY = os.getenv("HELIUS_API_KEY")

def get_tokens():
    try:
        url = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"
        headers = {"Content-Type": "application/json"}

        payload = {
            "jsonrpc": "2.0",
            "id": "getLatestTokens",
            "method": "getSignaturesForAddress",
            "params": [
                "4bcFeLv4NyFPPG3FrDhYxK1hCQ9J5AnnpXXz3SpA8z61",  # Raydium deployer örneği
                {"limit": 20}
            ]
        }

        res = requests.post(url, headers=headers, json=payload)
        data = res.json()

        if "result" not in data:
            return []

        token_list = []
        for item in data["result"]:
            token_list.append({
                "name": "Unknown",
                "symbol": "???",
                "signature": item.get("signature", "?"),
                "slot": item.get("slot", "?")
            })

        return token_list
    except Exception as e:
        print("HATA:", e)
        return []
