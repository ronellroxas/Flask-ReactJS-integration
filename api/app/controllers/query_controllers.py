from flask import json
import pandas as pd
from app.database.mongodb import metadata_db
from datetime import date

def index_page():
    return "Welcome to query index page."

def init_data():
    df = pd.read_csv(f'data/dummy_data.csv')
    data = df.to_json(orient='records')
    mongodb = metadata_db()
    mongodb.db['datasource_metadata'].drop()
    mongodb.db['datasource_metadata'].insert_many(json.loads(data))
    return data