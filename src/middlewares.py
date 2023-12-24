from flask import Blueprint, request
from werkzeug.exceptions import NotFound

middlewares_bp = Blueprint("middlewares", __name__)


@middlewares_bp.app_errorhandler(NotFound)
def not_found(_):
    return f"🔍 - Not Found - {request.path}", 404
