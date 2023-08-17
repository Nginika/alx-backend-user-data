#!/usr/bin/env python3
"""flask app and routes"""
from flask import Flask, jsonify


app = Flask(__name)



@app.route('/', method=['GET'], strict_slashes=False)
def payload() -> str:
    """return a json payload"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
