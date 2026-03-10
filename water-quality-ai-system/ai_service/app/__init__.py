from flask import Flask, jsonify

from app.routes.predict_route import predict_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(predict_bp)

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app
