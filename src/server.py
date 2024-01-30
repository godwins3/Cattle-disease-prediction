import logging
import os

import flask
from flask import request, Response, render_template
from flask_cors import CORS, cross_origin
from src.util.core import randomforest, KNN, DecisionTree, NaiveBayes

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return {"Message": "hooray server is running", "statusCode": 200}

@app.route('/disease-prediction', methods = ['GET', 'POST'])
def disease_predict():
    # if request.method == 'POST':
    data =flask.request.get_json()
    Symptom1 = data['Symptom1']
    Symptom2 = data['Symptom2']
    Symptom3 = data['Symptom3']
    Symptom4 = data['Symptom4']
    Symptom5 = data['Symptom5']

    rf_predict = randomforest(Symptom1, Symptom2, Symptom3, Symptom4, Symptom5)
    nb_predict = NaiveBayes(Symptom1, Symptom2, Symptom3, Symptom4, Symptom5)
    dt_predict = DecisionTree(Symptom1, Symptom2, Symptom3, Symptom4, Symptom5)

    return {
        'rf_predict': rf_predict,
        'nb_predict': nb_predict,
        'dt_predict': dt_predict,
        'statusCode': 200
    }