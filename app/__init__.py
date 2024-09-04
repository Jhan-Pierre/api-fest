from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import bp as festividades_bp
    app.register_blueprint(festividades_bp)

    return app
