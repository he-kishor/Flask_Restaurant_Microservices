from flask import Blueprint, request, jsonify
from src.services.Restourent_services import RestaurantService
from app import mongo

restaurent_bp = Blueprint("/restaurant",__name__)

Restaurant_Service = RestaurantService(mongo=mongo)

@restaurent_bp.route('/get_rest',methods=["GET"])
def create_restaurent():
    data={
    "name": "Rani Khet",
    "address": "Pune",
    "cuisine": "best",  # Optional
    }
    inserted_id= Restaurant_Service.create_restaurant(data)
    return jsonify({"message": "Restaurant created", "id": inserted_id}), 201

    