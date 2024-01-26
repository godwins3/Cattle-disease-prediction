import logging
import os

import flask
from flask import request, Response, render_template
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return upload()
    return render_template('index.html')