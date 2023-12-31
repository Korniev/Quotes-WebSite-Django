import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def get_mongo_db():
    client = os.getenv('DB_CONNECT')

    db = os.getenv('DB_NAME')
    return db
