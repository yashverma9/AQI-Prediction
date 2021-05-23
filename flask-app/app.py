from flask import Flask, jsonify, request, render_template
import json
import sys
import os
from flask_cors import CORS, cross_origin

import requests
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
    return int(model.predict(df)[0])


def getRecentJson():
    df = pd.read_csv("Model/data/AQI/recent.csv")
    
    date = df['date'].tolist()
    aqi = df['PM2.5'].tolist()
    dict = {"date": date , "aqi" : aqi }
    return dict


@app.route('/')
@cross_origin()
def getHello():
    return "Hello! This is running!"


@app.route('/city')
@cross_origin()
def get_city_data() -> dict:
    city = request.args['city']
    api_key = '4b3b3ba35fcd7a3d24f3adc38895bbdd' #Fill here
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric'  #http://api.worldweatheronline.com/premium/v1/past-weather.ashx?tp=24&q=Bengaluru&date=2021-04-16&enddate=2021-05-15&key=2b0714b1fb8e4b38a93185230211605&format=json
    return jsonify(requests.get(url).json())



@app.route('/getPrediction', methods = ['POST'])
@cross_origin()
def getPrediction():
    try:
        formData = request.json
        print(formData['params'])
        result = str(predict_aqi(formData['params'], 'xgb.pkl'))
    except:
        print(sys.exc_info())
        result = 'Server error'
    return jsonify(result)



@app.route('/aqiMonthChart') #Also for weekly
@cross_origin()
def aqiMonth():
    return jsonify(getRecentJson())


if __name__ == "__main__":
    app.run(debug=True, port = 5000)
