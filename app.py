from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from settings.DB.DB_connect import configure_app

app=Flask(__name__)

configure_app(app)
mongo = PyMongo(app)
#register routes

from src.routes_rout.restourent_routes import restaurent_bp
app.register_blueprint(restaurent_bp, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True)
    