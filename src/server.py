import logging
import os

import flask
from flask import request
from flask import Response
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)