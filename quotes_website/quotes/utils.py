from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['Go-it_HW8']
    return db
