from flask import Blueprint

from routes.example import example_bp

api_bp = Blueprint("api", __name__)


api_bp.register_blueprint(example_bp, url_prefix="/example")
