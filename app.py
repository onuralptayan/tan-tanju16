from flask import Flask, render_template
from helius_handler import get_tokens

app = Flask(__name__)

@app.route("/")
def index():
    tokens = get_tokens()
    return render_template("index.html", tokens=tokens)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
