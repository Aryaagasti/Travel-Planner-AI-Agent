from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Allow CORS for your frontend URL
    CORS(app, resources={r"/*": {"origins": "https://arya-s-ai-travel-planner.onrender.com"}})
    
    app.config.from_object('app.config.Config')

    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app
