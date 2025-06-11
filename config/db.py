from pymongo import MongoClient
import os


uri = os.getenv('MONGODB_URI')
conn = MongoClient(uri)