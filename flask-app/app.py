from flask import Flask, jsonify, request, render_template
import json
import sys
import os
from flask_cors import CORS, cross_origin

import pandas as pd
import pickle


original_stdout = sys.stdout
app = Flask(__name__)
CORS(app)
app.static_folder = 'static'
app.secret_key = 'the random string'
app.config['CORS_HEADERS'] = 'Content-Type'


def predict_aqi(data: dict, filename: str) -> float:
    df = pd.DataFrame([data])
    model = pickle.load(open(filename, 'rb'))
    return model.predict(df)[0]



@app.route('/')
@cross_origin()
def getHello():
    return "Hello! This is running!"


@app.route('/getPrediction', methods = ['POST'])
@cross_origin()
def getPrediction():
    try:
        formData = request.json
        print(formData)
        result = str(predict_aqi(formData, 'xgb.pkl'))
    except:
        print(sys.exc_info())
        result = 'Server error'
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True, port = 7000)
