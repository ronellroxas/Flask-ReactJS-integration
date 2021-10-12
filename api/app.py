from flask import Flask
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'API index route'

@app.route('/<filename>', methods=['GET'])
def getData(filename):
    df = None

    try:
        df = pd.read_csv('data/' + filename)

        return df.to_json(orient="records")
    except:
        return {"Message": "Error retrieving file."}