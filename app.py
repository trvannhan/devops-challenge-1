import os
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DevOps Challenge 1 - Team NHM")
APP_ENV = os.getenv("APP_ENV", "development")
APP_PORT = int(os.getenv("APP_PORT", "5000"))

@app.route("/")
def home():
    return APP_NAME

@app.route("/health")
def health():
    return {"status": "ok"}
@app.route("/version")
def version():
    return {"version": "v2", "team": "NHM"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=APP_PORT)
