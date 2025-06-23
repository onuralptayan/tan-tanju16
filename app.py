from flask import Flask, render_template
from utils.token_scanner import get_live_token_data
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        raw_data = get_live_token_data()

        tokens = []
        if isinstance(raw_data, dict) and "tokens" in raw_data:
            tokens = [t for t in raw_data["tokens"].values() if isinstance(t, dict)]
        elif isinstance(raw_data, list):
            tokens = [t for t in raw_data if isinstance(t, dict)]
        else:
            print("⚠️ Veri formatı tanınamadı:", type(raw_data))

    except Exception as e:
        print("❌ Hata oluştu:", e)
        tokens = []

    return render_template("index.html", tokens=tokens)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
