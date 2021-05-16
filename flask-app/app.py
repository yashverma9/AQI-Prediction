from flask import Flask, jsonify, request
import json
import sys
from flask_cors import CORS

original_stdout = sys.stdout
app = Flask(__name__)
CORS(app)
app.static_folder = 'static'
app.secret_key = 'the random string'

@app.route('/')
def getHello():
    return "Hello! This is running!"



if __name__ == "__main__":
    app.run(debug=True, port = 7000)
