import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class Config:
    MONGO_URI = os.environ.get("MONGO_URI", "")


config = Config()
