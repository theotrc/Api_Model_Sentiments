from crypt import methods
from pyexpat import model
from re import X
from flask import Flask
from flask import Blueprint, request
import requests
import json
import pickle
import pandas as pd
import numpy as np
import sklearn

open_model = open("clf_test.pkl", "rb")
model = pickle.load(open_model)

open_vect = open("vectorizer.pkl", "rb")
vect = pickle.load(open_vect)

route = Blueprint("route", __name__, static_folder="../static", template_folder='../templates/')

@route.route('/')
def runing():
    return '<h1>run</h1>'


@route.route('/predict', methods = ['get', 'post'])
def predict():
    record = request.json
    message = vect.transform([str(record['thoughts'])])
    prediction = model.predict(message)
    print(str(record['thoughts']))
    return prediction[0]
