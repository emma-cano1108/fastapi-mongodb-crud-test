from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('.env')
uri = os.getenv('MONGODB_URI')
conn = MongoClient(uri)