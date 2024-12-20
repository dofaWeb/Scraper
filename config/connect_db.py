import os
from pymongo import MongoClient
from config import log
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Database_config:
    """
    Class for configuring and connecting to a MongoDB database.
    """

    @staticmethod
    def connect_to_database(mongo_uri=None, database_name=None, collection_name=None):
        """
        Connect to the specified collection in the MongoDB database.

        :param mongo_uri: MongoDB URI
        :param database_name: MongoDB database name
        :param collection_name: MongoDB collection name
        :return: MongoDB collection instance or None if connection fails
        """

        if not mongo_uri or not database_name:
            log.log_error("Missing MongoDB connection settings.")
            return None

        try:
            client = MongoClient(mongo_uri)
            db = client[database_name]
            collection = db[collection_name]
            log.log_message(
                f"Connected to database {db.name} successfully!"
            )
            return collection
        except Exception as e:
            log.log_error(f"Failed to connect to database {database_name}.", e)
            return None