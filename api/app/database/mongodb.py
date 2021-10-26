from flask import current_app
import pymongo

class metadata_db:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(current_app.config['MONGO_CLIENT'])
        self.clientName = current_app.config['MONGO_CLIENT_NAME']
        self.db = self.client[self.clientName]
        