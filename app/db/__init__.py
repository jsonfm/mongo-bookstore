from pymongo import MongoClient

# config
from app.config import config

print("MONGO URI: ", config.MONGO_URI)
client = MongoClient(config.MONGO_URI)
db = client.get["bookstore"]
