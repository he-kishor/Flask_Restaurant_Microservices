from flask import Flask,Blueprint, request, jsonify
from src.services.Restourent_services import RestaurantService
from flask_pymongo import PyMongo
from settings.DB.DB_connect import configure_app

app=Flask(__name__)

configure_app(app)
mongo = PyMongo(app)

restaurent_bp = Blueprint("restaurant",__name__)

Restaurant_Service = RestaurantService(mongo=mongo)

@restaurent_bp.route('/get_rest',methods=["GET"])
def create_restaurent():
    try:
        data={
        "name": "Rani Khet",
        "address": "Pune",
        "cuisine": "best",  # Optional
        }

        response, statuscode= Restaurant_Service.create_restaurant(data,request)
        return jsonify(response), statuscode

    except Exception as e:
         return jsonify({"error": "Internal server error", "details": str(e)}), 500
