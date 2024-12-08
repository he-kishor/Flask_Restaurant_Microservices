from flask_pymongo import PyMongo
from settings.DB.validatedata import validate_data

#define schema for restourent
restaurant_schema = {
    "name": {"type": str, "required": True},
    "address": {"type": str, "required": True},
    "cuisine": {"type": str, "required": False},  # Optional
}

class RestaurantService:
    def __init__(self, mongo: PyMongo):
        self.db = mongo.cx.RestourentDB
        self.Restaurent_Col = self.db.Restourent_info

    def create_restaurant(self, restaurant_data):
        # Validate data
        
        is_valid, message = validate_data(restaurant_data, restaurant_schema)
        if not is_valid:
            return {"error": message}, 400

        # Insert data
        result = self.Restaurent_Col.insert_one(restaurant_data)
        return {"data":str(result.inserted_id)}