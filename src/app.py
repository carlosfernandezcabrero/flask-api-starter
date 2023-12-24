from flask import Flask

from middlewares import middlewares_bp
from routes.index import api_bp

API_VERSION = "v1"


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix=f"/{API_VERSION}")
    app.register_blueprint(middlewares_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
