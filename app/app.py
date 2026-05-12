from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Project Running"

@app.route("/health")
def health():
    # Returns the health status as a JSON object
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    # host='0.0.0.0' allows the app to be accessible within a Docker container or network
    app.run(host="0.0.0.0", port=5000)
