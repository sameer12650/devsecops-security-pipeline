
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
    app.run(debug=False, port=5000)
