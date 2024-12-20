import os
from bson.objectid import ObjectId
from fastapi import APIRouter
from config.connect_db import Database_config


mongo_uri = os.getenv("MONGODB_URI")
database_name = os.getenv("DATABASE")
collection_name = os.getenv("COLLECTION")
database_name = database_name.capitalize()
collection = Database_config.connect_to_database(
        mongo_uri, database_name, collection_name
            )

endPoints = APIRouter()

@endPoints.get("/blogs")
def get_all_blogs():
    """get all blogs"""
    results = list(collection.find())
    for result in results:
        result['_id'] = str(result['_id'])
    return {
        "data" : results
    }

@endPoints.get("/blog/{id}")
def get_blog(id):
    """get a specific blog via id"""
    result = collection.find_one({"_id": ObjectId(id)})
    result["_id"] = str(result["_id"])
    return {"data": result}