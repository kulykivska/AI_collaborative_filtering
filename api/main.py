import sys
import os
from fastapi import FastAPI
from pymongo import MongoClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from config import DATABASE_NAME, COLLECTION_NAME, CONNECTION_STRING

# Initialize FastAPI
app = FastAPI()

def get_mongo_collection(database_name, collection_name, connection_string):
    """
    Connects to MongoDB and returns the specified collection.

    :param database_name: Name of the database
    :param collection_name: Name of the collection
    :param connection_string: MongoDB connection string
    :return: MongoDB collection
    """
    client = MongoClient(connection_string)
    db = client[database_name]
    return db[collection_name]

collection = get_mongo_collection(DATABASE_NAME, COLLECTION_NAME, CONNECTION_STRING)

@app.get("/ratings/")
async def get_ratings():
    documents = list(collection.find({}, {"_id": 0, "user_id": 1, "item_id": 1, "rating": 1}))
    
    return {"ratings": documents}
