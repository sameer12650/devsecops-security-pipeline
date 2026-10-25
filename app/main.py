import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "application": "DevSecOps Security Pipeline",
        "status": "running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200




if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    app.run(host=host, debug=False, port=5000)