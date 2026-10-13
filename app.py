from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Challenge 1 - Team NHM"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

