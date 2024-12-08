import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def configure_app(app):
    # MongoDB URI
    app.config["MONGO_URI"] = os.getenv("Mongo_uri")
