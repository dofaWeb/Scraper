"""this module help to insert value into database"""

import os
from dotenv import load_dotenv
import pymongo
from config import log
from config.connect_db import Database_config


# Load environment variables
load_dotenv()


def insert_data(data):
    """
    Insert data into MongoDB collection.

    :param data: List of documents to insert
    """
    mongo_uri = os.getenv("MONGODB_URI")
    database_name = os.getenv("DATABASE")
    collection_name = os.getenv("COLLECTION")
    database_name = database_name.capitalize()

    if not mongo_uri or not database_name:
        log.log_error("Missing MongoDB connection settings.")
        return None

    collection = Database_config.connect_to_database(
        mongo_uri, database_name, collection_name
    )

    if collection is not None:
        try:
            if isinstance(data, list) and all(isinstance(doc, dict) for doc in data):
                for d in data:
                    collection.insert_one(d)
                log.log_message(
                    f"Inserted {len(data)} records successfully to database '{database_name}''."
                )
            else:
                raise TypeError("Data must be a list of dictionaries.")
        except pymongo.errors.DuplicateKeyError as e:
            log.log_error("Duplicate key error when inserting data into MongoDB.", e)
        except pymongo.errors.WriteError as e:
            log.log_error("Write error when inserting data into MongoDB.", e)
        except pymongo.errors.ConnectionFailure as e:
            log.log_error("Connection to MongoDB failed.", e)
        except TypeError as e:
            log.log_error("Invalid data type provided.", e)
        finally:
            print("Insert operation complete.")
    else:
        print("Collection is none.")
