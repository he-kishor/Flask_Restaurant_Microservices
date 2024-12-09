from flask_pymongo import PyMongo
from settings.DB.validatedata import validate_data
from settings.Middleware.checkauthenticate import check_auth_usermicroserivices

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

    def create_restaurant(self, restaurant_data,request):
        # Validate data
        query_params = request.args.to_dict()
        token=request.headers.get('Authorization')
        
        #---------------token handle-----------------------------
        if not token or 'Bearer' not in token:
            return {"error":"Authorization token missing or invalid"},401
        token = token.split("Bearer ")[-1]
        user_data = check_auth_usermicroserivices(token)
        if user_data.get('status')!=200:
            return{'error':user_data.get("message")},user_data.get('status')
       
            
        is_valid, message = validate_data(restaurant_data, restaurant_schema)
        if not is_valid:
            return {"error": message}, 400
        
    
        # Insert data
        result = self.Restaurent_Col.insert_one(restaurant_data)
        return {"data":user_data.get('data')},200
    