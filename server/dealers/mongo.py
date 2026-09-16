from pymongo import MongoClient
from django.conf import settings

_client = None
_db = None

def get_client():
    global _client
    if _client is None:
        _client = MongoClient(settings.MONGO_URI)
    return _client

def get_db():
    global _db
    if _db is None:
        _db = get_client()[settings.MONGO_DB_NAME]
    return _db

def get_dealers_collection():
    return get_db()['dealers']

def get_reviews_collection():
    return get_db()['reviews']

def get_cars_collection():
    return get_db()['cars']