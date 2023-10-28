from pymongo import MongoClient

# config
from app.config import config

client = MongoClient(config.MONGO_URI)
db = client.get["bookstore"]
