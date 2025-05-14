from flask import Flask, jsonify
from models import init_db, get_all_products

app = Flask(__name__)

@app.route("/products")
def list_products():
    return jsonify(get_all_products())

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)