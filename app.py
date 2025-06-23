
from flask import Flask, render_template
from utils.token_scanner import get_live_token_data

app = Flask(__name__)

@app.route('/')
def index():
    try:
        tokens = get_live_token_data()
        if isinstance(tokens, dict):
            tokens = list(tokens.values())
    except Exception as e:
        print("HATA:", e)
        tokens = []
    return render_template("index.html", tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)
