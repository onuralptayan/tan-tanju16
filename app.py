from flask import Flask, render_template
from utils.token_scanner import fetch_tokens
import os

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.getenv("API_KEY")
    tokens = fetch_tokens(api_key)
    return render_template("index.html", tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
