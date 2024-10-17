from flask import request, abort, redirect
import pandas as pd
import binascii
import os

import joblib

def index():
    return "Hello, world!"

def predict():
    data  = request.get_json()
    df = pd.DataFrame([data])
    df.reset_index(drop=True, inplace=True)
    print(df)
    model = joblib.load("regression.joblib")
    output = model.predict(df)
    return {
        "output": output[0]
    }

