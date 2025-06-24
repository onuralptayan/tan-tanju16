
import os
from flask import Flask, render_template
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    api_key = os.getenv("HELIUS_API_KEY")
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    url = f"https://api.helius.xyz/v0/tokens/mostRecent?api-key={api_key}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tokens = response.json()
    except Exception as e:
        print(f"API error: {e}")
        tokens = []

    return render_template("index.html", tokens=tokens)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
