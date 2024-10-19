from pymongo import MongoClient

database_name = "recommendation_db"
collection_name = "user_ratings"
connection_string = "mongodb://localhost:27017/"

# def create_mongo_collection(database_name, collection_name, connection_string):
# Connect to MongoDB
client = MongoClient(connection_string)
# Create a new database
database = client[database_name]
# Create a new collection
collection = database[collection_name]
# Insert a document into the collection
# collection.insert_one({"key": "value"})

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

def insert_data_to_mongo(documents, db_name='mydatabase', collection_name='mycollection'):
    """
    Inserts data into the specified MongoDB collection.

    :param data: Data to insert
    """
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(documents)
    client.close()


__all__ = ['get_mongo_collection', 'insert_data_to_mongo']